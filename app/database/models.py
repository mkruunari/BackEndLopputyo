from datetime import datetime
class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.events = []
class Event:
    def __init__(self, id, type, detail, player_id):
        self.id = id
        self.type = type
        self.detail = detail
        self.timestamp = datetime.now()
        self.player_id = player_id
