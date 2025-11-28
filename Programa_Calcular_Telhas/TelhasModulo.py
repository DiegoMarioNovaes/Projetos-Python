import math

# Dicionário: rendimento de cada tipo de telha por metro quadrado
RENDIMENTO_TELHAS = {
    "ceramica": 16,
    "fibrocimento": 2,
    "metalica": 1
}

def calcular_telhas(comprimento, largura, tipo):
    """
    Calcula quantidade de telhas usando rendimento por m².
    Retorna None se o tipo de telha não for encontrado.
    """
    tipo = tipo.lower()

    if tipo not in RENDIMENTO_TELHAS:
        return None

    area = comprimento * largura
    rendimento = RENDIMENTO_TELHAS[tipo]

    # Arredondar para cima
    return math.ceil(area * rendimento)
