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

# Lista de diferentes instâncias para teste
instancias = [
    {
        'Itens': [
            {'utilidade': 60, 'peso': 10},
            {'utilidade': 100, 'peso': 20},
            {'utilidade': 120, 'peso': 30}
        ],
        'capMochila': 50
    },
    {
        'Itens': [
            {'utilidade': 40, 'peso': 5},
            {'utilidade': 50, 'peso': 10},
            {'utilidade': 100, 'peso': 20},
            {'utilidade': 90, 'peso': 30}
        ],
        'capMochila': 60
    },
    {
        'Itens': [
            {'utilidade': 10, 'peso': 2},
            {'utilidade': 20, 'peso': 3},
            {'utilidade': 30, 'peso': 5},
            {'utilidade': 40, 'peso': 7}
        ],
        'capMochila': 10
    },
    {
        'Itens': [
            {'utilidade': 15, 'peso': 1},
            {'utilidade': 30, 'peso': 3},
            {'utilidade': 45, 'peso': 5},
            {'utilidade': 60, 'peso': 7}
        ],
        'capMochila': 10
    },
    {
        'Itens': [
            {'utilidade': 10, 'peso': 5},
            {'utilidade': 40, 'peso': 4},
            {'utilidade': 30, 'peso': 6},
            {'utilidade': 50, 'peso': 3}
        ],
        'capMochila': 8
    },
    {
        'Itens': [
            {'utilidade': 25, 'peso': 5},
            {'utilidade': 35, 'peso': 3},
            {'utilidade': 45, 'peso': 4},
            {'utilidade': 60, 'peso': 7}
        ],
        'capMochila': 10
    },
    {
        'Itens': [
            {'utilidade': 30, 'peso': 5},
            {'utilidade': 25, 'peso': 4},
            {'utilidade': 35, 'peso': 3},
            {'utilidade': 40, 'peso': 6}
        ],
        'capMochila': 10
    },
    {
        'Itens': [
            {'utilidade': 40, 'peso': 3},
            {'utilidade': 45, 'peso': 5},
            {'utilidade': 60, 'peso': 7},
            {'utilidade': 15, 'peso': 1}
        ],
        'capMochila': 10
    },
    {
        'Itens': [
            {'utilidade': 20, 'peso': 2},
            {'utilidade': 40, 'peso': 4},
            {'utilidade': 30, 'peso': 3},
            {'utilidade': 60, 'peso': 6}
        ],
        'capMochila': 8
    },
    {
        'Itens': [
            {'utilidade': 30, 'peso': 4},
            {'utilidade': 25, 'peso': 3},
            {'utilidade': 35, 'peso': 5},
            {'utilidade': 40, 'peso': 6}
        ],
        'capMochila': 10
    }
]

# Testando o algoritmo com diferentes instâncias
for idx, instancia in enumerate(instancias):
    Itens = instancia['Itens']
    capMochila = instancia['capMochila']
    resultado, sequencia_otima = prog_dinamica(Itens, capMochila)
    print(f"Instância {idx + 1}:")
    print("Utilidade máxima:", resultado)
    print("Sequência ótima de itens:", sequencia_otima)
    print()