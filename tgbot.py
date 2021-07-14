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

class MHBot_triggers():
    is_engaged = False
    is_end_story = False

triggers = MHBot_triggers()

def clean_user_input(response):
    response = response.strip()
    if response.endswith(".") == False:
        response = response + "."

    return response

# Message Handlers
@bot.message_handler(commands=['start'])
def opening_message(message):
    bot.send_message(message.chat.id, "Hey")
    
@bot.message_handler(commands=['start_chatting'])
def start_conversation(message):
    triggers.is_engaged = True
    triggers.is_end_story = False
    # bot.reply_to(message.message_id, message.text)
    orsen.initialize_story_prerequisites()
    orsen.world.reset_world()
    orsen.dialogue_planner.reset_new_world()

    temp_welcome = orsen.get_response(move_to_execute = orsen.dialogue_planner.get_welcome_message_type())
    bot.send_message(message.chat.id, temp_welcome)
    print(triggers.is_engaged)

@bot.message_handler(func=lambda m:True)
def continue_conversation(message):
    if triggers.is_engaged and not triggers.is_end_story == True:
        start_time = time.time()
        user_input = message.text

        Logger.log_conversation("LATENCY TIME (seconds): " + str(time.time() - start_time))
        user_input = clean_user_input(user_input)
        Logger.log_conversation("User : " + str(user_input))

        triggers.is_end_story = orsen.is_end_story(user_input)
        orsen_response = orsen.get_response(user_input)
        print("ending: ", triggers.is_end_story)
        bot.send_message(message.chat.id, orsen_response)
        
        Logger.log_conversation(CURR_ORSEN_VERSION + ": " + str(orsen_response))
    else:
        bot.send_message(message.chat.id, message.text)
        pass


    
print('success!')
bot.polling()