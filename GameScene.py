import pygame
from pygame.locals import *
from Constants import *
from Daddy import *
from Baby import *
from Enemy import *
from Projectile import *
from DynamicTexts import *
from Items import *

class GameScene(pygame.sprite.Sprite):
    """
    The main game scene and logic.
    Returns: GameScene object
    Functions: startGame, launchEnemy, shootDaddy, update
    Attributes: image, rect, background, HUD, numDP, numDH, numBH, numProj, daddy, daddySprite, baby, babySprite, enemyGroup, projectileGroup
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.numDP=0
        self.numDH=3
        self.heartString='♥♥♥'
        self.numBH=5
        self.babyHealthString='▓▓▓▓▓▓'
        self.numProj=10
        
        self.background = pygame.image.load('images/hardwoodFloor.jpg').convert()
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
        self.textDH = self.font.render(DADDY_HEARTS_LABEL+self.heartString, True, PINK, WHITE)
        self.textDH_rect = self.textDH.get_rect()
        self.textDH_rect.topleft = self.rect.topleft
        self.textDH_rect=self.textDH_rect.move(+2,+2)
        self.textProj = self.font.render(PROJECTILES_LABEL+str(self.numProj), True, BLACK, WHITE)
        self.textProj_rect = self.textProj.get_rect()
        self.textProj_rect.midleft = self.textDH_rect.midright
        self.textProj_rect = self.textProj_rect.move(+50,+0)
        self.textBH = self.font.render(BABY_HEALTH_LABEL+self.babyHealthString, True, PINK, WHITE)
        self.textBH_rect = self.textBH.get_rect()
        self.textBH_rect.topright = self.rect.topright
        self.textBH_rect=self.textBH_rect.move(-2,+2)
        self.image.blit(self.background, self.background_rect)
        self.image.blit(self.HUD_shadow, self.HUD_shadow_rect)
        self.image.blit(self.HUD, self.HUD_rect)
        self.image.blit(self.textDP, self.textDP_rect)
        self.image.blit(self.textDH, self.textDH_rect)
        self.image.blit(self.textProj, self.textProj_rect)
        self.image.blit(self.textBH, self.textBH_rect)
        
        #sounds
        self.zombieEats=pygame.mixer.Sound(file='audio/neck_snap.ogg')
        self.zombieDies=pygame.mixer.Sound(file='audio/kung_fu_punch.ogg')
        self.daddyDies=pygame.mixer.Sound(file='audio/Gag.ogg')
        self.whoosh=pygame.mixer.Sound(file='audio/Woosh.ogg')
        
    def startGame(self):
        #score
        self.numDP=0
        self.numDH=3
        self.heartString='♥♥♥'
        self.numBH=5
        self.babyHealthString='▓▓▓▓▓▓'
        self.numProj=10
        self.textBH = self.font.render(BABY_HEALTH_LABEL+self.babyHealthString, True, PINK, WHITE)
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
        #items
        self.item=Items()
        self.itemSprite=pygame.sprite.GroupSingle()
        #enemies!
        self.enemyGroup=pygame.sprite.Group()
        #projectiles!
        self.projectileGroup=pygame.sprite.Group()
        #sound volumes
        self.zombieEats.set_volume(.1)
        
    def launchEnemy(self):
        self.enemy=Enemy()
        self.enemyGroup.add(self.enemy)
        self.enemyGroup.draw(self.image)
      
    def shootDaddy(self):
        if self.numProj>0:
            if pygame.mixer.music.get_volume():pygame.mixer.Sound.play(self.whoosh)
            self.projectile=Projectile(self.daddy.direction, self.daddy.rect)
            self.projectileGroup.add(self.projectile)
            self.projectileGroup.draw(self.image)
            self.numProj-=1
    
    def daddyDown(self):
        if pygame.mixer.music.get_volume():pygame.mixer.Sound.play(self.daddyDies)
        self.daddy=Daddy()
        self.daddy.direction=SOUTH
        self.daddy.moveDaddy([STAND,SOUTH], self.baby.rect)
        self.enemyGroup.empty()
        self.projectileGroup.empty()
        self.numDH-=1
        self.heartString=''
        self.item.clearItem()
        for i in range(self.numDH):
            self.heartString=self.heartString+'♥'
        self.daddy.rect.center = self.rect.center
        self.daddySprite=pygame.sprite.GroupSingle(self.daddy)
        self.daddySprite.draw(self.image)
        
    def babyHealthDecrease(self):
        self.numBH-=.005
        self.babyHealthString='▓'
        for i in range(int(self.numBH)):
            self.babyHealthString=self.babyHealthString+'▓'
        self.textBH = self.font.render(BABY_HEALTH_LABEL+self.babyHealthString, True, PINK, WHITE)
        if pygame.mixer.music.get_volume():pygame.mixer.Sound.play(self.zombieEats)
    
    def randomItem(self):
        self.item=Items()
        while pygame.sprite.collide_mask(self.item, self.baby):
            self.item=Items()
        self.itemSprite=pygame.sprite.GroupSingle(self.item)
        self.itemSprite.draw(self.image)

    def update(self):
        #update the HUD
        self.textDP = self.font.render(DADDY_POINTS_LABEL+str(self.numDP), True, BLACK, WHITE)
        self.textDH = self.font.render(DADDY_HEARTS_LABEL+self.heartString, True, PINK, WHITE)
        self.textProj = self.font.render(PROJECTILES_LABEL+str(self.numProj), True, BLACK, WHITE)
        #redraw the scene
        self.image.blit(self.background, self.background_rect)
        self.daddySprite.draw(self.image)
        self.babySprite.draw(self.image)
        self.itemSprite.draw(self.image)
        #enemies
        for enemies in iter(self.enemyGroup):
            if ((enemies.rect.left > SCREEN_WIDTH) | (enemies.rect.right < 0) | (enemies.rect.bottom < 0) | (enemies.rect.top > SCREEN_HEIGHT)):
                self.enemyGroup.remove(enemies)
            if pygame.sprite.collide_mask(enemies, self.daddy):
                self.daddyDown()
            if not pygame.sprite.collide_mask(enemies, self.baby):
                enemies.move()
            if pygame.sprite.collide_mask(enemies, self.baby):
                self.babyHealthDecrease()
        self.enemyGroup.update()
        self.enemyGroup.draw(self.image)
        #projectiles
        for projectiles in iter(self.projectileGroup):
            #did you hit the zombie?
            for enemies in iter(self.enemyGroup):
                if pygame.sprite.collide_mask(projectiles, enemies):
                    if pygame.mixer.music.get_volume():pygame.mixer.Sound.play(self.zombieDies)
                    self.projectileGroup.remove(projectiles)
                    self.enemyGroup.remove(enemies)
                    self.numDP+=1
            #did you leave the screen?
            if ((projectiles.rect.right<0) | (projectiles.rect.left>SCREEN_WIDTH) | (projectiles.rect.bottom<0) | (projectiles.rect.top>SCREEN_HEIGHT)):
                self.projectileGroup.remove(projectiles)
        self.projectileGroup.update()
        self.projectileGroup.draw(self.image)
        #items
        if pygame.sprite.collide_mask(self.daddy, self.item):
            #self.itemSprite.empty()
            self.item.clearItem()
            self.numProj+=5
        #self.baby.update()
        self.image.blit(self.HUD_shadow, self.HUD_shadow_rect)
        self.image.blit(self.HUD, self.HUD_rect)
        self.image.blit(self.textDP, self.textDP_rect)
        self.image.blit(self.textDH, self.textDH_rect)
        self.image.blit(self.textProj, self.textProj_rect)
        self.image.blit(self.textBH, self.textBH_rect)