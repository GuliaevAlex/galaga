import pygame, sys
from game_logic import Game

def main():
    pygame.init()

    #screen size
    screen = pygame.display.set_mode((Game.screen_width, Game.screen_height))

    #titel & icon
    pygame.display.set_caption("Galaga")
    icon_image = pygame.image.load("enemy_1.png")
    pygame.display.set_icon(icon_image)

    clock = pygame.time.Clock()

    game = Game()

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
        
        screen.fill((30,30,30))
        game.run(screen)

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()