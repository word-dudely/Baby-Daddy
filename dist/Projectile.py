import pygame
from pygame.locals import *
from Constants import *

class Projectile(pygame.sprite.Sprite):
    """
    Things shot from Daddy at enemies. Rectangles most likely.
    Returns: projectile object
    Functions: update
    Attributes: image, rect, direction
    """
    def __init__(self, direction, daddy_rect):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        #self.image = pygame.Surface((15,30))
        #self.image.fill(WHITE)
        self.image=pygame.image.load('images/bottle.png')
        self.rect = self.image.get_rect()
        self.direction=direction
        
        if self.direction==NORTH:
            self.rect.midbottom=daddy_rect.midtop
        if self.direction==EAST:
            self.image=pygame.transform.rotate(self.image, 270)
            self.rect=self.image.get_rect()
            self.rect.midleft=daddy_rect.midright
        if self.direction==SOUTH:
            self.image=pygame.transform.flip(self.image, False, True)
            self.rect.midtop=daddy_rect.midbottom
        if self.direction==WEST:
            self.image=pygame.transform.rotate(self.image, 90)
            self.rect=self.image.get_rect()
            self.rect.midright=daddy_rect.midleft
        
    def update(self):
        if self.direction==NORTH:
            self.rect=self.rect.move(0,-4)
        if self.direction==EAST:
            self.rect=self.rect.move(+4,0)
        if self.direction==SOUTH:
            self.rect=self.rect.move(0,+4)
        if self.direction==WEST:
            self.rect=self.rect.move(-4,0)