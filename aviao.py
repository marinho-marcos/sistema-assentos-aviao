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

def marcar_assento(aeronave, fileira, coluna):
    fileira = fileira.upper()  # Garantir que a fileira seja maiúscula
    if validar_assento(fileira, coluna):
        if aeronave[fileira][coluna - 1] is None:  # Verificar se o assento está livre
            aeronave[fileira][coluna - 1] = True  # Marcar como ocupado
            print(f"Assento {fileira}{coluna} marcado com sucesso.")
        else:
            print(f"Assento {fileira}{coluna} já está ocupado.")

def desmarcar_assento(aeronave, fileira, coluna):
    fileira = fileira.upper()  # Garantir que a fileira seja maiúscula
    if validar_assento(fileira, coluna):
        if aeronave[fileira][coluna - 1] is not None:  # Verificar se o assento está ocupado
            aeronave[fileira][coluna - 1] = None  # Desocupar o assento
            print(f"Assento {fileira}{coluna} desmarcado com sucesso.")
        else:
            print(f"Assento {fileira}{coluna} já está vazio.")

def gerar_relatorio(aeronave):
    ocupados = 0
    total_pago = 0
    primeira_classe = 0
    classe_normal = 0

    print("\n=== Mapa dos assentos ===")
    for fileira, assentos in aeronave.items():
        esquema = ""
        for coluna in range(30):
            if assentos[coluna] is None:
                esquema += "O "  # Assento desmarcado
            else:
                esquema += "X "  # Assento marcado
        
        print(f"Fileira {fileira}: {esquema.strip()}")
    
    # Contagem e valores
    for fileira, assentos in aeronave.items():
        for coluna in range(30):
            if assentos[coluna] is not None:  # Assento ocupado
                ocupados += 1
                if coluna < 6:  # Primeira classe (primeiras 6 fileiras)
                    total_pago += 100
                    primeira_classe += 1
                else:  # Classe normal
                    total_pago += 80
                    classe_normal += 1

    print(f"\nTotal de assentos ocupados: {ocupados}")
    print(f"Total arrecadado: R${total_pago}")
    print(f"Assentos ocupados na primeira classe: {primeira_classe}")
    print(f"Assentos ocupados na classe normal: {classe_normal}")

# Função para permitir a seleção de múltiplos assentos
def selecionar_assentos(aeronave):
    while True:
        print("\n=== Seleção de Assentos ===")
        fileira = input("Informe a fileira (A-F) ou 'SAIR' para encerrar: ").upper()
        if fileira == "SAIR":
            break
        coluna = int(input("Informe o número do assento (1-30): "))
        marcar_assento(aeronave, fileira, coluna)

#MENU
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Marcar assentos")
        print("2. Desmarcar assento")
        print("3. Relatório")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            selecionar_assentos(aeronave)
        
        elif opcao == "2":
            fileira = input("Informe a fileira (A-F): ")
            coluna = int(input("Informe o número do assento (1-30): "))
            desmarcar_assento(aeronave, fileira, coluna)
        
        elif opcao == "3":
            gerar_relatorio(aeronave)
        
        elif opcao == "4":
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opção inválida.")

# Iniciar o programa
aeronave = criar_aeronave()
menu()