import pygame, sys
from pygame.math import Vector2
from pygame.rect import Rect


class Bullet(object):

    def __init__(self, game, pos, player,szybkosc=2):
        self.game = game
        self.szybkosc = szybkosc
        self.vel = Vector2(0, self.szybkosc)
        self.vel = pygame.math.Vector2.rotate(self.vel, -player.angel)
        self.pos = pos
        self.player=player

    def draw_bullet(self):
        pygame.draw.rect(self.game.screen, (0,255,0), Rect(self.pos, (10, 10)))
    def tick(self):
        if self.pos.x >= self.game.screen_x or self.pos.y >= self.game.screen_y or self.pos.y < 0 or self.pos.x < 0:
            return True
        else:
            self.pos+=self.vel
            return False
'''        

        if self.pos.x == self.game.player.pos.x or self.pos.y == self.game.player.pos.y:
            if not pocisk[2]:
                print('bullet kill you')
                sys.exit(0)
        else:
            pocisk[2] = False
'''











