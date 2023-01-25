import telebot

import config
import btn as btn

# Token connection.
bot = telebot.TeleBot(config.TOKEN)


# Sending a message from the text_channels.txt file to the channels entered in the link_channels.txt file.
# Only an administrator with a unique username has access to this command.
@bot.message_handler(commands=['channels'])
def message_to_channel(message):
    a_link = []
    text_file = open('text_channels.txt', 'r', encoding='utf-8')
    text = text_file.read()
    text_file.close()
    owner_id = message.from_user.username
    if owner_id == 'hrdrfstrsmtr':
        file = open('link_channels.txt')
        for i in file:
            if i != "\n":
                a_link.append(i)
        file.close()
        link = [x.replace('https://t.me/', '@') for x in a_link]
        links = [x.replace('\n', '') for x in link]
        for i in links:
            bot.send_message(i, text)


# Sending a message from the text_chats.txt file to the channels entered in the link_chats.txt file.
# Only an administrator with a unique username has access to this command.
@bot.message_handler(commands=['chats'])
def message_to_channel(message):
    a_link = []
    text_file = open('text_chats.txt', 'r', encoding='utf-8')
    text = text_file.read()
    text_file.close()
    owner_id = message.from_user.username
    if owner_id == 'hrdrfstrsmtr':
        file = open('link_chats.txt')
        for i in file:
            if i != "\n":
                a_link.append(i)
        file.close()
        link = [x.replace('https://t.me/', '@') for x in a_link]
        links = [x.replace('\n', '') for x in link]
        for i in links:
            bot.send_message(i, text)


# Commands that respond to button clicks.
@bot.message_handler(content_types=['text'])
def main_menu(message):
    owner_id = message.from_user.username
    if message.text == "/start":
        if owner_id == 'hrdrfstrsmtr':
            bot.send_message(message.chat.id, text="Hello boss, " + message.from_user.first_name + "! ",
                             reply_markup=btn.admin_menu)
        else:
            bot.send_message(message.chat.id, text="=)")
    if message.text == "Admin menu":
        bot.send_message(message.chat.id, text="Welcome to sending list, " + message.from_user.first_name + "!",
                         reply_markup=btn.mailing_menu)
    if message.text == "Sending to channels":
        bot.send_message(message.chat.id, text="""
            In order to send notifications to users in your TELEGRAM CHANNELS, you need to:
        1) in the text document "index" insert links to the channels you want to send out.
        2) paste the required text into the "text_channels" text document.
        3) enter the command "/channels"
        
        Before entering the command, make sure that all data is entered correctly.
        """, reply_markup=btn.mailing_menu)
    if message.text == "Sending to chats":
        bot.send_message(message.chat.id, text="""
            In order to send notifications to users in CHATS, you need to:
        1) in the "link_chats" text document, paste the links to the channels you want to send out.
        2) paste the desired text into the "text_chats" text document.
        3) enter the command "/chats"

        Before entering the command, make sure that all data is entered correctly.
        """, reply_markup=btn.mailing_menu)


if __name__ == '__main__':
    bot.polling(none_stop=True)
