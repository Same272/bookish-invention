import telebot
import buttons as bs
import database as db
from geopy import Photon
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

DOLLAR_TO_RUBLE = 100  # Замените на актуальный курс
EURO_TO_RUBLE = 110
geolocator = Photon(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
bot = telebot.TeleBot(token="")

# Кнопки для конвертации валют
def conversion_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("USD to RUB"), KeyboardButton("EUR to RUB"))
    markup.add(KeyboardButton("RUB to USD"), KeyboardButton("RUB to EUR"))
    return markup

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Добро пожаловать в бот конвертации валют!")
    checker = db.check_user(user_id)
    if checker:
        bot.send_message(user_id, "Главное меню:", reply_markup=conversion_menu())
    else:
        bot.send_message(user_id, "Введите своё имя для регистрации")
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_id = message.from_user.id
    name = message.text
    bot.send_message(user_id, "Теперь поделитесь своим номером", reply_markup=bs.phone_button())
    bot.register_next_step_handler(message, get_phone_number, name)

@bot.message_handler(func=lambda message: message.text in ["USD to RUB", "EUR to RUB", "RUB to USD", "RUB to EUR"])
def handle_conversion_buttons(message):
    user_id = message.from_user.id
    if message.text == "USD to RUB":
        msg = bot.send_message(user_id, "Введите сумму в долларах:")
        bot.register_next_step_handler(msg, process_usd_to_rub)
    elif message.text == "EUR to RUB":
        msg = bot.send_message(user_id, "Введите сумму в евро:")
        bot.register_next_step_handler(msg, process_eur_to_rub)
    elif message.text == "RUB to USD":
        msg = bot.send_message(user_id, "Введите сумму в рублях:")
        bot.register_next_step_handler(msg, process_rub_to_usd)
    elif message.text == "RUB to EUR":
        msg = bot.send_message(user_id, "Введите сумму в рублях:")
        bot.register_next_step_handler(msg, process_rub_to_eur)

# Обработка конвертации
def process_usd_to_rub(message):
    amount = validate_amount(message.text)
    if amount is not None:
        result = amount * DOLLAR_TO_RUBLE
        bot.send_message(message.chat.id, f"Результат: {result:.2f} RUB")
    else:
        bot.send_message(message.chat.id, "Ошибка: Введите корректное число.")

def process_eur_to_rub(message):
    amount = validate_amount(message.text)
    if amount is not None:
        result = amount * EURO_TO_RUBLE
        bot.send_message(message.chat.id, f"Результат: {result:.2f} RUB")
    else:
        bot.send_message(message.chat.id, "Ошибка: Введите корректное число.")

def process_rub_to_usd(message):
    amount = validate_amount(message.text)
    if amount is not None:
        result = amount / DOLLAR_TO_RUBLE
        bot.send_message(message.chat.id, f"Результат: {result:.2f} USD")
    else:
        bot.send_message(message.chat.id, "Ошибка: Введите корректное число.")

def process_rub_to_eur(message):
    amount = validate_amount(message.text)
    if amount is not None:
        result = amount / EURO_TO_RUBLE
        bot.send_message(message.chat.id, f"Результат: {result:.2f} EUR")
    else:
        bot.send_message(message.chat.id, "Ошибка: Введите корректное число.")

# Функция проверки введённого числа
def validate_amount(text):
    try:
        amount = float(text.replace(",", "."))
        return amount if amount >= 0 else None
    except ValueError:
        return None

bot.infinity_polling()