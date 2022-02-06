from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# adding language for compatibility with spacy 3.0
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

# Creating ChatBot Instance
chatbot = ChatBot('VHope', tagger_language=ENGSM)

 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)
# chatbot.set_trainer(ChatterBotCorpusTrainer)
# chatbot.train("chatterbot.corpus.english")