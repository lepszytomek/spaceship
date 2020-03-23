import pygame
from pygame.math import Vector2
from pygame.rect import Rect


class Bullet(object):

    def __init__(self, game):
        self.game = game
        self.pociski = []
        self.szybkosc = 2
        self.vel = Vector2(self.szybkosc,self.szybkosc)

    def shot(self):

        vel = pygame.math.Vector2.rotate(self.vel, self.game.player.angel)
        self.pociski.append([Vector2(self.game.player.pos), vel])

    def handlet_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                self.shot()


    def draw_bullet(self):
        for lokalizacja in self.pociski:
            pygame.draw.rect(self.game.screen, (0,255,0), Rect(lokalizacja[0], (10, 10)))
    def tick(self):
        for lokalizacja in self.pociski:
            if lokalizacja[0].x >= self.game.screen_x or lokalizacja[0].y >= self.game.screen_y or lokalizacja[0].y < 0 or lokalizacja[0].x < 0:
                self.pociski.remove(lokalizacja)
            else:
                lokalizacja[0]+=lokalizacja[1]















