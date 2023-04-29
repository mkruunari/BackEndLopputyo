from fastapi import APIRouter
from typing import List, Optional
from datetime import datetime
from app.database.models import Player
from fastapi.responses import JSONResponse
from fastapi import HTTPException
router = APIRouter()

players = []

@router.get("/players", status_code=200)
async def get_players():
    # return players
    return [{"id": player.id, "name": player.name} for player in players]

# @router.post("/players", status_code=201)
# async def create_player(name: str):
#     id = len(players) + 1
#     player = Player(id, name)
#     players.append(player)
#     return {"id": id, "name": name}


@router.post("/players", status_code=201)
async def create_player(name: str):
    if not name:
        return JSONResponse(content={"error": "Name cannot be empty"}, status_code=422)
    id = len(players) + 1
    player = Player(id, name)
    players.append(player)
    return {"id": id, "name": name}

@router.get("/players/{id}")
async def get_player(id: int):
    for player in players:
        if player.id == id:
            return player
    raise HTTPException(status_code=404, detail="Player not found")


# @router.get("/players/{id}")
# async def get_player(id: int):
#     for player in players:
#         if player.id == id:
#             return player
#     return {"message": "Player not found"}

@router.get("/players/{id}/events")
async def get_player_events(id: int, type: Optional[str] = None):
    for player in players:
        if player.id == id:
            if type and type not in ["level_started", "level_solved"]:
                raise HTTPException(status_code=400, detail="Bad Request")
            filtered_events = []
            for event in player.events:
                if not type or event["type"] == type:
                    filtered_events.append({
                        "id": event["id"], 
                        "type": event["type"], 
                        "detail": event["detail"], 
                        "timestamp": event["timestamp"], 
                        "player_id": event["player_id"]
                    })
            return filtered_events
    # Jos pelaajaa ei löydy, palauta 404
    raise HTTPException(status_code=404, detail="Player not found")


# @router.get("/players/{id}/events")
# async def get_player_events(id: int, type: str = None):
#     for player in players:
#         if player.id == id:
#             if type:
#                 return [{"id": event["id"], "type": event["type"], "detail": event["detail"], "timestamp": event["timestamp"], "player_id": event["player_id"]} for event in player.events if event["type"] == type]
#             else:
#                 if player.events:
#                     return [{"id": event["id"], "type": event["type"], "detail": event["detail"], "timestamp": event["timestamp"], "player_id": event["player_id"]} for event in player.events]
#                 else:
#                     return []
#     raise HTTPException(status_code=404, detail="Player not found")


# @router.get("/players/{id}/events")
# async def get_player_events(id: int, type: str = None):
#     for player in players:
#         if player.id == id:
#             if type:
#                 return [{"id": event["id"], "type": event["type"], "detail": event["detail"], "timestamp": event["timestamp"], "player_id": event["player_id"]} for event in player.events if event["type"] == type]
#             else:
#                 return [{"id": event["id"], "type": event["type"], "detail": event["detail"], "timestamp": event["timestamp"], "player_id": event["player_id"]} for event in player.events]
#     return {"message": "Player not found"}


@router.post("/players/{id}/events", status_code=201)
async def create_player_event(id: int, type: str, detail: str):
    for player in players:
        if player.id == id:
            # Tarkista, että annettu event-tyyppi on kelvollinen
            if type not in ["level_started", "level_solved"]:
                raise HTTPException(status_code=400, detail="Unknown event type")
            # Luodaan datetime-olio nykyisestä ajasta
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            event = {"id": len(player.events) + 1, "type": type, "detail": detail, "player_id": id, "timestamp": timestamp}
            player.events.append(event)
            return event
    # Jos pelaajaa ei löydy, palauta 404
    raise HTTPException(status_code=404, detail="Player not found")



# @router.post("/players/{id}/events")
# async def create_player_event(id: int, type: str, detail: str):
#     for player in players:
#         if player.id == id:
#             # Luodaan datetime-olio nykyisestä ajasta
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             event = {"id": len(player.events) + 1, "type": type, "detail": detail, "player_id": id, "timestamp": timestamp}
#             player.events.append(event)
#             return event
#     return {"message": "Player not found"}