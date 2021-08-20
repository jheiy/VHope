from EDEN.OCC import OCCManager
from EDEN.constants import * 
from src import *
from src.dbo.dialogue import DBODialogueTemplate
from src.dbo.concept.DBOConceptCustom import DBOConceptCustom
from src.dbo.concept.DBOConceptGlobalImpl import DBOConceptGlobalImpl
from nltk.tokenize import regexp_tokenize
from src.dialoguemanager import DialoguePlanner
from src.models.concept import LocalConcept
from src.models.dialogue.constants import DIALOGUE_LIST, DialogueHistoryTemplate, EDEN_DIALOGUE_LIST
from src.models.dialogue import *
from MHBot.PERMAnalysis.PERMAnalysis import PERMAnalysis
import time
import numpy as np

class EDENDialoguePlanner(DialoguePlanner):

    def __init__(self):
        super().__init__()
        self.occ_manager = OCCManager()
        self.perma_analysis = PERMAnalysis()
        self.ongoing_c_pumping = False
        self.perma_state = ''
        self.perma_texts = ''
        self.isRed = False
        self.custom_concept = DBOConceptGlobalImpl()
        self.low_perma = ''
        self.subj = ''
        self.pumping_type = ''
        self.concepts_topics = None
        self.curr_emotion = None

    def reset_new_world(self):
        self.world = None
        self.chosen_dialogue_move = None
        self.chosen_dialogue_template = []
        self.chosen_move_index = -1
        self.curr_event = None
        self.dialogue_history = []
        self.dialogue_template = DBODialogueTemplate('templates')
        self.frequency_count = np.zeros(len(DIALOGUE_LIST))
        self.is_usable = [False] * len(DIALOGUE_LIST)
        self.move_index = -1
        self.num_action_events = 0
        #occ manager
        self.ongoing_c_pumping = False
        self.response = ""
        self.seed_time = time.time()
        self.usable_templates = []
        np.random.seed(DEFAULT_SEED)
        self.occ_manager.reset_occ()
        self.curr_perma = None
        self.perma_analysis.reset()
        self.isRed = False
        self.perma_texts = ''
        self.labeled_perma = ''
        self.check_end = None
        self.is_cause = False
        self.is_deny = False
        self.is_label = False

    def perform_dialogue_planner(self, dialogue_move=""):
        print('--==--==-- EDEN - Perform Dialogue Planner --==--==--')
        #still no triggered phrase
        if dialogue_move == "":
            self.setup_templates_is_usable()

            Logger.log_dialogue_model_basic("Breakdown of values used:")
            Logger.log_dialogue_model_basic_example(DIALOGUE_LIST)
            Logger.log_dialogue_model_basic_example(self.is_usable)
            Logger.log_dialogue_model_basic_example(self.frequency_count)

            print("Breakdown of values used:")
            self.print_dialogue_list()

            #choose dialogue based on dialogue history
            self.chosen_move_index = self.choose_dialogue()
            Logger.log_dialogue_model_basic("Chosen dialogue index: " + str(self.chosen_move_index))
            self.chosen_dialogue_move = DIALOGUE_LIST[self.chosen_move_index].get_type()

            # choose dialogue template to be used
            self.chosen_dialogue_template = self.usable_templates[self.chosen_move_index]

        else:
            # self.setup_templates_is_usable(dialogue_move)
            self.chosen_dialogue_move = dialogue_move
            self.chosen_dialogue_template = self.get_usable_templates(dialogue_move)

        #add chosen dialogue move to history
        self.dialogue_history.append(DialogueHistoryTemplate(dialogue_type=self.chosen_dialogue_move))
        print("FINAL DIALOGUE LIST: ", self.chosen_dialogue_move)
        self.print_dialogue_list()
        
        print(self.chosen_dialogue_move)

        Logger.log_conversation("CHOSEN DIALOGUE MOVE: " + self.chosen_dialogue_move)

        return self.chosen_dialogue_move

    def check_auto_response(self, destructive = True, emotion_event = None):
        print('--==--==-- EDEN - Check auto Response --==--==--')
        next_move = self.check_trigger_phrases()
        if next_move != "":
            return next_move
        else:
            next_move = self.check_affirm_deny(True, emotion_event)
        return next_move

    # def choose_dialogue(self):
    #     for i in range(len(DIALOGUE_LIST)):
    #         if DIALOGUE_LIST[i].get_type() == DIALOGUE_TYPE_PUMPING_GENERAL:
    #             return i

    ###checks only dialogue that does not need to go through text understanding
    def check_trigger_phrases(self, event_chain =[]):
        print('--==--==-- EDEN - Check Trigger Phrases --==--==--')
        # if self.response in IS_END:
        # if self.response in IS_END and not self.ongoing_c_pumping:
        #     return DIALOGUE_TYPE_E_END
        return ""

    def check_affirm_deny(self, destructive = True, emotion_event = None):
        print('--==--==-- EDEN - Check Affirm Deny --==--==--')
        # check if last dialogue move has yes or no:
        last_move = self.get_last_dialogue_move()
        next_move = ""
        print("RESPONSE", self.response)
        tokens = regexp_tokenize(self.response,"[\w']+")
        if last_move is not None:
            if last_move.dialogue_type == DIALOGUE_TYPE_E_LABEL:
                for token in tokens:
                    if token in IS_AFFIRM:
                        if self.curr_perma == 'red':
                            self.isRed = True
                        self.ongoing_c_pumping = True
                        if not len(tokens) > 1:
                            self.is_label = True
                            return DIALOGUE_TYPE_C_PUMPING
                        else: 
                            self.is_cause = True
                            next_move =  DIALOGUE_TYPE_PUMPING_GENERAL
                    else:
                        self.is_deny = True
                        next_move = DIALOGUE_TYPE_E_PUMPING
                self.is_label = True
                
                    
            elif last_move.dialogue_type == DIALOGUE_TYPE_D_CORRECTING:
                for token in tokens:
                    if self.response in IS_AFFIRM:
                        next_move = DIALOGUE_TYPE_EVALUATION
                    else:
                        next_move = DIALOGUE_TYPE_D_PUMPING
            elif last_move.dialogue_type == DIALOGUE_TYPE_CLOSING_FOLLOWUP:
                for token in tokens:
                    if self.response in IS_AFFIRM:
                        next_move = DIALOGUE_TYPE_MHBOT_WELCOME
                    else:
                        next_move = DIALOGUE_TYPE_E_END 
            elif last_move.dialogue_type == DIALOGUE_TYPE_MHBOT_INTRO:
                for token in tokens:
                    if self.response in IS_AFFIRM:
                        next_move = DIALOGUE_TYPE_MHBOT_INTRO_FOLLOWUP
                    else:
                        next_move = DIALOGUE_TYPE_MHBOT_WELCOME
            elif last_move.dialogue_type == DIALOGUE_TYPE_COUNSELING:
                for token in tokens:
                    if self.response in IS_AFFIRM:
                        next_move = DIALOGUE_TYPE_FEEDBACK_Y
                    else:
                        next_move = DIALOGUE_TYPE_COUNSELING_FOLLOWUP
            elif last_move.dialogue_type == DIALOGUE_TYPE_COUNSELING_FOLLOWUP:
                for token in tokens:
                    if self.response in IS_AFFIRM:
                        next_move = DIALOGUE_TYPE_FEEDBACK_Y
                    else:
                        next_move = DIALOGUE_TYPE_FEEDBACK_N
            elif (last_move.dialogue_type == DIALOGUE_TYPE_E_PUMPING or last_move.dialogue_type == DIALOGUE_TYPE_PUMPING_GENERAL or 
                  last_move.dialogue_type == DIALOGUE_TYPE_PUMPING_SPECIFIC or last_move.dialogue_type == DIALOGUE_TYPE_E_EMPHASIS) and self.response.lower() in IS_END and self.ongoing_c_pumping:
                print("CHECKMATE")
                if destructive:
                    self.ongoing_c_pumping = False
                # return DIALOGUE_TYPE_PUMPING_GENERAL
            # elif self.ongoing_c_pumping and self.response.lower() in IS_DONE_EXPLAINING:
            if not self.ongoing_c_pumping and self.response.lower() in IS_END and (last_move.dialogue_type == DIALOGUE_TYPE_E_PUMPING or last_move.dialogue_type == DIALOGUE_TYPE_PUMPING_GENERAL or 
                  last_move.dialogue_type == DIALOGUE_TYPE_PUMPING_SPECIFIC or last_move.dialogue_type == DIALOGUE_TYPE_E_EMPHASIS):
                if not self.is_label:
                    print(self.is_label)
                    self.is_label = False
                    return DIALOGUE_TYPE_P_FEELING

                print("CHECKER3")
                if destructive:
                    self.ongoing_c_pumping = False
                print(emotion_event)
                print(self.curr_perma)
                if emotion_event is not None and self.curr_perma is not None:
                # if self.curr_event.emotion is not None:
                    # check if emotion should be disciplined
                    # if self.curr_event.emotion in DISCIPLINARY_EMOTIONS:
                    # if emotion_event.emotion in DISCIPLINARY_EMOTIONS:
                    #     next_move = DIALOGUE_TYPE_D_CORRECTING
                    # else:
                    #     # check if emotion is + or -
                    #     # if self.curr_event.emotion in POSITIVE_EMOTIONS:
                    #     if emotion_event.emotion in POSITIVE_EMOTIONS:
                    #         next_move = DIALOGUE_TYPE_D_PRAISE
                    #     else:
                    #         next_move = DIALOGUE_TYPE_EVALUATION
                    
                    self.check_end = True
                    
                    concepts = []
                    concept_and_topics = []
                    hasTopic_relations = []
                    topic = ['activity', 'person', 'accomplishment', 'achievement', 'attainment']
                    subject = ''
                    for x in self.world.objects:
                        print("OBJECT")
                        print(x.name)
                        for y in topic:
                            concept = self.custom_concept.get_related_concepts(x.name, y)
                            if concept:
                                print(type((concept.first, concept.relation, concept.second)))
                                concept_and_topics.append((concept.first, concept.relation, concept.second))
                                
                    for x in self.world.get_action_words():
                        print("ACTIONS")
                        print(x)
                        for y in topic:
                            concept = self.custom_concept.get_related_concepts(x, y)
                            if concept:
                                print((concept.first, concept.relation, concept.second))
                                concept_and_topics.append((concept.first, concept.relation, concept.second))
                    
                    for x in concept_and_topics:
                        print(concept_and_topics)
                        print(x)
                        print(x[0])
                    
                
                    lowest_label = self.perma_analysis.get_lowest_score()
                    self.low_perma = lowest_label
                    self.concepts_topics = concept_and_topics
                    
                    self.labeled_perma = self.curr_perma
                    print(lowest_label)

                    print('CURRENT PERMA SCORE:' + self.curr_perma)
                    if self.curr_perma == 'green':
                        if lowest_label == "POS_P" or lowest_label == "POS_E":
                            for x in concept_and_topics:
                                if x[2] == 'activity':
                                    if self.custom_concept.get_concept_by_relation(x[0], 'HasPrerequisite'):
                                        self.subj = x[0]
                                        return DIALOGUE_TYPE_PE_ADVICE
                                else:
                                    if lowest_label == 'POS_P':
                                        return DIALOGUE_TYPE_P_GENERAL
                                    elif lowest_label == 'POS_E':
                                        return DIALOGUE_TYPE_E_GENERAL
                            if not concept_and_topics:
                                if lowest_label == 'POS_P':
                                        return DIALOGUE_TYPE_P_GENERAL
                                elif lowest_label == 'POS_E':
                                    return DIALOGUE_TYPE_E_GENERAL
                        elif lowest_label == "POS_R":
                            for x in concept_and_topics:
                                if x[2] == 'person':
                                    if self.custom_concept.get_concept_by_relation('person', 'CapableOf'):
                                        self.subj = x[0]
                                        return DIALOGUE_TYPE_R_ADVICE
                                    else: 
                                        return DIALOGUE_TYPE_R_GENERAL
                            if not concept_and_topics:
                                return DIALOGUE_TYPE_R_GENERAL
                        elif lowest_label == "POS_M":
                            return DIALOGUE_TYPE_M_ADVICE
                        elif lowest_label == "POS_A":
                            for x in concept_and_topics:
                                if x[2] == 'accomplishment' or x[2] == 'attainment' or x[2] == 'achievement':
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_A_ADVICE
                                else: 
                                    return DIALOGUE_TYPE_A_GENERAL
                            if not concept_and_topics:
                                return DIALOGUE_TYPE_A_GENERAL
                    elif self.curr_perma == 'orange':
                        if lowest_label == "POS_P" or lowest_label == "POS_R" or lowest_label == "POS_M":
                            for x in concept_and_topics:
                                if x[2] == 'person':
                                    if self.custom_concept.get_concept_by_relation('person', 'CapableOf'):
                                        self.subj = x[0]
                                        return DIALOGUE_TYPE_PRM_SUGGEST
                                    else: 
                                        if lowest_label == 'POS_P':
                                            return DIALOGUE_TYPE_P_GENERAL
                                        elif lowest_label == 'POS_R':
                                            return DIALOGUE_TYPE_R_GENERAL
                                        elif lowest_label == 'POS_M':
                                            return DIALOGUE_TYPE_M_GENERAL
                                elif x[2] == 'hobby' and lowest_label == "POS_M":
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_M_SUGGEST
                                else:
                                    return DIALOGUE_TYPE_M_GENERAL
                            if not concept_and_topics:
                                if lowest_label == 'POS_P':
                                    return DIALOGUE_TYPE_P_GENERAL
                                elif lowest_label == 'POS_R':
                                    return DIALOGUE_TYPE_R_GENERAL
                                elif lowest_label == 'POS_M':
                                    return DIALOGUE_TYPE_M_GENERAL
                        elif lowest_label == "POS_A":
                            for x in concept_and_topics:
                                if x[2] == 'accomplishment' or x[2] == 'attainment' or x[2] == 'achievement':
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_A_SUGGEST
                                else: 
                                    return DIALOGUE_TYPE_A_GENERAL
                            if not concept_and_topics:
                                return DIALOGUE_TYPE_A_GENERAL
                        elif lowest_label == "POS_E":
                            for x in concept_and_topics:
                                if x[2] == 'activity':
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_E_SUGGEST
                                else:
                                    return DIALOGUE_TYPE_E_GENERAL
                            if not concept_and_topics:
                                return DIALOGUE_TYPE_E_GENERAL
                            
                    elif self.curr_perma == 'red':
                        self.curr_emotion = emotion_event.emotion
                        if lowest_label == "POS_P" or lowest_label == "POS_R" or lowest_label == "POS_M":
                            for x in concept_and_topics:
                                if x[2] == 'person':
                                    if self.custom_concept.get_concept_by_relation('person', 'CapableOf'):
                                        self.subj = x[0]
                                        return DIALOGUE_TYPE_PRM_SUGGEST
                                    else: 
                                        if lowest_label == 'POS_P':
                                            return DIALOGUE_TYPE_P_GENERAL
                                        elif lowest_label == 'POS_R':
                                            return DIALOGUE_TYPE_R_GENERAL
                                        elif lowest_label == 'POS_M':
                                            return DIALOGUE_TYPE_M_GENERAL
                                elif x[2] == 'hobby' and lowest_label == "POS_M":
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_M_SUGGEST
                                else:
                                    return DIALOGUE_TYPE_M_GENERAL
                            if not concept_and_topics:
                                if lowest_label == 'POS_P':
                                        return DIALOGUE_TYPE_P_GENERAL
                                elif lowest_label == 'POS_E':
                                        return DIALOGUE_TYPE_E_GENERAL
                        
                        elif lowest_label == "POS_A":
                            for x in concept_and_topics:
                                if x[2] == 'accomplishment' or x[2] == 'attainment' or x[2] == 'achievement':
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_A_SUGGEST
                                else: 
                                    return DIALOGUE_TYPE_A_GENERAL
                            if not concept_and_topics:
                                return DIALOGUE_TYPE_A_GENERAL
                        elif lowest_label == "POS_E":
                            for x in concept_and_topics:
                                if x[2] == 'activity':
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_E_SUGGEST
                                else:
                                    return DIALOGUE_TYPE_E_GENERAL
                            if not concept_and_topics:
                                return DIALOGUE_TYPE_E_GENERAL
                        # if emotion_event.emotion in DISCIPLINARY_EMOTIONS or NEGATIVE_EMOTIONS:
                        #     return DIALOGUE_TYPE_ACKNOWLEDGE
                        # else:
                        #     return DIALOGUE_TYPE_G_PRAISE
                            
            if self.is_deny:
                self.is_deny = False
                next_move = DIALOGUE_TYPE_E_PUMPING
            if self.is_cause:
                self.is_cause = False
                next_move = DIALOGUE_TYPE_PUMPING_GENERAL
                
                    # else: 
                    #     return general template
                        

            if next_move !="" and destructive:
                self.curr_event = emotion_event
                if self.response not in IS_AFFIRM and self.response not in IS_DENY and self.response not in IS_END:
                    self.perma_analysis.reset()
                    self.perma_texts = self.perma_texts + ' ' + self.response
                    self.curr_perma = self.perma_analysis.readLex(self.perma_texts)
        return next_move

    def check_based_prev_move(self, destructive = True):
        print('--==--==-- EDEN - Check based Prev Move --==--==--')
        last_move = self.get_last_dialogue_move()

        if last_move is not None:
            print("LAST MOVE IS: ", last_move.dialogue_type)
            if self.ongoing_c_pumping:
                print("currently ongoing c pumping: ", self.response.lower())
            ###START EDEN
            #check if last move is eden
            elif last_move.dialogue_type == DIALOGUE_TYPE_E_PUMPING:
                if destructive:
                    print("SETTING CURR_EVENT_EMOTION TO: ", self.response.upper())
                    Logger.log_occ_values("UPDATING EMOTION TO: " +  self.response.upper())
                    

                    retrieved_emotion = self.occ_manager.get_emotion_by_synonym(self.response.lower())
                    if retrieved_emotion != "":
                        self.curr_event.emotion = retrieved_emotion
                    else:
                        self.curr_event.emotion = self.response.upper()
                    
                    if self.response not in IS_AFFIRM and self.response not in IS_DENY and self.response not in IS_END:
                        self.perma_analysis.reset()
                        self.perma_texts = self.perma_texts + ' ' + self.response
                        print("UPDATING PERMA TO:", self.response.upper())
                        self.curr_perma = self.perma_analysis.readLex(self.perma_texts)
                    self.ongoing_c_pumping = True
                return DIALOGUE_TYPE_C_PUMPING
            elif last_move.dialogue_type == DIALOGUE_TYPE_D_PUMPING:
                return DIALOGUE_TYPE_EVALUATION
            elif last_move.dialogue_type == DIALOGUE_TYPE_EVALUATION:
                return DIALOGUE_TYPE_RECOLLECTION
            elif last_move.dialogue_type == DIALOGUE_TYPE_E_FOLLOWUP:
                return DIALOGUE_TYPE_PUMPING_GENERAL
            elif last_move.dialogue_type == DIALOGUE_TYPE_PE_ADVICE:
                return DIALOGUE_TYPE_ACT_WISDOM
            elif last_move.dialogue_type == DIALOGUE_TYPE_R_ADVICE:
                return DIALOGUE_TYPE_R_WISDOM
            elif last_move.dialogue_type == DIALOGUE_TYPE_M_ADVICE:
                return DIALOGUE_TYPE_M_WISDOM
            elif last_move.dialogue_type == DIALOGUE_TYPE_A_ADVICE:
                return DIALOGUE_TYPE_A_WISDOM
            elif (last_move.dialogue_type == DIALOGUE_TYPE_E_G_FOLLOWUP_N or last_move.dialogue_type == DIALOGUE_TYPE_M_G_FOLLOWUP_N
                  or last_move.dialogue_type == DIALOGUE_TYPE_R_G_FOLLOWUP or last_move.dialogue_type == DIALOGUE_TYPE_A_G_FOLLOWUP_N
                  or last_move.dialogue_type == DIALOGUE_TYPE_P_S_WISDOM):
                if self.labeled_perma == 'orange':
                    return DIALOGUE_TYPE_O_REFLECT
                elif self.labeled_perma == 'green':
                    return DIALOGUE_TYPE_P_PRAISE
            elif last_move.dialogue_type == DIALOGUE_TYPE_MHBOT_CLOSING:
                return DIALOGUE_TYPE_CLOSING_FOLLOWUP
            elif last_move.dialogue_type == DIALOGUE_TYPE_MHBOT_INTRO_FOLLOWUP:
                return DIALOGUE_TYPE_MHBOT_WELCOME
            elif last_move.dialogue_type == DIALOGUE_TYPE_ACKNOWLEDGE or last_move.dialogue_type == DIALOGUE_TYPE_G_PRAISE:
                return DIALOGUE_TYPE_COUNSELING
            elif last_move.dialogue_type == DIALOGUE_TYPE_P_PRAISE or last_move.dialogue_type == DIALOGUE_TYPE_O_REFLECT:
                return DIALOGUE_TYPE_MHBOT_CLOSING
            elif (last_move.dialogue_type == DIALOGUE_TYPE_ACT_WISDOM or last_move.dialogue_type == DIALOGUE_TYPE_R_WISDOM or 
                  last_move.dialogue_type == DIALOGUE_TYPE_M_WISDOM or last_move.dialogue_type == DIALOGUE_TYPE_A_WISDOM or 
                  last_move.dialogue_type == DIALOGUE_TYPE_P_S_WISDOM or last_move.dialogue_type == DIALOGUE_TYPE_RM_S_WISDOM or
                  last_move.dialogue_type == DIALOGUE_TYPE_M_S_WISDOM or last_move.dialogue_type == DIALOGUE_TYPE_A_S_WISDOM):
                if self.labeled_perma == 'orange':
                    return DIALOGUE_TYPE_O_REFLECT
                elif self.labeled_perma == 'green':
                    return DIALOGUE_TYPE_P_PRAISE
            elif (last_move.dialogue_type == DIALOGUE_TYPE_PRM_SUGGEST or last_move.dialogue_type == DIALOGUE_TYPE_E_SUGGEST or 
                    last_move.dialogue_type == DIALOGUE_TYPE_M_SUGGEST or last_move.dialogue_type == DIALOGUE_TYPE_A_SUGGEST):
                if last_move.dialogue_type == DIALOGUE_TYPE_PRM_SUGGEST:
                    return DIALOGUE_TYPE_RM_S_WISDOM
                elif last_move.dialogue_type == DIALOGUE_TYPE_E_SUGGEST: 
                    return DIALOGUE_TYPE_ACT_WISDOM
                elif last_move.dialogue_type == DIALOGUE_TYPE_M_SUGGEST: 
                    return DIALOGUE_TYPE_M_S_WISDOM
                elif last_move.dialogue_type == DIALOGUE_TYPE_A_SUGGEST: 
                    return DIALOGUE_TYPE_A_S_WISDOM
                

                #     return DIALOGUE_TYPE_PE_ADVICE
                # elif last_move.dialogue_type == DIALOGUE_TYPE_A_ADVICE or last_move.dialogue_type == DIALOGUE_TYPE_PE_ADVICE:
            elif (last_move.dialogue_type == DIALOGUE_TYPE_P_GENERAL or last_move.dialogue_type == DIALOGUE_TYPE_E_GENERAL or 
                  last_move.dialogue_type == DIALOGUE_TYPE_R_GENERAL or last_move.dialogue_type == DIALOGUE_TYPE_M_GENERAL or
                  last_move.dialogue_type == DIALOGUE_TYPE_A_GENERAL):
                    if self.labeled_perma == 'green':
                        if self.low_perma == "POS_P" or self.low_perma == "POS_E":
                            for x in self.concepts_topics:
                                if x[2] == 'activity':
                                    if self.custom_concept.get_concept_by_relation(x[0], 'HasPrerequisite'):
                                        self.subj = x[0]
                                        return DIALOGUE_TYPE_PE_ADVICE
                                else:
                                    return DIALOGUE_TYPE_P_S_WISDOM
                        elif self.low_perma == "POS_R":
                            for x in self.concepts_topics:
                                if x[2] == 'person':
                                    if self.custom_concept.get_concept_by_relation('person', 'CapableOf'):
                                        self.subj = x[0]
                                        return DIALOGUE_TYPE_R_ADVICE
                                    else: 
                                        return DIALOGUE_TYPE_R_WISDOM
                        elif self.low_perma == "POS_M":
                            return DIALOGUE_TYPE_M_ADVICE
                        elif self.low_perma == "POS_A":
                            for x in self.concepts_topics:
                                if x[2] == 'accomplishment' or x[2] == 'attainment' or x[2] == 'achievement':
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_A_ADVICE
                                else: 
                                    return DIALOGUE_TYPE_A_WISDOM
                        
                        if not self.concepts_topics:
                            if self.low_perma == "POS_P":
                                return DIALOGUE_TYPE_P_S_WISDOM
                            elif self.low_perma == "POS_E":
                                return DIALOGUE_TYPE_E_G_FOLLOWUP_N
                            elif self.low_perma == "POS_R":
                                return DIALOGUE_TYPE_R_G_FOLLOWUP
                            elif self.low_perma == "POS_M":
                                return DIALOGUE_TYPE_M_G_FOLLOWUP_N
                            elif self.low_perma == "POS_A":
                                return DIALOGUE_TYPE_A_G_FOLLOWUP_N
                            
                            
                    elif self.labeled_perma == 'orange':
                        if self.low_perma == "POS_P" or self.low_perma == "POS_R" or self.low_perma == "POS_M":
                            for x in self.concepts_topics:
                                if x[2] == 'person':
                                    if self.custom_concept.get_concept_by_relation('person', 'CapableOf'):
                                        self.subj = x[0]
                                        return DIALOGUE_TYPE_PRM_SUGGEST
                                    else: 
                                        if self.low_perma == "POS_P":
                                            return DIALOGUE_TYPE_P_S_WISDOM
                                        elif self.low_perma == "POS_R":
                                            return DIALOGUE_TYPE_R_G_FOLLOWUP
                                        elif self.low_perma == "POS_M":
                                            return DIALOGUE_TYPE_M_G_FOLLOWUP_N
                                elif x[2] == 'hobby' and self.low_perma == "POS_M":
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_M_SUGGEST
                                else:
                                    return DIALOGUE_TYPE_M_G_FOLLOWUP_N
                        elif self.low_perma == "POS_A":
                            for x in self.concepts_topics:
                                if x[2] == 'accomplishment' or x[2] == 'attainment' or x[2] == 'achievement':
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_A_SUGGEST
                                else: 
                                    return DIALOGUE_TYPE_A_G_FOLLOWUP_N
                        elif self.low_perma == "POS_E":
                            for x in self.concepts_topics:
                                if x[2] == 'activity':
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_E_SUGGEST
                                else:
                                    return DIALOGUE_TYPE_E_G_FOLLOWUP_N
                        
                        if not self.concepts_topics:
                            if self.low_perma == "POS_P":
                                return DIALOGUE_TYPE_P_S_WISDOM
                            elif self.low_perma == "POS_E":
                                return DIALOGUE_TYPE_E_G_FOLLOWUP_N
                            elif self.low_perma == "POS_R":
                                return DIALOGUE_TYPE_R_G_FOLLOWUP
                            elif self.low_perma == "POS_M":
                                return DIALOGUE_TYPE_M_G_FOLLOWUP_N
                            elif self.low_perma == "POS_A":
                                return DIALOGUE_TYPE_A_G_FOLLOWUP_N
                            
                    elif self.labeled_perma == 'red':
                        emotion_event = self.curr_emotion
                        
                        if self.low_perma == "POS_P" or self.low_perma == "POS_R" or self.low_perma == "POS_M":
                            for x in self.concepts_topics:
                                if x[2] == 'person':
                                    if self.custom_concept.get_concept_by_relation('person', 'CapableOf'):
                                        self.subj = x[0]
                                        return DIALOGUE_TYPE_PRM_SUGGEST
                                    else: 
                                        if emotion_event in DISCIPLINARY_EMOTIONS or NEGATIVE_EMOTIONS:
                                            return DIALOGUE_TYPE_ACKNOWLEDGE
                                        else:
                                            return DIALOGUE_TYPE_G_PRAISE
                                elif x[2] == 'hobby' and self.low_perma == "POS_M":
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_M_SUGGEST
                                else:
                                    if emotion_event in DISCIPLINARY_EMOTIONS or NEGATIVE_EMOTIONS:
                                        return DIALOGUE_TYPE_ACKNOWLEDGE
                                    else:
                                        return DIALOGUE_TYPE_G_PRAISE
                        elif self.low_perma == "POS_A":
                            for x in self.concepts_topics:
                                if x[2] == 'accomplishment' or x[2] == 'attainment' or x[2] == 'achievement':
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_A_SUGGEST
                                else: 
                                    if emotion_event in DISCIPLINARY_EMOTIONS or NEGATIVE_EMOTIONS:
                                        return DIALOGUE_TYPE_ACKNOWLEDGE
                                    else:
                                        return DIALOGUE_TYPE_G_PRAISE
                        elif self.low_perma == "POS_E":
                            for x in self.concepts_topics:
                                if x[2] == 'activity':
                                    self.subj = x[0]
                                    return DIALOGUE_TYPE_E_SUGGEST
                                else:
                                    if emotion_event in DISCIPLINARY_EMOTIONS or NEGATIVE_EMOTIONS:
                                        return DIALOGUE_TYPE_ACKNOWLEDGE
                                    else:
                                        return DIALOGUE_TYPE_G_PRAISE
                        
                        if not self.concepts_topics:
                            if emotion_event in DISCIPLINARY_EMOTIONS or NEGATIVE_EMOTIONS:
                                return DIALOGUE_TYPE_ACKNOWLEDGE
                            else:
                                return DIALOGUE_TYPE_G_PRAISE
                
            elif self.labeled_perma == 'red':
                if (last_move.dialogue_type == DIALOGUE_TYPE_PRM_SUGGEST or last_move.dialogue_type == DIALOGUE_TYPE_E_SUGGEST or 
                    last_move.dialogue_type == DIALOGUE_TYPE_M_SUGGEST or last_move.dialogue_type == DIALOGUE_TYPE_A_SUGGEST):
                        if emotion_event in DISCIPLINARY_EMOTIONS or NEGATIVE_EMOTIONS:
                            return DIALOGUE_TYPE_ACKNOWLEDGE
                        else:
                            return DIALOGUE_TYPE_G_PRAISE
        else:
            print("NO PREVIOUS DIALOGUE")
        return ""

    def check_based_curr_event(self, detected_event=None, curr_event=None):
        print('--==--==-- EDEN - Check based Curr Event --==--==--')
        if self.ongoing_c_pumping:
            if detected_event is not None and curr_event is not None:
                if detected_event.type == EVENT_EMOTION and detected_event.emotion == curr_event.emotion:
                    return DIALOGUE_TYPE_E_EMPHASIS
                # else:
                #     return DIALOGUE_TYPE_PUMPING_GENERAL
        return ""


    #emotion coaching model
    def is_model_ongoing(self):
        print('--==--==-- EDEN - Is Model Ongoing --==--==--')
        last_move = self.get_last_dialogue_move()
        if last_move is not None:
            if last_move.dialogue_type != EDEN_LAST_MODEL_MOVE\
                    and last_move.dialogue_type != DIALOGUE_TYPE_PUMPING_GENERAL \
                    and not self.ongoing_c_pumping:
                return True
        return False

    def init_set_dialogue_moves_usable(self, preselected_move=""):
        print('--==--==-- EDEN - Init set dialogue moves usable --==--==--')
        # check which dialogue moves are usable
        set_to_true = []
        if preselected_move =="":
            move_to_execute = self.check_based_prev_move()
            if move_to_execute != "":
                set_to_true.append(move_to_execute)
            else:
                print(self.curr_event)
                if self.curr_event is not None and self.curr_event.type == EVENT_EMOTION and self.curr_perma is not None: #IF EMOTION EVENT IS MADE
                    set_to_true.append(DIALOGUE_TYPE_E_LABEL)
                else:
                    for x in self.world.objects:
                        if type(x) is str:
                            if type(self.custom_concept.get_concept_by_relation(x, 'AtLocation')) is list:
                                for y in self.custom_concept.get_concept_by_relation(x, 'AtLocation'):
                                    if self.custom_concept.get_specific_concept(y[3], 'IsA', 'place'):
                                        set_to_true.append(DIALOGUE_TYPE_M_PUMP)
                                        self.pumping_type = 'AtPlace'
                            else:
                                concept = self.custom_concept.get_concept_by_relation(x, 'AtLocation')
                                print(concept)
                                if self.custom_concept.get_specific_concept(concept.second, 'IsA', 'place'):
                                    set_to_true.append(DIALOGUE_TYPE_M_PUMP)
                                    self.pumping_type = 'AtPlace'
                        else: 
                            if type(self.custom_concept.get_concept_by_relation(x.name, 'AtLocation')) is list:
                                for y in self.custom_concept.get_concept_by_relation(x.name, 'AtLocation'):
                                    if self.custom_concept.get_specific_concept(y[3], 'IsA', 'place'):
                                        set_to_true.append(DIALOGUE_TYPE_M_PUMP)
                                        self.pumping_type = 'AtPlace'
                            else:
                                concept = self.custom_concept.get_concept_by_relation(x.name, 'AtLocation')
                                print(concept)
                                if self.custom_concept.get_specific_concept(concept.second, 'IsA', 'place'):
                                    set_to_true.append(DIALOGUE_TYPE_M_PUMP)
                                    self.pumping_type = 'AtPlace'

                    for x in self.world.get_action_words():
                        if type(x) is str:
                            if self.custom_concept.get_related_concepts(x, 'fun'):
                                set_to_true.append(DIALOGUE_TYPE_M_PUMP)
                                self.pumping_type = 'isFun'                         
                        else:
                            if self.custom_concept.get_related_concepts(x.name, 'fun'):
                                set_to_true.append(DIALOGUE_TYPE_M_PUMP)
                                self.pumping_type = 'isFun'     
                    
                    
                    if len(self.get_usable_templates(DIALOGUE_TYPE_PUMPING_SPECIFIC)) > 0 and self.pumping_type == '':
                        set_to_true.append(DIALOGUE_TYPE_PUMPING_SPECIFIC)
                    set_to_true.append(DIALOGUE_TYPE_PUMPING_GENERAL)
                # if self.perma_state != '' and self.perma_analysis.isComplete():
                #     set_to_true.append(DIALOGUE_TYPE_P_REEVALUATE)
                # else:
                #     if len(self.get_usable_templates(DIALOGUE_TYPE_PUMPING_SPECIFIC)) > 0: #INCOMPLETE PERMA
                #         set_to_true.append(DIALOGUE_TYPE_PUMPING_SPECIFIC)
                #     set_to_true.append(DIALOGUE_TYPE_PUMPING_GENERAL)
        else:
            set_to_true.append(preselected_move)
        self.set_dialogue_list_true(set_to_true)

    def get_latest_event(self, last_fetched):
        print('--==--==-- EDEN - get latest event --==--==--')
        # returns only the first emotion detected
        emotions_found = []
        for i in range(0, len(last_fetched)):
            curr_event = last_fetched[i]

            # reset occ values
            self.occ_manager.set_values()
            # get emotion list (str)
            temp_emotion = self.occ_manager.get_occ_emotion(curr_event, self.response)
            if temp_emotion is not None and len(temp_emotion) > 0:
                for X in temp_emotion:
                    if not self.is_emotion_exist(X.emotion, emotions_found):
                        emotions_found.append(X)



            # # check if description later
            # if curr_event.type == EVENT_ACTION:
            #     # reset occ values
            #     self.occ_manager.set_values()
            #     # get emotion list (str)
            #     temp_emotion = self.occ_manager.get_occ_emotion(curr_event, self.response)
            #     if temp_emotion is not None and len(temp_emotion) > 0:
            #         for X in temp_emotion:
            #             if not self.is_emotion_exist(X.emotion, emotions_found):
            #                 emotions_found.append(X)
        #emotion found
        if len(emotions_found) > 0:
            # self.world.add_emotion_event(emotions_found)
            #return latest emotion
            listToStr = ' '.join([str(curr_emotion.emotion) for curr_emotion in emotions_found])
            Logger.log_occ_values("SIMPLIFIED EMOTIONS: " + listToStr)

            final_emotion = self.occ_manager.get_final_emotion(emotions_found)

            # Logger.log_occ_values("CHOSEN EMOTION: " + emotions_found[len(emotions_found)-1].emotion)
            Logger.log_occ_values("CHOSEN EMOTION: " + final_emotion.emotion)

            # return emotions_found[len(emotions_found)-1]
            return final_emotion

        #no emotion found
        else:
            if len(last_fetched) > 0:
                return last_fetched[len(last_fetched)-1]
        return None
        # return []

    def is_emotion_exist(self, emotion_to_check, emotion_list):
        print('--==--==-- EDEN - is emotion exist --==--==--')
        if len(emotion_list) > 0:
            for curr_emotion in emotion_list:
                if curr_emotion.emotion == emotion_to_check:
                    return True
        return False

    def is_repeat_story(self, move_to_execute):
        print('--==--==-- EDEN - is repeat story --==--==--')
        if move_to_execute == DIALOGUE_TYPE_RECOLLECTION:
            return True
        return False

    def finalize_dialogue_move(self, curr_dialogue_move):
        print('--==--==-- EDEN - Finalize dialogue Move --==--==--')
        if curr_dialogue_move == DIALOGUE_TYPE_D_PRAISE:
            return DIALOGUE_TYPE_EVALUATION
        elif curr_dialogue_move == DIALOGUE_TYPE_RECOLLECTION:
            return DIALOGUE_TYPE_E_END
        # if curr_dialogue_move == DIALOGUE_TYPE_P_PRAISE or curr_dialogue_move == DIALOGUE_TYPE_O_REFLECT:
        #     return DIALOGUE_TYPE_MHBOT_CLOSING
        return ""

    def get_curr_low(self):
        return self.low_perma
    
    def get_subj(self):
        return self.subj
    
    def get_pump_type(self):
        return self.pumping_type
    
    def get_welcome_message_type(self):
        return DIALOGUE_TYPE_MHBOT_INTRO
