import sqlite3
from datetime import datetime
connection = sqlite3.connect("prognoz.db")
sql = connection.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS users "
            "(user_id INTEGER, name TEXT, "
            "phone_number TEXT, reg_date DATETIME);")
sql.execute('CREATE TABLE IF NOT EXISTS prognoz'
            '(weatheer_id INTEGER, weather_name TEXT, weather_des TEXT, weather_photo REAL, reg_date DATETIME);')
def add_user(name, phone_number, user_id):
    connection = sqlite3.connect(".prognoz.db")
    sql = connection.cursor()
    sql.execute(f"INSERT INTO users (user_id, name, phone_number, reg_date) "
                "VALUES (?, ?, ?, ?);", (user_id, name, phone_number, datetime.now()))
    connection.commit()

def check_user(user_id):
    connection = sqlite3.connect("prognoz.db")
    sql = connection.cursor()
    checker = sql.execute("SELECT * FROM users WHERE user_id=?", (user_id, )).fetchone()
    if checker:
        return True
    elif not checker:
        return False
def get_all_users():
    connection = sqlite3.connect("prognoz.db")
    sql = connection.cursor()
    all_users = sql.execute("SELECT * FROM users;").fetchall()
    return all_users

def add_weather():
    connection = sqlite3.connect("prognoz.db")
    sql = connection.cursor()
    sql.execute('INSERT INTO prognoz(weather_name, weather_des, weather_photo, reg_date) '
                'VALUES (?,?,?,?);')
    connection.commit()
def delete_weather(weather_id):
    connection = sqlite3.connect("prognoz.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM products WHERE weather_id=?;", (weather_id, ))
    connection.commit()

def get_exact_weather(weather_id):
    connection = sqlite3.connect("prognoz.db")
    sql = connection.cursor()
    exact_weather = sql.execute("SELECT weather_name, weather_des, weather_photo "
                                "FROM products WHERE pr_id=?;", (weather_id, )).fetchone()
    return exact_weather