# -** coding: utf-8 -*-
import pygame
from pygame.locals import *

class Daddy(pygame.sprite.Sprite):
    """
    The player's main guy. The Daddy. Clicking on objects will move him to them.
    Returns: daddy object
    Functions: moveDaddy
    Attributes: speed[x,y]
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.speed = [2, 2]
        self.image = pygame.image.load('images/daddy.png')
        self.rect = self.image.get_rect()
        
    def moveDaddy(self):
        self.rect.top += self.speed[1]
        self.rect.left += self.speed[0]