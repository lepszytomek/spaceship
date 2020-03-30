import pygame, sys
from pygame.math import Vector2
from pygame.rect import Rect


class Bullet(object):

    def __init__(self, game, pos, player,szybkosc=6):
        self.game = game
        self.szybkosc = szybkosc
        self.vel = Vector2(0, self.szybkosc)
        self.vel = pygame.math.Vector2.rotate(self.vel, -player.angel)
        self.pos = pos
        self.player=player

    def draw_bullet(self):
        pygame.draw.rect(self.game.screen, (0,255,0), Rect(self.pos, (10, 10)))
    def tick(self, player):
        if self.game.screen.get_at((int(self.pos.x), int(self.pos.y)))[:3] == player.color:
            print('Bullet kill you. Player', player.numer, 'lose')
            sys.exit(0)
        if self.pos.x >= self.game.screen_x-10 or self.pos.y >= self.game.screen_y-10 or self.pos.y < 10 or self.pos.x < 10:
            return True
        else:
            self.pos+=self.vel
            return False









