from nltk.chat.util import Chat, reflections
from language import reflections_pt, sentences_pt

print('Ola, sou um chatbot!')
chat = Chat(sentences_pt, reflections_pt)
chat.converse()
