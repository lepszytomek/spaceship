import pygame, sys
from pygame.math import Vector2
from pygame.rect import Rect


class Bullet(object):

    def __init__(self, game):
        self.game = game
        self.pociski = []
        self.szybkosc = 4
        self.vel = Vector2(0, self.szybkosc)
        self.cold_down = 30
        self.i = self.cold_down
    def shot(self):

        vel = pygame.math.Vector2.rotate(self.vel, -self.game.player.angel)
        self.pociski.append([Vector2(self.game.player.pos), vel, True])

    def handlet_event(self, event):
        if event[pygame.K_SPACE] and self.i >= self.cold_down:
                self.shot()
                self.i-=self.cold_down
        elif self.i < self.cold_down:
            self.i+=1
    def draw_bullet(self):
        for lokalizacja in self.pociski:
            pygame.draw.rect(self.game.screen, (0,255,0), Rect(lokalizacja[0], (10, 10)))
    def tick(self):
        for pocisk in self.pociski:
            if pocisk[0].x >= self.game.screen_x or pocisk[0].y >= self.game.screen_y or pocisk[0].y < 0 or pocisk[0].x < 0:
                self.pociski.remove(pocisk)
            else:
                pocisk[0]+=pocisk[1]
            if pocisk[0].x == self.game.player.pos.x or pocisk[0].y == self.game.player.pos.y:
                if not pocisk[2]:
                    print('bullet kill you')
                    sys.exit(0)
            else:
                pocisk[2] = False












