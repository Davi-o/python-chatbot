from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from language import sentence_to_chatter_bot

from spacy.cli import download

#download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = "en_core_web_sm"

chatbot = ChatBot("chatbot", tagger_language=ENGSM)

training = ListTrainer(chatbot)
training.train(sentence_to_chatter_bot)

while True:
    msg = input("Envie uma mensagem \n")
    if msg.lower() == "sair":
        break
    response = chatbot.get_response(msg)
    if float(response.confidence) > 0.4:
        print("Chat: ", response)
    else:
        print("Chat: nao aprendi isso ainda")
