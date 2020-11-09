import pygame
import random
class Ball:
	width=0
	height=0
	radius=0
	(x,y)=(radius,radius)
	window=pygame.display.set_mode((width,height))
	def __init__(self,width,height,x,y,r):
		self.width=width; self.height=height;self.x=x; self.y=y
		self.radius=r
		pygame.init()
		self.window=pygame.display.set_mode((self.width,self.height))
		self.random_walk();
	def random_walk(self):
		pygame.draw.circle(self.window,(255,0,0),(self.x,self.y),self.radius)
		run=True
		while run:
			pygame.time.delay(50)
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					run=False

			x_pos=random.choice([10,-10])
			y_pos=random.choice([10,-10])
			self.x+=x_pos
			self.y+=y_pos
			if self.x<self.radius:
				self.x=self.radius
			elif  self.x>self.width-1-self.radius:
				self.x=self.width-1-self.radius
			if self.y<self.radius:
				self.y=self.radius
			elif self.y>self.height-1-self.radius:
				self.y=self.height-1-self.radius

			self.window.fill((0,0,255))
			pygame.draw.circle(self.window,(255,0,0),(self.x,self.y),self.radius)
			pygame.display.update()
		pygame.quit()
