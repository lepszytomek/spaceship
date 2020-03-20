import pygame, sys
from pygame.math import Vector2

class Bomba(object):

    def __init__(self, game):
        self.game = game
        self.poczantkowy_czas_wybuchu = 250.0
        self.czas_do_wybuch = self.poczantkowy_czas_wybuchu
        self.pos = Vector2()
        self.obszar_wybuchu = 100
        self.jest_bomba = False

    def stawianie_bomby(self):
        self.pos = Vector2(self.game.player.pos)
        self.jest_bomba = True


    def tick(self):
            if self.jest_bomba:
                if self.czas_do_wybuch <= 0:
                    self.jest_bomba = False
                    self.czas_do_wybuch = self.poczantkowy_czas_wybuchu
                    pos = self.game.player.pos - self.pos
                    pos.x = abs(pos.x)
                    pos.y = abs(pos.y)
                    if pos.x < self.obszar_wybuchu and pos.y < self.obszar_wybuchu:
                        print("bomb kill you")
                        sys.exit(0)
                else:
                    self.czas_do_wybuch -= 1

    def draw_bomba(self):
        pos = (int(self.pos.x), int(self.pos.y))
        pygame.draw.circle(self.game.screen, (255, 0, 0), pos, self.obszar_wybuchu)
        pygame.draw.circle(self.game.screen, (102, 255, 135), pos, 10)

    def handlet_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.stawianie_bomby()

