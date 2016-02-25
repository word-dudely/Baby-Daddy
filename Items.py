import pygame
from pygame.locals import *
from Constants import *
import random

class Items(pygame.sprite.Sprite):
    """
    Things picked up by Daddy. Bottles only at first.
    Returns: Item object
    Functions: update, clearItem
    Attributes: image, rect
    """
    def __init__(self, ITEM):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.buffer=120
        if (ITEM==BOTTLE):
            self.image=pygame.image.load('images/items/bottlePlus.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect = self.rect.move((random.random()*(SCREEN_WIDTH-(self.rect.width+self.buffer+self.buffer))), (random.random()*(SCREEN_HEIGHT-(self.rect.height+self.buffer+self.buffer))))
            self.rect=self.rect.move(+self.buffer,+self.buffer)
        if (ITEM==EMPTY):
            self.image=pygame.image.load('images/items/clearItem.png').convert_alpha()
            self.rect = self.image.get_rect()