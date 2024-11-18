import pygame
import circleshape
import constants

class Asteroid(circleshape.Circleshape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    