import random
import copy
from typing import Optional

from weapons import Weapon, weapons
from monsters import monsters
from potion import Potion

symbols = ["\U0001f7e0", #оранжевый круг
           "\U0001f7e3", #фиолетовый круг
           "\U0001f53a", #треугольник вершиной вверх
           "\U0001f53b", #треугольник вершиной вниз
           "\U0001f7ea", #фиолетовый квадрат
           "\U0001f7e9", #зелёный квадрат
]

class Room:
    def __init__(self, counter_room: int, parent_room: Optional["Room"] = None, create_win_key: Optional[bool] = True):
        is_monster = random.randint(0, 100)
        self.monster = None
        self.is_monster_alive = False
        if is_monster > 20:
            self.monster = copy.deepcopy(random.choice(monsters))
            while not self.monster.level <= counter_room:
                self.monster = copy.deepcopy(random.choice(monsters))
            self.is_monster_alive = True

        is_weapon = random.randint(0, 100)
        self.weapon = None
        if is_weapon > 50:
            self.weapon = random.choice(weapons)
            while not self.weapon.level <= counter_room:
                self.weapon = random.choice(weapons)

        is_potion = random.randint(0, 100)
        self.potion = None
        if is_potion > 30:
            self.potion = Potion()

        self.is_quest = False
        self.combination_symbols = []
        is_quest = random.randint(0, 100)
        if is_quest <= 30:
            self.is_quest = True
            for i in range(1, 4):
                self.combination_symbols.append(random.choice(symbols))

        self.win_key = False
        is_win_key = random.randint(0,100)
        if self.is_quest:
            chance_win_key = 20
        else:
            chance_win_key = 5
        if is_win_key <= chance_win_key and create_win_key:
            self.win_key = True

        definitely_create_room = random.randint(1, 4)

        self.is_front_room = False
        is_front_room = random.randint(0, 100)
        if is_front_room >= 50 or definitely_create_room == 1:
            self.is_front_room = True

        self.is_left_room = False
        is_left_room = random.randint(0, 100)
        if is_left_room >= 50 or definitely_create_room == 2:
            self.is_left_room = True

        self.is_right_room = False
        is_right_room = random.randint(0, 100)
        if is_right_room >= 50 or definitely_create_room == 3:
            self.is_right_room = True



        self.parent_room = parent_room
        self.front_room = None
        self.left_room = None
        self.right_room = None


