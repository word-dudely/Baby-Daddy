import pygame
from pygame.locals import *
from Constants import *

class Baby(pygame.sprite.Sprite):
    """
    The baby. Must be raised by the Daddy.
    Returns: baby object
    Functions: TBD
    Attributes: TBD
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((100,200))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move((200,200))