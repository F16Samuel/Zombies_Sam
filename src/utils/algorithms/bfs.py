from collections import deque

def bfs(graph, start, goal):
    # Queue to hold the nodes to explore
    queue = deque([start])
    # Dictionary to store the path
    parent = {start: None}

    while queue:
        node = queue.popleft()
        
        # If the goal is found, reconstruct the path
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]  # Return reversed path
        
        # Explore all neighbors
        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    
    return None  # Return None if no path exists
