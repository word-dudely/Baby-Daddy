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
        
        self.image = pygame.image.load('images/zombie/zombie_s01.png').convert_alpha()
        self.rect = self.image.get_rect()
        
        self.speed = [0,0]
        self.direction = random.sample([NORTH, EAST, SOUTH, WEST], 1)[0]
        
        self.i=0
        
        self.zombie_anim_s=['images/zombie/zombie_s01.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s02.png', 'images/zombie/zombie_s02.png', 'images/zombie/zombie_s02.png', 'images/zombie/zombie_s02.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s01.png', 'images/zombie/zombie_s04.png', 'images/zombie/zombie_s04.png', 'images/zombie/zombie_s04.png', 'images/zombie/zombie_s04.png']
        
        self.zombie_anim_w=['images/zombie/zombie_w01.png', 'images/zombie/zombie_w01.png', 'images/zombie/zombie_w01.png', 'images/zombie/zombie_w01.png', 'images/zombie/zombie_w01.png', 'images/zombie/zombie_w01.png', 'images/zombie/zombie_w02.png', 'images/zombie/zombie_w02.png', 'images/zombie/zombie_w02.png', 'images/zombie/zombie_w02.png', 'images/zombie/zombie_w02.png', 'images/zombie/zombie_w02.png', 'images/zombie/zombie_w03.png', 'images/zombie/zombie_w03.png', 'images/zombie/zombie_w03.png', 'images/zombie/zombie_w03.png', 'images/zombie/zombie_w03.png', 'images/zombie/zombie_w03.png', 'images/zombie/zombie_w04.png', 'images/zombie/zombie_w04.png', 'images/zombie/zombie_w04.png', 'images/zombie/zombie_w04.png', 'images/zombie/zombie_w04.png', 'images/zombie/zombie_w04.png']
        
        self.zombie_anim_n=['images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n02.png', 'images/zombie/zombie_n02.png', 'images/zombie/zombie_n02.png', 'images/zombie/zombie_n02.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n01.png', 'images/zombie/zombie_n04.png', 'images/zombie/zombie_n04.png', 'images/zombie/zombie_n04.png', 'images/zombie/zombie_n04.png']
        
        if (self.direction==NORTH):
            self.rect=self.rect.move((random.random()*(SCREEN_WIDTH-self.rect.width),SCREEN_HEIGHT))
            self.image = pygame.transform.rotate(self.image, -90)
            self.speed=[0,-1]
        elif(self.direction==EAST):
            self.rect=self.rect.move((0-self.rect.width,random.random()*(SCREEN_HEIGHT-self.rect.width)))
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed=[+1,0]
        elif(self.direction==SOUTH):
            self.rect=self.rect.move((random.random()*(SCREEN_WIDTH-self.rect.width), 25-self.rect.width))
            self.image = pygame.transform.rotate(self.image, 90)
            self.speed=[0,+1]
        elif(self.direction==WEST):
            self.rect=self.rect.move((SCREEN_WIDTH, random.random()*(SCREEN_HEIGHT-self.rect.width)))
            self.speed=[-1,0]
            
    def update(self):
        if self.direction==SOUTH:
            if self.i<(len(self.zombie_anim_s)-1): self.i+=1
            else: self.i=0
            self.image=pygame.image.load(self.zombie_anim_s[self.i]).convert_alpha()
        if self.direction==WEST:
            if self.i<(len(self.zombie_anim_w)-1): self.i+=1
            else: self.i=0
            self.image=pygame.image.load(self.zombie_anim_w[self.i]).convert_alpha()
        if self.direction==EAST:
            if self.i<(len(self.zombie_anim_w)-1): self.i+=1
            else: self.i=0
            self.image=pygame.image.load(self.zombie_anim_w[self.i]).convert_alpha()
            self.image = pygame.transform.flip(self.image, True, False)
        if self.direction==NORTH:
            if self.i<(len(self.zombie_anim_n)-1): self.i+=1
            else: self.i=0
            self.image=pygame.image.load(self.zombie_anim_n[self.i]).convert_alpha()
        
    def move(self):
        self.rect=self.rect.move(self.speed)
            