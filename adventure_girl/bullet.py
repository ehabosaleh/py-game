import pygame
class Bullet():
	x_b,y_b=0,0
	width,height=0,0
	def __init__(self,x,y,window):
		self.window=window
		self.x_b=x; self.y_b=y
		self.width,self.height=pygame.display.get_surface().get_size()
		p1=pygame.image.load("clash_1.png")
		p2=pygame.image.load("clash_2.png")
		self.projectile_1=pygame.transform.scale(p1,(25,10))
		self.projectile_2=pygame.transform.scale(p2,(25,10))
		
	def fire(self,direction,x,y):
		self.x_b=x+100; self.y_b= y+125
		if direction== True:		
			while self.x_b<self.width-1:
				if self.hit==True:
					break;
					
				self.x_b+=50
				self.window.blit(self.projectile_1,(self.x_b,self.y_b))
				self.clock.tick(15)
		else:
			while self.x_b>0:
				if self.hit==True:
					break;
				self.x_b-=50
				self.window.blit(self.projectile_2,(self.x_b,self.y_b))
				self.clock.tick(15)
		self.y_b=-100
		self.hit=False
				
	def get_bullet_position(self):
		return (self.x_b,self.y_b)

