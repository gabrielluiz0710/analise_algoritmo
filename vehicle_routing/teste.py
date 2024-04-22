import random
import copy
import time
from itertools import permutations

class VRPSolution:
    def __init__(self, routes, graph):
        self.routes = routes
        self.graph = graph
        self.cost = self.calculate_cost()

    def calculate_cost(self):
        cost = 0
        for route in self.routes:
            for i in range(len(route) - 1):
                cost += self.graph[route[i]][route[i+1]]
        return cost

def generate_initial_solution(graph, num_vehicles, distancias):
    num_nodes = len(graph)
    customers = list(range(1, num_nodes))
    random.shuffle(customers)
    routes = [[] for _ in range(num_vehicles)]
    capacities = [17] * num_vehicles
    for customer in customers:
        added = False
        for i in range(num_vehicles):
            if distancias[0][customer] <= capacities[i]:
                routes[i].append(customer)
                capacities[i] -= distancias[0][customer]
                added = True
                break
        if not added:
            # Se nenhum veículo puder atender o cliente, adicione-o à primeira rota
            routes[0].append(customer)
    return VRPSolution(routes, graph)

def get_neighborhood(solution):
    neighborhood = []
    for i in range(len(solution.routes)):
        for j in range(len(solution.routes[i])):
            for k in range(len(solution.routes)):
                if i != k:
                    new_solution = copy.deepcopy(solution)
                    customer = new_solution.routes[i].pop(j)
                    new_solution.routes[k].append(customer)
                    neighborhood.append(new_solution)
    return neighborhood

def tabu_search(graph, num_vehicles, max_iterations, tabu_size, distancias):
    current_solution = generate_initial_solution(graph, num_vehicles, distancias)
    best_solution = current_solution
    tabu_list = []

    start_time = time.time()

    for _ in range(max_iterations):
        neighborhood = get_neighborhood(current_solution)
        best_neighbor = None
        for neighbor in neighborhood:
            if neighbor not in tabu_list:
                if best_neighbor is None or neighbor.cost < best_neighbor.cost:
                    best_neighbor = neighbor
        if best_neighbor is None:
            break

        current_solution = best_neighbor
        if current_solution.cost < best_solution.cost:
            best_solution = current_solution

        tabu_list.append(current_solution)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    end_time = time.time()
    execution_time = end_time - start_time

    return best_solution, execution_time

def calcular_custo_rota(rota, distancias):
    custo = 0
    for i in range(len(rota) - 1):
        cidade_atual = rota[i]
        proxima_cidade = rota[i + 1]
        custo += distancias[cidade_atual][proxima_cidade]
    return custo

def VRP_Solver(num_customers, distancias, capacidade_veiculo, num_veiculos):
    menor_custo = float('inf')
    melhor_rota = None

    # Gerar todas as permutações das cidades para as rotas dos veículos
    cidades = list(range(1, num_customers))
    rotas_possiveis = permutations(cidades)

    start_time = time.time()

    # Calcular custo para cada rota e selecionar a melhor
    for rota in rotas_possiveis:
        rota = [0] + list(rota) + [0]  # Adicionar o depósito no início e no fim da rota
        custo_rota = calcular_custo_rota(rota, distancias)

        if custo_rota < menor_custo:
            menor_custo = custo_rota
            melhor_rota = rota

    end_time = time.time()
    execution_time = end_time - start_time

    return melhor_rota, menor_custo, execution_time

# Função para gerar um grafo aleatório com custos de aresta aleatórios
def generate_random_graph(num_nodes):
    graph = [[random.randint(1, 20) for _ in range(num_nodes)] for _ in range(num_nodes)]
    return graph

# Executar análises para diferentes números de clientes e veículos
num_customers_list = [3, 5, 7, 9, 11]  # Número de clientes para análise
num_vehicles_list = [2, 3, 5, 8]  # Número de veículos para análise

for num_customers in num_customers_list:
    for num_vehicles in num_vehicles_list:
        print(f"Análise para {num_vehicles} veículos e {num_customers} clientes:")
        
        # Gerar distâncias aleatórias para o número de clientes especificado
        distancias = [[0] * num_customers for _ in range(num_customers)]
        for i in range(num_customers):
            for j in range(num_customers):
                distancias[i][j] = random.randint(1, 10)  # Intervalo de distâncias reduzido
        
        # Definir capacidade do veículo
        capacidade_veiculo = 100  # Defina a capacidade conforme necessário
        
        # Executar algoritmo VRP exato
        melhor_rota, menor_custo, execution_time = VRP_Solver(num_customers, distancias, capacidade_veiculo, num_vehicles)
        
        # Resultados
        print("Algoritmo exato:")
        print("Melhor rota encontrada:", melhor_rota)
        print("Menor custo encontrado:", menor_custo)
        print("Tempo de execução:", execution_time, "segundos")
        print()
        
        # Executar algoritmo de busca tabu
        graph_tabu = generate_random_graph(num_customers)
        best_solution_tabu, execution_time_tabu = tabu_search(graph_tabu, num_vehicles, 100, 10, distancias)
        
        # Resultados
        print("Algoritmo de busca tabu:")
        print("Melhor custo encontrado:", best_solution_tabu.cost)
        print("Melhor rota encontrada:", best_solution_tabu.routes)
        print("Tempo de execução:", execution_time_tabu, "segundos")
        print()
