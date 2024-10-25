#this allows us to use code
#from the open-source library
#throughout this file
import pygame
from constants import *
from player import Player

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    
    player = Player(x, y)
    dt = 0
    print('Starting asteroids!')

    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)                       
        
        screen.fill(000)

        for thing in drawable:
            thing.draw(screen) 

        pygame.display.flip()
        
        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()
    

