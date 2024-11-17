import pygame
from game.player import Player
from game.zombie import Zombie
from game.map import GameMap
from utils.timer import GameTimer
from utils.utils import GameState

class Game:
    def __init__(self, screen):
        """
        Initializes the game.
        :param screen: The Pygame display screen.
        """
        pygame.init()

        # Grid setup
        self.grid_size = 50  # Size of each grid cell in pixels
        self.rows = 12       # Number of rows in the grid
        self.cols = 16       # Number of columns in the grid

        # Screen setup
        self.screen = screen
        self.screen = pygame.display.set_mode((self.cols * self.grid_size, self.rows * self.grid_size))
        pygame.display.set_caption("Zombie Apocalypse")

        # Game entities
        self.clock = pygame.time.Clock()
        self.game_state = GameState()
        self.game_map = GameMap(self.rows, self.cols, self.grid_size)  # Create map with grid details
        self.player = Player(self.game_map.start_position, self.grid_size)
        
        # Define initial zombie positions here
        initial_zombie_positions = [(5, 5), (7, 8), (3, 10)]  # Example starting positions
        self.zombies = [Zombie(pos, self.grid_size) for pos in initial_zombie_positions]
        
        self.goal_node = self.game_map.goal_position  # Set goal position from map
        self.timer = GameTimer()

        # Turn-based system variables
        self.player_moves = 1  # Player gets 1 moves per turn
        self.current_player_moves = 0

    def run(self):
        """
        Main game loop.
        """
        while self.game_state.get_state() != 'GAME_OVER':
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        """
        Handles user input events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.change_state('GAME_OVER')
            elif event.type == pygame.KEYDOWN and self.current_player_moves < self.player_moves:
                if event.key == pygame.K_UP:
                    self.player.move("up", self.game_map)  # Pass game_map as the grid argument
                elif event.key == pygame.K_DOWN:
                    self.player.move("down", self.game_map)  # Pass game_map as the grid argument
                elif event.key == pygame.K_LEFT:
                    self.player.move("left", self.game_map)  # Pass game_map as the grid argument
                elif event.key == pygame.K_RIGHT:
                    self.player.move("right", self.game_map)  # Pass game_map as the grid argument
                self.current_player_moves += 1


    def update(self):
        """
        Updates game entities and checks conditions.
        """
        if self.current_player_moves == self.player_moves:
            self.update_zombies()  # Zombies move after player finishes their turn
            self.current_player_moves = 0

        self.check_collisions()
        self.check_win_condition()

    def update_zombies(self):
        """
        Updates zombie positions.
        """
        for zombie in self.zombies:
            zombie.move_toward_player(self.game_map, (self.player.grid_x, self.player.grid_y))

    def check_collisions(self):
        """
        Checks for collisions between player and zombies.
        """
        for zombie in self.zombies:
            if self.player.rect.colliderect(zombie.rect):
                self.die()

    def check_win_condition(self):
        """
        Checks if the player has reached the goal node.
        """
        if (self.player.grid_x, self.player.grid_y) == self.goal_node:
            self.show_you_won_screen()

    def render(self):
        """
        Renders all game entities on the screen.
        """
        self.screen.fill((0, 0, 0))  # Clear the screen
        self.game_map.render(self.screen)
        self.player.render(self.screen)
        for zombie in self.zombies:
            zombie.render(self.screen)
        self.render_goal_node()
        pygame.display.flip()

    def render_goal_node(self):
        """
        Renders the goal node on the map.
        """
        goal_rect = pygame.Rect(
            self.goal_node[0] * self.grid_size,
            self.goal_node[1] * self.grid_size,
            self.grid_size,
            self.grid_size
        )
        pygame.draw.rect(self.screen, (0, 255, 255), goal_rect)  # Cyan color for goal node

    def show_you_lost_screen(self):
        """
        Displays the "You Lost" screen.
        """
        font = pygame.font.Font(None, 72)
        text = font.render("You Lost", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.fill((0, 0, 0))  # Clear screen
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds

    def show_you_won_screen(self):
        """
        Displays the "You Won" screen and ends the game.
        """
        font = pygame.font.Font(None, 72)
        text = font.render("You Won!", True, (0, 255, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.fill((0, 0, 0))  # Clear screen
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds
        pygame.quit()
        quit()

    def die(self):
        """
        Handles player death.
        """
        self.game_state.change_state('GAME_OVER')
        self.show_you_lost_screen()
        pygame.quit()
        quit()


if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))  # Dummy screen passed initially
    game = Game(screen)
    game.run()
