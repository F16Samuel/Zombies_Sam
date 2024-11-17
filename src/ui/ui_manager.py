import pygame
from ui.button import Button
from ui.textbox import TextBox
from ui.hud import HUD

class UIManager:
    def __init__(self):
        self.buttons = []
        self.textboxes = []
        self.hud = HUD()

    def render(self, screen):
        for button in self.buttons:
            button.render(screen)
        for textbox in self.textboxes:
            textbox.render(screen)
        self.hud.render(screen)

    def add_button(self, button):
        self.buttons.append(button)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def add_textbox(self, textbox):
        self.textboxes.append(textbox)
