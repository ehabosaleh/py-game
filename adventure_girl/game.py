import pygame
from adventure_girl import AdventureGirl
from  bullet import Bullet
from enemy import Enemy
import threading
class Game(AdventureGirl,Enemy,Bullet):
	
	def __init__(self,width,height,enemies_num):
		self.width=width
		self.height= height

		self.step=0
		self.p_direction=True
		pygame.init()
		self.window=pygame.display.set_mode((self.width,self.height))
		self.back_ground=pygame.image.load('BG.png')
		self.window.blit(self.back_ground,(0,0))
		pygame.display.update()
		AdventureGirl.__init__(self,self.width//2,self.height-270,self.window)
		Enemy.__init__(self,self.window)
		Bullet.__init__(self,0,0,self.window)
		self.clock=pygame.time.Clock()
		self.t1=threading.Thread(target=self.listen)
		self.t1.start()
		self.generate(enemies_num)
		self.t1.join()

	def generate(self,num):
		for i in range (0,num):
			t2=threading.Thread(target=self.attack)
			t2.start()
			t2.join()
			
	def listen(self):
		run=True
		pressed_left=False
		pressed_right=False
		pressed_shoot=False
		pressed_slide=False
		pressed_space=False
		pressed_melee=False
		p_direction=True
		i=0
		while run:
			
			for event in pygame.event.get():
				if event.type==pygame.QUIT:

					run=False
					break;
				elif event.type==pygame.KEYDOWN:
					if event.key==pygame.K_LEFT:
						pressed_left=True
					elif event.key==pygame.K_RIGHT:
						pressed_right=True
					elif event.key==pygame.K_SPACE:
						pressed_space=True
					elif event.key==pygame.K_LCTRL:
						pressed_shoot=True
					elif event.key==pygame.K_z:
						pressed_slide=True
					elif event.key==pygame.K_RCTRL:
						pressed_melee=True
				elif event.type==pygame.KEYUP:
					if event.key==pygame.K_LEFT:
						pressed_left=False
					elif event.key==pygame.K_RIGHT:
						pressed_right=False
					elif event.key==pygame.K_SPACE:
						pressed_space=False
					elif event.key==pygame.K_LCTRL:
						pressed_shoot=False
					elif event.key==pygame.K_z:
						pressed_slide=False
					elif event.key==pygame.K_RCTRL:
						pressed_melee=False
			if pressed_left==True:	
				for i in range(0,self.move_count):
					self.window.blit(self.back_ground,(0,0))
					self.move_left()
					pygame.display.update()
				self.step=0
				self.p_direction=False
				
				
			elif pressed_right==True:
				for i in range(0,self.move_count):
					self.window.blit(self.back_ground,(0,0))
					self.move_right()
					pygame.display.update()
				self.step=0
				self.p_direction=True
			elif pressed_shoot==True:

				for i in range(0,self.shoot_count):
					self.window.blit(self.back_ground,(0,0))	
					self.shoot( self.p_direction)

					pygame.display.update()
				t3=threading.Thread(target=self.fire,args=(self.p_direction,self.x,self.y,))
				t3.start()
				
				
			elif pressed_slide==True:
				for i in range(0,self.slide_count):
					self.window.blit(self.back_ground,(0,0))
					self.slide( self.p_direction)
					pygame.display.update()
				self.step=0
			elif pressed_space==True:
				for i in range(0,self.jump_count//2):
					self.window.blit(self.back_ground,(0,0))
					self.jump_1( self.p_direction)
					pygame.display.update()
					
				for i in range(0,self.jump_count//2):
					self.window.blit(self.back_ground,(0,0))
					self.jump_2( self.p_direction)
					pygame.display.update()
				self.step=0

			elif pressed_melee==True:
				for i in range(0,self.melee_count):
					self.window.blit(self.back_ground,(0,0))
					self.melee( self.p_direction)
					pygame.display.update()
				self.step=0
			else:
				for i in range (0,self.idle_count):
					
					self.window.blit(self.back_ground,(0,0))
					self.idle( self.p_direction)
					
					pygame.display.update()
				self.step=0
	
		pygame.quit()
		exit()
		
		
		
if __name__=='__main__':
	game=Game(1000,500,20)
