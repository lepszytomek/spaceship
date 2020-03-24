import time

import pygame, sys

from rocket import Rocket
from bomba import Bomba
from bullet import Bullet

class Game(object):

    def __init__(self):
        # Configuration
        self.tps_max = 100.0

        #initianizacion

        pygame.init()
        self.screen_x = 1280
        self.screen_y = 720
        self.screen = pygame.display.set_mode((self.screen_x, self.screen_y))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.bomby = []
        self.limit_bomb=3
        self.buletts=[]
        self.cold_down = 30
        self.i = self.cold_down
        self.players = [Rocket(self)]
        while True:
            # manewrowanie oknem
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                    if len(self.bomby) < self.limit_bomb:
                        self.bomby.append(Bomba(self, player=player))

            for player in self.players:
                # Tykanie
                self.tps_delta += self.tps_clock.tick() / 1000.0
                while self.tps_delta > 1 / self.tps_max:
                    self.tick(player)
                    self.tps_delta -= 1 / self.tps_max

                # drowing
                self.screen.fill((0, 0, 0))
                self.draw(player)
                pygame.display.flip()
                #time.sleep(5)

    def tick(self, player):
        event = player.tick()
        if event[pygame.K_SPACE] and self.i >= self.cold_down:
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
    def draw(self, player):
        for bomba in self.bomby:
            if bomba.wybuch>0:
                if bomba.draw_explosion():
                    self.bomby.remove(bomba)
            else:
                bomba.draw_bomba()

        for bullet in self.buletts:
            bullet.draw_bullet()

        player.draw()

if __name__ == "__main__":
    Game()




