def prog_dinamica(Itens, capMochila):
    matriz = [[0 for _ in range(capMochila + 1)] for _ in range(len(Itens) + 1)]
    selecionados = [[False for _ in range(capMochila + 1)] for _ in range(len(Itens) + 1)]

    for c in range(capMochila + 1):
        matriz[0][c] = 0

    for i in range(1, len(Itens) + 1):
        for c in range(capMochila + 1):
            aux1 = matriz[i - 1][c]
            if Itens[i - 1]['peso'] <= c:
                aux2 = matriz[i - 1][c - Itens[i - 1]['peso']] + Itens[i - 1]['utilidade']
            else:
                aux2 = 0
            matriz[i][c] = max(aux1, aux2)
            selecionados[i][c] = aux2 > aux1

    # Reconstruir a sequência ótima
    sequencia_otima = []
    c = capMochila
    for i in range(len(Itens), 0, -1):
        if selecionados[i][c]:
            sequencia_otima.append(i - 1)
            c -= Itens[i - 1]['peso']

    sequencia_otima.reverse()

    return matriz[len(Itens)][capMochila], sequencia_otima

# Exemplo de utilização
Itens = [
    {'utilidade': 60, 'peso': 10},
    {'utilidade': 100, 'peso': 20},
    {'utilidade': 120, 'peso': 30}
]
capMochila = 50

resultado, sequencia_otima = prog_dinamica(Itens, capMochila)
print("Utilidade máxima:", resultado)
print("Sequência ótima de itens:", sequencia_otima)
