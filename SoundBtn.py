import pygame
from pygame.locals import *
from Constants import *
import random

class SoundBtn(pygame.sprite.Sprite):
    """
    SoundBtn sprite.
    Returns: SoundBtn object
    Functions: None at the moment
    Attributes: image, rect, soundOn
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.soundOn=pygame.mixer.music.get_volume()
        if self.soundOn:
            self.image = pygame.image.load('images/sound_on.png')   
        else:
            self.image = pygame.image.load('images/sound_off.png')
        self.rect = self.image.get_rect()