
reflections_pt = {
    'eu': 'voce',
    'eu sou': 'voce e',
    'eu era': 'voce era',
    'eu iria': 'voce iria',
    'eu irei': 'voce ira',
    'meu': 'seu',
    'voce': 'eu',
    'voce e': 'eu sou',
    'voce era': 'eu era',
    'voce iria': 'eu iria',
    'seu': 'meu'
}

sentences_pt = [
    r'oi|ola|opa|eai|oii|eae',
    ['ola', 'como vai?', 'tudo bem?']
], [
    r'qual o seu nome?',
    ['Meu nome e ChatBot. Como posso ajuda-lo?']
], [
    r'(.*) sua idade',
    ['nao tenho nenhuma idade']
],[
    r'meu nome e (.*)',
    ['Ola %1, como voce esta hoje?']
],[
    r'sou (.*)',
    ['Ola %1, tudo bem?']
], [
    r'qual roupa voce me indica hoje?',
    ['uma blusa','uma calca', 'uma bermuda','um casaco']
], [
    r'quais roupas estao em promocao?',
    ['a bermuda', 'a blusa']
]

sentence_to_chatter_bot = [
    "oi", "como vai?",
    "qual seu nome", "sou um chatbot",
    "qual roupa voce me indica?", "indico uma camiseta",
    "qual roupa esta em promocao?", "a camiseta"
]
