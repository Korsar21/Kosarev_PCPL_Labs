import random
from weapons import Weapon
from potion import Potion
from typing import Optional


class Player:
    def __init__(self, name: str, weapon: Weapon):
        self.name = name
        self.health = 50
        self.weapon = weapon
        self.potion = None
        self.win_key = False


