import pygame
import sys
class AdventureGirl():
	width,height=0,0
	def __init__(self,x,y,window):
		self.window=window
		self.idle_count=1
		self.jump_count=10
		self.move_count=8
		self.shoot_count=3
		self.slide_count=5
		self.x=x
		self.y=y
		self.fps=15
		w=200;h=250
		run_l=[pygame.image.load(f"run/Run_L ({i}).png") for i in range(1,self.move_count+1)]
		run_r=[pygame.image.load(f"run/Run_R ({i}).png") for i in range(1,self.move_count+1)]
		self.run_left=[pygame.transform.scale(image,(w,h)) for image in run_l]
		self.run_right=[pygame.transform.scale(image,(w,h)) for image in run_r]
					
		jump_l=[pygame.image.load(f"jump/Jump_L ({i}).png") for i in range(1,self.jump_count+1)]
		jump_r=[pygame.image.load(f"jump/Jump_R ({i}).png") for i in range(1,self.jump_count+1)]
		self.jump_left=[pygame.transform.scale(image,(w,h)) for image in jump_l]
		self.jump_right=[pygame.transform.scale(image,(w,h)) for image in jump_r]
		w=250;h=250
		shoot_l=[pygame.image.load(f"shoot/Shoot_L ({i}).png") for i in range(1,self.shoot_count+1)]
		shoot_r=[pygame.image.load(f"shoot/Shoot_R ({i}).png") for i in range(1,self.shoot_count+1)]
		self.shoot_left=[pygame.transform.scale(image,(w,h)) for image in shoot_l]
		self.shoot_right=[pygame.transform.scale(image,(w,h)) for image in shoot_r]
		w=200;h=250
		
		
		idle_l=[pygame.image.load(f"idle/Idle_L ({i}).png") for i in range(1,self.idle_count+1)]
		idle_r=[pygame.image.load(f"idle/Idle_R ({i}).png") for i in range(1,self.idle_count+1)]
		self.idle_left=[pygame.transform.scale(image,(w,h)) for image in idle_l]
		self.idle_right=[pygame.transform.scale(image,(w,h)) for image in idle_r]
		
		w=250;h=200
		slide_l=[pygame.image.load(f"slide/Slide_L ({i}).png") for i in range(1,self.slide_count+1)]
		slide_r=[pygame.image.load(f"slide/Slide_R ({i}).png") for i in range(1,self.slide_count+1)]
		self.slide_left=[pygame.transform.scale(image,(w,h)) for image in slide_l]
		self.slide_right=[pygame.transform.scale(image,(w,h)) for image in slide_r]
		
		self.width,self.height=pygame.display.get_surface().get_size()
		
		
	def move_left(self):
		x=self.x-10
		if x<0:
			return None
		self.x=x
		self.window.blit(self.run_left[self.step],(self.x,self.y))
		self.step=(self.step+1)%self.move_count
		self.clock.tick(self.fps)
			
			
			
	def move_right(self):
		x=self.x+10
		if x>self.width-201:
			return None
		self.x=x
		self.window.blit(self.run_right[self.step],(self.x,self.y))
		self.step=(self.step+1)%self.move_count
		self.clock.tick(self.fps)
		
	def idle(self,right):

			if right==True:
				
				self.window.blit(self.idle_right[self.step],(self.x,self.y))
				self.step=(self.step+1)% self.idle_count
				self.clock.tick(self.fps)			
			else:

				
				self.window.blit(self.idle_left[self.step],(self.x,self.y))
				self.step=(self.step+1)% self.idle_count
				self.clock.tick(self.fps)	


	def jump_1(self,right):
		if right==True:	
			y=self.y-10
			x=self.x+10
			if x>self.width-201:
				return None
			self.x=x
			self.y=y
			
			self.window.blit(self.jump_right[self.step],(self.x,self.y))
			self.step=(self.step+1)%self.jump_count
			self.clock.tick(self.fps)	

		else:
			y=self.y-10
			x=self.x-10
			if x<0:
				return None
			self.x=x
			self.y=y
			self.window.blit(self.jump_left[self.step],(self.x,self.y))
			self.step=(self.step+1)%self.jump_count
			self.clock.tick(self.fps)	

			
	def jump_2(self,right):
		if right==True:
			y=self.y+10
			x=self.x+10

			if x>self.width-201:
				return None
			self.x=x
			self.y=y
			
			self.window.blit(self.jump_right[self.step],(self.x,self.y))
			self.step=(self.step+1)%self.jump_count
			self.clock.tick(self.fps)


		else:
			y=self.y+10
			x=self.x-10
			if x<0:
				return None
			self.x=x
			self.y=y
			
			self.window.blit(self.jump_left[self.step],(self.x,self.y))
			self.step=(self.step+1)%self.jump_count
			self.clock.tick(self.fps)

	def shoot(self,right):
		if right==True:
			
			self.window.blit(self.shoot_right[self.step],(self.x,self.y))
			self.step=(self.step+1)%self.shoot_count
			self.clock.tick(self.fps)

		else:
			self.step=(self.step+1)%self.shoot_count
			self.window.blit(self.shoot_left[self.step],(self.x,self.y))
			self.clock.tick(self.fps)

				

	def slide(self,right):
		y=self.y+40
		if right==True:
			x=self.x+8
			if x>self.width-201:
				return None
			self.x=x
			self.window.blit(self.slide_right[self.step],(self.x,y))
			self.step=(self.step+1)%self.slide_count
			self.clock.tick(self.fps)
		else:
			x=self.x-8
			if x<0:
				return None
			self.x=x
			
			self.window.blit(self.slide_left[self.step],(self.x,y))
			self.step=(self.step+1)%self.slide_count
			self.clock.tick(self.fps)
				
