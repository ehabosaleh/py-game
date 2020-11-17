import pygame
import random
class Enemy():
	x=0;y=0
	walk_count=0
	walk_left=[]
	walk_right=[]
	life=0
	width,height=0,0
	hit=False
	def __init__(self,x,y):
		self.x1=x; self.y1=y
		self.life=5
		self.walk_count=10
		(w,h)=(200,250)

		walk_l=[pygame.image.load(f"enemy_walk/Walk_L ({i}).png") for i in range(1,self.walk_count+1)]
		walk_r=[pygame.image.load(f"enemy_walk/Walk_R ({i}).png") for i in range(1,self.walk_count+1)]
		self.walk_left=[pygame.transform.scale(image,(w,h)) for image in walk_l]
		self.walk_right=[pygame.transform.scale(image,(w,h)) for image in walk_r]
		self.width,self.height=pygame.display.get_surface().get_size()
	def attack(self):
		while self.hit==False and self.x1>=0 :

				for i in range(0,self.walk_count):
					x=self.x1-4

					if x<0:
						break;
					self.x1=x
					#self.window.blit(self.back_ground,(0,0))
					self.window.blit(self.walk_left[i],(self.x1,self.y1))
					#pygame.display.update()
					pygame.time.delay(30)
			
			
