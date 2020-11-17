import pygame
from adventure_girl import AdventureGirl
from  bullet import Bullet
from enemy import Enemy
import threading
class Game(AdventureGirl,Enemy):
	
	def __init__(self):
		self.width, self.height= 1024,500
		pygame.init()
		self.window=pygame.display.set_mode((self.width,self.height))
		self.back_ground=pygame.image.load('BG.png')
		self.window.blit(self.back_ground,(0,0))
		pygame.display.update()
		AdventureGirl.__init__(self,0,self.height-270)
		Enemy.__init__(self,self.width-150,self.height-270)
		t1=threading.Thread(target=self.listen)
		t2=threading.Thread(target=self.attack)
		t1.start()
		t2.start()
		t1.join()
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
				self.move_left()
				p_direction=False
				
			elif pressed_right==True:
				self.move_right()
				p_direction=True
			elif pressed_shoot==True:
				self.shoot( p_direction)
			elif pressed_slide==True:
				self.slide( p_direction)
			elif pressed_space==True:
				self.jump_1( p_direction)
				self.jump_2( p_direction)
			elif pressed_melee==True:
				self.melee( p_direction)
			else:
				self.idle( p_direction)
	
		pygame.quit()
		exit()
		
		
		
if __name__=='__main__':
	game=Game()	

