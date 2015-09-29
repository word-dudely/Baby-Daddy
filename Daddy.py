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
        
        
        self.speed = 8
        self.image = pygame.image.load('images/daddy/daddy_s02.png')
        self.rect = self.image.get_rect()
        
        self.walk_n_anim = ['images/daddy/daddy_n01.png', 'images/daddy/daddy_n02.png','images/daddy/daddy_n03.png','images/daddy/daddy_n04.png','images/daddy/daddy_n05.png','images/daddy/daddy_n06.png','images/daddy/daddy_n07.png','images/daddy/daddy_n08.png']
        
        self.walk_e_anim = ['images/daddy/daddy_e01.png', 'images/daddy/daddy_e02.png','images/daddy/daddy_e03.png','images/daddy/daddy_e04.png','images/daddy/daddy_e05.png','images/daddy/daddy_e06.png']
        
        self.walk_s_anim = ['images/daddy/daddy_s01.png', 'images/daddy/daddy_s02.png','images/daddy/daddy_s03.png','images/daddy/daddy_s04.png','images/daddy/daddy_s05.png','images/daddy/daddy_s06.png','images/daddy/daddy_s07.png']
        
        self.walk_w_anim = ['images/daddy/daddy_w01.png', 'images/daddy/daddy_w02.png','images/daddy/daddy_w03.png','images/daddy/daddy_w04.png','images/daddy/daddy_w05.png','images/daddy/daddy_w06.png']
        
        self.i=0
        
    def moveDaddy(self, state, baby_rect):
        if ((state == WALK_E) & (self.rect.right < SCREEN_WIDTH)):
            if (((self.rect.bottom < baby_rect.top) | (self.rect.top > baby_rect.bottom)) | ((self.rect.right + self.speed < baby_rect.left) | (self.rect.left + self.speed > baby_rect.right))):
                self.rect.left += self.speed
                if (self.i<len(self.walk_e_anim)):
                    self.image = pygame.image.load(self.walk_e_anim[self.i])
                    self.i+=1
                else:
                    self.i=0
        if ((state == WALK_S) & (self.rect.bottom < SCREEN_HEIGHT)):
            if (((self.rect.left > baby_rect.right) | (self.rect.right < baby_rect.left)) | ((self.rect.bottom + self.speed < baby_rect.top) | (self.rect.top + self.speed > baby_rect.bottom))):
                self.rect.top += self.speed
                if (self.i<len(self.walk_s_anim)):
                    self.image = pygame.image.load(self.walk_s_anim[self.i])
                    self.i+=1
                else:
                    self.i=0
        if ((state == WALK_W) & (self.rect.left > 0)):
            if (((self.rect.bottom < baby_rect.top) | (self.rect.top > baby_rect.bottom)) | ((self.rect.left - self.speed > baby_rect.right) | (self.rect.right - self.speed < baby_rect.left))):
                self.rect.left -= self.speed
                if (self.i<len(self.walk_w_anim)):
                    self.image = pygame.image.load(self.walk_w_anim[self.i])
                    self.i+=1
                else:
                    self.i=0
        if ((state == WALK_N) & (self.rect.top > 25)):
            if (((self.rect.bottom - self.speed < baby_rect.top) | (self.rect.top - self.speed > baby_rect.bottom)) | ((self.rect.left > baby_rect.right) | (self.rect.right < baby_rect.left))):
                self.rect.top -= self.speed
                if (self.i<len(self.walk_n_anim)):
                    self.image = pygame.image.load(self.walk_n_anim[self.i])
                    self.i+=1
                else:
                    self.i=0
        if (state == STAND):
            pass