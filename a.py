#!/usr/bin/python
# added comment2
# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types

API_TOKEN = '6625958872:AAGbyN_pk5Zcf2jDcZFTTYCZbu4YA_beYTs'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

text=''
text_commands=[]
command_to_text = {}

@bot.message_handler(commands=['add_command'])
def set_location(message):
    global text_commands
    global command_to_text
    command_name = message.text.split()[1]
    text_commands.append(command_name)
    leng=len('/add_command ')+len(command_name)
    command_to_text[command_name] = message.text[leng:]
    bot.reply_to(message,'custom_command_added')

@bot.message_handler(commands=text_commands)
def send_locations(message):
    global command_to_text
    comm = message.text.split()[0][1:]
    print(command_to_text)
    bot.reply_to(message,command_to_text[comm])

@bot.message_handler(commands = ['button'])
def test_button(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('add')
    itembtn2 = types.KeyboardButton('vlad')
    itembtn3 = types.KeyboardButton('duda')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Choose one letter:", reply_markup=markup)



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
