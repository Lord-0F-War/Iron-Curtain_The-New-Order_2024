
import sys
import os
from PygameManager import pygame
from pygame.locals import *
from shapely.geometry import Polygon
import math



def generate_fading_colors(num_values, base_color):
	colors = []
	r, g, b = base_color
	step = 160 // num_values
	
	for i in range(num_values):
		colors.append((r, g, b))
		r = max(r - step, 0)
		g = max(g - step, 0)
		b = max(b - step, 0)
	
	return colors


def draw_pie_chart(surface, position, radius, values, colors):
	total = sum(values)
	start_angle = 0
	rects = []  # List to store rects around each drawn polygon
	
	for i, value in enumerate(values):
		angle = (value / total) * 360
		end_angle = start_angle + angle
		
		# Calculate the points of the pie segment
		points = [position]
		
		for a in range(int(start_angle), int(end_angle) + 1, 1):
			rad_angle = math.radians(a)
			x = position[0] + int(radius * math.cos(rad_angle))
			y = position[1] + int(radius * math.sin(rad_angle))
			points.append((int(x), int(y)))
		
		# Close the segment with the center point
		points.append(position)
		
		pygame.draw.polygon(surface, colors[i], points)
		# Get the rect around the drawn polygon
		#rect_around_polygon = [points[0], points[-2], points[1]]
		rect_around_polygon = points[0:-2]
		rects.append(rect_around_polygon)
		
		start_angle += angle
	return rects

def polygon_intersects_rectangle(polygon_vertices, rect):
    polygon = Polygon(polygon_vertices)
    rect_polygon = Polygon([(rect[0], rect[1]), (rect[0]+rect[2], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), (rect[0], rect[1]+rect[3])])

    return polygon.intersects(rect_polygon)

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





