import math
from TelhasModulo import calcular_telhas

def menu():
    opcoes = (
        "1 - Calcular quantidade de telhas",
        "2 - Sobre o programa",
        "3 - Sair"
    )

    while True:
        print("\n===== MENU PRINCIPAL =====")
        for opcao in opcoes:
            print(opcao)

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            executar_calculo()
        elif escolha == "2":
            print("\nPrograma criado para calcular a quantidade de telhas necessárias.")
        elif escolha == "3":
            print("Saindo do programa... Obrigado por usar!")
            break
        else:
            print("Opção inválida! Tente novamente.")

def executar_calculo():
    print("\n===== CÁLCULO DE TELHAS =====")
    print("Digite 'voltar' para retornar ao menu.")

    comp = input("Comprimento do telhado (m): ").strip().lower()
    if comp == "voltar":
        return

    larg = input("Largura do telhado (m): ").strip().lower()
    if larg == "voltar":
        return

    tipo = input("Tipo de telha (ceramica, fibrocimento, metalica): ").strip().lower()
    if tipo == "voltar":
        return

    # Tratamento de erros
    try:
        comp = float(comp)
        larg = float(larg)
    except ValueError:
        print("Valores inválidos! Digite apenas números.")
        return

    total_telhas = calcular_telhas(comp, larg, tipo)

    if total_telhas is None:
        print("Tipo de telha inválido!")
    else:
        print(f"\nQuantidade aproximada de telhas necessárias: {total_telhas}")

menu()
