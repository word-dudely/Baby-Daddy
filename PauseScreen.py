import pygame
from pygame.locals import *
from Constants import *
from DynamicTexts import *

class PauseScreen(pygame.sprite.Sprite):
    """
    PauseScreen sprite.
    Returns: PauseScreen object
    Functions: None at the moment
    Attributes: image, rect
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface(SCREEN_SIZE)
        self.image.fill(BLACK)
        self.rect=self.image.get_rect()
        
        self.fontBig = pygame.font.Font('fonts/ARBUCKLE.TTF', 70)
        
        self.textPaused=self.fontBig.render(PAUSED_TEXT, True, WHITE)
        self.textPaused_rect=self.textPaused.get_rect()
        self.textPaused_rect.center=self.rect.center
        
        self.image.blit(self.textPaused, self.textPaused_rect)