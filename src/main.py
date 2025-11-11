import pygame
from config import *
import time as t
import random as r
from block import *
from fallingobj import *


class Catchit:
    def __init__(self):
        pygame.init()
        #Game Attributes
        self.screen = pygame.display.set_mode((W, H))
        self.running = True

        #Delays and Timer
        self.clock = pygame.time.Clock()
        self.spawntimer = FPS*3

        #Sprites
        self.playergroup = pygame.sprite.GroupSingle()
        self.player = Block(self.screen, 397.0, 550.5)
        self.playergroup.add(self.player)

        self.fallingobjgroup = pygame.sprite.Group()

        #Gamemodes
        self.gamemode = HOMESCREEN

        #Scoring
        self.score = 0
    def game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((255, 255, 255))
            if self.gamemode == HOMESCREEN:
                self.homescreen()
            if self.gamemode == LEVEL1:
                self.level1()


            pygame.sprite.groupcollide(self.playergroup, self.fallingobjgroup, False, True, self.collision)
            pygame.display.flip()
            self.clock.tick(FPS)
    def homescreen(self):
        self.text("Catch It", 325, 50, 50, (0,0,0), True)
        self.text("A very blocky game.", 330, 100)
        self.text("Click [a] to start!", 310, 300, 30, (0,0,0), True)

        rect = pygame.Rect(390, 450, 50, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), rect)
        x = r.randint(1, 800)
        y = r.randint(1, 600)
        rect1 = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(self.screen, (0,255, 0), rect1)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            self.gamemode = LEVEL1


    def level1(self):
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj()
        self.display_score()
        self.check_win()
        self.text("Level 1", 20, 0,)
    def create_falling_obj(self):
        self.spawntimer -= 1
        if self.spawntimer == 0:
            x = r.randint(1, 800)
            obj = FallingObj(self.screen, x, 0)
            self.fallingobjgroup.add(obj)
            self.spawntimer = FPS*4

    def display_score(self):
        font = pygame.font.SysFont("Arial", 20)
        img = font.render(str(self.score), 1, (0, 0, 0))
        self.screen.blit(img, (0, 0))

    def text(self, text, x, y, size=20, color=(0,0,0), bold=False, italic=False):
        font = pygame.font.SysFont("Arial", size, bold, italic)
        img = font.render(text, 1, color)
        self.screen.blit(img, (x, y))


    def collision(self, player, item):
        if player.rect.colliderect(item.rect):
            self.score += 1
            return True
        else:
            return False

    def check_win(self):
        for obj in self.fallingobjgroup:
            if obj.rect.y >= 600:
                self.running = False
game = Catchit()
game.game()