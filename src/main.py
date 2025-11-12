import pygame
from config import *
import time as t
import random as r
from block import *
from fallingobj import *
import asyncio

class Catchit:
    def __init__(self):
        pygame.init()
        #Game Attributes
        self.screen = pygame.display.set_mode((W, H))
        self.running = True

        #Delays and Timer
        self.clock = pygame.time.Clock()
        self.spawntimer = FPS*3
        self.loadingtimer = FPS*3

        #Sprites
        self.playergroup = pygame.sprite.GroupSingle()
        self.player = Block(self.screen, 397.0, 550.5)
        self.playergroup.add(self.player)

        self.fallingobjgroup = pygame.sprite.Group()

        #Gamemodes
        self.gamemode = HOMESCREEN

        #Scoring
        self.score = 0
        self.bestscore = 0
    async def game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((255, 255, 255))
            if self.gamemode == HOMESCREEN:
                self.homescreen()
            if self.gamemode == GAMEOVER:
                self.gameover()
            if self.gamemode == LOADING:
                self.loading()
            if self.gamemode == LEVEL1:
                self.level1()
            elif self.gamemode == LEVEL2:
                self.level2()
            elif self.gamemode == LEVEL3:
                self.level3()
            elif self.gamemode == LEVEL4:
                self.level4()
            elif self.gamemode == LEVEL5:
                self.level5()
            elif self.gamemode == LEVEL6:
                self.level6()
            elif self.gamemode == LEVEL7:
                self.level7()
            elif self.gamemode == LEVEL8:
                self.level8()
            elif self.gamemode == LEVEL9:
                self.level9()
            elif self.gamemode == LEVEL10:
                self.level10()



            pygame.sprite.groupcollide(self.playergroup, self.fallingobjgroup, False, True, self.collision)
            pygame.display.flip()
            self.clock.tick(FPS)
            await asyncio.sleep(0)
    def homescreen(self):
        self.display_best_score()
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
            self.gamemode = LOADING




    def gameover(self):
        self.text("Game Over", 325, 50, 50, (0, 0, 0), True)
        self.text("A very blocky game.", 330, 100)
        self.text("Click [Space] to restart!", 310, 300, 30, (0, 0, 0), True)

        rect = pygame.Rect(390, 450, 50, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), rect)
        x = r.randint(1, 800)
        y = r.randint(1, 600)
        rect1 = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(self.screen, (255, 0, 0), rect1)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            self.fallingobjgroup.empty()
            self.gamemode = LEVEL1

    def loading(self):
        self.text("Loading Data", 290, 50, 50, (0, 0, 0), True)
        self.text("Two very blocky data.", 330, 100)
        self.text("Prioritizing is key, Ignore slow blocks and focus on getting faster ones before its to late.", 165, 500, 15, (0, 0, 0), True)

        rect = pygame.Rect(390, 450, 50, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), rect)
        x = r.randint(1, 800)
        y = r.randint(1, 600)
        rect1 = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(self.screen, (0, 0, 255), rect1)

        self.loadingtimer -= 1
        if self.loadingtimer == 0:
            self.gamemode = LEVEL1


    def level1(self):
        self.display_best_score()
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj(5, FPS)
        self.display_score()
        self.check_win()
        self.text("Level 1", 20, 0)
        if self.score >= 10:
            self.gamemode = LEVEL2

    def level2(self):
        self.display_best_score()
        self.screen.fill((255,0,0))
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj(5, FPS, (0,0,255))
        self.display_score()
        self.check_win()
        self.text("Level 2", 20, 0)
        if self.score >= 20:
            self.gamemode = LEVEL3

    def level3(self):
        self.screen.fill((0, 255, 0))
        self.display_best_score()
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj(10, FPS, (255, 0, 0))
        self.display_score()
        self.check_win()
        self.text("Level 3", 20, 0)
        if self.score >= 30:
            self.gamemode = LEVEL4

    def level4(self):
        self.screen.fill((0, 0, 255))
        self.display_best_score()
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj(5, FPS, (255,255,255))
        self.display_score()
        self.check_win()
        self.text("Level 4", 20, 0)
        if self.score >= 40:
            self.gamemode = LEVEL5

    def level5(self):
        self.screen.fill((135,206,235))
        self.display_best_score()
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj(5, FPS, (255, 127, 80))
        self.display_score()
        self.check_win()
        self.text("Level 5", 20, 0)
        if self.score >= 50:
            self.gamemode = LEVEL6

    def level6(self):
        self.screen.fill((152, 255, 152))
        self.display_best_score()
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj(5, FPS, (51, 51, 51))
        self.display_score()
        self.check_win()
        self.text("Level 6", 20, 0)
        if self.score >= 60:
            self.gamemode = LEVEL7

    def level7(self):
        self.screen.fill((230, 230, 250))
        self.display_best_score()
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj(5, FPS, (255, 215, 0))
        self.display_score()
        self.check_win()
        self.text("Level 7", 20, 0)
        if self.score >= 70:
            self.gamemode = LEVEL8

    def level8(self):
        self.screen.fill((220, 20, 60))
        self.display_best_score()
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj(5, FPS, (255, 255, 240))
        self.display_score()
        self.check_win()
        self.text("Level 8", 20, 0)
        if self.score >= 80:
            self.gamemode = LEVEL9

    def level9(self):
        self.screen.fill((0, 128, 128))
        self.display_best_score()
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj(5, FPS, (255, 160, 122))
        self.display_score()
        self.check_win()
        self.text("Level 9", 20, 0)
        if self.score >= 90:
            self.gamemode = LEVEL10

    def level10(self):
        self.screen.fill((75, 0, 130))
        self.display_best_score()
        self.playergroup.update()
        self.fallingobjgroup.update()
        self.create_falling_obj(5, FPS, (191, 255, 0))
        self.display_score()
        self.check_win()
        self.text("Level 10", 20, 0)
        if self.score >= 100:
            self.gamemode = HOMESCREEN



    def create_falling_obj(self, maxspeed, timer, color=(0,255,0)):
        self.spawntimer -= 1
        if self.spawntimer == 0:
            x = r.randint(5, 726)
            obj = FallingObj(self.screen, x, 0, maxspeed, color)
            self.fallingobjgroup.add(obj)
            self.spawntimer = timer

    def display_score(self):
        font = pygame.font.SysFont("Arial", 20)
        img = font.render(str(self.score), 1, (0, 0, 0))
        self.screen.blit(img, (0, 0))

    def display_best_score(self):
        font = pygame.font.SysFont("Arial", 20)
        img = font.render(f"Best: {str(self.bestscore)}", 1, (0, 0, 0))
        if self.score >= self.bestscore:
            self.bestscore = self.score
        self.screen.blit(img, (100, 0))

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
                self.gamemode = GAMEOVER
                self.score = 0
game = Catchit()
asyncio.run(game.game())