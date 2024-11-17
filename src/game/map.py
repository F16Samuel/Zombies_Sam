import pygame

class GameMap:
    def __init__(self, grid_height, grid_width, grid_size):
        """
        Initialize the game map with a grid layout.
        :param grid_height: Number of rows in the grid.
        :param grid_width: Number of columns in the grid.
        :param grid_size: Size of each grid cell in pixels.
        """
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid_size = grid_size

        # Define map layout: 'R' for road, 'O' for obstacle, 'G' for goal
        self.grid = [
            ['R', 'R', 'R', 'O', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['R', 'O', 'R', 'O', 'R', 'G', 'R', 'R', 'R', 'O', 'O', 'R', 'O', 'R', 'O', 'R'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'O', 'R', 'R', 'R', 'R', 'R', 'O', 'R', 'R'],
            ['O', 'R', 'O', 'O', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'O', 'R', 'R', 'R', 'R'],
            ['R', 'R', 'R', 'R', 'O', 'R', 'R', 'R', 'R', 'R', 'O', 'O', 'R', 'O', 'O', 'R'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'O', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['R', 'O', 'O', 'O', 'R', 'O', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'O', 'R'],
            ['R', 'R', 'R', 'O', 'R', 'R', 'R', 'R', 'R', 'O', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['R', 'O', 'R', 'R', 'R', 'R', 'O', 'R', 'R', 'R', 'R', 'R', 'O', 'O', 'R', 'R'],
            ['R', 'R', 'R', 'O', 'O', 'R', 'R', 'R', 'R', 'R', 'R', 'O', 'R', 'G', 'R', 'R'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
        ]

        # Dynamic starting and goal positions
        self.start_position = (0, 0)  # Starting position in grid coordinates (row, column)
        self.goal_position = (9, 13)  # Goal position in grid coordinates (row, column)

        self.zombie_positions = [
            (2, 2),  # Zombie 1 starting position
            (3, 3),  # Zombie 2 starting position
            (5, 8),  # Zombie 3 starting position
        ]

    @property
    def rows(self):
        """
        Returns the number of rows in the grid.
        :return: Integer representing the number of rows.
        """
        return self.grid_height

    @property
    def cols(self):
        """
        Returns the number of columns in the grid.
        :return: Integer representing the number of columns.
        """
        return self.grid_width

    def render(self, surface):
        """
        Render the map grid.
        :param surface: Pygame surface to render the map on.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.grid_size
                y = row * self.grid_size

                # Determine the color based on the cell type
                cell_type = self.grid[row][col]
                if cell_type == 'R':  # Road
                    color = (200, 200, 200)  # Light gray
                elif cell_type == 'O':  # Obstacle
                    color = (100, 100, 100)  # Dark gray
                elif cell_type == 'G':  # Goal
                    color = (0, 255, 0)  # Green
                else:
                    color = (50, 50, 50)  # Default background

                # Draw the grid cell
                pygame.draw.rect(surface, color, (x, y, self.grid_size, self.grid_size))

                # Draw grid lines for clarity
                pygame.draw.rect(surface, (0, 0, 0), (x, y, self.grid_size, self.grid_size), 1)

    def is_walkable(self, grid_x, grid_y):
        """
        Check if a grid cell is walkable (not an obstacle).
        :param grid_x: Column in the grid.
        :param grid_y: Row in the grid.
        :return: True if walkable, False otherwise.
        """
        if 0 <= grid_x < self.cols and 0 <= grid_y < self.rows:
            return self.grid[grid_y][grid_x] != 'O'
        return False

    def grid_to_pixel(self, grid_pos):
        """
        Convert grid coordinates to pixel coordinates.
        :param grid_pos: Tuple (row, column) in grid coordinates.
        :return: Tuple (x, y) in pixel coordinates.
        """
        grid_x, grid_y = grid_pos
        return grid_x * self.grid_size, grid_y * self.grid_size

    def pixel_to_grid(self, pixel_pos):
        """
        Convert pixel coordinates to grid coordinates.
        :param pixel_pos: Tuple (x, y) in pixel coordinates.
        :return: Tuple (row, column) in grid coordinates.
        """
        pixel_x, pixel_y = pixel_pos
        return pixel_x // self.grid_size, pixel_y // self.grid_size
