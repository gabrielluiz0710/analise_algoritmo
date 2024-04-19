from itertools import permutations

def calcular_custo_rota(rota, distancias):
    custo = 0
    for i in range(len(rota) - 1):
        cidade_atual = rota[i]
        proxima_cidade = rota[i + 1]
        custo += distancias[cidade_atual][proxima_cidade]
    return custo

def VRP_Solver(n_vertices, distancias, capacidade_veiculo):
    menor_custo = float('inf')
    melhor_rota = None

    # Gerar todas as permutações das cidades para as rotas dos veículos
    cidades = list(range(1, n_vertices))
    rotas_possiveis = permutations(cidades)

    # Calcular custo para cada rota e selecionar a melhor
    for rota in rotas_possiveis:
        rota = [0] + list(rota) + [0]  # Adicionar o depósito no início e no fim da rota
        custo_rota = calcular_custo_rota(rota, distancias)

        if custo_rota < menor_custo:
            menor_custo = custo_rota
            melhor_rota = rota

    return melhor_rota, menor_custo

# Exemplo de uso:
if __name__ == "__main__":
    n_vertices = 5  # Número de vértices (cidades)
    distancias = [
        [0, 10, 15, 20, 25],  # Distâncias da cidade 0 para as outras cidades
        [10, 0, 35, 25, 30],  # Distâncias da cidade 1 para as outras cidades
        [15, 35, 0, 30, 10],  # Distâncias da cidade 2 para as outras cidades
        [20, 25, 30, 0, 5],   # Distâncias da cidade 3 para as outras cidades
        [25, 30, 10, 5, 0]    # Distâncias da cidade 4 para as outras cidades
    ]
    capacidade_veiculo = 100  # Capacidade do veículo

    melhor_rota, menor_custo = VRP_Solver(n_vertices, distancias, capacidade_veiculo)
    print("Melhor rota:", melhor_rota)
    print("Menor custo:", menor_custo)
