import random

from pyexpat.errors import messages
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telebot import REPLY_MARKUP_TYPES

from player import Player
from weapons import Weapon
from room import Room

FIGHT_BUTTON_NAME = "Нанести урон"
CHANGE_WEAPON_BUTTON = "Поменять оружие"
GO_FORWARD = "Вперёд"
GO_LEFT = "Налево"
GO_RIGHT = "Направо"
GO_BACK = "Назад"
TAKE_KEY = "Взять ключ"
TAKE_POTION = "Взять зелье"
DRINK_POTION = "Выпить зелье"
READY_QUEST = "Выполнить квест"

def fight(current_room: Room, player: Player) -> tuple [str, str, bool]:
    current_room.monster.health = current_room.monster.health - player.weapon.damage
    monster_health_info = "Удар по монстру"
    player_health_info: str = "Вы убили монстра!"
    if current_room.monster.health <= 0:
        current_room.is_monster_alive = False
    else:
        player.health = player.health - current_room.monster.damage
        player_health_info = "Вас ударил монстр \U0001F494"
    player_alive = True
    if player.health <= 0:
        player_alive = False
    return monster_health_info, player_health_info, player_alive

def change_weapon(current_room: Room, player: Player) -> str:
    term: Weapon = player.weapon
    player.weapon = current_room.weapon
    current_room.weapon = term
    message = "Вы заменили оружие"
    return message

def take_potion(current_room: Room, player: Player) -> str:
    if player.potion is not None:
        player.potion.amount_restored_health = int((player.potion.amount_restored_health + current_room.potion.amount_restored_health) * 1.1)
        message = "Вы пополнили зелье"
    else:
        player.potion = current_room.potion
        message = "Вы взяли зелье"
    current_room.potion = None
    return message

def drink_potion(player: Player) -> str:
    player.health = player.health + player.potion.amount_restored_health
    player.potion = None
    message = "Вы выпили зелье"
    return message

# 1) запоминать current_room в новую current_room
# 2) для родительской (current_room) указать, связанные с ней комнаты (next_room)
# 3) присвоить current_room next_room

def transition_room(counter_room: int, current_room: Room, direction: str) -> tuple[str, Room, bool, bool]:
    is_new_room: bool = False
    if not current_room.front_room and direction == GO_FORWARD:
        current_room.front_room = Room(counter_room, current_room)
        is_new_room = True
    if not current_room.left_room and direction == GO_LEFT:
        current_room.left_room = Room(counter_room, current_room)
        is_new_room = True
    if not current_room.right_room and direction == GO_RIGHT:
        current_room.right_room = Room(counter_room, current_room)
        is_new_room = True

    if current_room.front_room and direction == GO_FORWARD:
        current_room = current_room.front_room
    if current_room.left_room and direction == GO_LEFT:
        current_room = current_room.left_room
    if current_room.right_room and direction == GO_RIGHT:
        current_room = current_room.right_room

    if current_room.is_quest:
        return "Квест! Чтобы перейти в комнату надо его выполнить", current_room, True, True

    message = "Вы перешли в другую комнату"
    return message, current_room, False, is_new_room

def go_back_room(current_room: Room) -> tuple[str, Room]:
    return "Вы вернулись в предыдущую комнату", current_room.parent_room

def status_game(current_room: Room, player: Player) -> tuple [str,  REPLY_MARKUP_TYPES]:
    if player.health <= 0:
        return "Вы проиграли текущую игру \U0001f480 \nНажмите /start для начала новой", ReplyKeyboardRemove()
    if player.win_key:
        return  "Ключ в руке! Вы победили! \U0001F3C6 \nНажмите /start для начала новой игры", ReplyKeyboardRemove()

    keyboard = ReplyKeyboardMarkup(row_width=3)
    message: str = f"{player.name}: {player.health} \U0001F90D \n{player.weapon.type}, урон: {player.weapon.damage} \U0001f3af\n"
    if player.potion is not None:
        button_drink_potion = KeyboardButton(DRINK_POTION)
        keyboard.add(button_drink_potion)
        message = message + f"Зелье: {player.potion.amount_restored_health} \U0001f499"
    if current_room.is_monster_alive or current_room.win_key or current_room.weapon is not None:
        message = message + "\n\nКомната:\n"
    if current_room.win_key:
        if current_room.is_monster_alive or current_room.is_quest:
            if current_room.is_monster_alive:
                message = message + f"Есть ключ! \U0001F511 Чтобы его получить - убейте монстра!\n"
            if current_room.is_quest:
                message = message + f"Есть ключ! \U0001F511 Чтобы его получить - пройди квест!\n"
        else:
            message = message + f"Есть ключ! \U0001F511 \n"
            button_take_key = KeyboardButton(TAKE_KEY)
            keyboard.add(button_take_key)

    if current_room.is_monster_alive:
        button_fight = KeyboardButton(FIGHT_BUTTON_NAME)
        keyboard.add(button_fight)
        message = message + f"Есть монстр: {current_room.monster.name}, {current_room.monster.damage} \U0001f3af, {current_room.monster.health} \U0001F5A4 \n"
    if current_room.weapon is not None:
        button_take_weapon = KeyboardButton(CHANGE_WEAPON_BUTTON)
        keyboard.add(button_take_weapon)
        message = message + f"Есть оружие: {current_room.weapon.type}, {current_room.weapon.damage} \U0001f3af \n"
    if current_room.potion is not None:
        button_take_potion = KeyboardButton(TAKE_POTION)
        keyboard.add(button_take_potion)
        message = message + f"Есть зелье \u2697\uFE0F: {current_room.potion.amount_restored_health} \U0001f499 \n"

    if not current_room.is_monster_alive:
        if current_room.is_front_room:
            button_go_front = KeyboardButton(GO_FORWARD)
            keyboard.add(button_go_front)
        if current_room.is_left_room:
            button_go_left = KeyboardButton(GO_LEFT)
            keyboard.add(button_go_left)
        if current_room.is_right_room:
            button_go_right = KeyboardButton(GO_RIGHT)
            keyboard.add(button_go_right)
    if current_room.parent_room:
        button_go_back = KeyboardButton(GO_BACK)
        keyboard.add(button_go_back)

    return message, keyboard


