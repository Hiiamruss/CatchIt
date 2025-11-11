import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            self.x -= 10
            self.rect.x = self.x
        if keys_pressed[pygame.K_d]:
            self.x += 10
            self.rect.x = self.x

        if self.x <= 5.5:
            self.x = 5.5
            self.rect.x = self.x
        if self.x >= 726.0:
            self.x = 726.0
            self.rect.x = self.x

        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)