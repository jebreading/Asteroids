import pygame
import circleshape
import constants
import random

class Asteroid(circleshape.CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20,50)
        new_vector_1 = pygame.Vector2(self.position.x, self.position.y).rotate(random_angle)
        new_vector_2 = pygame.Vector2(self.position.x, self.position.y).rotate(-random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_vector_1 * 1.2
        asteroid_2.velocity = new_vector_2 * 1.2
