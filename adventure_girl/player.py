import pygame
class AdventureGirl():
	(x,y)=(0,0)
	run_left=[]
	run_right=[]
	jump_left=[]
	jump_right=[]
	shoot_left=[]
	shoot_right=[]
	slide_left=[]
	slide_right=[]
	melee_left=[]
	melee_right=[]
	idle_left=[]
	idle_rigt=[]
	idle_count=0
	jump_count=0
	move_count=0
	shoot_count=0
	melee_count=0
	slide_count=0
	def __init__(self,x,y,win):
		self.idle_count=6
		self.jump_count=10
		self.move_count=8
		self.shoot_count=3
		self.melee_count=7
		self.slide_count=5
		self.x=x
		self.y=y
	
		run_l=[pygame.image.load(f"run/Run_L ({i}).png") for i in range(1,self.move_count+1)]
		run_r=[pygame.image.load(f"run/Run_R ({i}).png") for i in range(1,self.move_count+1)]
		self.run_left=[pygame.transform.scale(image,(150,200)) for image in run_l]
		self.run_right=[pygame.transform.scale(image,(150,200)) for image in run_r]
					
		jump_l=[pygame.image.load(f"jump/Jump_L ({i}).png") for i in range(1,self.jump_count+1)]
		jump_r=[pygame.image.load(f"jump/Jump_R ({i}).png") for i in range(1,self.jump_count+1)]
		self.jump_left=[pygame.transform.scale(image,(150,200)) for image in jump_l]
		self.jump_right=[pygame.transform.scale(image,(150,200)) for image in jump_r]
		
		shoot_l=[pygame.image.load(f"shoot/Shoot_L ({i}).png") for i in range(1,self.shoot_count+1)]
		shoot_r=[pygame.image.load(f"shoot/Shoot_R ({i}).png") for i in range(1,self.shoot_count+1)]
		self.shoot_left=[pygame.transform.scale(image,(150,200)) for image in shoot_l]
		self.shoot_right=[pygame.transform.scale(image,(150,200)) for image in shoot_r]
		
		slide_l=[pygame.image.load(f"slide/Slide_L ({i}).png") for i in range(1,self.slide_count+1)]
		slide_r=[pygame.image.load(f"slide/Slide_R ({i}).png") for i in range(1,self.slide_count+1)]
		self.slide_left=[pygame.transform.scale(image,(150,200)) for image in slide_l]
		self.slide_right=[pygame.transform.scale(image,(150,200)) for image in slide_r]
		
		melee_l=[pygame.image.load(f"melee/Melee_L ({i}).png") for i in range(1,self.melee_count+1)]
		melee_r=[pygame.image.load(f"melee/Melee_R ({i}).png") for i in range(1,self.melee_count+1)]
		self.melee_left=[pygame.transform.scale(image,(150,200)) for image in melee_l]
		self.melee_right=[pygame.transform.scale(image,(150,200)) for image in melee_r]
		
		idle_l=[pygame.image.load(f"idle/Idle_L ({i}).png") for i in range(1,self.idle_count+1)]
		idle_r=[pygame.image.load(f"idle/Idle_R ({i}).png") for i in range(1,self.idle_count+1)]
		self.idle_left=[pygame.transform.scale(image,(150,200)) for image in idle_l]
		self.idle_right=[pygame.transform.scale(image,(150,200)) for image in idle_r]
		self.window=win
		self.width,self.height=pygame.display.get_surface().get_size()
		self.back_ground=pygame.image.load("BG.png")
		
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
		
	def idle(self,right):
		
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
				pygame.time.delay(50)
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
					pygame.time.delay(50)
			
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
				pygame.time.delay(50)

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
				pygame.time.delay(50)
	def shoot(self,right):
		if right==True:
			for i in range (0,self.shoot_count):
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.shoot_right[i],(self.x,self.y))
				pygame.display.update()
				pygame.time.delay(50)
		else:
			for i in range(self.shoot_count,-1):
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.shoot_left[i],(self.x,self.x))
				pygame.display.update()
				pygame.time.delay(50)
				
	def melee (self,right):
		if right==True:
			for i in range(0,self.melee_count):
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.melee_right[i],(self.x,self.y))
				pygame.display.update()
				pygame.time.delay(50)
		else:
			for  i in range(0,range.melee_count):
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.melee_left[i],(self.x,self.y))
				pygame.display.update()
				pygame.time.delay(50)
	def slide(self,right):
		if right==True:
			for i in range(0,self.slide_count):
				x=self.x+4
				if x>self.width-201:
					break;
				self.x=x
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.slide_right[i],(self.x,self.y))
				pygame.display.update()
				pygame.time.delay(50)
		else:
			for i in range(0,self.slide_count):
				x=self.x-4
				if x<0:
					break;
				self.x=x
				self.window.blit(self.back_ground,(0,0))
				self.window.blit(self.slide_right[i],(self.x,self.y))
				pygame.display.update()
				pygame.time.delay(50)
				
class Enemey(AdentureGirl):
	

pygame.init()				
window=pygame.display.set_mode((500,500))				
player=AdventureGirl(0,300,window)
player.melee(True)
