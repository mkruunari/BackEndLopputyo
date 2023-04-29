from typing import Optional
from datetime import datetime
from fastapi import APIRouter
from typing import List
from fastapi import HTTPException
from app.routers.players import players
router = APIRouter()

#tehdään Event luokka, jossa tarvittavat elementit
class Event:
    def __init__(self, id: int, type: str, detail: str, player_id: int):
        self.id = id
        self.type = type
        self.detail = detail
        self.player_id = player_id
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

events_db = []

@router.get("/events")
async def get_events(type: Optional[str] = None):
    if type and type not in ["level_started", "level_solved"]:
        raise HTTPException(status_code=400, detail="Unknown event type")

    filtered_events = []
    for player in players:
        for event in player.events:
            if not type or event["type"] == type:
                filtered_events.append({
                    "id": event["id"],
                    "type": event["type"],
                    "detail": event["detail"],
                    "player_id": event["player_id"],
                    "timestamp": event["timestamp"]
                })
    
    if not filtered_events:
        return []

    return filtered_events



