import pygame, sys
from pygame.math import Vector2

class Bomba(object):

    def __init__(self, game, czas_do_wybuch = 250.0, obszar_wybuchu = 100, czas_animacji = 25):
        self.game = game
        self.max_czas_do_wybuchu = czas_do_wybuch
        self.czas_do_wybuch = czas_do_wybuch
        self.obszar_wybuchu = obszar_wybuchu
        self.czas_animacji = czas_animacji
        self.animacja_czasu = 0
        self.pos = Vector2(game.player.pos)



    def tick(self):
            self.animacja_czasu+=1
            if self.czas_do_wybuch <= 0:
                pos = self.game.player.pos - self.pos
                pos.x = abs(pos.x)
                pos.y = abs(pos.y)
                if pos.x < self.obszar_wybuchu and pos.y < self.obszar_wybuchu:
                    print("bomb kill you")
                    sys.exit(0)
                return True
            else:
                self.czas_do_wybuch -= 1
                return False
    def draw_bomba(self):
        pos = (int(self.pos.x), int(self.pos.y))
        pygame.draw.circle(self.game.screen, (255, 0, 0), pos, self.obszar_wybuchu)
        pygame.draw.circle(self.game.screen, (102, 255, 135), pos, int(self.max_czas_do_wybuchu/10))
        pygame.draw.circle(self.game.screen, (0, 0, 0), pos, int(self.animacja_czasu/10))

    def draw_explosion(self, pos):
        pos = (int(pos.x), int(pos.y))
        pygame.draw.circle(self.game.screen, (102, 255, 135), pos, self.obszar_wybuchu)

