# import telebot
# import webbrowser

# bot = telebot.TeleBot("6295155548:AAGnSZ8Ph7uaG5nDL8XECshgHz14hgkKxS0")
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://kun.uz')


# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, f"Salom!, {message.from_user.first_name} {message.from_user.last_name}")


# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, "<b>Yordam</b> <em><u>yo'q :)</u></em>", parse_mode='html')


# @bot.message_handler()
# def info(message):
#     if message.text.lower() == "salom":
#         bot.send_message(message.chat.id, f"Salom!, {message.from_user.first_name} {message.from_user.last_name}")
#     elif message.text.lower() == "id":
#         bot.reply_to(message, f'ID: {message.from_user.id}')

# # bot.infinity_polling()   # does the same thing
# bot.polling(none_stop=True) # does the same thing

# pip install pyTelegramBotAPI

import telebot
import webbrowser
bot = telebot.TeleBot("5845105440:AAHVIxm3P7JU7tfrih-nC-40dIm20DRiCkc")

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, f"Salom!  {message.from_user.first_name} {message.from_user.last_name}")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "<b>Yordam</b> <i><u> senga yo'q :) </u></i>", parse_mode="html")


@bot.message_handler(commands=["website"])
def help(message):
    webbrowser.open("https://youtube.com")


bot.polling(non_stop=True)