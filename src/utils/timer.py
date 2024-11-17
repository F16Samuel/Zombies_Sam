import time

# Game timer class to track elapsed time
class GameTimer:
    def __init__(self):
        self.start_time = time.time()  # Record start time
    
    def get_elapsed_time(self):
        """Get the elapsed time in seconds"""
        return time.time() - self.start_time
    
    def reset(self):
        """Reset the timer"""
        self.start_time = time.time()

# Countdown timer
def countdown_timer(seconds):
    """Countdown timer that returns the remaining time in seconds"""
    start = time.time()
    while True:
        elapsed = time.time() - start
        remaining = max(0, seconds - int(elapsed))
        if remaining == 0:
            return
        yield remaining  # Yield remaining time every cycle
