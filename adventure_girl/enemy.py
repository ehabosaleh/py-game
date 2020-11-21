import pygame
import random
class Enemy():
	x_e=0;y_e=0
	walk_count=0
	walk_left=[]
	life=0
	width,height=0,0
	hit=False
	def __init__(self,window):
		self.life=5
		self.walk_count=10
		self.dead_count=8
		self.enemy_step=0
		self.fps=10
		self.window=window
		(self.w,self.h)=(200,250)
		walk_l=[pygame.image.load(f"enemy_walk/Walk_L ({i}).png") for i in range(1,self.walk_count+1)]
		walk_r=[pygame.image.load(f"enemy_walk/Walk_R ({i}).png") for i in range(1,self.walk_count+1)]
		self.walk_left=[pygame.transform.scale(image,(self.w,self.h)) for image in walk_l]
		self.walk_right=[pygame.transform.scale(image,(self.w,self.h)) for image in walk_r]
		(self.w,self.h)=(200,250)
		dead_l=[pygame.image.load(f"dead_enemy/Dead_L ({i}).png") for i in range(1,self.dead_count+1)]
		dead_r=[pygame.image.load(f"dead_enemy/Dead_R ({i}).png") for i in range(1,self.dead_count+1)]
		self.dead_left=[pygame.transform.scale(image,(self.w,self.h)) for image in dead_l]
		self.dead_right=[pygame.transform.scale(image,(self.w,self.h)) for image in dead_r]
		
		self.width,self.height=pygame.display.get_surface().get_size()
	def attack(self):
		self.alive=True
		direction =random.choice([True,False])
		
		if direction==True:
			self.x_e=self.width-150;self.y_e=self.height-270		
			while self.alive:
				for i in range (0,self.walk_count):
					if self.get_enemy_position()<=self.get_bullet_position():
						self.alive=False;
						self.die(direction)
						break;	
					x=self.x_e-4
					if x<0:
						return None;
					self.x_e=x
					self.window.blit(self.walk_left[i],(self.x_e,self.y_e))
					self.clock.tick(self.fps)
					
		else:	
			self.x_e=-10;self.y_e=self.height-270
			while self.alive:
			
				for i in range (0,self.walk_count):
					if self.get_enemy_position()>=self.get_bullet_position()-self.w:
						self.alive=False;
						self.die(direction)
						break;	
					x=self.x_e+4
					if x>self.width-201:
						return None
					self.x_e=x
					self.window.blit(self.walk_right[i],(self.x_e,self.y_e))
					self.clock.tick(self.fps)			
		self.alive=True		
				
	def get_enemy_position(self):
		return self.x_e
	
	def die(self,right):
		if right==True:
			for i in range (0,self.dead_count):	
				self.window.blit(self.dead_left[i],(self.x_e,self.y_e))
				self.clock.tick(self.fps)


		else:		
			for i in range (0,self.dead_count):	
				self.window.blit(self.dead_right[i],(self.x_e,self.y_e))
				self.clock.tick(self.fps)


