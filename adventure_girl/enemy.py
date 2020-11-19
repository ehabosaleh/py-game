import pygame
import random
class Enemy():
	x_e=0;y_e=0
	walk_count=0
	walk_left=[]
	life=0
	width,height=0,0
	hit=False
	def __init__(self,x,y):
		self.x_e=x; self.y_e=y
		self.life=5
		self.walk_count=10
		self.enemy_step=0
		(w,h)=(200,250)
		walk_l=[pygame.image.load(f"enemy_walk/Walk_L ({i}).png") for i in range(1,self.walk_count+1)]
		walk_r=[pygame.image.load(f"enemy_walk/Walk_R ({i}).png") for i in range(1,self.walk_count+1)]
		self.walk_left=[pygame.transform.scale(image,(w,h)) for image in walk_l]
		self.walk_right=[pygame.transform.scale(image,(w,h)) for image in walk_r]
		self.width,self.height=pygame.display.get_surface().get_size()
	def attack(self):
		while True:
			for i in range (0,self.walk_count):	
				x=self.x_e-4
				self.enemy_step=(self.enemy_step+1 )%self.walk_count
				if x<0:
					return None;
				self.x_e=x
				self.window.blit(self.walk_left[i],(self.x_e,self.y_e))
				self.clock.tick(20)
	def get_position(self):
		return self.x_e
			
			
