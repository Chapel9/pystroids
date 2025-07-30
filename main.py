import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
   # print(f"Screen width: {SCREEN_WIDTH}")
   # print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0
    
    #making groups
    update_sprites = pygame.sprite.Group()
    draw_sprites = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()


    Asteroid.containers = (asteroid, update_sprites, draw_sprites)
    AsteroidField.containers = (update_sprites)
    asteroid_field = AsteroidField()
    Player.containers = (update_sprites, draw_sprites)

    player_object = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return     

        update_sprites.update(dt)          
        screen.fill("black")
       
        for sprite in draw_sprites:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
