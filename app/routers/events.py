from typing import Optional
from datetime import datetime
from fastapi import APIRouter
from typing import List
from fastapi import HTTPException
from app.database.models import Event
from app.routers.players import players

router = APIRouter()

@router.get("/events")
async def get_events(type: Optional[str] = None):
    if type and type not in ["level_started", "level_solved"]:
        raise HTTPException(status_code=400, detail="Unknown event type")

    filtered_events = []
    for player in players:
        for event in player.events:
            if not type or event.type == type:
                filtered_events.append(event)
    
    if not filtered_events:
        return []

    return filtered_events
