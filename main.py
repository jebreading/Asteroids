# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    nplayer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    afield = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        for u in updatable:
            u.update(dt)

        screen.fill("black")
        
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = Clock.tick(60)/1000


if __name__ == "__main__":
    main()