from web_scraping import documents, data
from language import user_welcoming, bot_welcoming
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
import random
import numpy as np
import string
from unidecode import unidecode

nltk.download('punkt')
nltk.download('stopwords')

def process_text(text, is_answer=False):
    text = text.lower()
    
    if not is_answer:
        text = text.translate(str.maketrans('', '', string.punctuation))
    
    text = unidecode(text)
    
    tokens = word_tokenize(text, language='portuguese')
    
    important_stopwords = {'e', 'ou', 'sim', 'nao', 'eh', 'ser', 'tem'}
    stop_words = set(stopwords.words('portuguese')) - important_stopwords
    
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return " ".join(filtered_tokens)

processed_questions = [process_text(item['pergunta']) for item in data]
processed_answers = [process_text(item['resposta'], is_answer=True) for item in data]

question_vector = TfidfVectorizer()
question_tfidf = question_vector.fit_transform(processed_questions)

answer_vector = TfidfVectorizer()
answer_tfidf = answer_vector.fit_transform(processed_answers)

def welcome(text):
    for word in text.split():
        if word.lower() in user_welcoming:
            return random.choice(bot_welcoming)
    return None

def find_similar_answer(question):
    processed_q = process_text(question)
    query_vec = question_vector.transform([processed_q])
    similarities = cosine_similarity(query_vec, question_tfidf)
    similar_index = np.argmax(similarities)
    return data[similar_index]['resposta']

def verify_answer(user_answer, correct_answer):
    user_pp = process_text(user_answer, is_answer=True)
    correct_pp = process_text(correct_answer, is_answer=True)
    
    if user_pp == correct_pp:
        return True
    
    answers = [correct_pp, user_pp]
    vectors = answer_vector.transform(answers)
    similarity = cosine_similarity(vectors)[0][1]
    
    keywords = set(word_tokenize(correct_pp))
    user_words = set(word_tokenize(user_pp))
    overlap = len(keywords & user_words) / len(keywords) if keywords else 0
    
    return similarity >= 0.6 or overlap >= 0.7

def actual_quiz():
    points = 0
    questions_made = 0
    
    print("\nBem-vindo ao Quiz de Conhecimentos Gerais!")
    print("Responda às perguntas. Digite 'sair' a qualquer momento para encerrar.\n")
    
    while True:
        question_item = random.choice(data)
        question = question_item['pergunta']
        correct_answer = question_item['resposta']
        
        print(f"Pergunta: {question}")
        user_answer = input("Sua resposta: ").strip()
        
        if user_answer.lower() in ['sair', 'exit', 'sair()']:
            print("\nQuiz encerrado!")
            break
        
        if verify_answer(user_answer, correct_answer):
            print(f"Correto! A resposta é: {correct_answer}")
            points += 1
        else:
            print(f"Incorreto. A resposta correta é: {correct_answer}")
        
        questions_made += 1
        print(f"Pontuação atual: {points}/{questions_made}")
        print("-" * 50 + "\n")
    
    if questions_made > 0:
        print(f"🏁 Resultado final: {points}/{questions_made} acertos!")
        print(f"📊 Porcentagem de acertos: {(points/questions_made)*100:.2f}%")