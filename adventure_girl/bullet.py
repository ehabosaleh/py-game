import pygame
class Bullet():
	x_b,y_b=0,0
	width,height=0,0
		
	def fire(self,direction,x,y):
		self.width,self.height=pygame.display.get_surface().get_size()
		self.x_b=x+100; self.y_b= y+100
		if direction== True:		
			while self.x_b<self.width-1 and self.x_b<self.get_position():
				self.x_b+=70
				pygame.draw.circle(self.window,(200,150,0),(self.x_b,self.y_b),4)
				self.clock.tick(20)
		else:
			while self.x_b>0:
				self.x_b-=1
				pygame.draw.circle(self.window,(200,150,0),(self.x_b,self.y_b),4)
				self.clock.tick(20)
	

