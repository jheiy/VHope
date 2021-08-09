"""DIALOGUE PLANNER"""
ORSEN1 = "ORSEN1"
ORSEN2 = "ORSEN2"
EDEN = "EREN"
MHBOT = "MHBOT"

"""UPDATE DEPENDING ON THE MODULE TO BE USED"""
CURR_ORSEN_VERSION = EDEN

""" FOR LOGS """
CONVERSATION_LOG = "conversation"
INFORMATION_EXTRACTION_LOG = "information_extraction"
DIALOGUE_MODEL_LOG = "dialogue_model"
EVENT_CHAIN_LOG = "event chain"
EMOTION_CLASSIFICATION = "emotion classification"
WELLBEING = "wellbeing"
DUMP_LOG = "dump"

""" PACKAGE VERSIONING CONTROL """
SPACY_VERSION = '2.1.0'
NEURALCOREF_VERSION = '4.0.0'
LAST_CHECK_DATE = "July 26, 2019"

""" DATABASE CREDENTIALS """
LOCATION = "localhost"
USERNAME = "root"
PASSWORD = "1234"
SCHEMA = "orsen_kb"

""" SQL COMMANDS """
FETCH_ONE = 1
FETCH_ALL = 2

""" GENERIC RESPONSES """
IS_AFFIRM = ['yes', 'yes.', 'yeah', 'yeah.', 'sure', 'sure.', 'yup', 'yup.']
IS_DENY = ['no', 'no.', 'nope', 'nope.']
IS_END = ['bye', 'bye.', 'the end', 'the end.', 'STOP', 'that is it', 'no more', 'nope', 'what do you think']
IS_DONE_EXPLAINING = ['nothing', 'i dont know', 'nothing.', 'i dont know.']

"""ORSEN2 RESPONSES"""
IS_DONT_LIKE = ['dont like', 'dont like.', 'don\'t like', 'don\'t like.']
IS_WRONG = ['wrong', 'wrong.']

""" CONSTANT VALUES CONTROL """

# EVENT TYPES #
EVENT_ACTION = "ACTION_EVENT"
EVENT_CREATION = "CREATION_EVENT"
EVENT_DESCRIPTION = "DESCRIPTION_EVENT"

# EMOTION_EVENT_ACTION = "EMOTION_ACTION_EVENT"
# EMOTION_EVENT_DESCRIPTION = "EMOTION_DESCRIPTION_EVENT"

SETTING_PLACE = 'PLACE'
SETTING_DATE = 'DATE'
SETTING_TIME = 'TIME'

""" ARRAY INDICES """

# ACTION EVENT #
ACTOR = 0
ACTION = 1
DIRECT_OBJECT = 2
ADVERB = 3
PREPOSITION = 4
OBJ_PREPOSITION = 5
# NEGATED = 3 # NOT USED

# CREATION EVENT #
SUBJECT = 0

# DESCRIPTION EVENT #
FIRST_TOKEN = 0
RELATION = 1
KEYWORD = 2
SECOND_TOKEN = 3
THIRD_TOKEN = 4
DESCRIPTION_NEGATED = 5

""" DIALOGUE MOVES """
#BASIC ORSEN
DIALOGUE_TYPE_FEEDBACK = "feedback"
DIALOGUE_TYPE_HINTING = "hinting"
DIALOGUE_TYPE_PROMPT = "prompt"
DIALOGUE_TYPE_PUMPING_GENERAL = "general"
DIALOGUE_TYPE_PUMPING_SPECIFIC = "specific"
THE_END = "end"

#JUVEYANCE
DIALOGUE_TYPE_SUGGESTING = "suggesting"

DIALOGUE_TYPE_SUGGESTING_AFFIRM = "suggesting_affirm"
DIALOGUE_TYPE_FOLLOW_UP = "follow_up"

DIALOGUE_TYPE_FOLLOW_UP_DONT_LIKE = "follow_up_dont_like"
DIALOGUE_TYPE_FOLLOW_UP_WRONG = "follow_up_wrong"

DIALOGUE_TYPE_KNOWLEDGE_ACQUISITION_PUMPING = "knowledge_acquisition_pumping"

DIALOGUE_TYPE_INPUT_MISHEARD = "INPUT_MISHEARD"
DIALOGUE_TYPE_UNKNOWN = "UNKNOWN"

