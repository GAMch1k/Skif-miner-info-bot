# Markups list here

# Imports

from telebot import types


# Fast buttons
back_btn = types.KeyboardButton("Нозад")
empty = types.ReplyKeyboardRemove()
# -------------------------------------------------------------

menu_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
info = types.KeyboardButton("Чё там?")
transactions = types.KeyboardButton("Шо по щекелям?")
settings = types.KeyboardButton("Сэтингс")

menu_main.add(info, transactions, settings)
# -------------------------------------------------------------

menu_settings = types.ReplyKeyboardMarkup(resize_keyboard=True)
id_change = types.KeyboardButton("Ид поменять")

menu_settings.add(id_change, back_btn)
# -------------------------------------------------------------

back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_markup.add(back_btn)
