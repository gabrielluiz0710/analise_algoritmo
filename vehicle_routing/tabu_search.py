import random

# Função para construir uma solução inicial
def construct_initial_solution(customers):
    # Supondo que 'customers' é uma lista de clientes, onde cada cliente é representado por um vértice
    # Aqui, a solução inicial é uma permutação aleatória dos clientes
    initial_solution = customers[:]
    random.shuffle(initial_solution)
    return initial_solution

# Função para calcular o custo total de uma solução de rota
def calculate_total_cost(solution, distance_matrix):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += distance_matrix[solution[i]][solution[i+1]]
    total_cost += distance_matrix[solution[-1]][solution[0]]  # Adiciona o custo de retorno ao depósito
    return total_cost

# Função para gerar uma vizinhança de uma solução
def generate_neighborhood(solution):
    neighborhood = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # Troca dois clientes na rota
            neighborhood.append(neighbor)
    return neighborhood

# Função para selecionar o melhor vizinho não-tabu
def select_best_neighbor(neighborhood, tabu_list, distance_matrix):
    best_neighbor = None
    best_cost = float('inf')
    for neighbor in neighborhood:
        if neighbor not in tabu_list:
            cost = calculate_total_cost(neighbor, distance_matrix)
            if cost < best_cost:
                best_neighbor = neighbor
                best_cost = cost
    return best_neighbor

# Função para atualizar a lista tabu
def update_tabu_list(tabu_list, move, tabu_tenure):
    tabu_list.append(move)
    if len(tabu_list) > tabu_tenure:
        tabu_list.pop(0)

# Função para realizar a busca tabu
def tabu_search_vrp(customers, distance_matrix, max_iterations, tabu_tenure):
    x = construct_initial_solution(customers)  # Constrói uma solução inicial
    best_solution = x.copy()                   # Melhor solução encontrada até o momento
    tabu_list = []                             # Lista tabu vazia
    iteration_count = 0                        # Contador de iterações sem melhoria

    while iteration_count < max_iterations:
        neighborhood = generate_neighborhood(x)  # Gera a vizinhança da solução atual
        best_neighbor = select_best_neighbor(neighborhood, tabu_list, distance_matrix)  # Seleciona o melhor vizinho não-tabu

        # Movimento para o melhor vizinho
        x = best_neighbor
        if calculate_total_cost(x, distance_matrix) < calculate_total_cost(best_solution, distance_matrix):
            best_solution = x.copy()
            iteration_count = 0  # Reinicia o contador de iterações sem melhoria
        else:
            iteration_count += 1

        # Atualização da Lista Tabu
        update_tabu_list(tabu_list, x, tabu_tenure)  # Atualiza a lista tabu com o movimento realizado

    return best_solution

# Exemplo de uso
customers = [1, 2, 3, 4, 5]  # Exemplo de clientes
distance_matrix = [[0, 10, 15, 20, 25],  # Exemplo de matriz de distâncias
                   [10, 0, 35, 25, 30],
                   [15, 35, 0, 30, 20],
                   [20, 25, 30, 0, 10],
                   [25, 30, 20, 10, 0]]
max_iterations = 1000   # Número máximo de iterações
tabu_tenure = 10        # Tempo de permanência na lista tabu

best_solution = tabu_search_vrp(customers, distance_matrix, max_iterations, tabu_tenure)
print("Melhor solução encontrada:", best_solution)
