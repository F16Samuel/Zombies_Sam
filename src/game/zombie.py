import pygame
from utils.algorithms.a_star import a_star  # Importing the A* algorithm

class Zombie(pygame.sprite.Sprite):
    def __init__(self, start_pos, grid_size):
        """
        Initialize a zombie.
        :param start_pos: Starting position of the zombie (row, column).
        :param grid_size: Size of each grid cell in pixels.
        """
        super().__init__()
        self.image = pygame.Surface((grid_size, grid_size))
        self.image.fill((255, 0, 0))  # Red zombie
        self.rect = self.image.get_rect()
        self.grid_size = grid_size

        # Set initial position in grid coordinates
        self.grid_x, self.grid_y = start_pos
        self.rect.topleft = (self.grid_x * grid_size, self.grid_y * grid_size)

    def move_toward_player(self, game_map, player_position):
        """
        Move the zombie toward the player's position using A*.
        :param game_map: The game map to check boundaries.
        :param player_position: The position of the player (x, y).
        """
        # Convert the game map into a 2D grid where 0 = walkable and 1 = obstacle
        grid = [[0 for _ in range(game_map.grid_width)] for _ in range(game_map.grid_height)]
        for x in range(game_map.grid_height):
            for y in range(game_map.grid_width):
                if game_map.grid[x][y] == 'O':  # Assuming obstacles are marked as 'O' in the grid
                    grid[x][y] = 1
        
        start = (self.grid_x, self.grid_y)
        goal = player_position

        # Use A* to find the path
        path = a_star(grid, start, goal)

        if path:
            # Move zombie one step toward the player
            next_step = path[0]  # Take the first step in the path
            self.grid_x, self.grid_y = next_step
            self.rect.topleft = (self.grid_x * self.grid_size, self.grid_y * self.grid_size)

    def update(self, game_map, player_position):
        """
        Update the zombie's position to move toward the player using A*.
        :param game_map: The current game map (for checking walkability).
        :param player_position: The player's current position (row, column).
        """
        self.move_toward_player(game_map, player_position)  # Use A* to move the zombie

    def render(self, surface):
        """
        Render the zombie on the given surface.
        :param surface: Pygame surface to render the zombie on.
        """
        surface.blit(self.image, self.rect.topleft)
