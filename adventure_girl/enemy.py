import pygame
import random
from bullet import Bullet
class Enemy():
	width,height=0,0
	def __init__(self,window):
		self.life=5
		self.walk_count=10
		self.dead_count=8
		self.enemy_step=0
		self.score=0
		self.fps=15
		self.hit=False	
		self.window=window
		self.enemy_walk=pygame.mixer.Sound('walking On Gravel.wav')
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
	def get_bullet_position(self):
		return Bullet.get_bullet_position(self)
	def attack(self):
		alive=True
		direction =random.choice([True,False])
		health=100
		
		if direction==True:
			self.x_e=self.width-150;self.y_e=self.height-270
			self.enemy_walk.play()		
			while alive:
				
				for i in range (0,self.walk_count):
					if self.get_enemy_position()[0]<self.get_bullet_position()[0] and self.get_bullet_position()[1]>self.get_enemy_position()[1]:
						health-=10
						self.hit=True
						if health==0:
							self.enemy_walk.stop()
							alive=False
							self.die(direction)
							break;	
					x=self.x_e-4
					if x<self.x+20:
						return None;
					self.x_e=x
					pygame.draw.rect(self.window,(150-health,100+health,0),(self.x_e+40,self.y_e,health,10))
					self.window.blit(self.walk_left[i],(self.x_e,self.y_e))
					self.clock.tick(self.fps)
					
		else:				
			self.enemy_walk.play()		
			self.x_e=0;self.y_e=self.height-270
			while alive:
				for i in range (0,self.walk_count):
					if self.get_enemy_position()[0]>self.get_bullet_position()[0]-self.w and self.get_bullet_position()[1]>self.get_enemy_position()[1]:
						health-=10
						self.hit=True
						if health==0:
							self.enemy_walk.stop()
							alive=False
							self.die(direction)
							break;	
					x=self.x_e+4
					if x>self.x:
						return None
					self.x_e=x
					pygame.draw.rect(self.window,(150-health,100+health,0),(self.x_e+40,self.y_e,health,10))
					self.window.blit(self.walk_right[i],(self.x_e,self.y_e))
					self.clock.tick(self.fps)

	def get_enemy_position(self):
		return (self.x_e,self.y_e)
	
	def die(self,right):
		if right==True:
			for i in range (0,self.dead_count):	
				self.window.blit(self.dead_left[i],(self.x_e,self.y_e))
				self.clock.tick(self.fps)
				


		else:		
			for i in range (0,self.dead_count):	
				self.window.blit(self.dead_right[i],(self.x_e,self.y_e))
				self.clock.tick(self.fps)
		self.score+=1

