import pygame

class TextBox:
    def __init__(self, x, y, width, height, placeholder="Enter text..."):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 255)
        self.text = ""
        self.placeholder = placeholder
        self.font = pygame.font.SysFont("Arial", 24)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text if self.text else self.placeholder, True, (0, 0, 0))
        surface.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def set_text(self, text):
        self.text = text
