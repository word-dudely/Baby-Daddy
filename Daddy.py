import pygame
from pygame.locals import *
from Constants import *

class Daddy(pygame.sprite.Sprite):
    """
    The player's main guy. The Daddy. Arrow keys move at the moment.
    Returns: daddy object
    Functions: moveDaddy
    Attributes: speed
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.speed = 2
        self.image = pygame.image.load('images/daddy.png')
        self.rect = self.image.get_rect()
        
    def moveDaddy(self, state):
        if (state == WALK_E):
            self.rect.left += self.speed
        if (state == WALK_S):
            self.rect.top += self.speed
        if (state == WALK_W):
            self.rect.left -= self.speed
        if (state == WALK_N):
            self.rect.top -= self.speed
        if (state == STAND):
            pass