import pygame

class Circle:
	width=0
	height=0
	(x,y)=(0,0)
	radius=0

	window=pygame.display.set_mode((width,height))
	def __init__(self,width,height,x,y,r):
		self.width=width
		self.height=height
		pygame.init()
		self.window=pygame.display.set_mode((width,height))
		pygame.display.set_caption(" ")
		self.x=x
		self.y=y
		self.radius=r
		pygame.draw.circle(self.window,(255,0,0),(self.x,self.y),self.radius)
		pygame.display.update()
	def move(self):
		run=True
		pressed_left=False; pressed_right=False;pressed_up=False;pressed_down=False;
		while run:
			pygame.time.delay(10)

			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					run=False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						pressed_left = True
					elif event.key == pygame.K_RIGHT:
						pressed_right = True
					elif event.key == pygame.K_UP:        
						pressed_up = True
					elif event.key == pygame.K_DOWN:    
						pressed_down = True
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT:        
						pressed_left = False
					elif event.key == pygame.K_RIGHT:     
						pressed_right = False
					elif event.key == pygame.K_UP:        
						pressed_up = False
					elif event.key == pygame.K_DOWN:    
						pressed_down = False
			if pressed_left == True:
				self.x=self.x-1
			elif pressed_right==True:
				self.x=self.x+1
			elif pressed_up==True:
				self.y=self.y-1
			elif pressed_down==True:
				self.y=self.y+1
			
			if self.x<0:
				self.x=0
			elif self.x>=self.width:
				self.x=self.width-1
			if self.y<0:
				self.y=0
			elif self.y>=self.height:
				self.y=self.height-1
			self.window.fill((0,0,0))

			pygame.draw.circle(self.window,(255,0,0),(self.x,self.y),self.radius)
			pygame.display.update()
		pygame.quit()
