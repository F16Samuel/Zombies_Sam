import pygame

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (200, 0, 0)  # Button color (red)
        self.font = pygame.font.SysFont("Arial", 24)
    
    def render(self, screen):
        # Draw the button background
        pygame.draw.rect(screen, self.color, self.rect)
        
        # Draw the text on the button
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        # Check if the button was clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):  # Check if the mouse click is inside the button
                if self.action:
                    self.action()  # Call the assigned action
