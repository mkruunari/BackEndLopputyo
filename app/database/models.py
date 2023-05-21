# from datetime import datetime
# #Player ja Class luokat, ja niiden tarvittavat attribuutit
# class Player:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         self.events = []
# class Event:
#     def __init__(self, id, type, detail, player_id):
#         self.id = id
#         self.type = type
#         self.detail = detail
#         self.timestamp = datetime.now()
#         self.player_id = player_id


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
    