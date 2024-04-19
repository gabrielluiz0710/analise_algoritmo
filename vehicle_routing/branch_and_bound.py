import itertools
import sys
import time

class Node:
    def __init__(self, path, cost, lower_bound):
        self.path = path
        self.cost = cost
        self.lower_bound = lower_bound

def calculate_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]
    return cost

def calculate_lower_bound(graph, path):
    return calculate_cost(graph, path)

def branch_and_bound_vrp(graph, num_vehicles):
    num_nodes = len(graph)
    best_solution = sys.maxsize
    initial_path = [0]
    queue = [Node(initial_path, 0, 0)]

    while queue:
        node = queue.pop(0)
        if len(node.path) == num_nodes:
            # Nó representa uma solução completa
            cost = node.cost + graph[node.path[-1]][0]  # Custos do último cliente de volta ao depósito
            if cost < best_solution:
                best_solution = cost
                best_path = node.path
        else:
            # Expande o nó em nós filhos
            remaining_nodes = set(range(num_nodes)) - set(node.path)
            for perm in itertools.permutations(remaining_nodes, len(remaining_nodes)):
                child_path = node.path + list(perm)
                child_cost = calculate_cost(graph, child_path)
                child_lower_bound = calculate_lower_bound(graph, child_path)
                if child_lower_bound < best_solution:
                    queue.append(Node(child_path, child_cost, child_lower_bound))

    return best_solution, best_path

# Função para gerar instâncias aleatórias de VRP com número variável de nós
def generate_random_instance(num_nodes):
    import random
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            graph[i][j] = random.randint(1, 100)  # Distâncias aleatórias
            graph[j][i] = graph[i][j]  # Grafo simétrico
    return graph

# Testar várias instâncias com números gigantes e mais nós
for num_nodes in [1, 2, 3, 4, 5]:
    print(f"Número de nós por instância: {num_nodes}")
    for num_instances in [100, 200, 300, 400, 500]:
        print(f"Número de instâncias: {num_instances}")
        total_time = 0
        best_solution = sys.maxsize
        for i in range(num_instances):
            graph = generate_random_instance(num_nodes)
            start_time = time.time()
            cost, _ = branch_and_bound_vrp(graph, 1)
            end_time = time.time()
            total_time += end_time - start_time
            best_solution = min(best_solution, cost)
        avg_time = total_time / num_instances
        print("Melhor solução:", best_solution)
        print("Tempo médio de execução:", avg_time, "segundos")
        print()
