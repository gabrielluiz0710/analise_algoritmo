import random
import time

def gerar_instancia_teste(num_itens, capacidade_maxima):
    itens = [{'utilidade': random.randint(10, 100), 'peso': random.randint(5, 50)} for _ in range(num_itens)]
    return itens, capacidade_maxima

def prog_dinamica(num_itens, capacidade_maxima):
    inicio = time.time()  # Inicia a contagem de tempo
    itens, capMochila = gerar_instancia_teste(num_itens, capacidade_maxima)

    matriz = [[0 for _ in range(capMochila + 1)] for _ in range(num_itens + 1)]
    selecionados = [[False for _ in range(capMochila + 1)] for _ in range(num_itens + 1)]

    for c in range(capMochila + 1):
        matriz[0][c] = 0

    for i in range(1, num_itens + 1):
        for c in range(capMochila + 1):
            aux1 = matriz[i - 1][c]
            if itens[i - 1]['peso'] <= c:
                aux2 = matriz[i - 1][c - itens[i - 1]['peso']] + itens[i - 1]['utilidade']
            else:
                aux2 = 0
            matriz[i][c] = max(aux1, aux2)
            selecionados[i][c] = aux2 > aux1

    # Reconstruir a sequência ótima
    sequencia_otima = []
    c = capMochila
    for i in range(num_itens, 0, -1):
        if selecionados[i][c]:
            sequencia_otima.append(i - 1)
            c -= itens[i - 1]['peso']

    sequencia_otima.reverse()

    num_itens_na_mochila = len(sequencia_otima)
    
    fim = time.time()  # Finaliza a contagem de tempo
    tempo_decorrido = fim - inicio  # Calcula o tempo decorrido

    return matriz[num_itens][capMochila], sequencia_otima, num_itens_na_mochila, tempo_decorrido

num_itens_list = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

# Valor fixo para capacidade_maxima
capacidade_maxima = 50

# Itera sobre os valores de num_itens e executa prog_dinamica para cada um
for num_itens in num_itens_list:
    resultado, _, num_itens_na_mochila, tempo_decorrido = prog_dinamica(num_itens, capacidade_maxima)
    print(f"Para num_itens = {num_itens}:")
    print("Utilidade máxima:", resultado)
    print("Número de itens colocados na mochila:", num_itens_na_mochila)
    print("Tempo decorrido:", tempo_decorrido, "segundos")
    print()