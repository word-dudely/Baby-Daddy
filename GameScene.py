import pygame
from pygame.locals import *
from Constants import *
from Daddy import *
from DynamicTexts import *

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
        
        self.numDP=0
        self.numLVL=0
        
        self.image = pygame.Surface(SCREEN_SIZE)
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        
        self.daddy=Daddy()
        self.daddy.rect = self.daddy.rect.move(400,400)
        self.daddySprite=pygame.sprite.RenderPlain(self.daddy)
        self.daddySprite.draw(self.image)
        
        #HUD
        self.HUD=pygame.Surface((SCREEN_WIDTH, 25))
        self.HUD_rect=self.HUD.get_rect()
        self.HUD_shadow=pygame.Surface((SCREEN_WIDTH, self.HUD_rect.height+2))
        self.HUD_shadow.set_alpha(75)
        self.HUD_shadow_rect=self.HUD_shadow.get_rect()
        pygame.draw.rect(self.HUD_shadow, BLACK, (0,0,SCREEN_WIDTH,self.HUD_shadow_rect.height), 0)
        pygame.draw.rect(self.HUD, WHITE, (0,0,SCREEN_WIDTH,self.HUD_rect.height), 0)
        self.font = pygame.font.Font('fonts/arialbd.ttf', 18)
        self.textDP = self.font.render(DADDY_POINTS_LABEL+str(self.numDP), True, BLACK, WHITE)
        self.textDP_rect = self.textDP.get_rect()
        self.textDP_rect.midtop = self.rect.midtop
        self.textDP_rect=self.textDP_rect.move(0,+2)
        self.textLVL = self.font.render(LEVEL_LABEL+str(self.numLVL), True, BLACK, WHITE)
        self.textLVL_rect = self.textLVL.get_rect()
        self.textLVL_rect.topleft = self.rect.topleft
        self.textLVL_rect=self.textLVL_rect.move(+2,+2)
        self.textTIMER = self.font.render(TIMER_LABEL, True, BLACK, WHITE)
        self.textTIMER_rect = self.textTIMER.get_rect()
        self.textTIMER_rect.topright = self.rect.topright
        self.textTIMER_rect=self.textTIMER_rect.move(-2,+2)
        self.image.blit(self.HUD_shadow, self.HUD_shadow_rect)
        self.image.blit(self.HUD, self.HUD_rect)
        self.image.blit(self.textDP, self.textDP_rect)
        self.image.blit(self.textLVL, self.textLVL_rect)
        self.image.blit(self.textTIMER, self.textTIMER_rect)


    def update(self):
        #update the HUD
        self.textDP = self.font.render(DADDY_POINTS_LABEL+str(self.numDP), True, BLACK, WHITE)
        self.textLVL = self.font.render(LEVEL_LABEL+str(self.numLVL), True, BLACK, WHITE)
        #redraw the scene
        self.image.fill(WHITE)
        self.daddySprite=pygame.sprite.RenderPlain(self.daddy)
        self.daddySprite.draw(self.image)
        self.image.blit(self.HUD_shadow, self.HUD_shadow_rect)
        self.image.blit(self.HUD, self.HUD_rect)
        self.image.blit(self.textDP, self.textDP_rect)
        self.image.blit(self.textLVL, self.textLVL_rect)
        self.image.blit(self.textTIMER, self.textTIMER_rect)