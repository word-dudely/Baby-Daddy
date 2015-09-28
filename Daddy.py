import pygame
from pygame.locals import *
from Constants import *
from Baby import *

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
        
        self.speed = 10
        self.image = pygame.image.load('images/zelda_sprites/walk_s01.png')
        self.rect = self.image.get_rect()
        
        self.walk_n_anim = ['images/zelda_sprites/walk_n01.png', 'images/zelda_sprites/walk_n02.png','images/zelda_sprites/walk_n03.png','images/zelda_sprites/walk_n04.png','images/zelda_sprites/walk_n05.png','images/zelda_sprites/walk_n06.png','images/zelda_sprites/walk_n07.png','images/zelda_sprites/walk_n08.png']
        
        self.walk_e_anim = ['images/zelda_sprites/walk_e01.png', 'images/zelda_sprites/walk_e02.png','images/zelda_sprites/walk_e03.png','images/zelda_sprites/walk_e04.png','images/zelda_sprites/walk_e05.png','images/zelda_sprites/walk_e06.png']
        
        self.walk_s_anim = ['images/zelda_sprites/walk_s01.png', 'images/zelda_sprites/walk_s02.png','images/zelda_sprites/walk_s03.png','images/zelda_sprites/walk_s04.png','images/zelda_sprites/walk_s05.png','images/zelda_sprites/walk_s06.png','images/zelda_sprites/walk_s07.png']
        
        self.walk_w_anim = ['images/zelda_sprites/walk_w01.png', 'images/zelda_sprites/walk_w02.png','images/zelda_sprites/walk_w03.png','images/zelda_sprites/walk_w04.png','images/zelda_sprites/walk_w05.png','images/zelda_sprites/walk_w06.png']
        
        self.i=0
        
    def moveDaddy(self, state):
        if ((state == WALK_E) & (self.rect.right < SCREEN_WIDTH)):
            self.rect.left += self.speed
            if (self.i<len(self.walk_e_anim)):
                self.image = pygame.image.load(self.walk_e_anim[self.i])
                self.i+=1
            else:
                self.i=0
        if ((state == WALK_S) & (self.rect.bottom < SCREEN_HEIGHT)):
            self.rect.top += self.speed
            if (self.i<len(self.walk_s_anim)):
                self.image = pygame.image.load(self.walk_s_anim[self.i])
                self.i+=1
            else:
                self.i=0
        if ((state == WALK_W) & (self.rect.left > 0)):
            self.rect.left -= self.speed
            if (self.i<len(self.walk_w_anim)):
                self.image = pygame.image.load(self.walk_w_anim[self.i])
                self.i+=1
            else:
                self.i=0
        if ((state == WALK_N) & (self.rect.top > 25)):
            self.rect.top -= self.speed
            if (self.i<len(self.walk_n_anim)):
                self.image = pygame.image.load(self.walk_n_anim[self.i])
                self.i+=1
            else:
                self.i=0
                
        if (state == STAND):
            pass