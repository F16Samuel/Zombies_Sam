# utils/algorithms/a_star.py
import heapq

def a_star(grid, start, goal):
    """
    A* algorithm for finding the shortest path in a grid.
    :param grid: 2D list representing the grid (0 for walkable, 1 for obstacles).
    :param start: Starting position (x, y).
    :param goal: Goal position (x, y).
    :return: List of steps as coordinates from start to goal.
    """
    # Directions for movement (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def heuristic(a, b):
        """Manhattan distance heuristic."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Priority queue (open list)
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), 0, start))  # (f, g, position)
    
    # Came from (for path reconstruction)
    came_from = {}
    
    # G score (cost to get to each position)
    g_score = {start: 0}
    
    while open_list:
        _, current_g, current = heapq.heappop(open_list)

        # If we reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()  # Return path from start to goal
            return path

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = current_g + 1  # Assume each move costs 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, tentative_g_score, neighbor))
                    came_from[neighbor] = current

    return []  # If no path found, return an empty list
