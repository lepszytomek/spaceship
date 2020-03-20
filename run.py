import time

import pygame, sys

from rocket import Rocket
from bomba import Bomba

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
        self.bomba = Bomba(self)
        self.player = Rocket(self)

        while True:
            # manewrowanie oknem
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                else:
                    self.bomba.handlet_event(event)


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
        self.bomba.tick()

    def draw(self):
        if self.bomba.jest_bomba:
            self.bomba.draw_bomba()
        self.player.draw()
if __name__ == "__main__":
    Game()




