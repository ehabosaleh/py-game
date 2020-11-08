import pygame

class Circle(pygame):
	width=0
	height=0
	(x,y)=(0,0)
	radius=0
	velocity=0
	window=pygame.set_mode((width,height))
	def __init__(self,velocity,width,height,(x,y),r):
		pygame.init()
		self.window=pygame.set_mode((width,height))
		pygame.display.set_caption(" ")
		self.x=x
		self.y=y
		self.velocity=velocity
		pygame.draw.circle(self.window,(255,0,0),(self.x,self.y),self.radius)
	def move(self):
		run=True
		while run:	
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					run=False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						self.y=self.y-1
					elif event.key == pygame.K_a:
						self.x=self.x-1
					elif event.key == pygame.K_s:
						self.y=self.y+1
					elif event.key == pygame.K_d:
				         	self.x=self.x+1 
			pygame.draw.circule(self.window,(self.x,self.y),self.radius)
			
pygame.quit()
