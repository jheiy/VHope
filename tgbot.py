from time import time
from src.dbo.user import DBOUser
from src.models.user import User
from src import Logger, IS_AFFIRM, IS_DENY, IS_END, UserHandler, DIALOGUE_TYPE_E_END, DIALOGUE_TYPE_RECOLLECTION, Pickle
from src.constants import *
from src.ORSEN import ORSEN
from src.textunderstanding.InputDecoder import InputDecoder
import datetime, time
import telebot

TOKEN = '1772588897:AAEykF5UTlq7qWQXuFqpGfjPSrFkliQcaes'

bot = telebot.TeleBot(TOKEN)
orsen = ORSEN()
Logger.setup_loggers()
is_engaged = False

@bot.message_handler(commands=['start'])
def opening_message(message):
    bot.send_message(message.chat.id, "Hey")
    

@bot.message_handler(commands=['start_chatting'])
def start_conversation(message):
    is_engaged = True
    # bot.reply_to(message.message_id, message.text)
    bot.send_message(message.chat.id, "Okay, let's begin!")
    orsen.initialize_story_prerequisites()
    orsen.world.reset_world()
    orsen.dialogue_planner.reset_new_world()

    temp_welcome = orsen.get_response(move_to_execute = orsen.dialogue_planner.get_welcome_message_type())
    print(temp_welcome)

@bot.message_handler(func=lambda m:True)
def continue_conversation(message):
    if is_engaged == True:
        pass    
    
    

bot.polling()