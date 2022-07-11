import pygame
import random


class Food():
	def __init__(self, size, screenSize):
			self.size = size

			self.x = self.get_num(0, screenSize[0], self.size)
			self.y = self.get_num(0, screenSize[1], self.size)

			self.body = pygame.Rect(self.x, self.y, self.size, self.size)

	def draw(self, screen, color):
		pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.size, self.size))



	# https://stackoverflow.com/a/56123877
	def get_num(self, a, b, x):
		if not a % x:
			return random.choice(range(a, b, x))
		else:
			return random.choice(range(a + x - (a%x), b, x))