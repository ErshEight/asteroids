import pygame
from circleshape import *
from constants import *

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, *Shot.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)