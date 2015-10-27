import pygame
from pygame.locals import *
from Constants import *
from DynamicTexts import *

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

        self.background = pygame.image.load('images/hardwoodFloor.jpg').convert()
        self.image=pygame.Surface(SCREEN_SIZE)
        self.rect=self.image.get_rect()
        
        self.font = pygame.font.Font('fonts/ARBUCKLE.TTF', 22)
        self.textControls1 = self.font.render(CONTROLS1, True, WHITE)
        self.textControls1_rect = self.textControls1.get_rect()
        self.textControls2 = self.font.render(CONTROLS2, True, WHITE)
        self.textControls2_rect = self.textControls2.get_rect()
        self.textControls1_shadow = self.font.render(CONTROLS1, True, BLACK)
        self.textControls1_shadow_rect = self.textControls1_shadow.get_rect()
        self.textControls2_shadow = self.font.render(CONTROLS2, True, BLACK)
        self.textControls2_shadow_rect = self.textControls2_shadow.get_rect()
        
        self.logo = pygame.image.load('images/menu/logo.png').convert_alpha()
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.midtop = self.rect.midtop
        
        self.logo_anim=['images/menu/logo_01.png','images/menu/logo_02.png','images/menu/logo_03.png','images/menu/logo_04.png','images/menu/logo_05.png','images/menu/logo_06.png','images/menu/logo_07.png']
        
        self.textControls1_rect.midtop = self.logo_rect.midbottom
        self.textControls1_rect=self.textControls1_rect.move(0,-3)
        self.textControls2_rect.midtop = self.textControls1_rect.midbottom
        self.textControls2_rect=self.textControls2_rect.move(0,+5)
        self.textControls1_shadow_rect.midtop = self.textControls1_rect.midtop
        self.textControls2_shadow_rect.midtop = self.textControls2_rect.midtop
        self.textControls1_shadow_rect=self.textControls1_shadow_rect.move(-1,+1)
        self.textControls2_shadow_rect=self.textControls2_shadow_rect.move(-1,+1)
        
        
        self.startBtn = pygame.image.load('images/menu/startBtn.png').convert_alpha()
        self.startBtn_rect = self.startBtn.get_rect()
        self.exitBtn = pygame.image.load('images/menu/exitBtn.png').convert_alpha()
        self.exitBtn_rect = self.exitBtn.get_rect()
        self.startBtn_rect.midbottom = self.rect.midbottom
        self.startBtn_rect = self.startBtn_rect.move(-150,-10)
        self.exitBtn_rect.midbottom = self.rect.midbottom
        self.exitBtn_rect = self.exitBtn_rect.move(+150,-10)
        self.image.blit(self.background, self.rect)
        self.image.blit(self.textControls1_shadow, self.textControls1_shadow_rect)
        self.image.blit(self.textControls2_shadow, self.textControls2_shadow_rect)
        self.image.blit(self.textControls1, self.textControls1_rect)
        self.image.blit(self.textControls2, self.textControls2_rect)
        self.image.blit(self.logo, self.logo_rect)
        self.image.blit(self.startBtn, self.startBtn_rect)
        self.image.blit(self.exitBtn, self.exitBtn_rect)
        self.i=0
        
    def update(self):
        #print(self.i)
        self.logo=pygame.image.load(self.logo_anim[self.i]).convert_alpha()
        if (self.i<(len(self.logo_anim)-1)):self.i+=1
        else: self.i=0
        self.image.blit(self.background, self.rect)
        self.image.blit(self.textControls1_shadow, self.textControls1_shadow_rect)
        self.image.blit(self.textControls2_shadow, self.textControls2_shadow_rect)
        self.image.blit(self.textControls1, self.textControls1_rect)
        self.image.blit(self.textControls2, self.textControls2_rect)
        self.image.blit(self.logo, self.logo_rect)
        self.image.blit(self.startBtn, self.startBtn_rect)
        self.image.blit(self.exitBtn, self.exitBtn_rect)