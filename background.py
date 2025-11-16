import pygame
import random

#simple code to generate "stars" as a background
class backg:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randint(0, self.screen_width)
        self.y = random.randint(0, self.screen_height)

    def render(self):
        pygame.draw.line(self.screen, "white", (self.x, self.y), (self.x, self.y), 1)
