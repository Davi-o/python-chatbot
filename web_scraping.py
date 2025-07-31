import requests
from bs4 import BeautifulSoup

url = 'https://www.exempl.com.br/perguntas-e-respostas-de-conhecimentos-gerais/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

container = soup.select_one('article, .post-content, .entry-content, main') or soup.body

questions = container.find_all('h2')

answers = [] 
for p in container.find_all('p'):
    if p.find('strong'):
        answer = p.find('strong')
        
        answers.append(answer.get_text(strip=True))

data = []
for i, question in enumerate(questions):
    entry = {
        'pergunta': question.get_text(strip=True),
        'resposta': answers[i] if i < len(answers) else "Resposta não encontrada"
    }
    data.append(entry)