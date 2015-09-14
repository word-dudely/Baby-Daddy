# -** coding: utf-8 -*-
import pygame, codecs, math, sys, time
from pygame.locals import *
from Daddy import *
from Constants import *
from DynamicTexts import *

def main():
    #window stuff
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
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
    
    #temp start button fix
    startBtn = pygame.image.load('images/startBtn.png').convert_alpha()
    startBtn_rect = startBtn.get_rect()
    startBtn_rect.centerx = background_rect.centerx
    startBtn_rect = startBtn_rect.move(0, background_rect.bottom-100)

    def changeMusic(newTrack, volume=GLOBAL_MUSIC_VOLUME):
        pygame.mixer.music.load('audio/'+newTrack)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volume)
        
    def createMenu(startBtn, startBtn_rect):
        pygame.mixer.music.fadeout(50)
        screen.blit(background, (0,0))
        logo = pygame.image.load('images/logo.png').convert_alpha()
        logo_rect = logo.get_rect()
        logo_rect.centerx = background_rect.centerx
        logo_rect=logo_rect.move(0,background_rect.top+100)
        screen.blit(logo, logo_rect)
        screen.blit(startBtn, startBtn_rect)
        pygame.display.flip()
        changeMusic('babyDaddyHookRepeat.ogg')
        
    def startGame(numDP=0, numLVL=0):
        screen.blit(background, (0,0))
        pygame.display.flip()
        pygame.mixer.music.fadeout(50)
        changeMusic('babyDaddyMainLoop.wav')
        #HUD
        font = pygame.font.Font('fonts/arialbd.ttf', 18)
        textDP = font.render(DADDY_POINTS_LABEL+str(numDP), True, BLACK, WHITE)
        textDP_rect = textDP.get_rect()
        textDP_rect.midtop = background_rect.midtop
        screen.blit(textDP, textDP_rect)
        textLVL = font.render(LEVEL_LABEL+str(numLVL), True, BLACK, WHITE)
        textLVL_rect = textLVL.get_rect()
        textLVL_rect.topleft = background_rect.topleft
        screen.blit(textLVL, textLVL_rect)
        pygame.display.flip()
        
        
        
    #display menu
    createMenu(startBtn, startBtn_rect)
    

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