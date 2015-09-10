# -** coding: utf-8 -*-
import pygame, codecs, math, sys
from pygame.locals import *

def main():
    #window stuff
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_icon(pygame.image.load('images/iconBaby.png'))
    pygame.display.set_caption('Baby Daddy')
    
    #globals
    clock = pygame.time.Clock()
    clock.tick(30)
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)
    background_rect=background.get_rect()
    MENU = True
    GAME = False
    #DaddyPoints
    numDP=0
    #Level
    numLVL=0
    globalMusicVolume=0.0

    def changeMusic(newTrack, volume=globalMusicVolume):
        pygame.mixer.music.load('audio/'+newTrack)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volume)
        
    #display menu
    screen.blit(background, (0,0))
    logo = pygame.image.load('images/logo.png').convert_alpha()
    logo_rect = logo.get_rect()
    logo_rect.centerx = background_rect.centerx
    logo_rect=logo_rect.move(0,background_rect.top+100)
    screen.blit(logo, logo_rect)
    startBtn = pygame.image.load('images/startBtn.png').convert_alpha()
    startBtn_rect = startBtn.get_rect()
    startBtn_rect.centerx = background_rect.centerx
    startBtn_rect = startBtn_rect.move(0, background_rect.bottom-100)
    screen.blit(startBtn, startBtn_rect)
    pygame.display.flip()
    changeMusic('babyDaddyHookRepeat.ogg')

    while MENU:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos
                if startBtn_rect.collidepoint(x,y):
                    GAME = True
                    MENU = False
                    screen.blit(background, (0,0))
                    pygame.display.flip()
                    pygame.mixer.music.fadeout(100)
                    changeMusic('babyDaddyMainLoop.wav')
            if not hasattr(event, 'key'): continue
            if event.key == K_ESCAPE: sys.exit(0)
            
    while GAME:
        font = pygame.font.Font('fonts/arialbd.ttf', 18)
        textDP = font.render("Daddy Points: "+str(numDP), True, BLACK, WHITE)
        textDP_rect = textDP.get_rect()
        textDP_rect.bottomleft = background_rect.bottomleft
        screen.blit(textDP, textDP_rect)
        textLVL = font.render("Level: "+str(numLVL), True, BLACK, WHITE)
        textLVL_rect = textLVL.get_rect()
        textLVL_rect.topleft = background_rect.topleft
        screen.blit(textLVL, textLVL_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            #super temp (like all of this)
            if event.type == MOUSEBUTTONDOWN:numDP+=1
            if event.type == QUIT:
                sys.exit(0)
            if not hasattr(event, 'key'): continue
            if event.key == K_ESCAPE: sys.exit(0)
            
if __name__ == '__main__': main()