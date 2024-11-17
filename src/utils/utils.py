import random

# Clamp a value to a given range (used for screen boundaries, health, etc.)
def clamp(value, min_value, max_value):
    """Clamp value within the range [min_value, max_value]"""
    return max(min(value, max_value), min_value)

# Generate a random event (for zombies, loot, etc.)
def random_event(events):
    """Return a random event from the list"""
    return random.choice(events)

# Game state manager
class GameState:
    def __init__(self):
        self.state = 'START'  # Initial state (could be 'START', 'PLAYING', 'GAME_OVER')

    def change_state(self, new_state):
        """Change the current game state"""
        self.state = new_state
    
    def get_state(self):
        """Return the current game state"""
        return self.state

# Load configuration or settings
def load_settings(filename):
    """Load game settings from a configuration file"""
    settings = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip() and '=' in line:
                    key, value = line.split('=')
                    settings[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Settings file {filename} not found.")
    return settings
