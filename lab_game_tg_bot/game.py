from room import Room
from player import Player

class Game:
    def __init__(self, room: Room, player: Player, counter_room: int):
        self.current_room = room
        self.user = player
        self.counter_room = counter_room