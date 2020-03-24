import time

import pygame, sys

from rocket import Rocket
from bomba import Bomba
from bullet import Bullet
from pygame.math import Vector2

class Game(object):

    def __init__(self):
        # Configuration
        #initianizacion

        pygame.init()
        self.screen_x = 1280
        self.screen_y = 720
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.bomby = []
        self.limit_bomb=3
        self.buletts=[]
        self.cold_down = 100
        self.i = self.cold_down
        size = self.screen.get_size()

        self.players = [Rocket(self, pos=Vector2(size[0], size[1])),
                        Rocket(self, color=(255, 0, 0), pos=Vector2(size[0]/4, size[1]/4),klawisze=False)]
        while True:
            # manewrowanie oknem
            for player in self.players:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        sys.exit(0)
                    if player.klawisze:
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                            if len(self.bomby) < self.limit_bomb:
                                self.bomby.append(Bomba(self, player=player))
                    else:
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
                            if len(self.bomby) < self.limit_bomb:
                                self.bomby.append(Bomba(self, player=player))


                # Tykanie
                player.tps_delta += player.tps_clock.tick() / 1000.0
                while player.tps_delta > 1 / player.tps_max:
                    self.tick(player)
                    player.tps_delta -= 1 / player.tps_max
                # drowing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
            #time.sleep(5)

    def tick(self, player):
        event = player.tick()
        if player.klawisze:
            if event[pygame.K_SPACE] and self.i >= self.cold_down:
                self.i -= self.cold_down
                self.buletts.append(Bullet(self, pygame.math.Vector2(player.pos.x, player.pos.y), player))
            elif self.i < self.cold_down:
                self.i += 1
        else:
            if event[pygame.K_RCTRL] and self.i >= self.cold_down:
                self.i -= self.cold_down
                self.buletts.append(Bullet(self, pygame.math.Vector2(player.pos.x, player.pos.y), player))
            elif self.i < self.cold_down:
                self.i += 1

        for bomba in self.bomby:
            if bomba.tick():
                bomba.wybuch=5
        for bullet in self.buletts:
            if bullet.tick():
                self.buletts.remove(bullet)
    def draw(self):
        for bomba in self.bomby:
            if bomba.wybuch>0:
                if bomba.draw_explosion():
                    self.bomby.remove(bomba)
            else:
                bomba.draw_bomba()

        for bullet in self.buletts:
            bullet.draw_bullet()
        for player in self.players:
            player.draw()

if __name__ == "__main__":
    Game()




