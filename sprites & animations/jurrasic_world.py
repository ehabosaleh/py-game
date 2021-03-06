import pygame

class Dinosaur:
	width=0
	height=0
	(x,y)=(0,0)
	walk_left=[]
	walk_right=[]
	idel_left=[]
	idel_right=[]
	jump_left=[]
	jump_right=[]
	idle_count=4
	move_count=10
	jump_count=12
	def __init__(self,width,height,x,y):
		self.width=width
		self.height=height
		pygame.init()
		self.window=pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption(" ")
		self.x=x
		self.y=y

		walk_l=[pygame.image.load("walk/Walk_L (1).png"),pygame.image.load("walk/Walk_L (2).png"),pygame.image.load("walk/Walk_L (3).png"),pygame.image.load("walk/Walk_L (4).png"),pygame.image.load("walk/Walk_L (5).png"),pygame.image.load("walk/Walk_L (6).png"),pygame.image.load("walk/Walk_L (7).png"),pygame.image.load("walk/Walk_L (8).png"),pygame.image.load("walk/Walk_L (9).png"),pygame.image.load("walk/Walk_L (10).png")]
		walk_r=[pygame.image.load("walk/Walk_R (1).png"),pygame.image.load("walk/Walk_R (2).png"),pygame.image.load("walk/Walk_R (3).png"),pygame.image.load("walk/Walk_R (4).png"),pygame.image.load("walk/Walk_R (5).png"),pygame.image.load("walk/Walk_R (6).png"),pygame.image.load("walk/Walk_R (7).png"),pygame.image.load("walk/Walk_R (8).png"),pygame.image.load("walk/Walk_R (9).png"),pygame.image.load("walk/Walk_R (10).png")]
		idle_l=[pygame.image.load("idle/Idle_L (1).png"),pygame.image.load("idle/Idle_L (2).png"),pygame.image.load("idle/Idle_L (3).png"), pygame.image.load("idle/Idle_L (4).png")]
		idle_r=[pygame.image.load("idle/Idle_R (1).png"),pygame.image.load("idle/Idle_R (2).png"),pygame.image.load("idle/Idle_R (3).png"), pygame.image.load("idle/Idle_R (4).png")]
		
		jump_l=[pygame.image.load("jump/Jump_L (1).png"), pygame.image.load("jump/Jump_L (2).png"), pygame.image.load("jump/Jump_L (3).png"), pygame.image.load("jump/Jump_L (4).png"), pygame.image.load("jump/Jump_L (5).png"),pygame.image.load("jump/Jump_L (6).png"), pygame.image.load("jump/Jump_L (7).png"), pygame.image.load("jump/Jump_L (8).png"), pygame.image.load("jump/Jump_L (9).png"), pygame.image.load("jump/Jump_L (10).png"), pygame.image.load("jump/Jump_L (11).png"), pygame.image.load("jump/Jump_L (12).png")]
		
		jump_r=[pygame.image.load("jump/Jump_R (1).png"), pygame.image.load("jump/Jump_R (2).png"), pygame.image.load("jump/Jump_R (3).png"), pygame.image.load("jump/Jump_R (4).png"), pygame.image.load("jump/Jump_R (5).png"),pygame.image.load("jump/Jump_R (6).png"), pygame.image.load("jump/Jump_R (7).png"), pygame.image.load("jump/Jump_R (8).png"), pygame.image.load("jump/Jump_R (9).png"), pygame.image.load("jump/Jump_R (10).png"), pygame.image.load("jump/Jump_R (11).png"), pygame.image.load("jump/Jump_R (12).png")]
		self.walk_left=[pygame.transform.scale(i,(200,150)) for i in walk_l]
		self.walk_right=[pygame.transform.scale(i,(200,150)) for i in walk_r]
		self.idle_left=[pygame.transform.scale(i,(200,150)) for i in idle_l]
		self.idle_right=[pygame.transform.scale(i,(200,150)) for i in idle_r]
		self.back_ground=pygame.image.load("BG.png")
		self.jump_left=[pygame.transform.scale(i,(200,150)) for i in jump_l]
		self.jump_right=[pygame.transform.scale(i,(200,150)) for i in jump_r]
		self.idle(True)

	def idle (self,right):
		if right==True:
			for i in range(0,self.idle_count):
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.idle_right[i],(self.x,self.y))
				pygame.display.update()
				pygame.time.delay(50)
			for i in range(self.idle_count-1,-1):
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.idle_right[i],(self.x,self.y))
				pygame.display.update()
				pygame.time.delay(50)
		else:
			for i in range(0,self.idle_count):
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.idle_left[i],(self.x,self.y))
				pygame.display.update()
				pygame.time.delay(50)
			for i in range(self.idle_count-1,-1):
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.idle_left[i],(self.x,self.y))
				pygame.display.update()
				pygame.time.delay(50)
	def jump_1(self,right):
		if right==True:
			for i in range(0,int(self.jump_count/2)):
				y=self.y-8
				x=self.x+4

				if x>self.width-201:
					break;
				self.x=x;
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.jump_right[i],(self.x,y))
				pygame.display.update()	
				pygame.time.delay(30)
		else:
			for i in range(0,int(self.jump_count/2)):
					y=self.y-8
					x=self.x-4

					if x<0:
						break;
					self.x=x;
					self.window.blit(self.back_ground,(0,0))
					self.window.blit(self.jump_left[i],(self.x,y))
					pygame.display.update()	
					pygame.time.delay(30)
			
	def jump_2(self,right):
		if right==True:
			for i in range(int(self.jump_count/2),self.jump_count):
				y=self.y+8
				x=self.x+4

				if x>self.width-201:
					break;
				self.x=x;
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.jump_right[i],(self.x,y))
				pygame.display.update()
				pygame.time.delay(30)

		else:
			for i in range(int(self.jump_count/2),self.jump_count):
				y=self.y+8
				x=self.x-4
				if x<0:
					break;
				self.x=x; 
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.jump_left[i],(self.x,y))
				pygame.display.update()
				pygame.time.delay(30)
				
	def move_left(self):
		for i in range(0,self.move_count):
			self.x-=2
			if self.x<0:
				self.x=0
				break	
			pygame.time.delay(20)
			self.window.blit(self.back_ground,(0,0))
			self.window.blit(self.walk_left[i],(self.x,self.y))
			pygame.display.update()
			
			
	def move_right(self):
		for i in range(0,self.move_count):
			self.x+=2
			if self.x>self.width-201:
				self.x=self.width-201
				break;
			pygame.time.delay(20)
			self.window.blit(self.back_ground,(0,0))
			self.window.blit(self.walk_right[i],(self.x,self.y))
			pygame.display.update()
			

	def listen(self):
		run=True
		pressed_left=False; pressed_right=False;pressed_up=False;pressed_down=False; pressed_space=False
		left=False;right=False		
		p_direction=1
		while run:		
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					run=False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						pressed_left = True
					elif event.key == pygame.K_RIGHT:
						pressed_right = True
					elif event.key==pygame.K_SPACE:
						pressed_space=True
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT:        
						pressed_left = False
					elif event.key == pygame.K_RIGHT:     
						pressed_right = False
				
			if pressed_left == True:
				self.move_left()
				p_direction=0;
			elif pressed_right==True:
				self.move_right()
				p_direction=1
			elif pressed_space==True:
				if p_direction==True:
					self.jump_1(True)
					self.jump_2(True)
				else:
					self.jump_1(False)
					self.jump_2(False)
				pressed_space=False
			else:
				if p_direction==1:
					self.idle(True)
				else:
					self.idle(False)
		pygame.quit()
