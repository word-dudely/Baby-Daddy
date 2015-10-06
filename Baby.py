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
        
        self.crib=pygame.image.load('images/crib.png')
        self.crib_rect=self.crib.get_rect()
        self.baby_idle_anim = ['images/baby/baby_00.png', 'images/baby/baby_01.png']        
        self.baby = pygame.image.load('images/baby/baby_00.png')
        self.baby_rect= self.baby.get_rect()
        self.baby_rect=self.baby_rect.move(0,+50)
        self.image.blit(self.baby, self.baby_rect)
        self.i=0
        
    def update(self):
        if self.i<(len(self.baby_idle_anim)-1):
            self.i+=1
        else: self.i=0
        self.baby = pygame.image.load(self.baby_idle_anim[self.i])
        self.image.blit(self.crib, self.crib_rect)
        self.image.blit(self.baby, self.baby_rect)