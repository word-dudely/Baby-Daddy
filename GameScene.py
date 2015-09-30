import pygame
from pygame.locals import *
from Constants import *
from Daddy import *
from Baby import *
from Enemy import *
from Projectile import *
from DynamicTexts import *

class GameScene(pygame.sprite.Sprite):
    """
    The main game scene and logic.
    Returns: game scene
    Functions: startGame, launchEnemy, punchDaddy, shootDaddy, update
    Attributes: image, rect, background, HUD, numDP, numLVL, daddy, daddySprite, baby, babySprite, enemyGroup, projectileGroup
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.numDP=0
        self.numLVL=0
        
        self.background = pygame.image.load('images/hardwoodFloor.jpg')
        self.background_rect=self.background.get_rect()
        self.image = pygame.Surface(SCREEN_SIZE)
        self.rect=self.image.get_rect()
        
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
        #self.textLVL_rect = self.textLVL.get_rect()
        #self.textLVL_rect.topleft = self.rect.topleft
        #self.textLVL_rect=self.textLVL_rect.move(+2,+2)
        #self.textTIMER = self.font.render(TIMER_LABEL, True, BLACK, WHITE)
        #self.textTIMER_rect = self.textTIMER.get_rect()
        #self.textTIMER_rect.topright = self.rect.topright
        #self.textTIMER_rect=self.textTIMER_rect.move(-2,+2)
        self.image.blit(self.background, self.background_rect)
        self.image.blit(self.HUD_shadow, self.HUD_shadow_rect)
        self.image.blit(self.HUD, self.HUD_rect)
        self.image.blit(self.textDP, self.textDP_rect)
        #self.image.blit(self.textLVL, self.textLVL_rect)
        #self.image.blit(self.textTIMER, self.textTIMER_rect)
        
    def startGame(self):
        #score
        self.numDP=0
        self.numLVL=0
        #daddy 
        self.daddy=Daddy()
        self.daddy.rect.center = self.rect.center
        self.daddySprite=pygame.sprite.GroupSingle(self.daddy)
        self.daddySprite.draw(self.image)
        #baby 
        self.baby=Baby()
        self.babySprite=pygame.sprite.GroupSingle(self.baby)
        self.babySprite.draw(self.image)
        while self.baby.rect.colliderect(self.daddy.rect):
            self.baby=Baby()
            self.babySprite.add(self.baby)
            self.babySprite.draw(self.image)
        #enemies!
        self.enemyGroup=pygame.sprite.Group()
        self.launchEnemy()
        #projectiles!
        self.projectileGroup=pygame.sprite.Group()
        
    def launchEnemy(self):
        self.enemy=Enemy()
        self.enemyGroup.add(self.enemy)
        self.enemyGroup.draw(self.image)
     
    #removed for now and replaced with projectiles
    def punchDaddy(self):
        self.punchSurface=pygame.Surface((30,30))
        self.punchSurface.fill(WHITE)
        self.punchRect=self.punchSurface.get_rect()
        if self.daddy.direction == NORTH:
            self.punchRect.midbottom=self.daddy.rect.midtop
        if self.daddy.direction == EAST:
            self.punchRect.midleft=self.daddy.rect.midright
        if self.daddy.direction == SOUTH:
            self.punchRect.midtop=self.daddy.rect.midbottom
        if self.daddy.direction == WEST:
            self.punchRect.midright=self.daddy.rect.midleft
        self.image.blit(self.punchSurface, self.punchRect)
        if self.punchRect.colliderect(self.enemy.rect):
            self.enemyGroup.remove(self.enemy)
            self.numDP+=10
            self.launchEnemy()
      
    def shootDaddy(self):
        self.projectile=Projectile(self.daddy.direction, self.daddy.rect)
        self.projectileGroup.add(self.projectile)
        self.projectileGroup.draw(self.image)
        

    def update(self):
        #update the HUD
        self.textDP = self.font.render(DADDY_POINTS_LABEL+str(self.numDP), True, BLACK, WHITE)
        #self.textLVL = self.font.render(LEVEL_LABEL+str(self.numLVL), True, BLACK, WHITE)
        #redraw the scene
        self.image.blit(self.background, self.background_rect)
        self.daddySprite.draw(self.image)
        self.babySprite.draw(self.image)
        #enemy mine
        self.enemy.update(self.baby.rect)
        self.enemyGroup.draw(self.image)
        if ((self.enemy.rect.left > SCREEN_WIDTH) | (self.enemy.rect.right < 0) | (self.enemy.rect.bottom < 0) | (self.enemy.rect.top > SCREEN_HEIGHT)):
            self.enemyGroup.remove(self.enemy)
            self.launchEnemy()
        if pygame.sprite.spritecollide(self.enemy, self.projectileGroup, True):
            self.enemyGroup.remove(self.enemy)
            self.numDP+=10
            self.launchEnemy()
        self.projectileGroup.update()
        self.projectileGroup.draw(self.image)
        self.image.blit(self.HUD_shadow, self.HUD_shadow_rect)
        self.image.blit(self.HUD, self.HUD_rect)
        self.image.blit(self.textDP, self.textDP_rect)
        #self.image.blit(self.textLVL, self.textLVL_rect)
        #self.image.blit(self.textTIMER, self.textTIMER_rect)