""" FOR LOGS """
CONVERSATION_LOG = "conversation"
INFORMATION_EXTRACTION_LOG = "information_extraction"
DIALOGUE_MODEL_LOG = "dialogue_model"

""" PACKAGE VERSIONING CONTROL """
SPACY_VERSION = '2.1.0'
NEURALCOREF_VERSION = '4.0.0'
LAST_CHECK_DATE = "July 26, 2019"

""" DATABASE CREDENTIALS """
LOCATION = "localhost"
USERNAME = "root"
PASSWORD = "rootroot"
SCHEMA = "orsen_kb"

""" SQL COMMANDS """
FETCH_ONE = 1
FETCH_ALL = 2

""" GENERIC RESPONSES """
IS_AFFIRM = ['yes', 'yes.', 'yeah', 'yeah.', 'sure', 'sure.', 'yup', 'yup.']
IS_DENY = ['no', 'no.', 'nope', 'nope.']
IS_END = ['bye', 'bye.', 'the end', 'the end.']


""" DIALOGUE MOVES """
#BASIC ORSEN
DIALOGUE_TYPE_FEEDBACK = "FEEDBACK"
DIALOGUE_TYPE_HINTING = "HINTING"
DIALOGUE_TYPE_PROMPT = "PROMPT"
DIALOGUE_TYPE_PUMPING_GENERAL = "PUMPING_GENERAL"
DIALOGUE_TYPE_PUMPING_SPECIFIC = "PUMPING_SPECIFIC"

#JUVEYANCE
DIALOGUE_TYPE_FOLLOW_UP_CONFIRM = "FOLLOW_UP_CONFIRM"
DIALOGUE_TYPE_FOLLOW_UP_ASK = "FOLLOW_UP_ASK"
DIALOGUE_TYPE_FOLLOW_UP_UNKNOWN = "FOLLOW_UP_???"
DIALOGUE_TYPE_SUGGESTING = "SUGGESTING"

DIALOGUE_TYPE_INPUT_MISHEARD = "INPUT_MISHEARD"
DIALOGUE_TYPE_UNKNOWN = "UNKNOWN"

""" QUOTES """

OPENING_QUOTES_STANDARD = "\""
CLOSING_QUOTES_STANDARD = "\""

OPENING_QUOTES_SPACY = "“"
CLOSING_QUOTES_SPACY = "”"

OPENING_QUOTES_STANFORD = "``"
CLOSING_QUOTES_STANFORD = "''"

OPENING_QUOTES = OPENING_QUOTES_STANDARD
CLOSING_QUOTES = CLOSING_QUOTES_STANDARD