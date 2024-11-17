from utils.algorithms.a_star import a_star

# Example of a simple graph for testing
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def find_path(start, goal, heuristic):
    path = a_star(graph, start, goal, heuristic)
    return path
