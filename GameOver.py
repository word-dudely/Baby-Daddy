import pygame
from pygame.locals import *
from Constants import *
from DynamicTexts import *

class GameOver(pygame.sprite.Sprite):
    """
    Game over dude.
    Returns: game over screen
    Functions: tbd
    Attributes: image, rect, text
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(SCREEN_SIZE)
        self.image.fill(BLACK)
        self.rect=self.image.get_rect()
        
        self.fontBig = pygame.font.Font('fonts/ARBUCKLE.TTF', 70)
        self.fontMed = pygame.font.Font('fonts/ARBUCKLE.TTF', 30)
        self.fontSmall = pygame.font.Font('fonts/arialbd.ttf', 22)
        
        
        self.textGameOver1=self.fontBig.render(END_GAME_TEXT1, True, WHITE)
        self.textGameOver1_rect=self.textGameOver1.get_rect()
        self.textGameOver1_rect.center=self.rect.center
        self.textGameOver1_rect=self.textGameOver1_rect.move(0,-100)
        
        self.textGameOver2=self.fontMed.render(END_GAME_TEXT2, True, WHITE)
        self.textGameOver2_rect=self.textGameOver2.get_rect()
        self.textGameOver2_rect.center=self.rect.center
        self.textGameOver2_rect=self.textGameOver2_rect.move(0,-20)
        
        self.textGameOver3=self.fontSmall.render(END_GAME_TEXT3, True, WHITE)
        self.textGameOver3_rect=self.textGameOver3.get_rect()
        self.textGameOver3_rect.center=self.rect.center
        self.textGameOver3_rect=self.textGameOver3_rect.move(0,+150)
        
        
        self.image.blit(self.textGameOver1, self.textGameOver1_rect)
        self.image.blit(self.textGameOver2, self.textGameOver2_rect)
        self.image.blit(self.textGameOver3, self.textGameOver3_rect)