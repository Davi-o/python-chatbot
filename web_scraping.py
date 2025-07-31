import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

url = 'https://www.exempl.com.br/perguntas-e-respostas-de-conhecimentos-gerais/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

container = soup.select_one('article, .post-content, .entry-content, main') or soup.body

questions = container.find_all('h2')

data = []
current_question = None

for element in container.find_all(True):
    if element.name == 'h2':
        question_text = unidecode(element.get_text(strip=True))
        current_question = {
            'pergunta': question_text,
            'element': element,
            'resposta': "Resposta não encontrada"
        }
        data.append(current_question)
    
    elif element.name == 'p' and current_question:
        strong_tag = element.find('strong')
        if strong_tag:
            answer_text = unidecode(strong_tag.get_text(strip=True))
            
            if len(answer_text) < 100:
                current_question['resposta'] = answer_text
                current_question = None

for item in data:
    if item['resposta'] == "Resposta não encontrada":
        element = item['element']

        next_sibling = element.find_next_sibling()
        while next_sibling:
            if next_sibling.name == 'p' and next_sibling.find('strong'):
                strong_tag = next_sibling.find('strong')
                answer = unidecode(strong_tag.get_text(strip=True))
                item['resposta'] = answer
                break
            next_sibling = next_sibling.find_next_sibling()

for item in data:
    del item['element']

documents = [f"{item['pergunta']} {item['resposta']}" for item in data]