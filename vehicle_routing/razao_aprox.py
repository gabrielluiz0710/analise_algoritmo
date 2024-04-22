import random
import copy
import time
from itertools import permutations

class VRPSolution:
    def __init__(self, routes):
        self.routes = routes
        self.cost = self.calculate_cost()

    def calculate_cost(self, graph):
        cost = 0
        for route in self.routes:
            for i in range(len(route) - 1):
                cost += graph[route[i]][route[i+1]]
        return cost

def generate_initial_solution(graph, num_vehicles):
    num_nodes = len(graph)
    customers = list(range(1, num_nodes))
    random.shuffle(customers)
    routes = [[] for _ in range(num_vehicles)]
    capacities = [17] * num_vehicles
    for customer in customers:
        added = False
        for i in range(num_vehicles):
            if graph[0][customer] <= capacities[i]:
                routes[i].append(customer)
                capacities[i] -= graph[0][customer]
                added = True
                break
        if not added:
            # Se nenhum veículo puder atender o cliente, adicione-o à primeira rota
            routes[0].append(customer)
    return VRPSolution(routes)

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

def tabu_search(graph, num_vehicles, max_iterations, tabu_size):
    current_solution = generate_initial_solution(graph, num_vehicles)
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

# Função para gerar um grafo aleatório com custos de aresta aleatórios
def generate_random_graph(num_nodes):
    graph = [[random.randint(1, 20) for _ in range(num_nodes)] for _ in range(num_nodes)]
    return graph

# Realiza a análise com instâncias gigantes
max_iterations = 100
tabu_size = 10

num_customers_list = [100, 200, 500, 1000]  # Número de clientes para análise
num_vehicles_list = [5, 10, 20]  # Número de veículos para análise

for num_customers in num_customers_list:
    for num_vehicles in num_vehicles_list:
        print(f"Análise para {num_vehicles} veículos e {num_customers} clientes:")
        
        # Gerar um grafo aleatório com o número de clientes especificado
        graph = generate_random_graph(num_customers)
        
        # Executar algoritmo de busca tabu
        best_solution_tabu, execution_time_tabu = tabu_search(graph, num_vehicles, max_iterations, tabu_size)
        
        # Executar algoritmo exato para obter a solução ótima
        melhor_rota, menor_custo, execution_time = VRP_Solver(num_customers, graph, 100, num_vehicles)
        
        # Calcular a razão de aproximação
        approx_ratio = best_solution_tabu.cost / menor_custo
        
        # Resultados
        print("Melhor custo encontrado pelo algoritmo de busca tabu:", best_solution_tabu.cost)
        print("Melhor rota encontrada pelo algoritmo de busca tabu:", best_solution_tabu.routes)
        print("Custo da solução ótima encontrada pelo algoritmo exato:", menor_custo)
        print("Razão de aproximação:", approx_ratio)
        print("Tempo de execução do algoritmo de busca tabu:", execution_time_tabu, "segundos")
        print()
