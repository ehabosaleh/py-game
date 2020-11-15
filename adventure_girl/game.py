import pygame
from adventure_girl import AdventureGirl
from  bullet import Bullet
from enemy import Enemy

class Game(AdventureGirl):
	
	def __init__(self):
		self.width, self.height= 1024,500
		pygame.init()
		self.window=pygame.display.set_mode((self.width,self.height))
		self.back_ground=pygame.image.load('BG.png')
		self.window.blit(self.back_ground,(0,0))
		super().__init__(0,self.height-200)
		self.listen()
	def listen(self):
		run=True
		pressed_left=False
		pressed_right=False
		pressed_shoot=False
		pressed_slide=False
		pressed_space=False
		pressed_melee=False
		p_direction=True
		while run:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					run=False
					break
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
						perssed_melee=False
				if pressed_left==True:
					
					self.move_left()
					p_direction=False
				
				elif pressed_right==True:
					self.move_right()
					p_direction=True
				elif pressed_shoot==True:
					if p_direction==True:
						self.shoot(True)
					else:
						self.shoot(False)
				elif pressed_slide==True:
					if p_direction==True:
						self.slide(True)
					else:
						self.slide(False)
				elif pressed_space==True:
					if p_direction==True:
						self.jump_1(True)
						self.jump_2(True)
					else:
						self.jump_1(False)
						self.jump_2(False)
				elif pressed_melee==True:
					if p_direction==True:
						self.melee(True)
					else:
						self.melee(False)
				else:
					if p_direction==True:
						self.idle(True)
					else:
						self.idle(False)
		pygame.quit()	
		
game=Game()	

