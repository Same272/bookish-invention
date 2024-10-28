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
    button_uzb = types.InlineKeyboardButton(text='Uzb', callback_data='uzb')
    button_rus = types.InlineKeyboardButton(text='Rus', callback_data='uzb')
    kb.add(button_uzb, button_rus)
    return kb