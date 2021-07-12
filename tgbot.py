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

@bot.message_handler(commands=['start'])
def opening_message(message):
    bot.send_message(message.chat.id, "Hey")
    pass

@bot.message_handler(commands=['chat'])
def start_conversation(message):
    # bot.reply_to(message.message_id, message.text)
    
    pass

bot.polling()