import pygame, codecs, math, sys, time
from pygame.locals import *
from Daddy import *
from Constants import *
from DynamicTexts import *
from MainMenu import *
#from GameScene import *

global gameState, daddyState

def main():
    #window stuff
    pygame.init()
    if (WINDOWED):screen = pygame.display.set_mode(SCREEN_SIZE)
    else:screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
    pygame.display.set_icon(pygame.image.load(ICON))
    pygame.display.set_caption(TITLE_BAR_TEXT)
    pygame.key.set_repeat(1,5)

    clock = pygame.time.Clock()
    clock.tick(30)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)
    background_rect = background.get_rect()
    
    gameState=MAIN_MENU
    daddyState=STAND
    #birth my sprites
    daddy=Daddy()
    menu=MainMenu()
    

    def changeMusic(newTrack, volume=GLOBAL_MUSIC_VOLUME):
        pygame.mixer.music.load('audio/'+newTrack)
        pygame.mixer.music.play(-1)
        if (SOUND_ENABLED):pygame.mixer.music.set_volume(volume)
        else:pygame.mixer.music.set_volume(0)
        
        
    def createMenu():
        gameState=MAIN_MENU
        menuSprite=pygame.sprite.RenderPlain(menu)
        menuSprite.draw(background)
        screen.blit(background, (0,0))
        pygame.mixer.music.fadeout(50)
        pygame.display.flip()
        changeMusic('babyDaddyHookRepeat.ogg')
        
    def startGame(daddy, numDP=0, numLVL=0):
        gameState=GAME_ON
        scene = pygame.Surface(screen.get_size())
        scene = scene.convert()
        scene.fill(WHITE)
        scene_rect = scene.get_rect()
        daddySprite=pygame.sprite.RenderPlain(daddy)
        daddySprite.draw(scene)
        screen.blit(scene, (0,25))
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
        textDP_rect.midtop = scene_rect.midtop
        textDP_rect=textDP_rect.move(0,+2)
        screen.blit(textDP, textDP_rect)
        textLVL = font.render(LEVEL_LABEL+str(numLVL), True, BLACK, WHITE)
        textLVL_rect = textLVL.get_rect()
        textLVL_rect.topleft = scene_rect.topleft
        textLVL_rect=textLVL_rect.move(+2,+2)
        screen.blit(textLVL, textLVL_rect)
        textTIMER = font.render(TIMER_LABEL, True, BLACK, WHITE)
        textTIMER_rect = textTIMER.get_rect()
        textTIMER_rect.topright = scene_rect.topright
        textTIMER_rect=textTIMER_rect.move(-2,+2)
        screen.blit(textTIMER, textTIMER_rect)
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
                    startGame(daddy)
                    gameState=GAME_ON
                if menu.exitBtn_rect.collidepoint(x,y):
                    sys.exit(0)
            if ((event.type == MOUSEBUTTONDOWN) & (gameState==GAME_ON)):
                x,y = event.pos
                if daddy.rect.collidepoint(x,y):
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
                daddy.moveDaddy(daddyState)
                daddySprite=pygame.sprite.RenderPlain(daddy)
                daddySprite.draw(background)
                screen.blit(background, (0,25))
                pygame.display.flip()
            if ((event.type == KEYUP) & (gameState==GAME_ON)):
                if event.key == K_ESCAPE: 
                    createMenu()
                    gameState=MAIN_MENU
                else:
                    daddyState = STAND
                    daddy.moveDaddy(daddyState)
        

            
if __name__ == '__main__': main()