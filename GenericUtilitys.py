
import sys
import os
from PygameManager import pygame
from pygame.locals import *


class ScalableFont:
	def __init__(self, font_name, font_size):
		self.exe_folder = os.path.dirname(sys.argv[0])
		self.fonts_folder = os.path.join(self.exe_folder, 'Fonts')
		
		self.font_name = font_name
		self.font_path = os.path.join(self.fonts_folder, self.font_name)
		self.font_size = font_size
		
		self.font = pygame.font.Font(self.font_path, font_size)

	def set_font_size(self, font_size):
		self.font_size = font_size
		self.font = pygame.font.Font(self.font_path, font_size)

	def render(self, text, antialias, color):
		return self.font.render(text, antialias, color)	


class Button:
	def __init__(self, x, y, width, height):
		self.rect = pygame.Rect(x, y, width, height)

	def draw(self, screen):
		pygame.draw.rect(screen, (255,0,0), self.rect, 2)		


class Slide:
	def __init__(self, x, y, width, height, min_value, max_value, initial_value):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.min_value = min_value
		self.max_value = max_value
		self.value = initial_value
		self.dragging = False

	def draw(self, screen):
		slider_x = int(self.x + (self.value - self.min_value) / (self.max_value - self.min_value) * self.width)

		pygame.draw.rect(screen, (255, 0, 0), (slider_x - 5, self.y - 5, 10, self.height + 10))

	def update(self):
		if self.dragging:
			mouse_x, _ = pygame.mouse.get_pos()
			new_value = (mouse_x - self.x) / self.width * (self.max_value - self.min_value) + self.min_value
			self.value = max(self.min_value, min(self.max_value, new_value))

	def dragging_slide(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
				self.dragging = True
		elif event.type == pygame.MOUSEBUTTONUP:
			self.dragging = False	





