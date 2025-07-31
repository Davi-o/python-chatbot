from conversation import welcome, actual_quiz, find_similar_answer

def main_menu():
    print(welcome("Oi"))
    
    while True:
        print("\n" + "=" * 50)
        print(" MENU PRINCIPAL ".center(50, '='))
        print("=" * 50)
        print("1. Iniciar Quiz")
        print("2. Fazer Perguntas")
        print("0. Sair")
        
        escolha = input("\nEscolha uma opção: ").strip()
        
        if escolha == '1':
            actual_quiz()
        elif escolha == '2':
            ask_questions()
        elif escolha in ['0', 'sair']:
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def ask_questions():
    print("\nModo de Perguntas Livres (digite 'sair' para voltar)")
    while True:
        question = input("\nVocê: ").strip()
        
        if question.lower() in ['sair', 'voltar']:
            break
            
        answer = find_similar_answer(question)
        print(f"Bot: {answer}")

if __name__ == "__main__":
    main_menu()