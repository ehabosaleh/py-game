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
	def __init__(self,x,y,window):
		self.x=x; self.y=y
		self.life=5
		self.walk_count=8
		walk_l=[pygame.image.load(f"enemy_walk/Walk ({i}).png") for i in range(1,self.walk_count+1)]
		walk_r=[pygame.image.load(f"enemy_walk/Walk ({i})(copy).png") for i in range(1,self.walk_count+1)]
		walk_left=[pygame.transform.scale(image) for image in walk_l]
		walk_right=[pygame.transform.scale(image) for image in walk_r]
		self.window=window
		self.attack(window)
		self.width,self.height=pygame.display.get_surface().get_size()
	def attack(self,window):
		while self.hit=False:
			direction= random.choose(["left","right"])
			if direction=="left":
				for i in range(0,self.walk_count):
					x=self.x-4
					if x<0:
						break;
					self.x=x
					self.window.blit(pygame.display.get_surface(),(0,0))
					self.window.blit(self.walk_left[i],(self.x,self.y))
					self.display.update()
					pygame.time.delay(50)
					
			else:
				for i in range(0,self.walk_count):
					x=self.x+4
					if x > self.width-201:
						break;
					self.x=x
					self.window.blit(pygame.display.get_surface(),(0,0))
					self.window.blit(self.walk_right[i],(self.x,self.y))
					self.display.update()
					pygame.time.delay(50)
					
