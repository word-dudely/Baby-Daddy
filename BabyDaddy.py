# -** coding: utf-8 -*-
import pygame, codecs, math, sys
from pygame.locals import *

screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('Baby Daddy')
clock = pygame.time.Clock()
BLACK = (0,0,0)
bg = pygame.image.load('images/logo.jpg')
screen.blit(bg, (0,0))
startBtn = pygame.image.load('images/startBtn.png').convert_alpha()
screen.blit(startBtn, (400, 650))
pygame.display.flip()

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            if Rect(400,650,200,50).collidepoint(x,y):
                print('Start!')
        if not hasattr(event, 'key'): continue
        if event.key == K_ESCAPE: sys.exit(0)
        