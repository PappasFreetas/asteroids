import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #create player obj at center of screen
    player_obj = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    clock = pygame.time.Clock()
    dt = 0
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player_obj.update(dt)
        screen.fill(color="black")
        player_obj.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time / 1000

# main() function is only called when the file is run directly
if __name__ == "__main__":
    main()