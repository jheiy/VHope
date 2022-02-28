import sys
sys.path.append('/home/jacky/Documents/GitHub/VHope')

from src.dbo.user import DBOUser
from src.models.user import User
from src import Logger, IS_AFFIRM, IS_DENY, IS_END, UserHandler, DIALOGUE_TYPE_E_END, DIALOGUE_TYPE_RECOLLECTION, Pickle
from src.constants import *
from src.ORSEN import ORSEN
from src.textunderstanding.InputDecoder import InputDecoder
from VHope.FTER.FTER import FTER

from flask import request, session

orsen = ORSEN()
# Database access
dbo_user = DBOUser('users', User)

class VHope:
    def __init__(self):
        self.user_ID = session['id']
        self.user_name = session['username']

    def welcome(self):
        print("J: USER ID= " + str(self.user_ID) + " USERNAME= " + self.user_name)

        if session['logged_in'] == True:
            print("J: Loggedin for the first time.")

            Logger.setup_loggers()
            orsen.initialize_story_prerequisites()
            orsen.world.reset_world()
            orsen.dialogue_planner.reset_new_world()

            user_log = str(self.user_ID) + " -> " + self.user_name
            Logger.V_log("USER: " + user_log)

            session['logged_in'] = False
        else:
            print("J: Not the first time.")


        if session['first'] == 1:
            welcome_msg = "Hello precious one. Welcome! I am VHope, an AI chatbot that can listen to your stories everyday and I will try my best to give you empathetic responses. What do you want to talk about first?"
        else:
            welcome_msg = orsen.get_response(move_to_execute = orsen.dialogue_planner.get_welcome_message_type())

        Logger.V_log("MHBOT >> " + welcome_msg)

        # fter = FTER()
        # welcome_msg = fter.generate(welcome_msg)
        # Logger.V_log("FTER >> " + welcome_msg)
        
        session['history'] = welcome_msg

        return welcome_msg

    def get_input():
        userText = request.args.get('msg')
        return userText

    def get_response(self):

        usr_text = VHope.get_input()
        Logger.V_log("UTTERANCE >> " + usr_text)
        session['history'] = session['history'] + " eof " + usr_text
        print("J: USER=" + self.user_name + " TEXT= " + usr_text)

        response_text = orsen.get_response(usr_text)

        # if with emotion, check well-being -- on ORSEN
        # if orsen.world.curr_emotion_event != None:
        #     Logger.V_log("EMOTION: " + orsen.world.curr_emotion_event.emotion)
        #     print("EMOTION TYPE " + str(type(orsen.world.curr_emotion_event.emotion)))

        session['history'] = session['history'] + " eof " + response_text

        return response_text