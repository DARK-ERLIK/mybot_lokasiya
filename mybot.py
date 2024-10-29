import telebot
import buttons  # импортируем файл с кнопками
from geopy import Photon
from database import add_user, init_db  # импортируем функцию init_db для инициализации базы

# Инициализация базы данных
init_db()

# Инициализация бота и геолокатора
geolocator = Photon(user_agent="Mozilla/5.0")
bot = telebot.TeleBot("7164617373:AAHPH2ns15ayAOc1R_NllyO2jNENr1udDbw")
# Создаём словарь для хранения данных пользователя
users_data = {}

# Обработка команды "/start"
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Добро пожаловать! Пожалуйста, выберите язык:", reply_markup=buttons.language_buttons())

# Обработка выбора языка
@bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
def set_language(call):
    user_id = call.from_user.id
    lang = "ru" if call.data == "lang_ru" else "uz"
    users_data[user_id] = {"language": lang}
    msg = "Введите своё имя:" if lang == "ru" else "Ismingizni kiriting:"
    bot.send_message(user_id, msg)
    bot.register_next_step_handler_by_chat_id(user_id, get_name)

# Получение имени пользователя
def get_name(message):
    user_id = message.from_user.id
    name = message.text
    users_data[user_id]["name"] = name
    lang = users_data[user_id]["language"]
    msg = "Теперь отправьте свой номер телефона:" if lang == "ru" else "Telefon raqamingizni yuboring:"
    bot.send_message(user_id, msg, reply_markup=buttons.phone_button())
    bot.register_next_step_handler(message, get_phone_number)

# Получение номера телефона пользователя
def get_phone_number(message):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact.phone_number
        users_data[user_id]["phone_number"] = phone_number
        lang = users_data[user_id]["language"]
        msg = "Теперь отправьте свою локацию:" if lang == "ru" else "Endi joylashuvingizni yuboring:"
        bot.send_message(user_id, msg, reply_markup=buttons.location_button())
        bot.register_next_step_handler(message, get_location)
    else:
        bot.send_message(user_id, "Пожалуйста, используйте кнопку для отправки номера.")
        bot.register_next_step_handler(message, get_phone_number)

# Получение локации пользователя
def get_location(message):
    user_id = message.from_user.id
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        address = geolocator.reverse((latitude, longitude)).address
        lang = users_data[user_id]["language"]

        # Сохранение данных в базу
        add_user(user_id, users_data[user_id]["name"], users_data[user_id]["phone_number"], address, lang)

        # Подтверждение
        msg = "Регистрация завершена!" if lang == "ru" else "Ro'yxatdan o'tish yakunlandi!"
        bot.send_message(user_id, msg)
    else:
        bot.send_message(user_id, "Пожалуйста, используйте кнопку для отправки локации.")
        bot.register_next_step_handler(message, get_location)

bot.infinity_polling()
