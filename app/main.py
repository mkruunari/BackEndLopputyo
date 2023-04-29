from typing import List, Optional
from fastapi import FastAPI
from datetime import datetime
from app.routers import players, events 

app = FastAPI()

app.include_router(players.router)
app.include_router(events.router)

# events_db = [
#     {
#         "id": 1123,
#         "type": "level_started",
#         "detail": "level_1212_001",
#         "timestamp": "2023-01-13 12:01:22",
#         "player_id": 1
#     },
#     {
#         "id": 1144,
#         "type": "level_solved",
#         "detail": "level_1333_034",
#         "timestamp": "2023-01-24 18:13:29",
#         "player_id": 4
#     }
# ]

# @app.get("/events")
# async def get_events(type: Optional[str] = None):
#     if type:
#         if type not in ["level_started", "level_solved"]:
#             return {"error": "Bad Request"}, 400
#         filtered_events = [{"id": event["id"], "type": event["type"], "detail": event["detail"], "timestamp": event["timestamp"], "player_id": event["player_id"]} for event in events_db if event["type"] == type]
#         return filtered_events
#     else:
#         return [{"id": event["id"], "type": event["type"], "detail": event["detail"], "timestamp": event["timestamp"], "player_id": event["player_id"]} for event in events_db]



# # players = []

# # class Player:
# #     def __init__(self, id, name):
# #         self.id = id
# #         self.name = name
# #         self.events = []

# # @app.get("/players")
# # async def get_players():
# #     return players

# # @app.post("/players")
# # async def create_player(name: str):
# #     id = len(players) + 1
# #     player = Player(id, name)
# #     players.append(player)
# #     return {"id": id, "name": name}

# # @app.get("/players/{id}")
# # async def get_player(id: int):
# #     for player in players:
# #         if player.id == id:
# #             return player
# #     return {"message": "Player not found"}

# # @app.get("/players/{id}/events")
# # async def get_player_events(id: int, type: str = None):
# #     for player in players:
# #         if player.id == id:
# #             if type:
# #                 return [event for event in player.events if event["type"] == type]
# #             else:
# #                 return player.events
# #     return {"message": "Player not found"}
# @app.get("/players/{id}/events")
# async def get_player_events(id: int, type: str = None):
#     for player in players:
#         if player.id == id:
#             if type:
#                 return [{"id": event["id"], "type": event["type"], "detail": event["detail"], "timestamp": event["timestamp"], "player_id": event["player_id"]} for event in player.events if event["type"] == type]
#             else:
#                 return [{"id": event["id"], "type": event["type"], "detail": event["detail"], "timestamp": event["timestamp"], "player_id": event["player_id"]} for event in player.events]
#     return {"message": "Player not found"}



# @app.post("/players/{id}/events")
# async def create_player_event(id: int, type: str, detail: str):
#     for player in players:
#         if player.id == id:
#             # Luodaan datetime-olio nykyisestä ajasta
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             event = {"id": len(player.events) + 1, "type": type, "detail": detail, "player_id": id, "timestamp": timestamp}
#             player.events.append(event)
#             return event
#     return {"message": "Player not found"}


#ens kerralla kaikki laitetaan databaseen