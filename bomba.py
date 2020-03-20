import pygame, sys
from pygame.math import Vector2

class Bomba(object):

    def __init__(self, game):
        self.game = game
        self.czas_do_wybuch = 500.0
        self.obszar_wybuchu = 100
        self.limit_bomb = 3
        self.bomby = []
        self.czas_animacji = 25
        self.wybuchy =[]

    def stawianie_bomby(self):
        pos = Vector2(self.game.player.pos)
        self.bomby.append([pos, self.czas_do_wybuch])


    def tick(self):
            for bomba in self.bomby:
                if bomba[1] <= 0:
                    pos = self.game.player.pos - bomba[0]
                    self.wybuchy.append([bomba[0], self.czas_animacji])
                    pos.x = abs(pos.x)
                    pos.y = abs(pos.y)
                    self.bomby = self.bomby[1:]
                    if pos.x < self.obszar_wybuchu and pos.y < self.obszar_wybuchu:
                        print("bomb kill you")
                        sys.exit(0)
                else:
                    bomba[1] -= 1

    def draw_bomba(self, bomba):
        pos = (int(bomba[0].x), int(bomba[0].y))
        pygame.draw.circle(self.game.screen, (255, 0, 0), pos, self.obszar_wybuchu)
        pygame.draw.circle(self.game.screen, (102, 255, 135), pos, 10)

    def draw_explosion(self, pos):
        pos = (int(pos.x), int(pos.y))
        pygame.draw.circle(self.game.screen, (102, 255, 135), pos, self.obszar_wybuchu)



    def handlet_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if len(self.bomby) < self.limit_bomb:
                self.stawianie_bomby()

