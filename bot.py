# This is "Skif-miner-info-bot" which was created by:
#  _______ _______ _______        __     ____   __    
# |     __|   _   |   |   |.----.|  |--.|_   | |  |--.
# |    |  |       |       ||  __||     | _|  |_|    < 
# |_______|___|___|__|_|__||____||__|__||______|__|__|
#                                              GAMch1k
# © 2022 GAMch1k studio


# Imports

import telebot
from assets import config
from assets.databaseAPI import *
from assets.stuff import *
from assets.markups import *


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(
        message.chat.id,
        f'Даров, {message.from_user.first_name}, это майнинг бот!\nЧе хочешь?',
        reply_markup=menu_main)
    new_user(message.chat.id)


@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.chat.type == 'private':
        if message.text == 'Чё там?':
            bot.send_message(message.chat.id, 'Ну вот кароче')

        elif message.text == 'Шо по щекелям?':
            bot.send_message(message.chat.id, 'Еба нихуёво так')

        elif message.text == 'Сэтингс':
            send = bot.send_message(
                message.chat.id,
                'Нихуя ты настройщек кншн',
                reply_markup=menu_settings)
            bot.register_next_step_handler(
                send, settings_menu
            )


@bot.message_handler(content_types=['text'])
def settings_menu(message):
    if message.chat.type == 'private':
        if message.text == 'Ид поменять':
            send = bot.send_message(
                message.chat.id,
                'Вставляй свой ид\nВставишь не тот - тебе пизда',
                reply_markup=back_markup)
            bot.register_next_step_handler(
                send, change_id_process
            )

        elif message.text == 'Нозад':
            send = bot.send_message(
                message.chat.id,
                'Пиздуй отселя',
                reply_markup=menu_main)
            bot.register_next_step_handler(
                send, main_menu
            )


@bot.message_handler(content_types=['text'])
def change_id_process(message):
    if message.chat.type == 'private':
        if message.text == 'Нозад':
            send = bot.send_message(
                message.chat.id,
                'Пиздуй отселя',
                reply_markup=menu_main)
            bot.register_next_step_handler(
                send, main_menu
            )
        else:
            add_nh_id(message.chat.id, message.text)

            send = bot.send_message(
                message.chat.id,
                'Ид изменён. Себастиан отсюда',
                reply_markup=menu_main)
            bot.register_next_step_handler(
                send, main_menu
            )


bot.polling(none_stop=True, timeout=123)
