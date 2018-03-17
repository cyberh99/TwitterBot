import telebot
import json
from libs.config import token
from libs.login_functions import *

bot = telebot.TeleBot(token)

user_step={}

#Funcion para obtener donde se encuentra el usuario

def get_user_sept(chat_id):
    if chat_id in user_step:
        return user_step[chat_id]
    else:
        add_user(chat_id)
        user_step[chat_id] = 0
        return 0

@bot.message_handler(commands=["start"])
def bot_starting(message):
    chat_id = message.chat.id
    if is_user(chat_id):
        bot.send_message(chat_id,"Bienvenido...")
    else:
        bot.send_message(chat_id, add_user(chat_id))
        user_step[chat_id] = 0


@bot.message_handler(commands=["register"])
def register_function(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,"Procede a introducir la informacion")

    user_step[chat_id] = 1

@bot.message_handler(func=lambda message: get_user_sept(message.chat.id) == 1)
def consumer_key(message):
    chat_id  = message.chat.id
    key = telebot.util.extract_arguments(message.text)

    if (len(str(key)) != 25):
        bot.send_message(chat_id, "No has el consumer key")
    else:
        write_db(chat_id,key)
        user_step[chat_id] = 2


@bot.message_handler(func=lambda message: get_user_sept(message.chat.id) == 2)
def consumer_secret_key(message):
    chat_id = message.chat.id
    key = telebot.util.extract_arguments(message.text)
    if len(key) != 50:
        bot.send_message("La longitud de la clave introducida no es correcta")
    else:
        # The key has the stimated length so we can continue
        write_db(chat_id,key)
        # Add one more to the users step
        user_step[chat_id] += 1


@bot.message_handler(func=lambda message: get_user_sept(message.chat.id) == 3)

def access_token_key(message):
    chat_id = message.chat.id
    key = telebot.util.extract_arguments(message.text)
    if len(key) != 50:
        bot.send_message("La longitud de la clave introducida no es correcta")
    else:
        # The key has the stimated length so we can continue
        write_db(chat_id,key)
        # Add one more to the users step
        user_step[chat_id] += 1


@bot.message_handler(func=lambda message: get_user_sept(message.chat.id) == 4)

def access_token_secret_key(message):
    chat_id = message.chat.id
    key = telebot.util.extract_arguments(message.text)
    if len(key) != 45:
        bot.send_message("La longitud de la clave introducida no es correcta")
    else:
        # The key has the stimated length so we can continue
        write_db(chat_id,key)
        # Add one more to the users step

    user_step[chat_id] = -1


bot.polling(True)