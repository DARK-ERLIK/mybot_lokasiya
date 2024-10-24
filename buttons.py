from telebot import types

def phone_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Теперь номер дебильника, то есть мобильника", request_contact=True)
    kb.add(button)
    return kb

def location_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Локацию свою вбей", request_location=True)
    kb.add(button)
    return kb