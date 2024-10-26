import telebot
import buttons as bt
from geopy import Photon

geolocator = Photon(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0")

bot = telebot.TeleBot("7164617373:AAHPH2ns15ayAOc1R_NllyO2jNENr1udDbw")
# Создаём словарь для хранения данных пользователя
users_data = {}

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "ЗдАрово чувак и вэлкам в бот python_warriors!")
    bot.send_message(user_id, "Как тебя записать-то, не салагой же? Давай, шустро вводи имечко своё")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_id = message.from_user.id
    name = message.text
    bot.send_message(user_id, "Теперь номер дебильника, то есть мобильника", reply_markup=bt.phone_buttons())
    bot.register_next_step_handler(message, get_phone_number, name)

def get_phone_number(message, name):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        bot.send_message(user_id, "Локацию свою вбей", reply_markup=bt.location_button())
        bot.register_next_step_handler(message, get_location, name, phone_number)
    else:
        bot.send_message(user_id, "Альтернативно одарённый что-ли? Отправь через кнопку меню")
        bot.register_next_step_handler(message, get_phone_number, name)

def get_location(message, name, phone_number):
    user_id = message.from_user.id
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        address = geolocator.reverse((latitude, longitude)).address
        db.add_user(user_id, name, phone_number, address)  # Сохраняем данные пользователя в базе данных
        bot.send_message(user_id, "Наконец-то, гратс! ты успешно зарегился!")
    else:
        bot.send_message(user_id, "Слепошара, отправь ЧЕРЕЗ кнопку меню")
        bot.register_next_step_handler(message, get_location, name, phone_number)

bot.infinity_polling()
