import heapq

def dijkstra(graph, start, goal):
    # Min-heap priority queue
    queue = [(0, start)]  # (cost, node)
    # Dictionary to store the shortest path cost
    costs = {start: 0}
    # Dictionary to store the path
    parent = {start: None}

    while queue:
        current_cost, node = heapq.heappop(queue)

        # If the goal is found, reconstruct the path
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]  # Return reversed path
        
        # Explore all neighbors
        for neighbor, cost in graph[node].items():
            new_cost = current_cost + cost
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(queue, (new_cost, neighbor))
    
    return None  # Return None if no path exists
