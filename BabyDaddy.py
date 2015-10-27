import pygame, codecs, math, sys, time
from pygame.locals import *
from Daddy import *
from Baby import *
from Enemy import *
from Constants import *
from DynamicTexts import *
from MainMenu import *
from GameScene import *
from SoundBtn import *
from GameOver import *

global gameState, daddyState

def main():
    #window stuff
    pygame.init()
    if (WINDOWED):screen = pygame.display.set_mode(SCREEN_SIZE)
    else:screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
    pygame.display.set_icon(pygame.image.load(ICON))
    pygame.display.set_caption(TITLE_BAR_TEXT)
    pygame.key.set_repeat(40,40)
    #load the clock for the timerate
    clock = pygame.time.Clock()
    #set the initial volume based on the constants
    if SOUND_ENABLED:pygame.mixer.music.set_volume(GLOBAL_MUSIC_VOLUME)
    else:pygame.mixer.music.set_volume(0)
    #main game surface
    screen_surface = pygame.Surface(screen.get_size())
    screen_surface_rect = screen_surface.get_rect()
    #states
    gameState=MAIN_MENU
    daddyState=[STAND,SOUTH]
    babyState=IDLE
    #sprites
    menu=MainMenu()
    game=GameScene()
    gameOver=GameOver()
    soundBtn=SoundBtn()
    #and the program container
    spriteContainer=pygame.sprite.GroupSingle()
    
    
    
    def toggleSound():
        soundOn=pygame.mixer.music.get_volume()
        if soundOn:
            pygame.mixer.music.set_volume(0)
            soundBtn.image=pygame.image.load('images/sound_off.png').convert_alpha()
        else:
            pygame.mixer.music.set_volume(GLOBAL_MUSIC_VOLUME)
            soundBtn.image=pygame.image.load('images/sound_on.png').convert_alpha()
        spriteContainer.draw(screen_surface)
        soundBtnContainer.draw(screen_surface) 
        screen.blit(screen_surface, (0,0))
        pygame.display.flip()

    def changeMusic(newTrack, volume=GLOBAL_MUSIC_VOLUME):
        soundOn=pygame.mixer.music.get_volume()
        pygame.mixer.music.load('audio/'+newTrack)
        pygame.mixer.music.play(-1)
        if (soundOn):pygame.mixer.music.set_volume(volume)
        else:pygame.mixer.music.set_volume(0)
        
        
    def createMenu():
        pygame.time.set_timer(USEREVENT+1, 0)
        spriteContainer.add(menu)
        spriteContainer.draw(screen_surface)
        soundBtnContainer.draw(screen_surface)
        screen.blit(screen_surface, (0,0))
        pygame.mixer.music.fadeout(50)
        pygame.display.flip()
        changeMusic('babyDaddyHookRepeat.ogg')
        
    def startGame():
        spriteContainer.add(game)
        spriteContainer.draw(screen_surface)
        screen.blit(screen_surface, (0,0))
        pygame.mixer.music.fadeout(50)
        changeMusic('babyDaddyMainLoop.wav')
        pygame.display.flip()
        pygame.time.set_timer(USEREVENT+1, 1500)
        game.startGame()
    
    def createGameOver():
        spriteContainer.add(gameOver)
        spriteContainer.draw(screen_surface)
        screen.blit(screen_surface, (0,0))
        pygame.time.set_timer(USEREVENT+1, 0)
        changeMusic('Sad_Male.ogg')
        pygame.display.flip()
        
        
    #display soundBtn
    soundBtn.rect.bottomright = screen_surface_rect.bottomright
    soundBtn.rect=soundBtn.rect.move(-15,-15)
    soundBtnContainer=pygame.sprite.GroupSingle(soundBtn)  
    #display menu
    createMenu()
    
    #state machine/infinite loop. This may get messy...
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos
                if soundBtn.rect.collidepoint(x,y):
                    toggleSound()
            if ((event.type == MOUSEBUTTONDOWN) & (gameState==MAIN_MENU)):
                x,y = event.pos
                if menu.startBtn_rect.collidepoint(x,y):
                    startGame()
                    gameState=GAME_ON
                if menu.exitBtn_rect.collidepoint(x,y):
                    sys.exit(0)
            if ((event.type == MOUSEBUTTONDOWN) & (gameState==GAME_OVER)):
                createMenu()
                gameState=MAIN_MENU
            if ((event.type == KEYDOWN) & (gameState==GAME_ON)):
                if (event.key == K_RIGHT) | (event.key == K_d):
                    daddyState = [WALK,EAST]
                if (event.key == K_DOWN) | (event.key == K_s):
                    daddyState = [WALK,SOUTH]
                if (event.key == K_LEFT) | (event.key == K_a):
                    daddyState = [WALK,WEST]
                if (event.key == K_UP) | (event.key == K_w):
                    daddyState = [WALK,NORTH]
                game.daddy.moveDaddy(daddyState, game.baby.rect)
            if ((event.type == KEYUP) & (gameState==GAME_ON)):
                if event.key == K_SPACE:
                    game.shootDaddy()
                if event.key == K_ESCAPE: 
                    createMenu()
                    gameState=MAIN_MENU
                else:
                    daddyState[0] = STAND
                    game.daddy.moveDaddy(daddyState, game.baby.rect)
            if ((event.type==USEREVENT+1)&(gameState==GAME_ON)):
                game.launchEnemy()
        if gameState==MAIN_MENU:
            pygame.time.delay(200)
            menu.update()
            spriteContainer.draw(screen_surface)
            soundBtnContainer.draw(screen_surface)  
            screen.blit(screen_surface, (0,0))
            pygame.display.flip()
        if gameState==GAME_ON:
            game.update()
            spriteContainer.draw(screen_surface)
            soundBtnContainer.draw(screen_surface)  
            screen.blit(screen_surface, (0,0))
            pygame.display.flip()
            if ((game.numDH==0) | (game.numBH<=0)):
                createGameOver()
                gameState=GAME_OVER
        clock.tick(60)
        

            
if __name__ == '__main__': main()