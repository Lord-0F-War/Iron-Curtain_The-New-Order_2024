import pygame
from pygame.locals import *

class Pygame:
	def __init__(self, screen_width, screen_height):
		self.all_sprites = pygame.sprite.Group()
		self.screen_width = screen_width
		self.screen_height = screen_height
	
	def start_pygame(self):
		pygame.init()
		pygame.font.init()
		
		return pygame
	
	def config_pygame(self):
		pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP, USEREVENT, MOUSEWHEEL, MOUSEBUTTONUP, MOUSEBUTTONDOWN])
		self.clock = pygame.time.Clock()  
		
		self.display = pygame.display.set_mode((self.screen_width, self.screen_height))
		self.screen = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
		self.surface_alfa = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)

		self.territory_ownership_surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)

		self.screen.fill((0, 0, 0))
		self.surface_alfa.fill((0, 0, 0, 0))

		self.date_tick = pygame.USEREVENT + 1
		self.FPS_update = pygame.USEREVENT + 2
		self.key_delay = pygame.USEREVENT + 3
		self.screen_update = pygame.USEREVENT + 4
		
		pygame.time.set_timer(self.date_tick, 10) # 100 ticks per second
		pygame.time.set_timer(self.FPS_update, 50)
		pygame.time.set_timer(self.key_delay, 42)
		pygame.time.set_timer(self.screen_update, 40) # 25 fps

		pygame.mixer.init(buffer=8192) 
		pygame.K_1
		return (self.clock, QUIT, self.date_tick, self.FPS_update, self.key_delay, self.screen_update, self.display, self.screen, self.surface_alfa, self.territory_ownership_surface)

