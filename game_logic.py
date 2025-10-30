import pygame
from player import Player
from laser import Laser

class Game:
    screen_width  = 600
    screen_height = 600

    def __init__(self):
       player_sprite = Player((Game.screen_width/2, Game.screen_height),Game.screen_width, 5)
       self.player = pygame.sprite.GroupSingle(player_sprite)


    def run(self,screen):
        self.player.update()

        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        
