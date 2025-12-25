import telebot, time

from game import Game
from message import *
from start_message import *

bot = telebot.TeleBot('6081763073:AAFqpS-UjiUM3yxRs66OSKMCkcUBJ4zUVfI')

sessions: dict[int, Game] = {}

@bot.message_handler(commands=['start'])
def before_handle_start(message: Message):
    bot.send_message(message.chat.id, welcome_message, parse_mode='HTML')
    bot.send_message(message.chat.id, "Введите имя персонажа")
    bot.register_next_step_handler(message, handle_start)

def handle_start(message: Message):
    global sessions

    knife = Weapon("Нож \U0001F5E1\uFE0F", 2, 0)
    player = Player(message.text, knife)
    current_room = Room(0, create_win_key=False)
    sessions[message.chat.id] = Game(current_room, player, 0)
    start_message, keyboard = status_game(current_room, player)

    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, start_message, reply_markup=keyboard)

#@bot.message_handler(content_types=['text'])
#def reaction_text(message: Message):
#    bot.send_message(message.chat.id, message.text)

def handle_quest(message: Message):
    global sessions

    result_no_space = "".join(sessions[message.chat.id].current_room.combination_symbols)

    if message.text == result_no_space:
        sessions[message.chat.id].current_room.is_quest = False
        bot.send_message(message.chat.id, "Квест пройден!")
    else:
        sessions[message.chat.id].current_room = sessions[message.chat.id].current_room.parent_room
        bot.send_message(message.chat.id, "Квест провален!")

    status_message, keyboard = status_game(sessions[message.chat.id].current_room, sessions[message.chat.id].user)
    bot.send_message(message.chat.id, status_message, reply_markup=keyboard)
    return

@bot.message_handler(content_types=['text'])
def handle_button(message: Message):
    global sessions

    if not message.chat.id in sessions:
        bot.send_message(message.chat.id, "Вызовите команду /start")
        return

    if message.text == FIGHT_BUTTON_NAME:
        monster_health_info, player_health_info, player_alive = fight(sessions[message.chat.id].current_room, sessions[message.chat.id].user)
        bot.send_message(message.chat.id, monster_health_info)
        bot.send_message(message.chat.id, player_health_info)

    if message.text == CHANGE_WEAPON_BUTTON:
        info_changed_weapon = change_weapon(sessions[message.chat.id].current_room, sessions[message.chat.id].user)
        bot.send_message(message.chat.id, info_changed_weapon)

    if message.text == TAKE_POTION:
        info_taken_potion = take_potion(sessions[message.chat.id].current_room, sessions[message.chat.id].user)
        bot.send_message(message.chat.id, info_taken_potion)

    if message.text == DRINK_POTION:
        info_drunk_potion = drink_potion(sessions[message.chat.id].user)
        bot.send_message(message.chat.id, info_drunk_potion)

    if message.text == GO_FORWARD or message.text == GO_LEFT or message.text == GO_RIGHT:
        info_changed_room, sessions[message.chat.id].current_room, is_quest, is_new_room = transition_room(sessions[message.chat.id].counter_room, sessions[message.chat.id].current_room, message.text)
        bot.send_message(message.chat.id, info_changed_room)
        if is_new_room:
            sessions[message.chat.id].counter_room += 1
        if is_quest:
            keyboard = ReplyKeyboardMarkup(row_width=1)
            button_ready_quest = KeyboardButton(READY_QUEST)
            keyboard.add(button_ready_quest)
            bot.send_message(message.chat.id, info_quest, reply_markup=keyboard, parse_mode='HTML')
            return

    if message.text == READY_QUEST:
        for i in range (len(sessions[message.chat.id].current_room.combination_symbols)):
            send_message = bot.send_message(message.chat.id, sessions[message.chat.id].current_room.combination_symbols[i], reply_markup=ReplyKeyboardRemove())
            time.sleep(0.09)
            bot.delete_message(message.chat.id, send_message.id)
        bot.register_next_step_handler(message, handle_quest)
        return

    if message.text == GO_BACK:
        info_changed_room, sessions[message.chat.id].current_room = go_back_room(sessions[message.chat.id].current_room)
        bot.send_message(message.chat.id, info_changed_room)

    if message.text == TAKE_KEY:
        sessions[message.chat.id].user.win_key = True

    status_message, keyboard = status_game(sessions[message.chat.id].current_room, sessions[message.chat.id].user)
    bot.send_message(message.chat.id, status_message, reply_markup=keyboard)

    if sessions[message.chat.id].user.health <= 0 or sessions[message.chat.id].user.win_key:
        del sessions[message.chat.id]

bot.polling(none_stop=True)
