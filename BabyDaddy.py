import pygame, codecs, math, sys, time
from pygame.locals import *
from Daddy import *
from Constants import *
from DynamicTexts import *
from MainMenu import *
from GameScene import *

global gameState, daddyState

def main():
    #window stuff
    pygame.init()
    if (WINDOWED):screen = pygame.display.set_mode(SCREEN_SIZE)
    else:screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
    pygame.display.set_icon(pygame.image.load(ICON))
    pygame.display.set_caption(TITLE_BAR_TEXT)
    pygame.key.set_repeat(25,25)

    clock = pygame.time.Clock()
    clock.tick(30)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)
    background_rect = background.get_rect()
    #prime the states
    gameState=MAIN_MENU
    daddyState=STAND
    #birth my sprites
    #daddy=Daddy()
    menu=MainMenu()
    game=GameScene()
    

    def changeMusic(newTrack, volume=GLOBAL_MUSIC_VOLUME):
        pygame.mixer.music.load('audio/'+newTrack)
        pygame.mixer.music.play(-1)
        if (SOUND_ENABLED):pygame.mixer.music.set_volume(volume)
        else:pygame.mixer.music.set_volume(0)
        
        
    def createMenu():
        gameState=MAIN_MENU
        menuBG=pygame.Surface(SCREEN_SIZE)
        menuSprite=pygame.sprite.RenderPlain(menu)
        menuSprite.draw(menuBG)
        screen.blit(menuBG, (0,0))
        pygame.mixer.music.fadeout(50)
        pygame.display.flip()
        changeMusic('babyDaddyHookRepeat.ogg')
        
    def startGame():
        gameState=GAME_ON
        gameSprite=pygame.sprite.RenderPlain(game)
        gameSprite.draw(background)
        screen.blit(background, (0,0))
        pygame.mixer.music.fadeout(50)
        changeMusic('babyDaddyMainLoop.wav')
        pygame.display.flip()
        
        
        
    #display menu
    createMenu()
    
    #state machine/infinite loop. This will get messy...
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if ((event.type == MOUSEBUTTONDOWN) & (gameState==MAIN_MENU)):
                x,y = event.pos
                if menu.startBtn_rect.collidepoint(x,y):
                    startGame()
                    gameState=GAME_ON
                if menu.exitBtn_rect.collidepoint(x,y):
                    sys.exit(0)
            if ((event.type == MOUSEBUTTONDOWN) & (gameState==GAME_ON)):
                x,y = event.pos
                if game.daddy.rect.collidepoint(x,y):
                    print("Daddy!")
            if ((event.type == KEYDOWN) & (gameState==GAME_ON)):
                if event.key == K_RIGHT:
                    daddyState = WALK_E
                if event.key == K_DOWN:
                    daddyState = WALK_S
                if event.key == K_LEFT:
                    daddyState = WALK_W
                if event.key == K_UP:
                    daddyState = WALK_N
                game.daddy.moveDaddy(daddyState)
                game.update()
                gameSprite=pygame.sprite.RenderPlain(game)
                gameSprite.draw(background)
                screen.blit(background, (0,0))
                pygame.display.flip()
            if ((event.type == KEYUP) & (gameState==GAME_ON)):
                if event.key == K_ESCAPE: 
                    createMenu()
                    gameState=MAIN_MENU
                else:
                    daddyState = STAND
                    game.daddy.moveDaddy(daddyState)
        

            
if __name__ == '__main__': main()