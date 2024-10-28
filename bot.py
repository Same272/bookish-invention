import telebot
import buttons as bs
import database as db
from geopy import Photon

geolocator = Photon(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
bot = telebot.TeleBot(token="7802696911:AAF3nQirJdZK3CQ53CGISVLd2xH8qzY8ukA")

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Добро пожаловать в бот погода!")
    checker = db.check_user(user_id)
    if checker == True:
        bot.send_message(user_id, "Главное меню: ", reply_markup=bs.main_menu_kb())
    elif checker == False:
        bot.send_message(user_id, "Введите своё имя для регистрации")
        print(message.text)
        bot.register_next_step_handler(message, get_name)
def get_name(message):
    user_id = message.from_user.id
    name = message.text
    print(message.text)
    bot.send_message(user_id, "Теперь поделитесь своим номером",
                     reply_markup=bs.phone_button())
    bot.register_next_step_handler(message, get_phone_number, name)
def get_phone_number(message, name):
    user_id = message.from_user.id
    if message.contact:
        phone_number = message.contact
        print(phone_number)
        bot.send_message(user_id, "Отправьте свою локацию", reply_markup=bs.location_button())
        bot.register_next_step_handler(message, get_location, name, phone_number)
    else:
        bot.send_message(user_id, 'Отправьте свой номер через кнопку в меню')
        bot.register_next_step_handler(message, get_phone_number, name)
def get_location(message, name, phone_number):
    user_id = message.from_user.id
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        address = geolocator.reverse((latitude, longitude)).address
        print(name, phone_number, address)
        bot.send_message(user_id, 'Вы успешно зарегистрировались')
        bot.send_message(user_id, 'Главное меню', reply_markup=bs.main_menu_kb())
    else:
        bot.send_message(user_id, 'Отправьте свою локацию через кнопку в меню')
        bot.load_next_step_handlers(message)
@bot.callback_query_handler(lambda call: call.data in ['uzb', 'rus'])
def all_call(call):
    user_id = call.message.chat.id
    bot.send_message(user_id, 'Выберите язык:')
    if call.data == 'uzb':
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, 'Язык был изменен на узбекский')
    elif call.data == 'rus':
        bot.delete_message(user_id, call.message.message_id)
        bot.send_message(user_id, "Язык был изменен на русский")
bot.infinity_polling()