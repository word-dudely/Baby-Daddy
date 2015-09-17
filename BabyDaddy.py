# -** coding: utf-8 -*-
import pygame, codecs, math, sys, time
from pygame.locals import *
from Daddy import *
from Constants import *
from DynamicTexts import *

def main():
    #window stuff
    pygame.init()
    if (WINDOWED):screen = pygame.display.set_mode(SCREEN_SIZE)
    else:screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
    pygame.display.set_icon(pygame.image.load(ICON))
    pygame.display.set_caption(TITLE_BAR_TEXT)

    clock = pygame.time.Clock()
    clock.tick(30)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)
    background_rect=background.get_rect()
    
    #temp, need to setup state engine asap
    MENU=True
    
    daddy=Daddy()
    daddySprite=pygame.sprite.RenderPlain(daddy)
    daddySprite.draw(background)
    
    #temp button fix
    startBtn = pygame.image.load('images/startBtn.png').convert_alpha()
    startBtn_rect = startBtn.get_rect()
    startBtn_rect.midbottom = background_rect.midbottom
    startBtn_rect = startBtn_rect.move(0,-10)
    exitBtn = pygame.image.load('images/exitBtn.png').convert_alpha()
    exitBtn_rect = exitBtn.get_rect()
    exitBtn_rect.bottomleft=background_rect.bottomleft
    exitBtn_rect = exitBtn_rect.move(+5,-10)

    def changeMusic(newTrack, volume=GLOBAL_MUSIC_VOLUME):
        pygame.mixer.music.load('audio/'+newTrack)
        pygame.mixer.music.play(-1)
        if (SOUND_ENABLED):pygame.mixer.music.set_volume(volume)
        else:pygame.mixer.music.set_volume(0)
        
        
    def createMenu(startBtn, startBtn_rect, exitBtn, exitBtn_rect):
        pygame.mixer.music.fadeout(50)
        screen.blit(background, (0,0))
        logo = pygame.image.load('images/logo.png').convert_alpha()
        logo_rect = logo.get_rect()
        logo_rect.centerx = background_rect.centerx
        logo_rect=logo_rect.move(0,background_rect.top+100)
        screen.blit(logo, logo_rect)
        screen.blit(startBtn, startBtn_rect)
        screen.blit(exitBtn, exitBtn_rect)
        pygame.display.flip()
        changeMusic('babyDaddyHookRepeat.ogg')
        
    def startGame(numDP=0, numLVL=0):
        screen.blit(background, (0,0))
        pygame.display.flip()
        pygame.mixer.music.fadeout(50)
        changeMusic('babyDaddyMainLoop.wav')
        #HUD
        HUD=pygame.Surface((SCREEN_WIDTH, 25))
        HUD_rect=HUD.get_rect()
        HUD_shadow=pygame.Surface((SCREEN_WIDTH, HUD_rect.height+2))
        HUD_shadow.set_alpha(75)
        HUD_shadow_rect=HUD_shadow.get_rect()
        pygame.draw.rect(HUD_shadow, BLACK, (0,0,SCREEN_WIDTH,HUD_shadow_rect.height), 0)
        pygame.draw.rect(HUD, WHITE, (0,0,SCREEN_WIDTH,HUD_rect.height), 0)
        screen.blit(HUD_shadow, HUD_shadow_rect)
        screen.blit(HUD, HUD_rect)
        font = pygame.font.Font('fonts/arialbd.ttf', 18)
        textDP = font.render(DADDY_POINTS_LABEL+str(numDP), True, BLACK, WHITE)
        textDP_rect = textDP.get_rect()
        textDP_rect.midtop = background_rect.midtop
        textDP_rect=textDP_rect.move(0,+2)
        screen.blit(textDP, textDP_rect)
        textLVL = font.render(LEVEL_LABEL+str(numLVL), True, BLACK, WHITE)
        textLVL_rect = textLVL.get_rect()
        textLVL_rect.topleft = background_rect.topleft
        textLVL_rect=textLVL_rect.move(+2,+2)
        screen.blit(textLVL, textLVL_rect)
        textTIMER = font.render(TIMER_LABEL, True, BLACK, WHITE)
        textTIMER_rect = textTIMER.get_rect()
        textTIMER_rect.topright = background_rect.topright
        textTIMER_rect=textTIMER_rect.move(-2,+2)
        screen.blit(textTIMER, textTIMER_rect)
        pygame.display.flip()
        
        
        
    #display menu
    createMenu(startBtn, startBtn_rect, exitBtn, exitBtn_rect)
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos
                if startBtn_rect.collidepoint(x,y) & MENU:
                    startGame()
                    MENU=False
                if daddy.rect.collidepoint(x,y):
                    print("Daddy!")
            if event.type == KEYDOWN:
                if ((event.key == K_ESCAPE) & (MENU==False)): 
                    createMenu(startBtn, startBtn_rect)
                    MENU=True
        

            
if __name__ == '__main__': main()