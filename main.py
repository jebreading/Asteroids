# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame.locals import *
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pygame.Surface.fill(screen,(000,000,000))
            pygame.display.flip()

if __name__ == "__main__":
    main()