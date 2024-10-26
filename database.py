# Функция для инициализации базы данных и создания таблицы пользователей
def init_db():
    connection = sqlite3.connect("mybot.db")
    sql = connection.cursor()

    # Создаем таблицу пользователей, если она еще не создана
    sql.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    name TEXT,
                    phone_number TEXT,
                    address TEXT,
                    reg_date DATETIME)''')
    connection.commit()
    connection.close()


# Функция для добавления пользователя
def add_user(user_id, name, phone_number, address):
    connection = sqlite3.connect("bot_database.db")
    sql = connection.cursor()
    sql.execute("INSERT INTO users (user_id, name, phone_number, address, reg_date) VALUES (?, ?, ?, ?, ?)",
                (user_id, name, phone_number, address, datetime.now()))
    connection.commit()
    connection.close()
