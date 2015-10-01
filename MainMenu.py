import pygame
from pygame.locals import *
from Constants import *

class MainMenu(pygame.sprite.Sprite):
    """
    The Main Menu!
    Returns: menu object
    Functions: tbd
    Attributes: image, rect, logo, startBtn, startBtn_rect, exitBtn, exitBtn_rect
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(SCREEN_SIZE)
        self.image.fill(PINK)
        self.rect=self.image.get_rect()
        self.logo = pygame.image.load('images/logo.png').convert_alpha()
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.midtop = self.rect.midtop
        self.logo_rect=self.logo_rect.move(0,+25)
        self.startBtn = pygame.image.load('images/startBtn.png').convert_alpha()
        self.startBtn_rect = self.startBtn.get_rect()
        self.exitBtn = pygame.image.load('images/exitBtn.png').convert_alpha()
        self.exitBtn_rect = self.exitBtn.get_rect()
        self.startBtn_rect.midbottom = self.rect.midbottom
        self.startBtn_rect = self.startBtn_rect.move(-150,-10)
        self.exitBtn_rect.midbottom = self.rect.midbottom
        self.exitBtn_rect = self.exitBtn_rect.move(+150,-10)
        self.image.blit(self.logo, self.logo_rect)
        self.image.blit(self.startBtn, self.startBtn_rect)
        self.image.blit(self.exitBtn, self.exitBtn_rect)