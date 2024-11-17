import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, start_position, grid_size):
        """
        Initialize the player on a grid.
        :param start_position: Tuple (grid_x, grid_y), initial position on the grid.
        :param grid_size: Size of each grid cell (e.g., 50 pixels).
        """
        super().__init__()
        self.grid_x, self.grid_y = start_position  # Unpack the start_position tuple
        self.grid_size = grid_size
        self.image = pygame.Surface((grid_size, grid_size))
        self.image.fill((0, 255, 0))  # Green player
        self.rect = self.image.get_rect(topleft=(self.grid_x * grid_size, self.grid_y * grid_size))

    def move(self, direction, grid):
        """
        Move the player in the specified direction.
        :param direction: The direction to move (up, down, left, right).
        :param grid: The game map to check boundaries.
        """
        if direction == "up" and grid.is_walkable(self.grid_x, self.grid_y - 1):
            self.grid_y -= 1
        elif direction == "down" and grid.is_walkable(self.grid_x, self.grid_y + 1):
            self.grid_y += 1
        elif direction == "left" and grid.is_walkable(self.grid_x - 1, self.grid_y):
            self.grid_x -= 1
        elif direction == "right" and grid.is_walkable(self.grid_x + 1, self.grid_y):
            self.grid_x += 1

        # Update the rect position based on the grid position
        self.rect.topleft = (self.grid_x * self.grid_size, self.grid_y * self.grid_size)

    def move_up(self, grid):
        self.move(0, -1, grid)

    def move_down(self, grid):
        self.move(0, 1, grid)

    def move_left(self, grid):
        self.move(-1, 0, grid)

    def move_right(self, grid):
        self.move(1, 0, grid)

    def render(self, surface):
        surface.blit(self.image, self.rect.topleft)
