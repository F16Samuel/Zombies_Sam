import pygame
from game.game import Game
from ui.ui_manager import UIManager
from ui.button import Button

def main():
    """
    Entry point for the Zombie Apocalypse Game.
    Handles initialization, UI setup, and the main game loop.
    """
    pygame.init()
    
    # Screen and clock setup
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Zombie Apocalypse Game")
    clock = pygame.time.Clock()
    
    # Game instance
    game = Game(screen)
    
    # UI Manager and Buttons
    ui_manager = UIManager()
    start_button = Button(
        x=(screen_width // 2) - 50,  # Centered horizontally
        y=(screen_height // 2) - 25,  # Centered vertically
        width=100,
        height=50,
        text="Start Game",
        action=game.run
    )
    ui_manager.add_button(start_button)

    # Main loop: Handle the menu and game states
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            
            # Handle UI events like button clicks
            ui_manager.handle_event(event)
        
        # Render UI elements
        ui_manager.render(screen)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

        # Check if the game state transitions to "in-progress"
        if game.game_state.get_state() == "IN_PROGRESS":
            game.run()  # Start the game
            # After the game finishes, reset to the menu
            game.game_state.change_state("MENU")

    pygame.quit()

if __name__ == "__main__":
    main()