#EDEN
DIALOGUE_TYPE_E_LABEL = "e-label"
DIALOGUE_TYPE_E_PUMPING = "e-pumping"
DIALOGUE_TYPE_C_PUMPING = "c-pumping"
DIALOGUE_TYPE_D_PRAISE = "d-praise"
DIALOGUE_TYPE_E_EMPHASIS = "e-emphasis"
DIALOGUE_TYPE_D_CORRECTING = "d-correcting"
DIALOGUE_TYPE_D_PUMPING = "d-pumping"
DIALOGUE_TYPE_EVALUATION = "evaluation"
DIALOGUE_TYPE_RECOLLECTION = "recollection"
DIALOGUE_TYPE_E_END = "e-end"
EDEN_LAST_MODEL_MOVE = DIALOGUE_TYPE_RECOLLECTION
DIALOGUE_TYPE_E_FOLLOWUP = "e-followup"
DIALOGUE_TYPE_EDEN_WELCOME = "eden_welcome"

#MHBOT
DIALOGUE_TYPE_MHBOT_INTRO = "mhbot_intro"
DIALOGUE_TYPE_MHBOT_INTRO_FOLLOWUP = "mhbot_intro_followup"
DIALOGUE_TYPE_MHBOT_WELCOME = "mhbot_welcome"
DIALOGUE_TYPE_P_PUMPING = "p_pumping"
DIALOGUE_TYPE_P_LABELLING = "p_labelling"
DIALOGUE_TYPE_P_REEVALUATE = "p_reevaluate"
DIALOGUE_TYPE_MHBOT_C_PUMPING = "m_c_pumping"
DIALOGUE_TYPE_S_PUMPING = "s_pumping"
DIALOGUE_TYPE_P_PRAISE = "p_praise"
DIALOGUE_TYPE_O_REFLECT = "o_reflect"
DIALOGUE_TYPE_ACKNOWLEDGE = "a-pumping"
DIALOGUE_TYPE_E_FEEDBACK = "e-feedback"
DIALOGUE_TYPE_G_PRAISE = "g-praise"
DIALOGUE_TYPE_MHBOT_CLOSING = "mhbot_closing"
DIALOGUE_TYPE_CLOSING_FOLLOWUP = "closing_followup"
DIALOGUE_TYPE_COUNSELING = "counseling"
DIALOGUE_TYPE_COUNSELING_FOLLOWUP = "counseling_followup"
DIALOGUE_TYPE_FEEDBACK_Y = "counseling_feedback_y"
DIALOGUE_TYPE_FEEDBACK_N = "counseling_feedback_n"
DIALOGUE_TYPE_P_REFLECT_CARE = "p_care"
DIALOGUE_TYPE_P_REFLECT_ENJOY = "p_enjoy"
DIALOGUE_TYPE_P_REFLECT_MUSIC = "p_music"
DIALOGUE_TYPE_P_REFLECT_MUSIC_F2 = "p_music_f2"
DIALOGUE_TYPE_P_REFLECT_MUSIC_POS = "p_music_pos"
DIALOGUE_TYPE_P_REFLECT_MUSIC_NEG = "p_music_neg"
DIALOGUE_TYPE_P_REFLECT_GRATEFUL = "p_grateful_q1"
DIALOGUE_TYPE_P_REFLECT_GRATEFUL_YES = "p_grateful_yes"
DIALOGUE_TYPE_P_REFLECT_GRATEFUL_NO = "p_grateful_no"
DIALOGUE_TYPE_P_REFLECT_GRATEFUL_F2 = "p_grateful_f2"
DIALOGUE_TYPE_P_REFLECT_GRATEFUL2 = "p_grateful_q2"
DIALOGUE_TYPE_E_REFLECT_ACTIVITY = "e_activity"
DIALOGUE_TYPE_E_REFLECT_PAST = "e_past_q1"
DIALOGUE_TYPE_E_REFLECT_PAST_F2 = "e_past_q1_f2"
DIALOGUE_TYPE_E_REFLECT_NATURE = "e_nature_q1"
DIALOGUE_TYPE_E_REFLECT_NATURE2 = "e_nature_q2"
DIALOGUE_TYPE_E_REFLECT_EXCEL = "e_excel_q1"
DIALOGUE_TYPE_R_REFLECT_ENJOY = "r_enjoy_q1"
DIALOGUE_TYPE_R_REFLECT_FRIEND = "r_friend_q1"
DIALOGUE_TYPE_R_REFLECT_FRIEND2 = "r_friend_q2"
DIALOGUE_TYPE_R_REFLECT_FRIEND2_F2 = "r_friend_q2_f"
DIALOGUE_TYPE_M_REFLECT_ORG = "m_org_q1"
DIALOGUE_TYPE_M_REFLECT_NEW = "m_new_q1"
DIALOGUE_TYPE_M_REFLECT_BORED = "m_bored_q1"
DIALOGUE_TYPE_M_REFLECT_PASSION = "m_passion_q1"
DIALOGUE_TYPE_M_REFLECT_FRIEND = "m_friend_q1"
DIALOGUE_TYPE_A_REFLECT_GOAL = "a_goal_q1"
DIALOGUE_TYPE_A_REFLECT_GOAL2 = "a_goal_q2"
DIALOGUE_TYPE_A_REFLECT_SUCCESS = "a_success_q2"
DIALOGUE_TYPE_A_REFLECT_ACHIEVE = "a_achieve_q2"
DIALOGUE_TYPE_PE_ADVICE = "pe_advice"
DIALOGUE_TYPE_PRM_SUGGEST = "prm_suggest"
DIALOGUE_TYPE_A_ADVICE = "a_advice"
DIALOGUE_TYPE_M_SUGGEST = "m_suggest"
DIALOGUE_TYPE_A_SUGGEST = "a_suggest"

