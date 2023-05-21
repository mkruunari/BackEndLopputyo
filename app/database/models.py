from datetime import datetime
from typing import List
from pydantic import BaseModel, ValidationError, validator

class PlayerIn(BaseModel):
    name: str

#tarvitaan @router.post("/players/{id}/events"  
class EventIn(BaseModel):
    type: str
    detail: str

    #laukasee statuskoodi 422
    @validator('detail')
    def check_detail(cls, detail):
        if not detail:
            raise ValueError("Detail cannot be empty")
        return detail

class Event(BaseModel):
    id: int
    type: str
    detail: str
    timestamp: datetime
    player_id: int

class PlayerDb(BaseModel):
    id: int
    name: str
    events: List[Event]
    