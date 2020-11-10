import pygame
from jurrasic_world import Dinosaur

width=1000
height=680
(x,y)=(0,height-100)
radius=7
dinosaur=Dinosaur(width,height,x,y,radius)
dinosaur.listen()
