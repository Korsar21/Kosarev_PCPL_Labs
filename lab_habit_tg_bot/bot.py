import telebot, logging, time

from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from enum import Enum

COMPLETED = "Выполнил"
LATER = "Позже"
READY = "Погнали"
CONGRATS = "Ура!"
FAILURE = "Эхх"

#ONE_HOUR_DELAY = 60 * 60
#TIME_TO_SLEEP = 60 * 60 * 24

ONE_HOUR_DELAY = 2
TIME_TO_SLEEP = 10

class HabitState(Enum):
    SAVE_HABIT = 1
    SAVE_PERIOD = 2
    NOT_STARTED = 3
    IN_PROGRESS = 4
    FINISHED = 5

class Bot:
    def __init__(self, token: str):
        self.bot = telebot.TeleBot(token)
        self.current_state = HabitState.SAVE_HABIT
        self.habit = ""
        self.period = 0
        self.day_counter = 1
        self.exercise_done = False
        self.delta_delay = 0

    def start_work(self):
        self.bot.polling(none_stop=True, logger_level=logging.INFO)

    def init_handlers(self):
        @self.bot.message_handler(func=lambda message: self.current_state == HabitState.SAVE_HABIT)
        def save_habit(message: Message):
            self.bot.send_message(message.chat.id, "Напишите название привычки, которую Вы хотите привить", reply_markup=ReplyKeyboardRemove())
            self.current_state = HabitState.SAVE_PERIOD

        @self.bot.message_handler(func=lambda message: self.current_state == HabitState.SAVE_PERIOD)
        def save_period(message: Message):
            self.habit = message.text
            self.bot.send_message(message.chat.id, "Сколько дней подряд Вы хотите заниматься?")
            self.current_state = HabitState.NOT_STARTED

        @self.bot.message_handler(func=lambda message: self.current_state == HabitState.NOT_STARTED)
        def not_started_handler(message: Message):
            try:
                self.period = int(message.text)
            except ValueError:
                self.bot.send_message(message.chat.id,"Введите число!")
                return

            keyboard = ReplyKeyboardMarkup(row_width=1)
            button_ready = KeyboardButton(READY)
            keyboard.add(button_ready)
            self.bot.send_message(message.chat.id, f"Ваша привычка {self.habit}\nСколько дней Вы хотите заниматься: {self.period}\n", reply_markup=keyboard)
            self.current_state = HabitState.IN_PROGRESS

        @self.bot.message_handler(func=lambda message: self.current_state == HabitState.IN_PROGRESS)
        def in_progress_handlers(message: Message):
            if message.text == COMPLETED:
                self.bot.send_message(message.chat.id,f"День {self.day_counter}:\nЗадание на сегодня выполнено! Вы молодец!", reply_markup=ReplyKeyboardRemove())
                self.day_counter += 1
                if self.day_counter > self.period:
                    self.current_state = HabitState.FINISHED
                    keyboard = ReplyKeyboardMarkup(row_width=1)
                    button_challenge_done = KeyboardButton(CONGRATS)
                    keyboard.add(button_challenge_done)
                    self.bot.send_message(message.chat.id,"Это был последний день!", reply_markup=keyboard)
                    return
                time.sleep(TIME_TO_SLEEP - self.delta_delay)
                self.delta_delay = 0
            if message.text == LATER:
                self.bot.send_message(message.chat.id,f"Хорошо, напомню попозже", reply_markup=ReplyKeyboardRemove())
                time.sleep(ONE_HOUR_DELAY)
                self.delta_delay += ONE_HOUR_DELAY
                if self.delta_delay > TIME_TO_SLEEP:
                    keyboard = ReplyKeyboardMarkup(row_width=1)
                    button_fail_challenge = KeyboardButton(FAILURE)
                    keyboard.add(button_fail_challenge)
                    self.bot.send_message(message.chat.id,"Вы слишком много откладывали! Челлендж провален!", reply_markup=keyboard)
                    self.current_state = HabitState.SAVE_HABIT
                    return

            keyboard = ReplyKeyboardMarkup(row_width=1)
            button_completed_exercise = KeyboardButton(COMPLETED)
            keyboard.add(button_completed_exercise)
            button_later = KeyboardButton(LATER)
            keyboard.add(button_later)
            self.bot.send_message(message.chat.id,f"День {self.day_counter}:\nВам надо сегодня выполнить упражнение по вашей привычке '{self.habit}'", reply_markup=keyboard)

        @self.bot.message_handler(func=lambda message: self.current_state == HabitState.FINISHED)
        def finished_handlers(message: Message):
            self.bot.send_message(message.chat.id,f"Поздравляем! День {self.period}/{self.period}\nВы привили себе привычку '{self.habit}'!", reply_markup=ReplyKeyboardRemove())
            self.bot.send_message(message.chat.id,"Чтобы привить новую привычку нажмите /start")
            self.current_state = HabitState.SAVE_HABIT
            self.day_counter = 1



