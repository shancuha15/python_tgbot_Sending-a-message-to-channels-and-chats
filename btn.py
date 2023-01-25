from telebot import types

btn_admin_menu = types.KeyboardButton('Admin menu')
admin_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btn_admin_menu)

btn_sending_to_chats = types.KeyboardButton('Sending to chats')
btn_sending_to_channels = types.KeyboardButton('Sending to channels')
mailing_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btn_sending_to_channels,
                                                                                btn_sending_to_chats)
