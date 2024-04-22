import itertools
import time

def calcular_custo_rota(graph, rota):
    custo = 0
    for i in range(len(rota) - 1):
        custo += graph[rota[i]][rota[i+1]]
    return custo

def calcular_custo_total(graph, rotas):
    custo_total = 0
    for rota in rotas:
        custo_total += calcular_custo_rota(graph, rota)
    return custo_total

def forca_bruta_vrp(graph, capacidade_veiculo, num_veiculos):
    num_clientes = len(graph) - 1  
    clientes = list(range(1, num_clientes + 1))

    melhor_custo = float('inf')
    melhor_rota = []

    start_time = time.time()

    # Gerar todas as permutações possíveis das rotas dos veículos
    for permutacao in itertools.permutations(clientes):
        rotas = [[] for _ in range(num_veiculos)]
        capacidade_atual = [capacidade_veiculo] * num_veiculos
        cliente_idx = 0

        for cliente in permutacao:
            for i in range(num_veiculos):
                if capacidade_atual[i] >= graph[0][cliente]:
                    rotas[i].append(cliente)
                    capacidade_atual[i] -= graph[0][cliente]
                    break

        for i in range(num_veiculos):
            rotas[i].insert(0, 0)  
            rotas[i].append(0)     

        custo_total = calcular_custo_total(graph, rotas)

        if custo_total < melhor_custo:
            melhor_custo = custo_total
            melhor_rota = rotas

    end_time = time.time()

    execution_time = end_time - start_time

    return melhor_custo, melhor_rota, execution_time

graph = [
    [0, 5, 8, 7, 10, 8, 6, 5, 6, 7],
    [5, 0, 7, 6, 8, 6, 4, 3, 4, 5],
    [8, 7, 0, 6, 7, 6, 4, 6, 5, 6],
    [7, 6, 6, 0, 6, 5, 4, 5, 4, 5],
    [10, 8, 7, 6, 0, 3, 4, 5, 6, 7],
    [8, 6, 6, 5, 3, 0, 2, 3, 4, 5],
    [6, 4, 4, 4, 4, 2, 0, 2, 3, 4],
    [5, 3, 6, 5, 5, 3, 2, 0, 2, 3],
    [6, 4, 5, 4, 6, 4, 3, 2, 0, 2],
    [7, 5, 6, 5, 7, 5, 4, 3, 2, 0]
]

capacidade_veiculo = 17
num_veiculos = 6  

melhor_custo, melhor_rota, execution_time = forca_bruta_vrp(graph, capacidade_veiculo, num_veiculos)

print("Melhor custo encontrado:", melhor_custo)
print("Melhor rota encontrada:", melhor_rota)
print("Tempo de execução:", execution_time, "segundos")