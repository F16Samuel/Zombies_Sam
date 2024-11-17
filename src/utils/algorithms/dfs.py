def dfs(graph, start, goal):
    # Stack to hold the nodes to explore
    stack = [start]
    # Dictionary to store the path
    parent = {start: None}

    while stack:
        node = stack.pop()
        
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
                stack.append(neighbor)
    
    return None  # Return None if no path exists
