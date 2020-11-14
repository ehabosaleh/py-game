import pygame
from adventure_girl import AdventureGirl
from  bullet import Bullet
from enemy import Enemy

width, height= 1024,500
pygame.init()
window=pygame.display.mode((width,height))
back_ground=pygame.image.load('BG.png')
window.blit(back_ground,(0,0))
