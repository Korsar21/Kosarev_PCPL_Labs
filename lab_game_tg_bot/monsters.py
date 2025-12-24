import random

class Monster:
    def __init__(self, name: str, health: int, damage: int, level: int):
        self.name = name
        self.health = health
        self.damage = damage
        self.level = level

monsters: list[Monster] = [
    Monster("Горилла \U0001f98d", random.randint(8, 12), random.randint(5, 7), 0),
    Monster("Пламяный огр \U0001f525", random.randint(12, 18), random.randint(8, 10), 2),
    Monster("Скелет-великан 💀", random.randint(15, 20), random.randint(6, 9), 4),
    Monster("Тень-убийца 👤", random.randint(35, 50), random.randint(15, 20), 4),
    Monster("Ночной призрак 👻", random.randint(40, 60), random.randint(18, 22), 4),
    Monster("Тролль вепрь \U0001f417", random.randint(20, 25), random.randint(10, 12), 6),
    Monster("Темный рыцарь ⚔️", random.randint(40, 55), random.randint(18, 22), 6),
    Monster("Чёрный волк \U0001f43a", random.randint(70, 85), random.randint(30, 35), 6),
    Monster("Громовая птица \U0001f426", random.randint(50, 65), random.randint(20, 25), 8),
    Monster("Маг-колдун 🧙‍♂️", random.randint(25, 30), random.randint(12, 15), 8),
    Monster("Гигантский паук 🕷", random.randint(30, 40), random.randint(14, 17), 10),
    Monster("Циклоп \U0001f9d1", random.randint(55, 70), random.randint(22, 28), 10),
    Monster("Турнирный гладиатор 🏆", random.randint(45, 60), random.randint(20, 25), 10),
    Monster("Вогненный феникс 🔥", random.randint(55, 70), random.randint(25, 30), 12),
    Monster("Змей-Горыныч 🐉", random.randint(40, 50), random.randint(18, 22), 12),
    Monster("Древний страж \U0001f9cd", random.randint(45, 55), random.randint(20, 25), 14),
    Monster("Царевич-демон 👑", random.randint(60, 80), random.randint(25, 30), 14),
    Monster("Рогатый демон 🦑", random.randint(70, 85), random.randint(30, 35), 14),
    Monster("Лавовый монстр \U0001f47f", random.randint(80, 100), random.randint(35, 40), 14),
    Monster("Древний феникс \U0001f989", random.randint(75, 90), random.randint(30, 35), 16),
    Monster("Змей-амфибия 🐍", random.randint(80, 95), random.randint(35, 40), 16),
    Monster("Титан из недр Земли 🗿", random.randint(100, 130), random.randint(45, 50), 20),
    Monster("Ледяной дракон 🐉❄️", random.randint(50, 70), random.randint(25, 30), 20),
    Monster("Голем из стали ⚙️", random.randint(100, 120), random.randint(40, 45), 20),
    Monster("Темный дракон \U0001f409", random.randint(90, 110), random.randint(40, 45), 18),
    Monster("Космическая тварь \U0001f47e", random.randint(80, 100), random.randint(35, 40), 18),
    Monster("Мифический Лев \U0001f981", random.randint(70, 90), random.randint(28, 35), 18),
    Monster("Властелин Бездны", random.randint(60, 80), random.randint(25, 30), 16),
    Monster("Гигантская гидра 🐍", random.randint(60, 75), random.randint(30, 35), 22),
    Monster("Призрачный вестник ⚰️", random.randint(120, 140), random.randint(50, 55), 22)
]
