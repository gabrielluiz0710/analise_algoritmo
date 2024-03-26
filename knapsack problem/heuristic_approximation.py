import random

def prog_aprHeur(Itens, capMochila):
    sequencia_aproximada = []
    quickSort(Itens, 0, len(Itens) - 1)
    utilidade_maxima = aproxima(Itens, capMochila, sequencia_aproximada)
    imprime(utilidade_maxima, sequencia_aproximada)

def quickSort(Itens, left, right):
    def troca(a, b):
        Itens[a], Itens[b] = Itens[b], Itens[a]

    def seleciona_aleatorio(left, right):
        return random.randint(left, right)

    last = left
    if left >= right:
        return
    troca(left, seleciona_aleatorio(left, right))
    for i in range(left + 1, right + 1):
        if (Itens[i]['utilidade'] / Itens[i]['peso']) > (Itens[left]['utilidade'] / Itens[left]['peso']):
            last += 1
            troca(i, last)
    troca(left, last)
    quickSort(Itens, left, last - 1)
    quickSort(Itens, last + 1, right)

def aproxima(Itens, capMochila, sequencia_aproximada):
    utilidade_maxima = 0
    peso_atual = 0
    i = len(Itens) - 1
    while i >= 0 and peso_atual + Itens[i]['peso'] <= capMochila:
        sequencia_aproximada.append(i)
        utilidade_maxima += Itens[i]['utilidade']
        peso_atual += Itens[i]['peso']
        i -= 1
    return utilidade_maxima

def imprime(utilidade_maxima, sequencia_aproximada):
    print("Utilidade máxima:", utilidade_maxima)
    print("Sequência aproximada:", sequencia_aproximada[::-1])  # Revertendo a sequência de índices

# Exemplo de utilização
Itens = [
    {'utilidade': 60, 'peso': 10},
    {'utilidade': 100, 'peso': 20},
    {'utilidade': 120, 'peso': 30}
]
capMochila = 50

prog_aprHeur(Itens, capMochila)
