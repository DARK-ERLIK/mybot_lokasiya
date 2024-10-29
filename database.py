import sqlite3
from datetime import datetime
connection = sqlite3.connect("mybot.db")

# Функция для инициализации базы данных и создания таблицы пользователей
def init_db():
    connection = sqlite3.connect("mybot.db")
    sql = connection.cursor()
    sql.execute("CREATE TABLE IF NOT EXISTS users "
        "(user_id INTEGER PRIMARY KEY, name TEXT, "
        "phone_number TEXT, address TEXT, "
        "reg_date DATETIME, language TEXT);")
    connection.commit()
    connection.close()

# Функция для добавления пользователя в базу данных
def add_user(user_id, name, phone_number, address, language):
    connection = sqlite3.connect("mybot.db")
    sql = connection.cursor()
    sql.execute("INSERT INTO users (user_id, name, phone_number, address, reg_date, language) VALUES (?, ?, ?, ?, ?, ?)",
                (user_id, name, phone_number, address, datetime.now(), language))
    connection.commit()
    connection.close()
