import pygame
from constants import *
from player import Player
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    # create player obj at center of screen
    player_obj = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #player_obj.update(dt)
        for thing in updatable:
            thing.update(dt)
        screen.fill("black")
        #player_obj.draw(screen)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time / 1000

# main() function is only called when the file is run directly
if __name__ == "__main__":
    main()