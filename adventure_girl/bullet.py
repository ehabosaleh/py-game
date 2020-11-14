class Bullet():
	x,y=0,0
	width,height=0,0
	def __init__(self,x,y,window):
		self.x=x; self.y= y
		self.window=window
		self.width,self.height=pygame.display.get_surface().get_size()
	def fire(self,direction):
		if direction== "Right":
			while self.x<self.width-1:
				self.x+=1
				pygame.blit(pygame.display.get_surface(),(0,0))
				pygame.draw.circle(self.window,(255,0,0),(self.x,self.y),1)
				pygame.update()
				pygame.time.delay(10)
		else:
			while self.x>0:
				self.x-=1
				pygame.blit(pygame.display.get_surface(),(0,0))
				pygame.draw.circle(self.window,(255,0,0),(self.x,self.y),1)
				pygame.update()
				pygame.time.delay(10)
	

