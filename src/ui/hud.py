import pygame

class HUD:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 24)
    
    def render(self, surface):
        health_text = self.font.render("Health: 100", True, (255, 0, 0))
        score_text = self.font.render("Score: 0", True, (0, 255, 0))
        surface.blit(health_text, (10, 10))
        surface.blit(score_text, (10, 40))
