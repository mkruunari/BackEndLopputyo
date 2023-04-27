from fastapi import APIRouter
from typing import List, Optional
from datetime import datetime
from database.models import Player

router = APIRouter()

players = []

@router.get("/players")
async def get_players():
    # return players
    return [{"id": player.id, "name": player.name} for player in players]

@router.post("/players")
async def create_player(name: str):
    id = len(players) + 1
    player = Player(id, name)
    players.append(player)
    return {"id": id, "name": name}

@router.get("/players/{id}")
async def get_player(id: int):
    for player in players:
        if player.id == id:
            return player
    return {"message": "Player not found"}

@router.get("/players/{id}/events")
async def get_player_events(id: int, type: str = None):
    for player in players:
        if player.id == id:
            if type:
                return [{"id": event["id"], "type": event["type"], "detail": event["detail"], "timestamp": event["timestamp"], "player_id": event["player_id"]} for event in player.events if event["type"] == type]
            else:
                return [{"id": event["id"], "type": event["type"], "detail": event["detail"], "timestamp": event["timestamp"], "player_id": event["player_id"]} for event in player.events]
    return {"message": "Player not found"}


@router.post("/players/{id}/events")
async def create_player_event(id: int, type: str, detail: str):
    for player in players:
        if player.id == id:
            # Luodaan datetime-olio nykyisestä ajasta
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            event = {"id": len(player.events) + 1, "type": type, "detail": detail, "player_id": id, "timestamp": timestamp}
            player.events.append(event)
            return event
    return {"message": "Player not found"}
