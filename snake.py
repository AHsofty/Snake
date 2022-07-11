import pygame
import random

class Snake():
	def __init__(self, bodyType, position=(0,0), size=20):
		self.bodyType = bodyType
		self.body = pygame.Rect(position, (size,size))
		
		if self.bodyType == "head":
			self.direction = "right"
		
		self.size = size
		self.x = position[0]
		self.y = position[1]
		self.prevX = self.x
		self.prevY = self.y



	def draw(self, screen, color):
		pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.size, self.size))


	def move(self, bodies):
		self.prevX = self.x
		self.prevY = self.y

		if self.bodyType == "head":
			if self.direction == "right":
				self.x += self.size

			if self.direction == "left":
				self.x -= self.size

			if self.direction == "up":
				self.y -= self.size

			if self.direction == "down":
				self.y += self.size
		else:
			for idx, i in enumerate(bodies):
				if i is self:
					self.x = bodies[idx-1].prevX		
					self.y = bodies[idx-1].prevY
					break