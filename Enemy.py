import pygame
from pygame.locals import *
from Constants import *
import random

class Enemy(pygame.sprite.Sprite):
    """
    The enemy. Must be stopped by the Daddy.
    Returns: enemy object
    Functions: TBD
    Attributes: speed, direction
    """
    def __init__(self):
        #Call the parent class (Sprite) constructor
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((20,20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        
        self.speed = [0,0]
        self.direction = random.sample([MOVE_N, MOVE_E, MOVE_S, MOVE_W], 1)[0]
        
        if (self.direction==MOVE_N):
            self.rect=self.rect.move((random.random()*SCREEN_WIDTH,SCREEN_HEIGHT-20))
            self.speed=[0,-1]
        elif(self.direction==MOVE_E):
            self.rect=self.rect.move((0,random.random()*SCREEN_HEIGHT))
            self.speed=[+1,0]
        elif(self.direction==MOVE_S):
            self.rect=self.rect.move((random.random()*SCREEN_WIDTH, +25))
            self.speed=[0,+1]
        elif(self.direction==MOVE_W):
            self.rect=self.rect.move((SCREEN_WIDTH-20, random.random()*SCREEN_HEIGHT))
            self.speed=[-1,0]
            