from typing import List, Optional
from fastapi import FastAPI
from datetime import datetime
from app.routers import players, events 

app = FastAPI()

app.include_router(players.router)
app.include_router(events.router)

