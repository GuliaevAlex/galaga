import pygame
from player import Player

class Game:
    def __init__(self):
       player_sprite = Player((300,600))
       self.player = pygame.sprite.GroupSingle(player_sprite)


    def run(self,screen):
        self.player.draw(screen)
        
