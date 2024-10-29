from telebot import types

# Кнопки для выбора языка
def language_buttons():
    kb = types.InlineKeyboardMarkup()
    btn_ru = types.InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")
    btn_uz = types.InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="lang_uz")
    kb.add(btn_ru, btn_uz)
    return kb

# Кнопки для телефона и локации
def phone_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("📞 Отправить номер", request_contact=True)
    kb.add(button)
    return kb

def location_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("📍 Отправить локацию", request_location=True)
    kb.add(button)
    return kb
