def criar_aeronave():
    fileiras = ['A', 'B', 'C', 'D', 'E', 'F']  # As fileiras da aeronave
    aeronave = {fileira: [None] * 30 for fileira in fileiras}  # Criar 30 assentos por fileira
    return aeronave

def validar_assento(fileira, coluna):
    fileiras_validas = ['A', 'B', 'C', 'D', 'E', 'F']
    if fileira not in fileiras_validas:
        print(f"Fileira {fileira} inválida. As fileiras válidas são: A, B, C, D, E, F.")
        return False
    if not (1 <= coluna <= 30):
        print(f"Coluna {coluna} inválida. O número do assento deve estar entre 1 e 30.")
        return False
    return True

def marcar_assento(aeronave):
    while True:
        entrada = input("Digite o assento que deseja marcar EX: A10 (ou 'sair' para parar): ").strip()
        
        if entrada.lower() == 'sair':
            break  # Sai do loop e volta ao menu
        
        # Tenta extrair fileira e coluna da entrada
        try:
            fileira = entrada[0].upper()  # Primeira letra é a fileira
            coluna = int(entrada[1:])  # O restante é a coluna (convertido para inteiro)

            if validar_assento(fileira, coluna):  # Verifica se o assento é válido
                if aeronave[fileira][coluna - 1] is None:  # Verifica se o assento está livre
                    aeronave[fileira][coluna - 1] = True  # Marca como ocupado
                    print(f"Assento {fileira}{coluna} marcado com sucesso.")
                else:
                    print(f"Assento {fileira}{coluna} já está ocupado.")
            else:
                print(f"Assento {fileira}{coluna} é inválido.")
        
        except (ValueError, IndexError):
            print("Formato de assento inválido. Use formato correto (ex: A10).")

    print("Você saiu da marcação de assentos.")

def desmarcar_assento(aeronave, fileira, coluna):
    fileira = fileira.upper()  # Garantir que a fileira seja maiúscula
    if validar_assento(fileira, coluna):
        if aeronave[fileira][coluna - 1] is not None:  # Verificar se o assento está ocupado
            aeronave[fileira][coluna - 1] = None  # Desocupar o assento
            print(f"Assento {fileira}{coluna} desmarcado com sucesso.")
        else:
            print(f"Assento {fileira}{coluna} já está vazio.")

def remarcar_assento(aeronave):
    fileira_atual = input("Informe a fileira do assento atual (A-F): ").upper()
    coluna_atual = int(input("Informe o número do assento atual (1-30): "))
    
    if validar_assento(fileira_atual, coluna_atual):
        if aeronave[fileira_atual][coluna_atual - 1] is None:
            print(f"O assento {fileira_atual}{coluna_atual} está vazio. Não é possível remarcar.")
            return
        
        fileira_nova = input("Informe a nova fileira (A-F): ").upper()
        coluna_nova = int(input("Informe o novo número do assento (1-30): "))

        if validar_assento(fileira_nova, coluna_nova):
            if aeronave[fileira_nova][coluna_nova - 1] is None:  # Novo assento está livre
                desmarcar_assento(aeronave, fileira_atual, coluna_atual)
                aeronave[fileira_nova][coluna_nova - 1] = True  # Marca o novo assento como ocupado
                print(f"Assento {fileira_atual}{coluna_atual} foi remarcado para {fileira_nova}{coluna_nova}.")
            else:
                print(f"O novo assento {fileira_nova}{coluna_nova} já está ocupado.")
    else:
        print("Assento atual inválido.")

def gerar_relatorio(aeronave):
    ocupados = 0
    total_pago = 0
    primeira_classe = 0
    classe_normal = 0
    total_primeira_classe = 0
    total_classe_normal = 0

    print("\n=== Mapa dos assentos ===")
    for fileira, assentos in aeronave.items():
        esquema = ""
        for coluna in range(30):
            if assentos[coluna] is None:
                esquema += "O "  # Assento desmarcado
            else:
                esquema += "X "  # Assento marcado
        
        print(f"Fileira {fileira}: {esquema.strip()}")  # Exibir esquema dos assentos por fileira
    
    # Contagem e valores
    for fileira, assentos in aeronave.items():
        for coluna in range(30):
            if assentos[coluna] is not None:  # Assento ocupado
                ocupados += 1
                if coluna < 6:  # Primeira classe (primeiras 6 fileiras)
                    total_pago += 100
                    total_primeira_classe += 100  # Acumulando valor arrecadado na primeira classe
                    primeira_classe += 1
                else:  # Classe normal
                    total_pago += 80
                    total_classe_normal += 80  # Acumulando valor arrecadado na classe normal
                    classe_normal += 1

    print(f"\nAssentos ocupados na primeira classe: {primeira_classe}")
    print(f"Assentos ocupados na classe normal: {classe_normal}")
    print(f"Total de assentos ocupados: {ocupados}")
    print(f"Total arrecadado na primeira classe: R${total_primeira_classe}")
    print(f"Total arrecadado na classe normal: R${total_classe_normal}")
    print(f"Total arrecadado: R${total_pago}")

# MENU
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Marcar assento")
        print("2. Desmarcar assento")
        print("3. Remarcar assento")
        print("4. Relatório")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            marcar_assento(aeronave)
        
        elif opcao == "2":
            fileira = input("Informe a fileira (A-F): ")
            coluna = int(input("Informe o número do assento (1-30): "))
            desmarcar_assento(aeronave, fileira, coluna)
        
        elif opcao == "3":
            remarcar_assento(aeronave)
        
        elif opcao == "4":
            gerar_relatorio(aeronave)
        
        elif opcao == "5":
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opção inválida.")

# Iniciar o programa
aeronave = criar_aeronave()
menu()