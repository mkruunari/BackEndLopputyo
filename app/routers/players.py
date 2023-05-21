# from fastapi import APIRouter
# from typing import List, Optional
# from datetime import datetime
# from app.database.models import Player
# from fastapi.responses import JSONResponse
# from fastapi import HTTPException
# router = APIRouter()

# players = []

# @router.get("/players", status_code=200)
# async def get_players():
#     # palauttaa pelaajat
#     return [{"id": player.id, "name": player.name} for player in players]



# @router.post("/players", status_code=201)
# async def create_player(name: str):
#     if not name:
#         return JSONResponse(content={"error": "Name cannot be empty"}, status_code=422)
#     id = len(players) + 1
#     player = Player(id, name)
#     players.append(player)
#     return {"id": id, "name": name}

# @router.get("/players/{id}")
# async def get_player(id: int):
#     for player in players:
#         if player.id == id:
#             return player
#     raise HTTPException(status_code=404, detail="Player not found")



# @router.get("/players/{id}/events")
# async def get_player_events(id: int, type: Optional[str] = None):
#     for player in players:
#         if player.id == id:
#             if type and type not in ["level_started", "level_solved"]:
#                 raise HTTPException(status_code=400, detail="Bad Request")
#             filtered_events = []
#             for event in player.events:
#                 if not type or event["type"] == type:
#                     filtered_events.append({
#                         "id": event["id"], 
#                         "type": event["type"], 
#                         "detail": event["detail"], 
#                         "timestamp": event["timestamp"], 
#                         "player_id": event["player_id"]
#                     })
#             return filtered_events
#     # Jos pelaajaa ei löydy, palautetaan 404
#     raise HTTPException(status_code=404, detail="Player not found")


# @router.post("/players/{id}/events", status_code=201)
# async def create_player_event(id: int, type: str, detail: str):
#     for player in players:
#         if player.id == id:
#             # Tarkistetaan, et oikea type on kelvollinen, muuten 400
#             if type not in ["level_started", "level_solved"]:
#                 raise HTTPException(status_code=400, detail="Unknown event type")
#             # Luodaan datetime-olio nykyisestä ajasta
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             event = {"id": len(player.events) + 1, "type": type, "detail": detail, "player_id": id, "timestamp": timestamp}
#             player.events.append(event)
#             return event
#      # Jos pelaajaa ei löydy, palautetaan 404
#     raise HTTPException(status_code=404, detail="Player not found")


from fastapi import APIRouter
from typing import List, Optional
from datetime import datetime
from app.database.models import PlayerIn, PlayerDb, Event, EventIn
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import ValidationError


router = APIRouter()

players: List[PlayerDb] = []

class PlayerResponse(BaseModel):
    id: int
    name: str

@router.get("/players", status_code=200, response_model=List[PlayerResponse])
async def get_players():
    player_responses = []
    for player in players:
        player_responses.append(PlayerResponse(id=player.id, name=player.name))
    return player_responses

@router.post("/players", status_code=201, response_model=PlayerResponse)
async def create_player(player: PlayerIn):
    if not player.name:
        return JSONResponse(content={"error": "Name cannot be empty"}, status_code=422)
    id = len(players) + 1
    player_db = PlayerDb(id=id, name=player.name, events=[])
    players.append(player_db)
    return PlayerResponse(id=player_db.id, name=player_db.name)


@router.get("/players/{id}")
async def get_player(id: int):
    for player in players:
        if player.id == id:
            return player
    raise HTTPException(status_code=404, detail="Player not found")

@router.get("/players/{id}/events")
async def get_player_events(id: int, type: Optional[str] = None):
    for player in players:
        if player.id == id:
            if type and type not in ["level_started", "level_solved"]:
                raise HTTPException(status_code=400, detail="Unknown event type")
            filtered_events = []
            for event in player.events:
                if not type or event.type == type:
                    filtered_events.append(event)
            return filtered_events
    raise HTTPException(status_code=404, detail="Player not found")


@router.post("/players/{id}/events", status_code=201, response_model=Event)
async def create_player_event(id: int, event: EventIn):
    for player in players:
        if player.id == id:
            if event.type not in ["level_started", "level_solved"]:
                raise HTTPException(status_code=400, detail="Unknown event type")
            
            #Tarkistaa, onko Event luokan validointi onnistunu
            try:
                event_db = Event(
                    id=len(player.events) + 1,
                    type=event.type,
                    detail=event.detail,
                    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    player_id=id
                )
            except ValidationError as e:
                raise HTTPException(status_code=422, detail=str(e))
            
            player.events.append(event_db)
            return event_db
    
    raise HTTPException(status_code=404, detail="Player not found")
