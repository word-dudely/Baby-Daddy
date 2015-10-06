import pygame
from pygame.locals import *
from Constants import *
import random

class Baby(pygame.sprite.Sprite):
    """
    The baby. Must be saved by the Daddy.
    Returns: baby object
    Functions: TBD
    Attributes: image, rect
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('images/crib.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move((random.random()*(SCREEN_WIDTH-self.rect.width)), (random.random()*(SCREEN_HEIGHT-self.rect.height)))
        
        self.baby = pygame.image.load('images/baby/baby_00.png')
        self.baby_rect= self.baby.get_rect()
        self.baby_rect=self.baby_rect.move(0,+50)
        self.image.blit(self.baby, self.baby_rect)
        