"""ORSEN"""
DIALOGUE_TYPE_ORSEN_WELCOME = "orsen_welcome"

""" CONSTANTS BASED ON ENGLISH CONCEPTS """

VOICE_PASSIVE = "PASSIVE"
VOICE_ACTIVE = "ACTIVE"

# 23 TOTAL HELPING VERBS
HELPING_VERBS = ["am", "are", "is", "was", "were", "be", "being", "been", "have", "has", "had", "shall", "will", "do", "does", "did", "may", "must", "might", "can", "could", "would", "should"]
RELATIVE_PRONOUNS = ["who", " whom", " whose", " which", " that", " whoever", " what", " whomever", " whatever", " whichever"]


""" RELATIONS """

IS_A = "IsA"
PART_OF = "PartOf"
AT_LOCATION = "AtLocation"
HAS_PREREQ = "HasPrerequisite"
CREATED_BY = "CreatedBy"
USED_FOR = "UsedFor"
CAUSES = "Causes"
DESIRES = "Desires"
CAPABLE_OF = "CapableOf"
HAS_PROPERTY = "HasProperty"
HAS_A = "HasA"
RECEIVES_ACTION = "ReceivesAction"

LOCATED_NEAR = "LocatedNear"

RELATIONS = [IS_A, PART_OF, AT_LOCATION, HAS_PREREQ, CREATED_BY, USED_FOR, CAUSES, DESIRES, CAPABLE_OF, HAS_PROPERTY,
             HAS_A, RECEIVES_ACTION]

""" QUOTES """

OPENING_QUOTES_STANDARD = "\""
CLOSING_QUOTES_STANDARD = "\""

OPENING_QUOTES_SPACY = "“"
CLOSING_QUOTES_SPACY = "”"

OPENING_QUOTES_STANFORD = "``"
CLOSING_QUOTES_STANFORD = "''"

OPENING_QUOTES = OPENING_QUOTES_STANDARD
CLOSING_QUOTES = CLOSING_QUOTES_STANDARD

""" DIALOGUE TRIGGERS """

PROMPT_TRIGGER = ["help me start.",
                  "help me start"]
PUMPING_TRIGGER = ["give me an idea.", "what should i talk about?", "help me.", "i'm stuck.",
                   "give me an idea", "what should i talk about", "help me", "i'm stuck",
                   "orsen + suggest"]
HINTING_TRIGGER = ["what's next?", "give me a hint.",
                   "what's next", "give me a hint",
                   "orsen + hint"]

SUGGESTING_TRIGGER = ["give me a suggestion", "give me a suggestion."]                   

""" KNOWLEDGE ACQUISITION RELATED """
MIGRATION_SCORE_THRESHOLD = 5

DEFAULT_SEED = 1

