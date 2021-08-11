from time import time
from src.dbo.user import DBOUser
from src.models.user import User
from src import Logger, IS_AFFIRM, IS_DENY, IS_END, UserHandler, DIALOGUE_TYPE_E_END, DIALOGUE_TYPE_RECOLLECTION, Pickle
from src.constants import *
from src.ORSEN import ORSEN
from src.textunderstanding.InputDecoder import InputDecoder
import datetime, time
import telebot

TOKEN = 'Ask Jaime'

bot = telebot.TeleBot(TOKEN)
orsen = ORSEN()
Logger.setup_loggers()
participants = {}

class MHBot_triggers():
    is_engaged = False
    is_end_story = False

triggers = MHBot_triggers()

class Participant:
    def __init__(self, chat_id, first_name, last_name):
        self.chat_id = chat_id
        self.first_name = first_name
        self.last_name = last_name

def clean_user_input(response):
    response = response.strip()
    if response.endswith(".") == False:
        response = response + "."

    return response

# Message Handlers
@bot.message_handler(commands=['start'])
def opening_message(message):
    bot.send_message(message.chat.id, "Hi! This is MHBot, a chatbot dedicated to Maintaining Optimal Mental Health among College Students, an undergraduate thesis by Rebecalyn Lao, Melody Go, Jaime Pastor, and Lenard To. You can input /start_chatting to begin our conversation.")
    # bot.send_message(message.chat.id, message.from_user)
    participants["{0}".format(message.chat.id)] = Participant(message.chat.id, message.from_user.first_name, message.from_user.last_name)
    # bot.send_message(participants["{0}".format(message.chat.id)].chat_id, text=participants["{0}".format(message.chat.id)].first_name)
    
@bot.message_handler(commands=['start_chatting'])
def start_conversation(message):
    if message.chat.id not in participants.keys():
        participants["{0}".format(message.chat.id)] = Participant(message.chat.id, message.from_user.first_name, message.from_user.last_name)
    # bot.send_message(participants["{0}".format(message.chat.id)].chat_id, text="Hi, " + participants["{0}".format(message.chat.id)].first_name)
    triggers.is_engaged = True
    triggers.is_end_story = False
    # bot.reply_to(message.message_id, message.text)
    orsen.initialize_story_prerequisites()
    orsen.world.reset_world()
    orsen.dialogue_planner.reset_new_world()

    temp_welcome = orsen.get_response(move_to_execute = orsen.dialogue_planner.get_welcome_message_type())
    bot.send_message(participants["{0}".format(message.chat.id)].chat_id, temp_welcome)
    # print(triggers.is_engaged)

@bot.message_handler(commands=['stop'])
def emergency_stop(message):
    triggers.is_end_story = True
    triggers.is_engaged = False
    bot.send_message(participants["{0}".format(message.chat.id)].chat_id, 'Okay. If you want to start a new conversation with me, you can start by typing /start_chatting .')
    pass

@bot.message_handler(func=lambda m:True)
def continue_conversation(message):
    if triggers.is_engaged and not triggers.is_end_story == True:
        user_input = message.text

        # Logger.log_conversation("LATENCY TIME (seconds): " + str(time.time() - start_time))
        user_input = clean_user_input(user_input)
        Logger.log_conversation(participants["{0}".format(message.chat.id)].first_name + " " + " : " + str(user_input))

        triggers.is_end_story = orsen.is_end_story(user_input)        

        if not triggers.is_end_story:
            # no login functionalities yet; can be looked into in future development updates
            # try:
            #     Pickle.pickle_world_wb(pickle_filepath, orsen.world.get_pickled_world())
            # except Exception as e:
            #     Logger.log_conversation("ERROR: " + str(e))
            # print('HELLO')
            orsen_response = orsen.get_response(user_input)
            bot.send_message(participants["{0}".format(message.chat.id)].chat_id, orsen_response)
            Logger.log_conversation("MHBot" + ": " + str(orsen_response))
            
        elif triggers.is_end_story:
            bot.send_message(participants["{0}".format(message.chat.id)].chat_id, orsen_response)
            Logger.log_conversation("MHBot" + ": " + str(orsen_response))
            pass

    elif triggers.is_engaged is False:
        if message.chat.id not in participants.keys():
            participants["{0}".format(message.chat.id)] = Participant(message.chat.id, message.from_user.first_name, message.from_user.last_name)
        bot.send_message(participants["{0}".format(message.chat.id)].chat_id, "No current conversation ongoing. Let's talk about your day by typing /start_chatting .")
        pass
    
print('success!')
bot.polling()