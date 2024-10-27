from telebot import types
def phone_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Поделиться контактом', request_contact=True)
    kb.add(button)
    return kb

def location_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Отправьте свою локацию', request_location=True)
    kb.add(button)
    return kb
def main_menu_kb():
    kb = types.InlineKeyboardMarkup(row_width=2)
    button_today = types.InlineKeyboardButton(text='Сегодня', callback_data='today')
    button_tomorrow = types.InlineKeyboardButton(text='На завтра', callback_data='tomorrow')
    kb.add(button_today, button_tomorrow)
    return kb