import pygame
from pygame.locals import *
from Constants import *
from Daddy import *

class GameScene(pygame.sprite.Sprite):
    """
    Sets up and runs the game scene
    Returns: game scene
    Functions: update
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface(SCREEN_SIZE)
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        
        self.daddy=Daddy()
        self.daddySprite=pygame.sprite.RenderPlain(self.daddy)
        self.daddySprite.draw(self.image)


    def update(self):
        #redraw the scene
        self.image.fill(WHITE)
        self.daddySprite=pygame.sprite.RenderPlain(self.daddy)
        self.daddySprite.draw(self.image)