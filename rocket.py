import pygame
from pygame.math import Vector2

class Rocket(object):

    def __init__(self, game):
        self.game = game
        self.speed = 0.6
        self.gravity = 0.5

        size = self.game.screen.get_size()

        self.pos = Vector2(size[0]/2,size[1]/2)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
        self.angel = 0.0

    def add_force(self, force):
        self.acc += force

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0,-self.speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0,self.speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed,0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed,0))

        # fizyka
        self.vel*=0.8
      #  self.vel-=Vector2(0,-self.gravity)

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0
        if self.pos[0] >= self.game.screen_x:
            self.pos[0] = 0
        if self.pos[1] >= self.game.screen_y:
            self.pos[1] = 0
        if self.pos[0] < 0:
            self.pos[0] = self.game.screen_x
        if self.pos[1] < 0:
            self.pos[1] = self.game.screen_y
        return pressed
    def draw(self):
        # trójkąt
        points=[Vector2(0,-10), Vector2(5,5), Vector2(-5,5)]
        # obracanie trójkąta w kierunku lotu
        self.angel = self.vel.angle_to(Vector2(0,1))
        points = [p.rotate(self.angel) for p in points]
        #naprawa osi y
        points = [Vector2(p.x,p.y*-1) for p in points]

        # pozycja
        points=[self.pos+p*4 for p in points]
        # rysowańsko
        pygame.draw.polygon(self.game.screen, (0, 100,255), points)



