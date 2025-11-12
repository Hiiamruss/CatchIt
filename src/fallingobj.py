import pygame
import random as r

class FallingObj(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, maxspeed, color):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.speed = r.randint(1, maxspeed)
        self.color = color

        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def update(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.y += self.speed
        self.rect.y = self.y