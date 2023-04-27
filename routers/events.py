from typing import Optional
from datetime import datetime
from fastapi import APIRouter
from typing import List

#from .models import Player, PlayerCreate, PlayerInDB

router = APIRouter()

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
    if type:
        if type not in ["level_started", "level_solved"]:
            return {"error": "Bad Request"}, 400
        filtered_events = [{"id": event.id, "type": event.type, "detail": event.detail, "timestamp": event.timestamp, "player_id": event.player_id} for event in events_db if event.type == type]
        return filtered_events
    else:
        return [{"id": event.id, "type": event.type, "detail": event.detail, "timestamp": event.timestamp, "player_id": event.player_id} for event in events_db]

@router.post("/events")
async def create_event(type: str, detail: str, player_id: int):
    if type not in ["level_started", "level_solved"]:
        return {"error": "Bad Request"}, 400
    id = len(events_db) + 1
    event = Event(id, type, detail, player_id)
    events_db.append(event)
    return {"id": id, "type": type, "detail": detail, "timestamp": event.timestamp, "player_id": player_id}
