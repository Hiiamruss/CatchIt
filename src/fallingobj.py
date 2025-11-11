import pygame
import random as r

class FallingObj(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.speed = r.randint(1, 20)

        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def update(self):
        pygame.draw.rect(self.screen, (0,255,0), self.rect)
        self.y += self.speed
        self.rect.y = self.y