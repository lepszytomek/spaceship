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
        self.player = Rocket(self)
        self.bullet = Bullet(self)

        while True:
            # manewrowanie oknem
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
                    if len(self.bomby) < self.limit_bomb:
                        self.bomby.append(Bomba(self,))



            # Tykanie
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # drowing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()
            #time.sleep(5)

    def tick(self):
        self.player.tick()
        for bomba in self.bomby:
            if bomba.tick():
                bomba.wybuch=5

        self.bullet.tick()
    def draw(self):
        for bomba in self.bomby:
            if bomba.wybuch>0:
                if bomba.draw_explosion():
                    self.bomby.remove(bomba)
            else:
                bomba.draw_bomba()
        self.player.draw()
        self.bullet.draw_bullet()
if __name__ == "__main__":
    Game()




