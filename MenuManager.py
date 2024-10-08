
import GenericUtilitys
from PygameManager import pygame
from pyvidplayer import Video
import CountriesManager
import math

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

#----------------------------------------------------#

class ESC_Menu:
	def __init__(self, screen_width, screen_height, ESC_menu_background, generic_hover_over_button_sound, generic_click_menu_sound, 
			  hovered_green_button_menu_image, hovered_red_button_menu_image, Options_Menu) -> None:
		
		self.Options_Menu = Options_Menu 

		self.hovered_green_button_menu_image, self.hovered_red_button_menu_image =  hovered_green_button_menu_image, hovered_red_button_menu_image
		self.hover_over_button_sound, self.click_menu_sound = generic_hover_over_button_sound, generic_click_menu_sound
		self.hovered_button = 'none'
		self.last_hovered_button = None		

		self.ESC_menu_background = ESC_menu_background

		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y		

		menu_gui_width = self.ESC_menu_background.get_width()
		menu_gui_height = self.ESC_menu_background.get_height()
		
		self.menu_gui_middle_x = (screen_width/2 - menu_gui_width/2)
		self.menu_gui_middle_y = (screen_height/2 - menu_gui_height/2)	

		self.hovered_green_button_menu_image = pygame.transform.smoothscale(hovered_green_button_menu_image, (371 * self.factor_x, 34 * self.factor_y))
		self.hovered_red_button_menu_image = pygame.transform.smoothscale(hovered_red_button_menu_image, (371 * self.factor_x, 34 * self.factor_y))

		options_button_width = 371 * self.factor_x
		options_button_height = 34 * self.factor_y
		options_button_x_offset = 59 * self.factor_x
		options_button_y_offset = 101 * self.factor_y
		self.options_button = GenericUtilitys.Button(self.menu_gui_middle_x + options_button_x_offset, self.menu_gui_middle_y + options_button_y_offset, options_button_width, options_button_height)
		
		main_menu_button_width = 371 * self.factor_x
		main_menu_button_height = 34 * self.factor_y
		main_menu_button_x_offset = 59 * self.factor_x
		main_menu_button_y_offset = 420 * self.factor_y
		self.main_menu_button = GenericUtilitys.Button(self.menu_gui_middle_x + main_menu_button_x_offset, self.menu_gui_middle_y + main_menu_button_y_offset, main_menu_button_width, main_menu_button_height)
		
		quit_button_width = 371 * self.factor_x
		quit_button_height = 34 * self.factor_y
		quit_button_x_offset = 59 * self.factor_x
		quit_button_y_offset = 465 * self.factor_y
		self.quit_button = GenericUtilitys.Button(self.menu_gui_middle_x + quit_button_x_offset, self.menu_gui_middle_y + quit_button_y_offset, quit_button_width, quit_button_height)						
		

	def get_button_by_interaction(self, mouse_rect, is_options_open):
		if is_options_open == False:
			if self.options_button.rect.colliderect(mouse_rect):
				return 'options'
			elif self.main_menu_button.rect.colliderect(mouse_rect):
				return 'main_menu'
			elif self.quit_button.rect.colliderect(mouse_rect):
				return 'quit'		
			else:
				return 'none'
		else:
			return self.Options_Menu.get_button_by_interaction(mouse_rect)


	def get_clicked_button(self, mouse_rect, is_options_open):
		if is_options_open == False:
			clicked_button = self.get_button_by_interaction(mouse_rect, is_options_open)
			if clicked_button != 'none':
				self.hover_over_button_sound.fadeout(150)
				self.click_menu_sound.play()
			return clicked_button
		else:
			return self.Options_Menu.get_clicked_button(mouse_rect)
	

	def get_hovered_button(self, mouse_rect, is_options_open):
		if is_options_open == False:
			hovered_button = self.get_button_by_interaction(mouse_rect, is_options_open)
			if self.hovered_button != 'none':
				if self.hovered_button != self.last_hovered_button:
					self.hover_over_button_sound.play()
					self.last_hovered_button = self.hovered_button
			else:
				self.last_hovered_button = None
			
			return hovered_button
		else:
			return self.Options_Menu.get_hovered_button(mouse_rect)	
	

	def draw(self, surface_alfa, is_options_open):
		if is_options_open == False:
			surface_alfa.blit(self.ESC_menu_background, (self.menu_gui_middle_x, self.menu_gui_middle_y))

			if self.hovered_button != 'none':
				if self.hovered_button == 'options':
					surface_alfa.blit(self.hovered_green_button_menu_image, self.options_button.rect)
				elif self.hovered_button == 'main_menu':
					surface_alfa.blit(self.hovered_green_button_menu_image, self.main_menu_button.rect)
				elif self.hovered_button == 'quit':
					surface_alfa.blit(self.hovered_red_button_menu_image, self.quit_button.rect)
		else:
			self.Options_Menu.draw(surface_alfa)			
class Options_Menu:
	def __init__(self, screen_width, screen_height, options_menu_background, generic_hover_over_button_sound, generic_click_menu_sound, 
			  hovered_green_button_menu_image, hovered_red_button_menu_image, Sounds_Manager, Main_Menu) -> None:
		
		self.Sounds_Manager = Sounds_Manager
		self.Main_Menu = Main_Menu

		self.hover_over_button_sound, self.click_menu_sound = generic_hover_over_button_sound, generic_click_menu_sound
		self.hovered_button = 'none'
		self.last_hovered_button = None		

		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y	

		self.hovered_green_button_menu_image = pygame.transform.smoothscale(hovered_green_button_menu_image, (371 * self.factor_x, 34 * self.factor_y))
		self.hovered_red_button_menu_image = pygame.transform.smoothscale(hovered_red_button_menu_image, (371 * self.factor_x, 34 * self.factor_y))		

		self.options_menu_background = pygame.transform.smoothscale_by(options_menu_background, (self.factor_x,self.factor_y))			

		menu_gui_width = self.options_menu_background.get_width()
		menu_gui_height = self.options_menu_background.get_height()
		
		self.options_menu_gui_middle_x = (screen_width/2 - menu_gui_width/2)
		self.options_menu_gui_middle_y = (screen_height/2 - menu_gui_height/2)		


		back_button_width = 371 * self.factor_x
		back_button_height = 34 * self.factor_y
		back_button_x_offset = 63 * self.factor_x
		back_button_y_offset = 887 * self.factor_y
		self.back_button = GenericUtilitys.Button(self.options_menu_gui_middle_x + back_button_x_offset, self.options_menu_gui_middle_y + back_button_y_offset, back_button_width, back_button_height)	
		
		resolutions_button_width = 371 * self.factor_x
		resolutions_button_height = 34 * self.factor_y
		resolutions_button_x_offset = 62 * self.factor_x
		self.resolution_2560x1440_button = GenericUtilitys.Button(self.options_menu_gui_middle_x + resolutions_button_x_offset, self.options_menu_gui_middle_y + 100 * self.factor_y,
												  resolutions_button_width, resolutions_button_height)	
		self.resolution_1920x1080_button = GenericUtilitys.Button(self.options_menu_gui_middle_x + resolutions_button_x_offset, self.options_menu_gui_middle_y + 145 * self.factor_y,
												  resolutions_button_width, resolutions_button_height)	
		self.resolution_1600x900_button = GenericUtilitys.Button(self.options_menu_gui_middle_x + resolutions_button_x_offset, self.options_menu_gui_middle_y + 190 * self.factor_y,
												  resolutions_button_width, resolutions_button_height)	
		self.resolution_1440x900_button = GenericUtilitys.Button(self.options_menu_gui_middle_x + resolutions_button_x_offset, self.options_menu_gui_middle_y + 235 * self.factor_y,
												  resolutions_button_width, resolutions_button_height)	
		self.resolution_1280x1024_button = GenericUtilitys.Button(self.options_menu_gui_middle_x + resolutions_button_x_offset, self.options_menu_gui_middle_y + 280 * self.factor_y,
												  resolutions_button_width, resolutions_button_height)										

		self.clicked_resolution_button = f'resolution_{screen_width}x{screen_height}'


		self.brightness_slider = GenericUtilitys.Slide(self.options_menu_gui_middle_x + 457* self.factor_x, self.options_menu_gui_middle_y + 135* self.factor_y, 374* self.factor_x, 10* self.factor_y, 0, 180, 0)
		
		self.music_slider = GenericUtilitys.Slide(self.options_menu_gui_middle_x + 852* self.factor_x, self.options_menu_gui_middle_y + 135* self.factor_y, 374* self.factor_x, 10* self.factor_y, 0, max_value = 100, initial_value = 10)
		self.sound_slider = GenericUtilitys.Slide(self.options_menu_gui_middle_x + 852* self.factor_x, self.options_menu_gui_middle_y + 270* self.factor_y, 374* self.factor_x, 10* self.factor_y, 0, max_value = 100, initial_value = 50)
		
		pygame.mixer.music.set_volume(self.music_slider.value/100)	
		self.Sounds_Manager.change_volume(self.sound_slider.value/100)

		self.Main_Menu.main_menu_intro_video.set_volume(self.sound_slider.value/100)		


	def get_button_by_interaction(self, mouse_rect):
		if self.back_button.rect.colliderect(mouse_rect):
			return 'back'
		
		elif self.resolution_2560x1440_button.rect.colliderect(mouse_rect):
			return 'resolution_2560x1440'	
		elif self.resolution_1920x1080_button.rect.colliderect(mouse_rect):
			return 'resolution_1920x1080'
		elif self.resolution_1600x900_button.rect.colliderect(mouse_rect):
			return 'resolution_1600x900'
		elif self.resolution_1440x900_button.rect.colliderect(mouse_rect):
			return 'resolution_1440x900'
		elif self.resolution_1280x1024_button.rect.colliderect(mouse_rect):
			return 'resolution_1280x1024'
																
		else:
			return 'none'


	def get_clicked_button(self, mouse_rect):
		clicked_button = self.get_button_by_interaction(mouse_rect)
		if clicked_button != 'none':
			self.hover_over_button_sound.fadeout(150)
			self.click_menu_sound.play()
			self.clicked_resolution_button = clicked_button
		return clicked_button
	

	def get_hovered_button(self, mouse_rect):
		hovered_button = self.get_button_by_interaction(mouse_rect)
		if self.hovered_button != 'none':
			if self.hovered_button != self.last_hovered_button:
				self.hover_over_button_sound.play()
				self.last_hovered_button = self.hovered_button
		else:
			self.last_hovered_button = None
		
		return hovered_button	
	

	def interacting_with_UI_slides(self, key_event):
		self.brightness_slider.dragging_slide(key_event)
		self.music_slider.dragging_slide(key_event)
		self.sound_slider.dragging_slide(key_event)		

		self.brightness_slider.update()
		self.music_slider.update()
		self.sound_slider.update()

		self.Main_Menu.main_menu_intro_video.set_volume(self.sound_slider.value/100)

		pygame.mixer.music.set_volume(self.music_slider.value/100)
		self.Sounds_Manager.change_volume(self.sound_slider.value/100)


	def draw(self, surface_alfa):
		surface_alfa.blit(self.options_menu_background, (self.options_menu_gui_middle_x, self.options_menu_gui_middle_y))

		self.brightness_slider.draw(surface_alfa)
		self.music_slider.draw(surface_alfa)
		self.sound_slider.draw(surface_alfa)

		if self.hovered_button != 'none':
			if self.hovered_button == 'back':
				surface_alfa.blit(self.hovered_red_button_menu_image, self.back_button.rect)			

			elif self.hovered_button == 'resolution_2560x1440':
				surface_alfa.blit(self.hovered_green_button_menu_image, self.resolution_2560x1440_button.rect)	
			elif self.hovered_button == 'resolution_1920x1080':
				surface_alfa.blit(self.hovered_green_button_menu_image, self.resolution_1920x1080_button.rect)	
			elif self.hovered_button == 'resolution_1600x900':
				surface_alfa.blit(self.hovered_green_button_menu_image, self.resolution_1600x900_button.rect)	
			elif self.hovered_button == 'resolution_1440x900':
				surface_alfa.blit(self.hovered_green_button_menu_image, self.resolution_1440x900_button.rect)	
			elif self.hovered_button == 'resolution_1280x1024':
				surface_alfa.blit(self.hovered_green_button_menu_image, self.resolution_1280x1024_button.rect)

		if self.clicked_resolution_button == 'resolution_2560x1440':
			surface_alfa.blit(self.hovered_green_button_menu_image, self.resolution_2560x1440_button.rect)	
		elif self.clicked_resolution_button == 'resolution_1920x1080':
			surface_alfa.blit(self.hovered_green_button_menu_image, self.resolution_1920x1080_button.rect)	
		elif self.clicked_resolution_button == 'resolution_1600x900':
			surface_alfa.blit(self.hovered_green_button_menu_image, self.resolution_1600x900_button.rect)	
		elif self.clicked_resolution_button == 'resolution_1440x900':
			surface_alfa.blit(self.hovered_green_button_menu_image, self.resolution_1440x900_button.rect)	
		elif self.clicked_resolution_button == 'resolution_1280x1024':
			surface_alfa.blit(self.hovered_green_button_menu_image, self.resolution_1280x1024_button.rect)	

#----------------------------------------------------#

class Main_Menu:
	def __init__(self, screen_width, screen_height, pygame, game_logo, python_logo, menu_gui, hovered_green_button_menu_image, hovered_red_button_menu_image, 
			new_game_menu_background, hover_over_button_sound, click_menu_sound):
		
		self.hovered_button = 'none'
		self.last_hovered_button ='none'

		self.hover_over_button_sound = hover_over_button_sound
		self.click_menu_sound = click_menu_sound

		self.new_game_menu_background = new_game_menu_background
		new_game_menu_background_width = self.new_game_menu_background.get_width()
		new_game_menu_background_height = self.new_game_menu_background.get_height()
		
		self.new_game_menu_background_middle_x = (screen_width/2 - new_game_menu_background_width/2)
		self.new_game_menu_background_middle_y = (screen_height/1.65 - new_game_menu_background_height/2)		
		self.is_in_new_game_menu = False
		
		self.screen_width = screen_width
		self.screen_height = screen_height
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y

		self.python_logo = python_logo
		self.python_logo = pygame.transform.smoothscale_by(self.python_logo, (self.factor_x,self.factor_y))

		self.game_logo = game_logo
		self.game_logo = pygame.transform.smoothscale_by(self.game_logo, (self.factor_x,self.factor_y))

		self.menu_gui = pygame.transform.smoothscale_by(menu_gui, (self.factor_x,self.factor_y))
		
		self.hovered_green_button_menu_image = pygame.transform.smoothscale(hovered_green_button_menu_image, (371 * self.factor_x, 34 * self.factor_y))
		self.hovered_red_button_menu_image = pygame.transform.smoothscale(hovered_red_button_menu_image, (371 * self.factor_x, 34 * self.factor_y))

		
		menu_gui_width = self.menu_gui.get_width()
		menu_gui_height = self.menu_gui.get_height()
		
		self.menu_gui_middle_x = (screen_width/2 - menu_gui_width/2)
		self.menu_gui_middle_y = (screen_height/1.35 - menu_gui_height/2)	

		
		start_button_width = 371 * self.factor_x
		start_button_height = 34 * self.factor_y
		start_button_x_offset = 49 * self.factor_x
		start_button_y_offset = 459 * self.factor_y
		self.start_button = GenericUtilitys.Button(self.menu_gui_middle_x + start_button_x_offset, self.menu_gui_middle_y + start_button_y_offset, start_button_width, start_button_height)	

		quit_button_width = 371 * self.factor_x
		quit_button_height = 34 * self.factor_y
		quit_button_x_offset = 516 * self.factor_x
		quit_button_y_offset = 459 * self.factor_y
		self.quit_button = GenericUtilitys.Button(self.menu_gui_middle_x + quit_button_x_offset, self.menu_gui_middle_y + quit_button_y_offset, quit_button_width, quit_button_height)	

		options_button_width = 371 * self.factor_x
		options_button_height = 34 * self.factor_y
		options_button_x_offset = 516 * self.factor_x
		options_button_y_offset = 403 * self.factor_y
		self.options_button = GenericUtilitys.Button(self.menu_gui_middle_x + options_button_x_offset, self.menu_gui_middle_y + options_button_y_offset, options_button_width, options_button_height)

		# NEW GAME / LOAD SAVE  MENU

		new_game_button_width = 371 * self.factor_x
		new_game_button_height = 34 * self.factor_y
		new_game_button_x_offset = 59 * self.factor_x
		new_game_button_y_offset = 28 * self.factor_y
		self.new_game_button = GenericUtilitys.Button(self.new_game_menu_background_middle_x + new_game_button_x_offset, self.new_game_menu_background_middle_y + new_game_button_y_offset, new_game_button_width, new_game_button_height)

		load_save_button_width = 371 * self.factor_x
		load_save_button_height = 34 * self.factor_y
		load_save_button_x_offset = 59 * self.factor_x
		load_save_button_y_offset = 79 * self.factor_y
		self.load_save_button = GenericUtilitys.Button(self.new_game_menu_background_middle_x + load_save_button_x_offset, self.new_game_menu_background_middle_y + load_save_button_y_offset, load_save_button_width, load_save_button_height)

		back_button_width = 371 * self.factor_x
		back_button_height = 34 * self.factor_y
		back_button_x_offset = 59 * self.factor_x
		back_button_y_offset = 162 * self.factor_y
		self.back_button = GenericUtilitys.Button(self.new_game_menu_background_middle_x + back_button_x_offset, self.new_game_menu_background_middle_y + back_button_y_offset, back_button_width, back_button_height)

		self.main_menu_intro_video = Video("game_intro.mp4", size=(936 * self.factor_x, 378 * self.factor_y))
		self.main_menu_intro_video.set_volume(0)


	def get_button_by_interaction(self, mouse_rect):
		if self.start_button.rect.colliderect(mouse_rect):
			return 'start'
		elif self.quit_button.rect.colliderect(mouse_rect):
			return 'quit'
		elif self.options_button.rect.colliderect(mouse_rect):
			return 'options'
		elif self.new_game_button.rect.colliderect(mouse_rect):
			return 'new_game'
		elif self.load_save_button.rect.colliderect(mouse_rect):
			return 'load_save'
		elif self.back_button.rect.colliderect(mouse_rect):
			return 'back'		
		else:
			return 'none'


	def get_clicked_button(self, mouse_rect):
		clicked_button = self.get_button_by_interaction(mouse_rect)
		if clicked_button != 'none':
			if self.is_in_new_game_menu == False:
				self.hover_over_button_sound.fadeout(150)
				self.click_menu_sound.play()	
			else:
				if clicked_button == 'new_game':
					self.hover_over_button_sound.fadeout(150)
					self.click_menu_sound.play()
				elif clicked_button == 'load_save':
					self.hover_over_button_sound.fadeout(150)
					self.click_menu_sound.play()
				elif clicked_button == 'back':		
					self.hover_over_button_sound.fadeout(150)
					self.click_menu_sound.play()								

		return clicked_button


	def get_hovered_button(self, mouse_rect):
		self.hovered_button = self.get_button_by_interaction(mouse_rect)
		if self.is_in_new_game_menu == False:
			if self.hovered_button != self.last_hovered_button and self.hovered_button not in ['new_game', 'load_save', 'back'] and self.hovered_button != 'none':
				self.hover_over_button_sound.play()
				self.last_hovered_button = self.hovered_button
				return self.hovered_button
			elif self.hovered_button != 'none':
				return self.last_hovered_button
			else:
				self.last_hovered_button = 'none'
				return 'none'
		else:
			if self.hovered_button != self.last_hovered_button and self.hovered_button in ['new_game', 'load_save', 'back'] and self.hovered_button != 'none':
				self.hover_over_button_sound.play()
				self.last_hovered_button = self.hovered_button
				return self.hovered_button
			elif self.hovered_button != 'none':
				return self.last_hovered_button
			else:
				self.last_hovered_button = 'none'
				return 'none'				


	def draw(self, screen):
		screen.blit(self.python_logo, (0, self.screen_height - self.python_logo.get_height()))

		screen.blit(self.game_logo, (60 * self.factor_x, 20 * self.factor_y))	
		
		if self.is_in_new_game_menu == False:
			self.main_menu_intro_video.draw(screen, (self.menu_gui_middle_x + 2 * self.factor_x, self.menu_gui_middle_y + 2 * self.factor_y))

			if self.main_menu_intro_video.frames >= 608:
				self.main_menu_intro_video.restart()	

			screen.blit(self.menu_gui, (self.menu_gui_middle_x, self.menu_gui_middle_y))

			if self.hovered_button != 'none':
				if self.hovered_button == 'start':
					screen.blit(self.hovered_green_button_menu_image, self.start_button.rect)
				elif self.hovered_button == 'quit':
					screen.blit(self.hovered_red_button_menu_image, self.quit_button.rect)
				elif self.hovered_button == 'options':
					screen.blit(self.hovered_green_button_menu_image, self.options_button.rect)
			else:
				self.hover_over_button_sound.fadeout(200)
		else:
			screen.blit(self.new_game_menu_background, (self.new_game_menu_background_middle_x, self.new_game_menu_background_middle_y))
			if self.hovered_button != 'none':
				if self.hovered_button == 'new_game':
					screen.blit(self.hovered_green_button_menu_image, self.new_game_button.rect)
				elif self.hovered_button == 'load_save':
					screen.blit(self.hovered_green_button_menu_image, self.load_save_button.rect)
				elif self.hovered_button == 'back':
					screen.blit(self.hovered_red_button_menu_image, self.back_button.rect)										
			else:
				self.hover_over_button_sound.fadeout(200)

#----------------------------------------------------#

class Scenario_Selection_Menu:
	def __init__(self, screen_width, screen_height, pygame, game_logo, python_logo, menu_gui, hovered_select_scenario_button_menu_image, hovered_back_button_menu_image,
	      	 hover_over_button_sound, generic_click_menu_sound) -> None:
		
		self.hovered_button = 'none'
		self.last_hovered_button ='none'
		
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y

		self.screen_height = screen_height

		self.python_logo = python_logo
		self.python_logo = pygame.transform.smoothscale_by(self.python_logo, (self.factor_x,self. factor_y))		

		self.game_logo = game_logo
		self.game_logo = pygame.transform.smoothscale_by(self.game_logo, (self.factor_x,self. factor_y))		

		self.menu_gui = pygame.transform.smoothscale_by(menu_gui, (self.factor_x,self. factor_y))
		self.hovered_select_scenario_button_menu_image = pygame.transform.smoothscale_by(hovered_select_scenario_button_menu_image, (self.factor_x, self.factor_y))
		self.hovered_back_button_menu_image = pygame.transform.smoothscale_by(hovered_back_button_menu_image, (self.factor_x, self.factor_y))

		menu_gui_width = self.menu_gui.get_width()
		menu_gui_height = self.menu_gui.get_height()
		
		self.menu_gui_middle_x = (screen_width/2 - menu_gui_width/2)
		self.menu_gui_middle_y = (screen_height - menu_gui_height) / 1.3

		start_button_width = 205 * self.factor_x
		start_button_height = 43 * self.factor_y
		start_button_x_offset = 470 * self.factor_x
		start_button_y_offset = 673 * self.factor_y
		self.start_button = GenericUtilitys.Button(self.menu_gui_middle_x + start_button_x_offset, self.menu_gui_middle_y + start_button_y_offset, start_button_width, start_button_height)	

		back_button_width = 205 * self.factor_x
		back_button_height = 43 * self.factor_y
		back_button_x_offset = 51 * self.factor_x
		back_button_y_offset = 673 * self.factor_y
		self.back_button = GenericUtilitys.Button(self.menu_gui_middle_x + back_button_x_offset, self.menu_gui_middle_y + back_button_y_offset, back_button_width, back_button_height)	

		self.hover_over_button_sound = hover_over_button_sound

		self.click_menu_sound = generic_click_menu_sound


	def get_button_by_interaction(self, mouse_rect):
		if self.start_button.rect.colliderect(mouse_rect):
			return 'start'
		elif self.back_button.rect.colliderect(mouse_rect):
			return 'back'
		else:
			return None


	def get_clicked_button(self, mouse_rect):
		clicked_button = self.get_button_by_interaction(mouse_rect)
		if clicked_button != None:
			self.hover_over_button_sound.fadeout(150)
			self.click_menu_sound.play()
		return clicked_button


	def get_hovered_button(self, mouse_rect):
		hovered_button = self.get_button_by_interaction(mouse_rect)
		if self.hovered_button != None:
			if self.hovered_button != self.last_hovered_button:
				self.hover_over_button_sound.play()
				self.last_hovered_button = self.hovered_button	
		else:
			self.last_hovered_button = self.hovered_button
		return hovered_button


	def draw(self, screen):
		screen.blit(self.menu_gui, (self.menu_gui_middle_x, self.menu_gui_middle_y))

		screen.blit(self.python_logo, (0, self.screen_height - self.python_logo.get_height()))		

		screen.blit(self.game_logo, (60 * self.factor_x,  20 * self.factor_y))

		if self.hovered_button != 'none':
			if self.hovered_button == 'start':
				screen.blit(self.hovered_select_scenario_button_menu_image, self.start_button.rect)
			if self.hovered_button == 'back':
				screen.blit(self.hovered_back_button_menu_image, self.back_button.rect)
		else:
			self.hover_over_button_sound.fadeout(200)	

#----------------------------------------------------#

class Country_Selection_Screen:
	def __init__(self,
				screen_width, screen_height, pygame, countries, generic_hover_over_button_sound, generic_click_button_sound, 
				country_selection_background, country_info_display_background, political_compass_image, ideologies_CRT_overlay_effect,
				hovered_start_game_button, hovered_select_national_spirit_button_image, hovered_select_country_button_image, 
				generic_leader, CRT_flag_overlay_effect, blocked_select_national_spirit_button, blocked_select_country_button, blocked_start_game_button,
				blocked_full_right_side, blocked_all_laws, national_spirits_background, generic_national_spirits, progressbar, progressbar_vertical,
				progressbar_small, progressbar_huge, selected_law_background, laws_description_image):	
		
		self.Country_Selection_Menu = Country_Selection_Menu(
				screen_width, screen_height, pygame, generic_hover_over_button_sound, generic_click_button_sound, 
				country_selection_background, political_compass_image, ideologies_CRT_overlay_effect,
				hovered_start_game_button, hovered_select_national_spirit_button_image, hovered_select_country_button_image, 
				generic_leader, CRT_flag_overlay_effect, blocked_select_national_spirit_button, 
				blocked_select_country_button, blocked_start_game_button, blocked_full_right_side, blocked_all_laws, progressbar, progressbar_vertical,
				progressbar_small, progressbar_huge)		
		
		self.Flag_Selection_Menu = Flag_Selection_Menu(screen_width, screen_height, pygame, countries, 
				generic_hover_over_button_sound, generic_click_button_sound, country_info_display_background)
		
		self.National_Spirits_Selection_Menu = National_Spirits_Selection_Menu(screen_width, screen_height,
				national_spirits_background, generic_national_spirits, generic_hover_over_button_sound, generic_click_button_sound)
		
		self.Laws_Group_Menu = Laws_Group_Menu(screen_width, screen_height, pygame, generic_hover_over_button_sound, generic_click_button_sound, selected_law_background,
				laws_description_image)
		
		self.selected_flag_image = None

	def get_clicked_button(self, mouse_rect):
		if self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == False and self.Country_Selection_Menu.is_laws_group_menu_open == False:
			clicked_button = self.Country_Selection_Menu.get_clicked_ideology(mouse_rect)
			if clicked_button != None:
				return clicked_button			
		
			clicked_button = self.Flag_Selection_Menu.get_clicked_button(mouse_rect)
			if clicked_button != None:
				pygame.mixer.music.fadeout(200)
				self.Flag_Selection_Menu.flag_rects = []
				self.Country_Selection_Menu.is_flag_selection_menu_open = False
				self.selected_flag_image = clicked_button
				self.Country_Selection_Menu.selected_flag_image = self.selected_flag_image
				self.Country_Selection_Menu.selected_selectable_national_spirits = []
				self.National_Spirits_Selection_Menu.selected_country = self.Flag_Selection_Menu.selected_country		
				self.Country_Selection_Menu.selected_country = self.Flag_Selection_Menu.selected_country	
				self.Laws_Group_Menu.selected_country = self.Flag_Selection_Menu.selected_country	
				return clicked_button
			
		clicked_button = self.Country_Selection_Menu.get_clicked_button(mouse_rect)
		self.Laws_Group_Menu.opened_law_group = self.Country_Selection_Menu.clicked_law_group
		if clicked_button != None and self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == False and self.Country_Selection_Menu.is_laws_group_menu_open == False and clicked_button != 'select_country':
			return clicked_button		
		
		if self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == True:
			clicked_button = self.National_Spirits_Selection_Menu.get_clicked_national_spirit(mouse_rect)
			if clicked_button != None:
				return clicked_button

		if self.Country_Selection_Menu.is_laws_group_menu_open == True:
			clicked_button = self.Laws_Group_Menu.get_clicked_button(mouse_rect)
			if clicked_button == 'close':
				self.Country_Selection_Menu.is_laws_group_menu_open = False
				self.Laws_Group_Menu.last_hovered_rect = None
			return clicked_button

	def get_hovered_button(self, mouse_rect):	
		hovered_button = self.Country_Selection_Menu.get_hovered_button(mouse_rect)
		if hovered_button != None:
			return hovered_button	
		
		if self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == False and self.Country_Selection_Menu.is_laws_group_menu_open == False:
			hovered_button = self.Country_Selection_Menu.get_hovered_ideology_rect(mouse_rect)
			if hovered_button != None:
				self.Country_Selection_Menu.hovered_ideology_rect = hovered_button
				self.Flag_Selection_Menu.hovered_ideology_rect = hovered_button
				return hovered_button	

		hovered_button = self.Country_Selection_Menu.get_hovered_national_spirit(mouse_rect)
		if hovered_button != None:
			self.Country_Selection_Menu.hovered_national_spirit = hovered_button
			return hovered_button
		else:
			self.Country_Selection_Menu.hovered_national_spirit = hovered_button				

		if self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == True:
			hovered_button = self.National_Spirits_Selection_Menu.get_hovered_national_spirit(mouse_rect)
			if hovered_button != None:
				self.National_Spirits_Selection_Menu.hovered_national_spirit = hovered_button
				return hovered_button
			else:
				self.National_Spirits_Selection_Menu.hovered_national_spirit = hovered_button
		
		if self.Country_Selection_Menu.is_laws_group_menu_open == True:
			hovered_rect = self.Laws_Group_Menu.get_hovered_rect(mouse_rect)
	
	def music_player(self):
		if pygame.mixer.music.get_busy() == False and self.selected_flag_image != None:
			self.main_menu_music_started = True
			pygame.mixer.music.load(self.Flag_Selection_Menu.selected_country.country_music_playlist[0])
			pygame.mixer.music.play()

	def draw(self, screen, mouse_pos, mouse_rect):
		self.Country_Selection_Menu.draw(screen, mouse_rect)

		if self.Country_Selection_Menu.hovered_ideology_rect != None:
			self.Flag_Selection_Menu.draw_flag_selection_preview(screen, self.Country_Selection_Menu.last_hovered_ideology, mouse_pos)

		if self.Country_Selection_Menu.is_flag_selection_menu_open == True:
			self.Flag_Selection_Menu.draw(screen, self.Country_Selection_Menu.clicked_ideology, mouse_rect)

		if self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == True:
			self.National_Spirits_Selection_Menu.draw(screen)		

		if self.Country_Selection_Menu.is_laws_group_menu_open == True:		
			self.Laws_Group_Menu.draw(screen)				

class Country_Selection_Menu:
	def __init__(self, screen_width, screen_height, pygame, 
		generic_hover_over_button_sound, generic_click_menu_sound, country_selection_background, political_compass_image, 
		ideologies_CRT_overlay_effect, hovered_start_game_button, hovered_select_national_spirit_button_image, hovered_select_country_button_image,
		generic_leader, CRT_flag_overlay_effect, blocked_select_national_spirit_button, blocked_select_country_button, blocked_start_game_button, 
		blocked_full_right_side, blocked_all_laws, progressbar, progressbar_vertical, progressbar_small, progressbar_huge):
		
		self.national_spirits_display_rects = []
		self.hovered_national_spirit = None
		self.last_hovered_national_spirit = None

		self.selected_country: CountriesManager.Country = None

		self.selected_selectable_national_spirits = []

		self.mouse_pos = [0, 0]
		
		self.clicked_law_group = None

		self.hovered_ideology_rect = None
		self.last_hovered_ideology = None
		
		self.hovered_button = None
		self.last_hovered_button = None
		
		self.is_flag_selection_menu_open = False
		self.selected_flag_image = None

		self.is_flag_national_spirits_selection_menu_open = False
		self.is_laws_group_menu_open = False
		
		self.screen_width = screen_width 
		self.screen_height = screen_height
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y
		self.factor = self.factor_x * self.factor_y

		self.pygame = pygame


		self.progressbar_huge = pygame.transform.smoothscale_by(progressbar_huge, (self.factor_x, self.factor_y))
		self.progressbar = pygame.transform.smoothscale_by(progressbar, (self.factor_x, self.factor_y))
		self.progressbar_vertical = pygame.transform.smoothscale_by(progressbar_vertical, (self.factor_x, self.factor_y))
		self.progressbar_small = pygame.transform.smoothscale_by(progressbar_small, (self.factor_x, self.factor_y))

		self.country_selection_background = pygame.transform.smoothscale_by(country_selection_background, (self.factor_x, self.factor_y))
		self.political_compass_image = pygame.transform.smoothscale_by(political_compass_image, (self.factor_x, self.factor_y))
		self.ideologies_CRT_overlay_effect = pygame.transform.smoothscale_by(ideologies_CRT_overlay_effect, (self.factor_x, self.factor_y))
		self.CRT_flag_overlay_effect = pygame.transform.smoothscale_by(CRT_flag_overlay_effect, (self.factor_x, self.factor_y))

		self.hovered_start_game_button = pygame.transform.smoothscale_by(hovered_start_game_button, (self.factor_x, self.factor_y))
		self.hovered_select_national_spirit_button_image = pygame.transform.smoothscale_by(hovered_select_national_spirit_button_image, (self.factor_x, self.factor_y))
		self.hovered_select_country_button_image = pygame.transform.smoothscale_by(hovered_select_country_button_image, (self.factor_x, self.factor_y))

		self.blocked_select_national_spirit_button = pygame.transform.smoothscale_by(blocked_select_national_spirit_button, (self.factor_x, self.factor_y))
		self.blocked_select_country_button = pygame.transform.smoothscale_by(blocked_select_country_button, (self.factor_x, self.factor_y))
		self.blocked_start_game_button = pygame.transform.smoothscale_by(blocked_start_game_button, (self.factor_x, self.factor_y))

		self.blocked_full_right_side = pygame.transform.smoothscale_by(blocked_full_right_side, (self.factor_x, self.factor_y))
		self.blocked_all_laws = pygame.transform.smoothscale_by(blocked_all_laws, (self.factor_x, self.factor_y))

		self.generic_leader_image = generic_leader
		self.selected_leader_image = self.generic_leader_image
		
		political_compass_image_rect = self.political_compass_image.get_rect()
		political_compass_image_rect[0] += 15 * self.factor_x
		political_compass_image_rect[1] += 31 * self.factor_y
		#self.Country_Selection_National_Spirits_Selection_Menu.background_position = [political_compass_image_rect[0]*0.65, political_compass_image_rect[1]*0.95]

		self.leader_portrait_position = (1059 * self.factor_x, 29 * self.factor_y)
		self.country_flag_position = (1209 * self.factor_x, 94 * self.factor_y)

		self.country_name_position = (1212 * self.factor_x, 41 * self.factor_y)
		self.leader_name_position = (1071 * self.factor_x, 222 * self.factor_y)

		self.national_spirits_position = [1437*self.factor_x, 104*self.factor_y]

		#### MAIN BUTTONS
		start_game_button_width = 268 * self.factor_x
		start_game_button_height = 70 * self.factor_y
		self.start_game_button_x_offset = 1639 * self.factor_x
		self.start_game_button_y_offset = 248 * self.factor_y		
		self.start_game_button = GenericUtilitys.Button(self.start_game_button_x_offset, self.start_game_button_y_offset, start_game_button_width, start_game_button_height)	

		select_national_spirit_button_width = 211 * self.factor_x
		select_national_spirit_button_height = 70 * self.factor_y
		self.select_national_spirit_button_x_offset = 1424 * self.factor_x
		self.select_national_spirit_button_y_offset = 248 * self.factor_y		
		self.select_national_spirit_button = GenericUtilitys.Button(self.select_national_spirit_button_x_offset, self.select_national_spirit_button_y_offset, select_national_spirit_button_width, select_national_spirit_button_height)	

		select_country_button_width = 362 * self.factor_x
		select_country_button_height = 70 * self.factor_y
		self.select_country_button_x_offset = 1059 * self.factor_x
		self.select_country_button_y_offset = 248 * self.factor_y		
		self.select_country_button = GenericUtilitys.Button(self.select_country_button_x_offset, self.select_country_button_y_offset, select_country_button_width, select_country_button_height)					
		####

		#### LAWS BUTTONS
		law_button_width = 208 * self.factor_x
		law_button_height = 27 * self.factor_y		


		### FIRST ROW
		self.first_row_law_button_y_offset_1 = 428 * self.factor_y
		self.first_row_law_button_y_offset_2 = 461 * self.factor_y
		self.first_row_law_button_y_offset_3 = 494 * self.factor_y
		self.first_row_law_button_y_offset_4 = 527 * self.factor_y
		self.first_row_law_button_y_offset_5 = 560 * self.factor_y
		self.first_row_law_button_y_offset_6 = 593 * self.factor_y
		self.first_row_law_button_y_offset_7 = 626 * self.factor_y
		self.first_row_law_button_y_offset_8 = 659 * self.factor_y
		self.first_row_law_button_y_offset_9 = 692 * self.factor_y	
		
		## POLITICAL LAWS
		self.political_law_button_x_offset = 1269 * self.factor_x
		
		self.political_law_button_1 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.political_law_button_2 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.political_law_button_3 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.political_law_button_4 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.political_law_button_5 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.political_law_button_6 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.political_law_button_7 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.political_law_button_8 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_8, law_button_width, law_button_height)
		self.political_law_button_9 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_9, law_button_width, law_button_height)				
		##

		## MILITARY LAWS
		self.military_law_button_x_offset = 1701 * self.factor_x

		self.military_law_button_1 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.military_law_button_2 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.military_law_button_3 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.military_law_button_4 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.military_law_button_5 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.military_law_button_6 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.military_law_button_7 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.military_law_button_8 = GenericUtilitys.Button(self.military_law_button_x_offset, 672 * self.factor_y, law_button_width, law_button_height)		
		##
		###

		### SECOND ROW
		self.second_row_law_button_y_offset_1 = 779 * self.factor_y
		self.second_row_law_button_y_offset_2 = 812 * self.factor_y
		self.second_row_law_button_y_offset_3 = 845 * self.factor_y
		self.second_row_law_button_y_offset_4 = 878 * self.factor_y
		self.second_row_law_button_y_offset_5 = 911 * self.factor_y
		self.second_row_law_button_y_offset_6 = 944 * self.factor_y
		self.second_row_law_button_y_offset_7 = 977 * self.factor_y
		self.second_row_law_button_y_offset_8 = 1010 * self.factor_y
		self.second_row_law_button_y_offset_9 = 1043 * self.factor_y	
		
		## ECONOMIC LAWS
		self.economical_law_button_x_offset = 1269 * self.factor_x
		
		self.economical_law_button_1 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.economical_law_button_2 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.economical_law_button_3 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.economical_law_button_4 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.economical_law_button_5 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.economical_law_button_6 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.economical_law_button_7 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.economical_law_button_8 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_8, law_button_width, law_button_height)
		self.economical_law_button_9 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_9, law_button_width, law_button_height)				
		##

		## SOCIAL LAWS
		self.social_law_button_x_offset = 1701 * self.factor_x

		self.social_law_button_1 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.social_law_button_2 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.social_law_button_3 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.social_law_button_4 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.social_law_button_5 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.social_law_button_6 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.social_law_button_7 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.social_law_button_8 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_8, law_button_width, law_button_height)
		self.social_law_button_9 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_9, law_button_width, law_button_height)			


		# INFORMATION ------------#

		self.hovering_diplomatic_information_rect = False
		self.hovering_military_information_rect = False
		self.hovering_economic_information_rect = False
		self.hovering_domestic_information_rect = False	

		size_x = 168 * self.factor_x
		size_y = 13 * self.factor_y		

		self.diplomatic_information_rect = 	self.pygame.Rect(1568 * self.factor_x, 325 * self.factor_y, size_x, size_y)
		self.military_information_rect = 	self.pygame.Rect(1568 * self.factor_x, 344 * self.factor_y, size_x, size_y)
		self.economic_information_rect = 	self.pygame.Rect(1744 * self.factor_x, 325 * self.factor_y, 160 * self.factor_x, size_y)
		self.domestic_information_rect = 	self.pygame.Rect(1744 * self.factor_x, 344 * self.factor_y, 160 * self.factor_x, size_y)			


		self.hovering_military_approval_rating_rect = False
		self.hovering_domestic_approval_rating_rect = False
		self.hovering_midia_approval_rating_rect = False
		self.hovering_secret_service_approval_rating_rect = False
		self.hovering_politics_approval_rating_rect = False
		
		self.hovering_internal_and_external_market_approval_rating_rect = False

		size_x = 43 * self.factor_x
		size_y = 25 * self.factor_y
		height = 349 * self.factor_y

		self.military_approval_rating_rect = 		self.pygame.Rect(1063 * self.factor_x, height, size_x, size_y)
		self.domestic_approval_rating_rect = 		self.pygame.Rect(1140 * self.factor_x, height, size_x, size_y)
		self.midia_approval_rating_rect = 			self.pygame.Rect(1217 * self.factor_x, height, size_x, size_y)
		self.secret_service_approval_rating_rect = 	self.pygame.Rect(1294 * self.factor_x, height, size_x, size_y)
		self.politics_approval_rating_rect = 		self.pygame.Rect(1371 * self.factor_x, height, size_x, size_y)

		self.internal_and_external_market_approval_rating_rect = self.pygame.Rect(1451 * self.factor_x, 346 * self.factor_y, 101 * self.factor_x, 28 * self.factor_y)	

		# INFORMATION ------------#


		self.hover_over_button_sound = generic_hover_over_button_sound

		self.click_menu_sound = generic_click_menu_sound

		self.clicked_ideology = None
		self.clicked_ideology_rect = None
		self.ideology_rects = {
			#
			'Marxist_Leninism': pygame.Rect(0, 0, 95, 97),
			'Command_Socialism': pygame.Rect(98, 0, 201, 97),
			'National_Syndicalism': pygame.Rect(304, 0, 406, 97),
			'Corporautocracy': pygame.Rect(714, 0, 194, 97),
			'Absolute_Monarchism': pygame.Rect(911, 0, 105, 97),		
			#

			##
			'Consumer_Socialism': pygame.Rect(0, 102, 299, 200),
			'Authoritarian_Market_Socialism': pygame.Rect(304, 102, 202, 200),
			'Social_Statism': pygame.Rect(510, 102, 200, 151),
			'Pinochetism': pygame.Rect(714, 102, 302, 151),				
			##

			###
			'Democratic_Socialism': pygame.Rect(0, 305, 299, 405),
			'Social_Democracy': pygame.Rect(304, 305, 202, 405),
			'Keynesianism': pygame.Rect(510, 258, 200, 248),
			#'Chicago_School': pygame.Rect(714, 258, 302, 248),				
			###		

			####
			'Social_Liberalism': pygame.Rect(510, 511, 200, 199),
			#'Classical_Liberalism': pygame.Rect(714, 511, 302, 199),			
			####			

			#####
			#'Libertarian_Socialism': pygame.Rect(0, 715, 299, 205),
			#'Libertarian_Market_Socialism': pygame.Rect(304, 715, 202, 205),
			#'Social_Libertarianism': pygame.Rect(510, 715, 200, 205),
			'Libertarian_Capitalism': pygame.Rect(714, 715, 302, 99),
			#'Minarcho_Capitalism': pygame.Rect(714, 818, 302, 102),								
			#####
			
			######
			#'Anarcho_Communism': pygame.Rect(0, 924, 299, 92),
			#'Mutualism': pygame.Rect(304, 924, 202, 92),
			#'Voluntaryism': pygame.Rect(510, 924, 251, 92),
			'Anarcho_Capitalism': pygame.Rect(766, 924, 250, 92)
			######			
		}	

		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(13 * self.factor_y))	

	def get_button_by_interaction(self, mouse_rect):
		if self.start_game_button.rect.colliderect(mouse_rect) and self.selected_country != None:
			return 'start_game'
		elif self.select_national_spirit_button.rect.colliderect(mouse_rect) and self.selected_country != None:
			return 'select_national_spirit'
		elif self.select_country_button.rect.colliderect(mouse_rect):
			return 'select_country'				
		elif self.selected_country != None:
			
			for number in range(9):
				button = getattr(self, f'political_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					return f'political_{str(number+1)}'
			
			for number in range(8):
				button = getattr(self, f'military_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					return f'military_{str(number+1)}'	

			for number in range(9):
				button = getattr(self, f'economical_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					return f'economical_{str(number+1)}'
			
			for number in range(9):
				button = getattr(self, f'social_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					return f'social_{str(number+1)}'						

		return None

	def get_clicked_button(self, mouse_rect):
		clicked_button = self.get_button_by_interaction(mouse_rect)
		if self.is_flag_selection_menu_open == False:
			if clicked_button != None:
				self.hover_over_button_sound.fadeout(50)
				self.click_menu_sound.play()
				self.clicked_law_group = None

				if clicked_button == 'select_national_spirit' and self.is_flag_selection_menu_open == False and self.is_laws_group_menu_open == False:
					self.is_flag_national_spirits_selection_menu_open = not self.is_flag_national_spirits_selection_menu_open

				elif clicked_button == 'start_game':
					pass

				elif self.is_flag_selection_menu_open == False and self.is_flag_national_spirits_selection_menu_open == False and not (clicked_button == 'select_country' or clicked_button == 'select_national_spirit' or clicked_button == 'start_game'):
					if self.is_laws_group_menu_open == False:
						self.is_laws_group_menu_open = True
						self.clicked_law_group = clicked_button
					else:
						self.clicked_law_group = clicked_button

		if clicked_button == 'select_country' and self.is_flag_national_spirits_selection_menu_open == False and self.is_laws_group_menu_open == False:
			self.is_flag_selection_menu_open = not self.is_flag_selection_menu_open
			
		return clicked_button
	def get_clicked_ideology(self, mouse_rect):
		if self.is_flag_selection_menu_open == False:
			for ideology, rect in self.ideology_rects.items():
				rect = pygame.Rect(rect[0]*self.factor_x + 15 * self.factor_x, rect[1]*self.factor_y + 31 * self.factor_y, rect[2]*self.factor_x, rect[3]*self.factor_y)
				if rect.colliderect(mouse_rect):
					self.clicked_ideology = ideology
					self.clicked_ideology_rect = rect
					self.selected_country = None
					self.hover_over_button_sound.fadeout(50)
					self.click_menu_sound.play()					
					return self.clicked_ideology
	
	def get_hovered_button(self, mouse_rect):
		if self.is_flag_selection_menu_open == False:
			self.hovered_button = self.get_button_by_interaction(mouse_rect)

			if self.hovered_button != None:
				self.hovered_rect = None
				self.hovering_diplomatic_information_rect = False
				self.hovering_military_information_rect = False
				self.hovering_economic_information_rect = False
				self.hovering_domestic_information_rect = False	
				self.hovering_internal_and_external_market_approval_rating_rect = False
				self.hovering_military_approval_rating_rect = False
				self.hovering_domestic_approval_rating_rect = False
				self.hovering_midia_approval_rating_rect = False
				self.hovering_secret_service_approval_rating_rect = False
				self.hovering_politics_approval_rating_rect = False					
				if self.hovered_button != self.last_hovered_button:
					self.hover_over_button_sound.play()
					self.last_hovered_button = self.hovered_button
					return self.hovered_button
			else:
				self.last_hovered_button = None			
				
				self.hovering_diplomatic_information_rect = False
				self.hovering_military_information_rect = False
				self.hovering_economic_information_rect = False
				self.hovering_domestic_information_rect = False	
				self.hovering_internal_and_external_market_approval_rating_rect = False
				self.hovering_military_approval_rating_rect = False
				self.hovering_domestic_approval_rating_rect = False
				self.hovering_midia_approval_rating_rect = False
				self.hovering_secret_service_approval_rating_rect = False
				self.hovering_politics_approval_rating_rect = False	

				self.hovered_rect = None
				if self.diplomatic_information_rect.colliderect(mouse_rect):
					self.hovered_rect = 1
					self.hovering_diplomatic_information_rect = True
				elif self.military_information_rect.colliderect(mouse_rect):	
					self.hovered_rect = 2
					self.hovering_military_information_rect = True
				elif self.economic_information_rect.colliderect(mouse_rect):
					self.hovered_rect = 3	
					self.hovering_economic_information_rect = True
				elif self.domestic_information_rect.colliderect(mouse_rect):
					self.hovered_rect = 4									
					self.hovering_domestic_information_rect = True

				elif self.internal_and_external_market_approval_rating_rect.colliderect(mouse_rect):
					self.hovered_rect = 5
					self.hovering_internal_and_external_market_approval_rating_rect = True

				elif self.military_approval_rating_rect.colliderect(mouse_rect):
					self.hovered_rect = 6
					self.hovering_military_approval_rating_rect = True
				elif self.domestic_approval_rating_rect.colliderect(mouse_rect):
					self.hovered_rect = 7
					self.hovering_domestic_approval_rating_rect = True
				elif self.midia_approval_rating_rect.colliderect(mouse_rect):
					self.hovered_rect = 8
					self.hovering_midia_approval_rating_rect = True
				elif self.secret_service_approval_rating_rect.colliderect(mouse_rect):
					self.hovered_rect = 9
					self.hovering_secret_service_approval_rating_rect = True
				elif self.politics_approval_rating_rect.colliderect(mouse_rect):	
					self.hovered_rect = 10											
					self.hovering_politics_approval_rating_rect = True

				if self.hovered_rect != None:
					if self.last_hovered_rect != self.hovered_rect:
						self.hover_over_button_sound.play()
						self.last_hovered_rect = self.hovered_rect
				else:
					self.last_hovered_rect = None										
					self.hover_over_button_sound.fadeout(100)				

				return self.hovered_rect
	def get_hovered_ideology_rect(self, mouse_rect):
		if self.is_flag_selection_menu_open == False:
			for ideology, rect in self.ideology_rects.items():
				rect = pygame.Rect(rect[0]*self.factor_x + 15 * self.factor_x, rect[1]*self.factor_y + 31 * self.factor_y, rect[2]*self.factor_x, rect[3]*self.factor_y)
				if rect.colliderect(mouse_rect) and ideology != self.last_hovered_ideology:
					self.last_hovered_ideology = ideology
					self.hover_over_button_sound.play()
					return rect
				elif rect.colliderect(mouse_rect):
					return rect

			self.hovered_ideology_rect = None
	def get_hovered_national_spirit(self, mouse_rect):
		if self.is_flag_selection_menu_open == False:
			for rect, national_spirit in self.national_spirits_display_rects:
				if rect.colliderect(mouse_rect):
					if national_spirit != self.last_hovered_national_spirit:
						self.last_hovered_national_spirit = national_spirit
						self.hover_over_button_sound.play()
					return national_spirit
			return None

	def draw(self, screen, mouse_rect):
		screen.blit(self.political_compass_image, (15 * self.factor_x, 31 * self.factor_y))
		
		# Leader Portrait
		if self.selected_country != None and self.is_flag_selection_menu_open == False:
			self.selected_leader_image = self.selected_country.country_leader_image
			screen.blit(self.selected_leader_image, self.leader_portrait_position)
		else:
			screen.blit(self.generic_leader_image, self.leader_portrait_position)
		
		# Flag
		if self.selected_country != None:
			screen.blit(self.selected_flag_image, self.country_flag_position)	
			screen.blit(self.CRT_flag_overlay_effect, self.country_flag_position)	
		
		# BEHIND BACKGROUND
		screen.blit(self.country_selection_background, (0, 0))
		# IN FRONT OF BACKGROUND

		# Country Name | Leader Name | National Spirits
		if self.is_flag_selection_menu_open == False and self.selected_flag_image != None:
			if self.selected_country != None:
				country_name_text = self.medium_scalable_font.render(self.selected_country.country_name, True, (255, 255, 255))
				screen.blit(country_name_text, self.country_name_position)	

				leader_name = self.selected_country.country_leader_name
				leader_name_text = self.big_scalable_font.render(leader_name, True, (255, 255, 255))

				if leader_name_text.get_width() > 350 * self.factor_x:
					leader_name_text = self.medium_scalable_font.render(leader_name, True, (255, 255, 255))
				
				screen.blit(leader_name_text, self.leader_name_position)

				# LAWS PROGRESS BAR	
				for number in range(9):
					button = getattr(self, f'political_law_button_{str(number+1)}', None)
					law_rating = int((self.progressbar_huge.get_width()/100) * self.selected_country.political_laws_groups[number].active_law_rating)
					screen.blit(self.progressbar_huge.subsurface((0, 0, law_rating, self.progressbar_huge.get_height())), (button.rect[:2]))
				
				for number in range(8):
					button = getattr(self, f'military_law_button_{str(number+1)}', None)
					law_rating = int((self.progressbar_huge.get_width()/100) * self.selected_country.military_laws_groups[number].active_law_rating)
					screen.blit(self.progressbar_huge.subsurface((0, 0, law_rating, self.progressbar_huge.get_height())), (button.rect[:2]))	
				
				for number in range(9):
					button = getattr(self, f'economical_law_button_{str(number+1)}', None)
					law_rating = int((self.progressbar_huge.get_width()/100) * self.selected_country.economical_laws_groups[number].active_law_rating)
					screen.blit(self.progressbar_huge.subsurface((0, 0, law_rating, self.progressbar_huge.get_height())), (button.rect[:2]))
				
				for number in range(9):
					button = getattr(self, f'social_law_button_{str(number+1)}', None)
					law_rating = int((self.progressbar_huge.get_width()/100) * self.selected_country.social_laws_groups[number].active_law_rating)
					screen.blit(self.progressbar_huge.subsurface((0, 0, law_rating, self.progressbar_huge.get_height())), (button.rect[:2]))				

				#----------------------------------------------------------------------------------------------------------------------------------------#
				# COUNTRY INFOS
					
				diplomacy_rating = int((self.progressbar.get_width()/100) * self.selected_country.diplomacy_rating)
				screen.blit(self.progressbar.subsurface((0, 0, diplomacy_rating, self.progressbar.get_height())), (1643 * self.factor_x, 327 * self.factor_y))

				military_rating = int((self.progressbar.get_width()/100) * self.selected_country.military_rating)	
				screen.blit(self.progressbar.subsurface((0, 0, military_rating, self.progressbar.get_height())), (1643 * self.factor_x, 346 * self.factor_y))
				
				economy_rating = int((self.progressbar.get_width()/100) * self.selected_country.economy_rating)
				screen.blit(self.progressbar.subsurface((0, 0, economy_rating, self.progressbar.get_height())), (1811 * self.factor_x, 327 * self.factor_y))

				domestic_rating = int((self.progressbar.get_width()/100) * self.selected_country.domestic_rating)	
				screen.blit(self.progressbar.subsurface((0, 0, domestic_rating, self.progressbar.get_height())), (1811 * self.factor_x, 346 * self.factor_y))	


				internal_economy_rating = int((self.progressbar_small.get_width()/100) * self.selected_country.internal_economy_rating)
				screen.blit(self.progressbar_small.subsurface((0, 0, internal_economy_rating, self.progressbar_small.get_height())), (1483 * self.factor_x, 349 * self.factor_y))

				external_economy_rating = int((self.progressbar_small.get_width()/100) * self.selected_country.external_economy_rating)	
				screen.blit(self.progressbar_small.subsurface((0, 0, external_economy_rating, self.progressbar_small.get_height())), (1483 * self.factor_x, 364 * self.factor_y))

					# 	VERTICAL
				height = 350 * self.factor_y
				military_approval_rating = int((self.progressbar_vertical.get_height()/100) * self.selected_country.military_approval_rating)	
				screen.blit(self.progressbar_vertical.subsurface((0, self.progressbar_vertical.get_height() - military_approval_rating, self.progressbar_vertical.get_width(), military_approval_rating)), (1100 * self.factor_x, height + self.progressbar_vertical.get_height() - military_approval_rating))

				domestic_approval_rating = int((self.progressbar_vertical.get_height()/100) * self.selected_country.domestic_approval_rating)	
				screen.blit(self.progressbar_vertical.subsurface((0, self.progressbar_vertical.get_height() - domestic_approval_rating, self.progressbar_vertical.get_width(), domestic_approval_rating)), (1177 * self.factor_x, height + self.progressbar_vertical.get_height() - domestic_approval_rating))
				
				midia_approval_rating = int((self.progressbar_vertical.get_height()/100) * self.selected_country.midia_approval_rating)
				screen.blit(self.progressbar_vertical.subsurface((0, self.progressbar_vertical.get_height() - midia_approval_rating, self.progressbar_vertical.get_width(), midia_approval_rating)), (1254 * self.factor_x, height + self.progressbar_vertical.get_height() - midia_approval_rating))

				secret_service_approval_rating = int((self.progressbar_vertical.get_height()/100) * self.selected_country.secret_service_approval_rating)	
				screen.blit(self.progressbar_vertical.subsurface((0, self.progressbar_vertical.get_height() - secret_service_approval_rating, self.progressbar_vertical.get_width(), secret_service_approval_rating)), (1331 * self.factor_x, height + self.progressbar_vertical.get_height() - secret_service_approval_rating))	

				politics_approval_rating = int((self.progressbar_vertical.get_height()/100) * self.selected_country.politics_approval_rating)	
				screen.blit(self.progressbar_vertical.subsurface((0, self.progressbar_vertical.get_height() - politics_approval_rating, self.progressbar_vertical.get_width(), politics_approval_rating)), (1408 * self.factor_x, height + self.progressbar_vertical.get_height() - politics_approval_rating))				

				self.info_height = 327 * self.factor_y
				## STABILITY
				text_country_stability = self.small_scalable_font.render(str(self.selected_country.country_stability)+'%', True, (255, 255, 255))
				text_country_stability_position = (1092 * self.factor_x, self.info_height)	
				screen.blit(text_country_stability, text_country_stability_position)
				## WAR SUPPORT
				text_country_war_support = self.small_scalable_font.render(str(self.selected_country.country_war_support)+'%', True, (255, 255, 255))
				text_country_war_support_position = (1192 * self.factor_x, self.info_height)	
				screen.blit(text_country_war_support, text_country_war_support_position)
				## PARTY POPULARITY
				text_country_party_popularity = self.small_scalable_font.render(str(self.selected_country.country_party_popularity)+'%', True, (255, 255, 255))
				text_country_party_popularity_position = (1277 * self.factor_x, self.info_height)	
				screen.blit(text_country_party_popularity, text_country_party_popularity_position)	

				## LAND MANPOWER
				manpower = self.selected_country.country_land_manpower
				if manpower >= 1000000:
					formatted_manpower = f'{manpower / 1000000:.1f} M'
				elif manpower >= 1000:
					formatted_manpower = f'{manpower / 1000:.1f} K'
				else:
					formatted_manpower = str(manpower)
			
				text_country_land_manpower = self.small_scalable_font.render(formatted_manpower, True, (255, 255, 255))
				text_country_land_manpower_position = (1373 * self.factor_x, self.info_height)	
				screen.blit(text_country_land_manpower, text_country_land_manpower_position)
				
				## AIR MANPOWER
				manpower = self.selected_country.country_air_manpower
				if manpower >= 1000000:
					formatted_manpower = f'{manpower / 1000000:.1f} M'
				elif manpower >= 1000:
					formatted_manpower = f'{manpower / 1000:.1f} K'
				else:
					formatted_manpower = str(manpower)

				text_country_air_manpower = self.small_scalable_font.render(formatted_manpower, True, (255, 255, 255))
				text_country_air_manpower_position = (1490 * self.factor_x, self.info_height)	
				screen.blit(text_country_air_manpower, text_country_air_manpower_position)

				## COUNTRY GDP
				GDP = self.selected_country.country_GDP
				if abs(GDP) < 1e6:
					formatted_GDP = f"${GDP:,.3f}"
				elif abs(GDP) < 1e9:
					formatted_GDP = f"${GDP / 1e6:.3f} M"
				elif abs(GDP) < 1e12:
					formatted_GDP = f"${GDP / 1e9:.3f} B"
				elif abs(GDP) < 1e15:
					formatted_GDP = f"${GDP / 1e12:.3f} T"
				else:
					formatted_GDP = f"${GDP:.3f}"
					
				text_country_GDP = self.small_scalable_font.render(formatted_GDP, True, (255, 255, 255))
				text_country_GDP_position = (1653 * self.factor_x, 360 * self.factor_y)	
				screen.blit(text_country_GDP, text_country_GDP_position)

				#----------------------------------------------------------------------------------------------------------------------------------------#

				self.national_spirits_display_rects = []
				x_index = 0
				y_index = 0
	
				if len(self.selected_country.country_national_spirits) > 10:
					for national_spirit in self.selected_country.country_national_spirits:
						scaled_national_spirit_icon = pygame.transform.scale_by(national_spirit.national_spirit_icon, 0.5)

						x_offset = scaled_national_spirit_icon.get_width() * 1.23
						y_offset = scaled_national_spirit_icon.get_height()
						
						screen.blit(scaled_national_spirit_icon, (self.national_spirits_position[0] + x_offset*x_index, self.national_spirits_position[1] + y_offset*y_index))
						
						national_spirit.rect = self.pygame.Rect(self.national_spirits_position[0] + x_offset*x_index, self.national_spirits_position[1] + y_offset*y_index,
															scaled_national_spirit_icon.get_width(), scaled_national_spirit_icon.get_height())
						self.national_spirits_display_rects.append([national_spirit.rect, national_spirit])	

						if x_index < 9:
							x_index += 1
						else:
							x_index = 0
							y_index += 1							
				else:	
					for national_spirit in self.selected_country.country_national_spirits:
						x_offset = national_spirit.national_spirit_icon.get_width() * 1.27
						y_offset = national_spirit.national_spirit_icon.get_height()					
						
						screen.blit(national_spirit.national_spirit_icon, (self.national_spirits_position[0] + x_offset*x_index, self.national_spirits_position[1] + y_offset*y_index))
						
						national_spirit.rect = self.pygame.Rect(self.national_spirits_position[0] + x_offset*x_index, self.national_spirits_position[1] + y_offset*y_index,
															national_spirit.national_spirit_icon.get_width(), national_spirit.national_spirit_icon.get_height())
						self.national_spirits_display_rects.append([national_spirit.rect, national_spirit])	

						if x_index < 4:
							x_index += 1
						else:
							x_index = 0
							y_index += 1


				# CULTURE
				culture_national_spirit = self.selected_country.country_culture
				screen.blit(culture_national_spirit.national_spirit_icon, (1838 * self.factor_x, 104 * self.factor_y))
				
				culture_national_spirit.rect = self.pygame.Rect(1838 * self.factor_x, 104 * self.factor_y,
						culture_national_spirit.national_spirit_icon.get_width(), culture_national_spirit.national_spirit_icon.get_height())					
				
				self.national_spirits_display_rects.append([culture_national_spirit.rect, culture_national_spirit])						
				
				# RELIGION	
				religion_national_spirit = self.selected_country.country_religion
				screen.blit(religion_national_spirit.national_spirit_icon, (1838 * self.factor_x, 104 * self.factor_y + religion_national_spirit.national_spirit_icon.get_height()))
				
				religion_national_spirit.rect = self.pygame.Rect(1838 * self.factor_x, 104 * self.factor_y + religion_national_spirit.national_spirit_icon.get_height(),
						religion_national_spirit.national_spirit_icon.get_width(), religion_national_spirit.national_spirit_icon.get_height())					
				
				self.national_spirits_display_rects.append([religion_national_spirit.rect, religion_national_spirit])	

				if self.hovering_diplomatic_information_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.diplomatic_information_rect, 2)
					hovering_diplomatic_information_description_title_text = self.small_scalable_font.render("DIPLOMATIC INFORMATION", True, (255, 255, 255))
					text_position = (1423 * self.factor_x + hovering_diplomatic_information_description_title_text.get_width(), mouse_rect[1] + 20)

					hovering_diplomatic_information_description_text = self.tiny_scalable_font.render("\n\n    SOMETHING: 100% \n\n    SOMETHING: 80% \n\n    SOMETHING: 60%", True, (255, 255, 255))	
					
					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x - hovering_diplomatic_information_description_title_text.get_width(), text_position[1], hovering_diplomatic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_diplomatic_information_description_title_text.get_height()+30 * self.factor_y + hovering_diplomatic_information_description_text.get_height()))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x - hovering_diplomatic_information_description_title_text.get_width(), text_position[1], hovering_diplomatic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_diplomatic_information_description_title_text.get_height()+30 * self.factor_y + hovering_diplomatic_information_description_text.get_height()), 4)				
					
					screen.blit(hovering_diplomatic_information_description_title_text, (text_position[0] - hovering_diplomatic_information_description_title_text.get_width()/2 +10 * self.factor_x, text_position[1]+12 * self.factor_y))
					screen.blit(hovering_diplomatic_information_description_text, (text_position[0] - hovering_diplomatic_information_description_title_text.get_width(), text_position[1]+15 * self.factor_y + hovering_diplomatic_information_description_title_text.get_height()))	
				if self.hovering_military_information_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.military_information_rect, 2)
					hovering_military_information_description_title_text = self.small_scalable_font.render("MILITARY INFORMATION", True, (255, 255, 255))
					text_position = (1423 * self.factor_x + hovering_military_information_description_title_text.get_width(), mouse_rect[1] + 20)

					manpower = self.selected_country.army_staff
					if manpower >= 1000000:
						formatted_manpower = f'{manpower / 1000000:.1f} M'
					elif manpower >= 1000:
						formatted_manpower = f'{manpower / 1000:.1f} K'
					else:
						formatted_manpower = str(manpower)
					hovering_military_information_description_text = self.tiny_scalable_font.render(f"\n\n    ARMY STAFF: \n\n    PRODUCTION CAPACITY: ", True, (255, 255, 255))	
					hovering_military_information_description_values_text = self.tiny_scalable_font.render(f"\n\n                {formatted_manpower} \n\n                {self.selected_country.production_capacity_total}", True, (255, 255, 255))	

					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x - hovering_military_information_description_title_text.get_width(), text_position[1], hovering_military_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_military_information_description_title_text.get_height()+30 * self.factor_y + hovering_military_information_description_text.get_height()))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x - hovering_military_information_description_title_text.get_width(), text_position[1], hovering_military_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_military_information_description_title_text.get_height()+30 * self.factor_y + hovering_military_information_description_text.get_height()), 4)				
					
					screen.blit(hovering_military_information_description_title_text, (text_position[0] - hovering_military_information_description_title_text.get_width()/2 +10 * self.factor_x, text_position[1]+12 * self.factor_y))
					screen.blit(hovering_military_information_description_text, (text_position[0] - hovering_military_information_description_title_text.get_width(), text_position[1]+15 * self.factor_y + hovering_military_information_description_title_text.get_height()))
					screen.blit(hovering_military_information_description_values_text, (text_position[0] - hovering_military_information_description_title_text.get_width() + 140 * self.factor_x, text_position[1]+15 * self.factor_y + hovering_military_information_description_title_text.get_height()))								
				if self.hovering_economic_information_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.economic_information_rect, 2)
					hovering_economic_information_description_title_text = self.small_scalable_font.render("ECONOMIC INFORMATION", True, (255, 255, 255))
					text_position = (1423 * self.factor_x + hovering_economic_information_description_title_text.get_width(), mouse_rect[1] + 20)

					treasury = self.selected_country.treasury
					if abs(treasury) < 1e6:
						formatted_treasury = f"${treasury:,.3f}"
					elif abs(treasury) < 1e9:
						formatted_treasury = f"${treasury / 1e6:.3f} M"
					elif abs(treasury) < 1e12:
						formatted_treasury = f"${treasury / 1e9:.3f} B"
					elif abs(treasury) < 1e15:
						formatted_treasury = f"${treasury / 1e12:.3f} T"
					else:
						formatted_treasury = f"${treasury:.3f}"

					debt = self.selected_country.debt
					if abs(debt) < 1e6:
						formatted_debt = f"${debt:,.3f}"
					elif abs(debt) < 1e9:
						formatted_debt = f"${debt / 1e6:.3f} M"
					elif abs(debt) < 1e12:
						formatted_debt = f"${debt / 1e9:.3f} B"
					elif abs(debt) < 1e15:
						formatted_debt = f"${debt / 1e12:.3f} T"
					else:
						formatted_debt = f"${debt:.3f}"				

					hovering_economic_information_description_text = self.tiny_scalable_font.render(f"\n\n    TREASURY: \n\n    GDP/c: \n\n    DEBT: \n\n\n        CREDIT RATING: \n\n        INFLATION: \n\n        UNEMPLOYMENT: ", True, (255, 255, 255))	
					hovering_economic_information_description_values_text = self.tiny_scalable_font.render(f"\n\n{formatted_treasury} \n\n${self.selected_country.country_GDP/self.selected_country.country_population:,.2f}\n\n{formatted_debt}\n\n\n        {self.selected_country.credit_rating}%\n\n        {self.selected_country.inflation}%\n\n        {self.selected_country.unemployment}%", True, (255, 255, 255))
					
					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x - hovering_economic_information_description_title_text.get_width(), text_position[1], hovering_economic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_economic_information_description_title_text.get_height()+30 * self.factor_y + hovering_economic_information_description_text.get_height()))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x - hovering_economic_information_description_title_text.get_width(), text_position[1], hovering_economic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_economic_information_description_title_text.get_height()+30 * self.factor_y + hovering_economic_information_description_text.get_height()), 4)				
					
					screen.blit(hovering_economic_information_description_title_text, (text_position[0] - hovering_economic_information_description_title_text.get_width()/2 +10 * self.factor_x, text_position[1]+12 * self.factor_y))
					screen.blit(hovering_economic_information_description_text, (text_position[0] - hovering_economic_information_description_title_text.get_width(), text_position[1]+15 * self.factor_y + hovering_economic_information_description_title_text.get_height()))
					screen.blit(hovering_economic_information_description_values_text, (text_position[0] - hovering_economic_information_description_title_text.get_width() + 135 * self.factor_x, text_position[1]+15 * self.factor_y + hovering_economic_information_description_title_text.get_height()))
				if self.hovering_domestic_information_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.domestic_information_rect, 2)
					hovering_domestic_information_description_title_text = self.small_scalable_font.render("DOMESTIC INFORMATION", True, (255, 255, 255))
					text_position = (1423 * self.factor_x + hovering_domestic_information_description_title_text.get_width(), mouse_rect[1] + 20)

					population_formated = locale.format_string("%d", self.selected_country.country_population, grouping=True)
					country_immigration_formated = locale.format_string("%d", self.selected_country.country_immigration, grouping=True)
					country_emigration_formated = locale.format_string("%d", self.selected_country.country_emigration, grouping=True)
					country_births_formated = locale.format_string("%d", self.selected_country.country_births, grouping=True)			
					country_deaths_formated = locale.format_string("%d", self.selected_country.country_deaths, grouping=True)
					
					hovering_domestic_information_description_text = self.tiny_scalable_font.render(f"\n\n    POPULATION: \n\n      IMMIGRATION: \n\n      EMIGRATION: \n\n      BIRTHS: \n\n      DEATHS: \n\n      LITERACY RATE: \n\n\n    POPULATION POLITICAL LEANING: ", True, (255, 255, 255))	
					hovering_domestic_information_description_values_text = self.tiny_scalable_font.render(f"\n\n{population_formated} \n\n    {country_immigration_formated} \n\n    {country_emigration_formated} \n\n    {country_births_formated} \n\n    {country_deaths_formated} \n\n    {self.selected_country.country_literacy_rate}% \n\n\n                        {self.selected_country.population_political_leaning}", True, (255, 255, 255))
					
					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x - hovering_domestic_information_description_title_text.get_width(), text_position[1], hovering_domestic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_domestic_information_description_title_text.get_height()+30 * self.factor_y + hovering_domestic_information_description_text.get_height()))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x - hovering_domestic_information_description_title_text.get_width(), text_position[1], hovering_domestic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_domestic_information_description_title_text.get_height()+30 * self.factor_y + hovering_domestic_information_description_text.get_height()), 4)				
					
					screen.blit(hovering_domestic_information_description_title_text, (text_position[0] - hovering_domestic_information_description_title_text.get_width()/2 +10 * self.factor_x, text_position[1]+12 * self.factor_y))
					screen.blit(hovering_domestic_information_description_text, (text_position[0] - hovering_domestic_information_description_title_text.get_width(), text_position[1]+15 * self.factor_y + hovering_domestic_information_description_title_text.get_height()))			
					screen.blit(hovering_domestic_information_description_values_text, (text_position[0] - hovering_domestic_information_description_title_text.get_width() + 160 * self.factor_x, text_position[1]+15 * self.factor_y + hovering_domestic_information_description_title_text.get_height()))			

				if self.hovering_internal_and_external_market_approval_rating_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.internal_and_external_market_approval_rating_rect, 3)
					hovering_internal_and_external_market_approval_rating_rect = self.small_scalable_font.render(f"INTERNAL MARKET APPROVAL RATING:  {self.selected_country.internal_economy_rating}%\n\nEXTERNAL MARKET APPROVAL RATING:  {self.selected_country.external_economy_rating}%", True, (255, 255, 255))
					text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
					
					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_internal_and_external_market_approval_rating_rect.get_width()+24 * self.factor_x, hovering_internal_and_external_market_approval_rating_rect.get_height()+10 * self.factor_y))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_internal_and_external_market_approval_rating_rect.get_width()+24 * self.factor_x, hovering_internal_and_external_market_approval_rating_rect.get_height()+10 * self.factor_y), 2)				
					
					screen.blit(hovering_internal_and_external_market_approval_rating_rect, (text_position[0], text_position[1]+6 * self.factor_y))	
				
				if self.hovering_military_approval_rating_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.military_approval_rating_rect, 3)
					hovering_military_approval_rating_description_text = self.small_scalable_font.render(f"MILITARY APPROVAL RATING:  {self.selected_country.military_approval_rating}%", True, (255, 255, 255))
					text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
					
					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_military_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_military_approval_rating_description_text.get_height()+10 * self.factor_y))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_military_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_military_approval_rating_description_text.get_height()+10 * self.factor_y), 3)				
					
					screen.blit(hovering_military_approval_rating_description_text, (text_position[0], text_position[1]+6 * self.factor_y))	
				if self.hovering_domestic_approval_rating_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.domestic_approval_rating_rect, 3)
					hovering_domestic_approval_rating_description_text = self.small_scalable_font.render(f"DOMESTIC APPROVAL RATING:  {self.selected_country.domestic_approval_rating}%", True, (255, 255, 255))
					text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
					
					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_domestic_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_domestic_approval_rating_description_text.get_height()+10 * self.factor_y))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_domestic_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_domestic_approval_rating_description_text.get_height()+10 * self.factor_y), 3)				
					
					screen.blit(hovering_domestic_approval_rating_description_text, (text_position[0], text_position[1]+6 * self.factor_y))	
				if self.hovering_midia_approval_rating_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.midia_approval_rating_rect, 3)
					hovering_midia_approval_rating_description_text = self.small_scalable_font.render(f"MIDIA APPROVAL RATING:  {self.selected_country.midia_approval_rating}%", True, (255, 255, 255))
					text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
					
					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_midia_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_midia_approval_rating_description_text.get_height()+10 * self.factor_y))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_midia_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_midia_approval_rating_description_text.get_height()+10 * self.factor_y), 3)				
					
					screen.blit(hovering_midia_approval_rating_description_text, (text_position[0], text_position[1]+6 * self.factor_y))	
				if self.hovering_secret_service_approval_rating_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.secret_service_approval_rating_rect, 3)
					hovering_secret_service_approval_description_text = self.small_scalable_font.render(f"SECRET SERVICE APPROVAL RATING:  {self.selected_country.secret_service_approval_rating}%", True, (255, 255, 255))
					text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
					
					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_secret_service_approval_description_text.get_width()+24 * self.factor_x, hovering_secret_service_approval_description_text.get_height()+10 * self.factor_y))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_secret_service_approval_description_text.get_width()+24 * self.factor_x, hovering_secret_service_approval_description_text.get_height()+10 * self.factor_y), 3)				
					
					screen.blit(hovering_secret_service_approval_description_text, (text_position[0], text_position[1]+6 * self.factor_y))	
				if self.hovering_politics_approval_rating_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.politics_approval_rating_rect, 3)
					hovering_politics_approval_rating_description_text = self.small_scalable_font.render(f"POLITICIANS APPROVAL RATING:  {self.selected_country.politics_approval_rating}%", True, (255, 255, 255))
					text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
					
					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_politics_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_politics_approval_rating_description_text.get_height()+10 * self.factor_y))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_politics_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_politics_approval_rating_description_text.get_height()+10 * self.factor_y), 3)				
					
					screen.blit(hovering_politics_approval_rating_description_text, (text_position[0], text_position[1]+6 * self.factor_y))													


		if self.clicked_ideology == None: # Blocked Buttons
			screen.blit(self.blocked_select_country_button, (self.select_country_button_x_offset, self.select_country_button_y_offset))
			screen.blit(self.blocked_select_national_spirit_button, (self.select_national_spirit_button_x_offset, self.select_national_spirit_button_y_offset))
			screen.blit(self.blocked_start_game_button, (self.start_game_button_x_offset, self.start_game_button_y_offset))				
			screen.blit(self.blocked_full_right_side, (self.screen_width - self.blocked_full_right_side.get_width(), 0))		
		elif self.selected_country == None:
			screen.blit(self.blocked_select_national_spirit_button, (self.select_national_spirit_button_x_offset, self.select_national_spirit_button_y_offset))
			screen.blit(self.blocked_start_game_button, (self.start_game_button_x_offset, self.start_game_button_y_offset))
			screen.blit(self.blocked_all_laws, (self.screen_width - self.blocked_all_laws.get_width(), self.screen_height - self.blocked_all_laws.get_height()))
			self.national_spirits_display_rects = []
				
		if self.clicked_ideology_rect != None:
			pygame.draw.rect(screen, (255,255,255), self.clicked_ideology_rect, 5)

		screen.blit(self.ideologies_CRT_overlay_effect, (15 * self.factor_x, 31 * self.factor_y))			

		if self.hovered_button != None and self.hovered_rect == None: # Buttons Selection 
			
			if self.hovered_button == 'start_game':
				screen.blit(self.hovered_start_game_button, (self.start_game_button_x_offset, self.start_game_button_y_offset))
			
			elif self.hovered_button == 'select_national_spirit':
				screen.blit(self.hovered_select_national_spirit_button_image, (self.select_national_spirit_button_x_offset, self.select_national_spirit_button_y_offset))
			
			elif self.hovered_button == 'select_country':
				screen.blit(self.hovered_select_country_button_image, (self.select_country_button_x_offset, self.select_country_button_y_offset))				

			elif type(self.hovered_button) is str:
				splited_button = self.hovered_button.split('_')
				button_name = splited_button[0] + '_law_button_' + splited_button[1]
				button = getattr(self, button_name, None)
				if button:
					self.pygame.draw.rect(screen, (0,255,0), button.rect, 3)
		
		else: # Fade Audio
			self.hover_over_button_sound.fadeout(50)

		if self.hovered_national_spirit != None:
			pygame.draw.rect(screen, (255,255,255), self.hovered_national_spirit.rect, 2)

			national_spirit_description_text = self.small_scalable_font.render(self.hovered_national_spirit.national_spirit_description, True, (255, 255, 255))
			text_position = (1429 * self.factor_x, 239 * self.factor_y)

			pygame.draw.rect(screen, (6,15,20), (1423 * self.factor_x, 232 * self.factor_y, 484 * self.factor_x, national_spirit_description_text.get_height() + 10 * self.factor_y))
			pygame.draw.rect(screen, (43,219,211), (1423 * self.factor_x, 232 * self.factor_y, 484 * self.factor_x, national_spirit_description_text.get_height() + 10 * self.factor_y), 2)

			screen.blit(national_spirit_description_text, text_position)				
class Flag_Selection_Menu:
	def __init__(self, screen_width, screen_height, pygame, countries, generic_hover_over_button_sound, generic_click_menu_sound, country_info_display_background) -> None:
		self.countries = countries

		self.selected_country = None

		self.pygame = pygame
		
		self.screen_width = screen_width
		self.screen_height = screen_height
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y		

		self.flag_rects = []
		self.hovered_ideology_rect = None

		self.country_info_display_background = pygame.transform.smoothscale_by(country_info_display_background, (self.factor_x, self.factor_y))

		self.last_selected_country_name = None
		self.selected_country_name: CountriesManager.Country = None

		self.normal_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(30 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))		
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))


		self.hover_over_button_sound, self.click_sound = generic_hover_over_button_sound, generic_click_menu_sound

	def get_button_by_interaction(self, mouse_rect):
		for rect in self.flag_rects:
			if rect[0].colliderect(mouse_rect):
				self.selected_country = rect[3]
				self.hover_over_button_sound.fadeout(50)
				self.click_sound.play()	
				return rect[1]	
		else:
			return None

	def get_clicked_button(self, mouse_rect):
		clicked_button = self.get_button_by_interaction(mouse_rect)
		return clicked_button

	def draw(self, screen, selected_ideology, mouse_rect):
		pygame.draw.rect(screen, (6,15,20), (self.screen_width * 0.05, self.screen_height*0.51, self.screen_width * 0.9, self.screen_height*0.48))
		pygame.draw.rect(screen, (43,219,211), (self.screen_width * 0.05, self.screen_height*0.51, self.screen_width * 0.9, self.screen_height*0.48), 2)
		
		if selected_ideology != None:
			self.flag_rects = []
			countries_with_selected_ideology = []
			for country in self.countries:
				if country.country_ruler_ideology == selected_ideology:
					countries_with_selected_ideology.append(country)
					

			for i, country in enumerate(countries_with_selected_ideology):
				flag_position = (0, 0)
				flag = country.country_flag_image
				flag_width = flag.get_width()
				total_flags = len(countries_with_selected_ideology)
				flags_spacing = flag_width/ (total_flags * 1.25)
				total_width_of_flags = total_flags * flag_width + (total_flags - 1) * flags_spacing
				available_space = self.screen_width - total_width_of_flags
				left_padding = available_space / 2
				
				x_position = left_padding + i * (flag_width + flags_spacing)
				flag_position = (x_position, self.screen_height * 0.55)

				flag_rect = pygame.Rect(flag_position, flag.get_size())
				self.flag_rects.append([flag_rect, flag, i, country])				
				screen.blit(flag, flag_position)

			screen.blit(self.country_info_display_background, (self.screen_width/2 - self.country_info_display_background.get_width()/2, self.screen_height - self.country_info_display_background.get_height() * 1.05))

			for rect in self.flag_rects:
				if rect[0].colliderect(mouse_rect) and self.country_info_display_background != None:
					pygame.draw.rect(screen, (255,255,255), rect[0], 2)
					
					self.selected_country_name = countries_with_selected_ideology[rect[2]].country_name
					country_name_text = self.normal_scalable_font.render(self.selected_country_name, True, (255, 255, 255))
					if country_name_text.get_width() > 300 * self.factor_x:
						country_name_text = self.small_scalable_font.render(self.selected_country_name, True, (255, 255, 255))
					if country_name_text.get_width() > 300 * self.factor_x:
						country_name_text = self.small_scalable_font.render(self.selected_country_name, True, (255, 255, 255))						

					text_position = (self.screen_width/2 - country_name_text.get_width()/1.95, self.screen_height - self.country_info_display_background.get_height() + self.country_info_display_background.get_height() * 0.079 - country_name_text.get_height() /2)
					screen.blit(country_name_text, text_position)

					country_info_display_background_position = [self.screen_width/2 - self.country_info_display_background.get_width()/2, self.screen_height - self.country_info_display_background.get_height() * 1.05]

					# LEADER
					leader_name = countries_with_selected_ideology[rect[2]].country_leader_name
					leader_name_text = self.small_scalable_font.render(leader_name, True, (255, 255, 255))
					if leader_name_text.get_width() > 265 * self.factor_x:
						leader_name_text = self.small_scalable_font.render(leader_name, True, (255, 255, 255))

					text_position = (66 * self.factor_x + country_info_display_background_position[0], 77 * self.factor_y + country_info_display_background_position[1])
					screen.blit(leader_name_text, text_position)

					# RUILING PARTY
					ruling_party_name = countries_with_selected_ideology[rect[2]].country_ruling_party
					ruling_party_name_text = self.small_scalable_font.render(ruling_party_name, True, (255, 255, 255))
					if ruling_party_name_text.get_width() > 265 * self.factor_x:
						ruling_party_name_text = self.small_scalable_font.render(ruling_party_name, True, (255, 255, 255))
					
					text_position = (66 * self.factor_x + country_info_display_background_position[0], 143 * self.factor_y + country_info_display_background_position[1])
					screen.blit(ruling_party_name_text, text_position)		

					# GOVERNMENT
					government_name_text = countries_with_selected_ideology[rect[2]].country_government
					government_name_text = self.small_scalable_font.render(government_name_text, True, (255, 255, 255))
					if government_name_text.get_width() > 265 * self.factor_x:
						government_name_text = self.small_scalable_font.render(government_name_text, True, (255, 255, 255))
					
					text_position = (66 * self.factor_x + country_info_display_background_position[0], 209 * self.factor_y + country_info_display_background_position[1])
					screen.blit(government_name_text, text_position)		

					# ELECTIONS
					elections_name = countries_with_selected_ideology[rect[2]].country_elections
					elections_name_text = self.small_scalable_font.render(elections_name, True, (255, 255, 255))
					if elections_name_text.get_width() > 265 * self.factor_x:
						elections_name_text = self.small_scalable_font.render(elections_name, True, (255, 255, 255))
					
					text_position = (165 * self.factor_x + country_info_display_background_position[0], 252 * self.factor_y + country_info_display_background_position[1])
					screen.blit(elections_name_text, text_position)															

					# BRIEF HISTORY
					brief_history_name = countries_with_selected_ideology[rect[2]].country_brief_history
					brief_history_name_text = self.small_scalable_font.render(brief_history_name, True, (255, 255, 255))
					
					text_position = (920 * self.factor_x + country_info_display_background_position[0], 65 * self.factor_y + country_info_display_background_position[1])
					screen.blit(brief_history_name_text, text_position)		

					self.selected_leader_image = countries_with_selected_ideology[rect[2]].country_leader_image
					self.selected_leader_image = self.pygame.transform.smoothscale(self.selected_leader_image, (155 * self.factor_x, 212 * self.factor_y))
					screen.blit(self.selected_leader_image, (self.country_info_display_background.get_width() * 0.2421 + self.screen_width/2 - self.country_info_display_background.get_width()/2, self.screen_height - self.country_info_display_background.get_height() * 1.05 + self.country_info_display_background.get_height() * 0.1516))					

					national_spirits_position = [country_info_display_background_position[0] + 541*self.factor_x, country_info_display_background_position[1] + 63*self.factor_y]
					for i, national_spirit in enumerate(countries_with_selected_ideology[rect[2]].country_national_spirits):
						if i > 3:
							break
						offset = national_spirit.national_spirit_icon.get_width() * 1.28
						screen.blit(national_spirit.national_spirit_icon, (national_spirits_position[0]+offset*i, national_spirits_position[1]))


					if self.selected_country_name != self.last_selected_country_name:
						self.hover_over_button_sound.play()
						self.last_selected_country_name = self.selected_country_name

	def draw_flag_selection_preview(self, screen, hovered_ideology, mouse_pos):
		if hovered_ideology != None:
			pygame.draw.rect(screen, (255,255,255), self.hovered_ideology_rect, 2)							
			self.flag_rects = []

			countries_with_selected_ideology = []
			for country in self.countries:
				if country.country_ruler_ideology == hovered_ideology:
					countries_with_selected_ideology.append(country)

			for i, country in enumerate(countries_with_selected_ideology):
				flag = country.country_flag_image
				flag_position = (0, 0)
				flag_width = flag.get_width()
				total_flags = len(countries_with_selected_ideology)
				flags_spacing = flag_width/ (total_flags * 1.25)
				total_width_of_flags = total_flags * flag_width + (total_flags - 1) * flags_spacing
				available_space = self.screen_width/1.83 - total_width_of_flags
				left_padding = available_space / 2
				
				x_position = left_padding + i * (flag_width + flags_spacing)
				y_position = self.screen_height * 0.84 if mouse_pos[1] < self.screen_height/2 else self.screen_height * 0.055
				flag_position = (x_position, y_position)

				flag_rect = pygame.Rect(flag_position, flag.get_size())
				self.flag_rects.append([flag_rect, flag, i])

				pygame.draw.rect(screen, (6,15,20), (x_position - flag_width/10, y_position - flag.get_height()/10, flag_width + flag_width/5, flag.get_height() + flag.get_height()/5))
				pygame.draw.rect(screen, (43,219,211), (x_position - flag_width/10, y_position - flag.get_height()/10, flag_width + flag_width/5, flag.get_height() + flag.get_height()/5), 2)				

				screen.blit(flag, flag_position)
class National_Spirits_Selection_Menu:
	def __init__(self, screen_width, screen_height, national_spirits_background, selectable_national_spirits_list, hover_over_button_sound, click_sound) -> None:
		self.screen_width = screen_width
		self.screen_height = screen_height
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y	

		self.background_position = [13 * self.factor_x, 29 * self.factor_y]

		self.national_spirits_background = national_spirits_background
		
		self.selectable_national_spirits_list = selectable_national_spirits_list
		self.selectable_national_spirits_rects = []
		
		self.selected_country: CountriesManager.Country = None

		self.hovered_national_spirit = None
		self.last_hovered_national_spirit = None

		self.hover_over_button_sound = hover_over_button_sound
		self.click_sound = click_sound


		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(32 * self.factor_y))
		self.normal_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(26.6 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(20 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))		

		self.color_cache = {}
		self.color_timer = 0

	def get_hovered_national_spirit(self, mouse_rect):
		for rect, national_spirit in self.selectable_national_spirits_rects:
			rect = pygame.Rect(rect)
			if rect.colliderect(mouse_rect):
				if national_spirit != self.last_hovered_national_spirit:
					self.last_hovered_national_spirit = national_spirit
					self.hover_over_button_sound.play()
					return national_spirit
				else:
					return national_spirit
		self.last_hovered_national_spirit = None		
		return None

	def get_clicked_national_spirit(self, mouse_rect):
		self.hover_over_button_sound.fadeout(50)

		for rect, national_spirit in self.selectable_national_spirits_rects:
			rect = pygame.Rect(rect)
			if rect.colliderect(mouse_rect):
				if national_spirit not in self.selected_country.country_national_spirits: 
					if(self.selected_country.country_national_spirits_points_left - national_spirit.points_cost) >= 0:
						self.selected_country.country_national_spirits.append(national_spirit)
						self.selected_country.country_national_spirits_points_left -= national_spirit.points_cost
					self.click_sound.play()	
				else:
					self.selected_country.country_national_spirits.remove(national_spirit)
					self.selected_country.country_national_spirits_points_left += national_spirit.points_cost
					self.click_sound.play()	

				return national_spirit
		
		return None

	def draw(self, screen):
		screen.blit(self.national_spirits_background, self.background_position)

		points_text = f"{self.selected_country.country_national_spirits_total_points}    -    {self.selected_country.country_national_spirits_points_left}"
		points_text_render = self.big_scalable_font.render(points_text, True, (255, 255, 255))
		text_position = (self.background_position[0] + 725 * self.factor_x - points_text_render.get_width()/2, self.background_position[1] + 40 * self.factor_y)
		screen.blit(points_text_render, text_position)		

		selectable_national_spirits_position = [95*self.factor_x, 125*self.factor_y]
		x_index = 0
		y_index = 0
		
		self.selectable_national_spirits_rects = []

		for national_spirit in self.selectable_national_spirits_list:
			x_offset = national_spirit.national_spirit_icon.get_width() * 1.37
			y_offset = national_spirit.national_spirit_icon.get_height() * 1.28

			screen.blit(national_spirit.national_spirit_icon, (selectable_national_spirits_position[0] + x_offset*x_index, selectable_national_spirits_position[1] + y_offset*y_index))
			
			self.selectable_national_spirits_rects.append(((selectable_national_spirits_position[0] + x_offset*x_index, selectable_national_spirits_position[1] + y_offset*y_index, 
															national_spirit.national_spirit_icon.get_width(),  national_spirit.national_spirit_icon.get_height()), national_spirit))

			if x_index < 4:
				x_index += 1
			else:
				x_index = 0
				y_index += 1

		
		selected_national_spirits_set = set(self.selected_country.country_national_spirits)
		self.color_cache = {}

		for rect, national_spirit in self.selectable_national_spirits_rects:
			if national_spirit == self.hovered_national_spirit:
				if national_spirit in selected_national_spirits_set:
					color = (255, 0, 0)
				else:
					color = (255, 255, 255)
			else:
				if national_spirit in selected_national_spirits_set:
					color = (0, 255, 0)
				else:
					color = None 

			self.color_cache[(rect, national_spirit)] = color
		
		self.color_timer = 0


		for rect, national_spirit in self.selectable_national_spirits_rects:
			color = self.color_cache.get((rect, national_spirit))
			if color is not None:
				rect = pygame.Rect(rect)
				pygame.draw.rect(screen, color, rect, 2)


		if self.hovered_national_spirit != None:
			national_spirit_description_text = self.small_scalable_font.render(self.hovered_national_spirit.national_spirit_description, True, (255, 255, 255))
			text_position = (534 * self.factor_x, 132 * self.factor_y)

			pygame.draw.rect(screen, (6,15,20), (525 * self.factor_x, 125 * self.factor_y, 495 * self.factor_x, national_spirit_description_text.get_height() + 10 * self.factor_y))
			pygame.draw.rect(screen, (43,219,211), (525 * self.factor_x, 125 * self.factor_y, 495 * self.factor_x, national_spirit_description_text.get_height() + 10 * self.factor_y), 2)

			screen.blit(national_spirit_description_text, text_position)
class Laws_Group_Menu:
	def __init__(self, screen_width, screen_height, pygame, generic_hover_over_button_sound, generic_click_menu_sound, selected_law_background, laws_description_image):
		self.mouse_pos = [0, 0]

		self.screen_width = screen_width 
		self.screen_height = screen_height
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y
		self.factor = self.factor_x * self.factor_y

		self.pygame = pygame

		self.selected_country: CountriesManager.Country = None
		self.laws_butons_rect = []
		self.last_hovered_rect = None

		self.background_position = [13 * self.factor_x, 29 * self.factor_y]

		self.close_button = GenericUtilitys.Button(976 * self.factor_x + self.background_position[0], 14 * self.factor_y + self.background_position[1], 30 * self.factor_x, 30 * self.factor_y)		

		self.selected_law_background = pygame.transform.smoothscale_by(selected_law_background, (self.factor_x, self.factor_y))		
		self.laws_description_image = pygame.transform.smoothscale_by(laws_description_image, (self.factor_x, self.factor_y))	

		self.opened_law_group = None

		self.hover_over_button_sound = generic_hover_over_button_sound
		self.click_menu_sound = generic_click_menu_sound

		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(13 * self.factor_y))

	def get_hovered_rect(self, mouse_rect):
		for rect in self.laws_butons_rect:
			rect = pygame.Rect(rect)
			if rect.colliderect(mouse_rect):
				if rect != self.last_hovered_rect:
					self.last_hovered_rect = rect
					self.hover_over_button_sound.play()
				return rect
		if self.close_button.rect.colliderect(mouse_rect):
			if self.close_button.rect != self.last_hovered_rect:
				self.last_hovered_rect = self.close_button.rect
				self.hover_over_button_sound.play()	
			return rect		

		self.last_hovered_rect = None		
		return None		

	def get_clicked_button(self, mouse_rect):
		self.hover_over_button_sound.fadeout(50)
		if self.close_button.rect.colliderect(mouse_rect):
			self.click_menu_sound.play()
			return 'close'
	
	def draw(self, screen):
		screen.blit(self.selected_law_background, self.background_position)

		self.laws_butons_rect = []

		if self.opened_law_group != None:

			if self.close_button.rect == self.last_hovered_rect:
				pygame.draw.rect(screen, (255,255,255), self.close_button.rect, 2)

			
			splited = self.opened_law_group.split('_')
			laws_group = None
			if splited[0] == 'political':
				laws_group = self.selected_country.political_laws_groups[int(splited[1]) - 1]
			elif splited[0] == 'military':
				laws_group = self.selected_country.military_laws_groups[int(splited[1]) - 1]
			elif splited[0] == 'economical':
				laws_group = self.selected_country.economical_laws_groups[int(splited[1]) - 1]
			elif splited[0] == 'social':
				laws_group = self.selected_country.social_laws_groups[int(splited[1]) - 1]											

			if laws_group != None:
				laws = laws_group.laws

				height = 120 * len(laws) - 80
				start_pos = (1017 - height) / 2
				
				is_any_description_being_displayed = False
				for index, law in enumerate(laws):
					rect = (40 * self.factor_x, (start_pos + 120 * index) * self.factor_y, 424 * self.factor_x, 80 * self.factor_y)
					overlay_rect = (39 * self.factor_x, (start_pos-1 + 120 * index) * self.factor_y, 426 * self.factor_x, 82 * self.factor_y)

					pygame.draw.rect(screen, (6,15,20), rect)
					if self.last_hovered_rect != rect:
						if index == laws_group.active_law_index:
							pygame.draw.rect(screen, (255,38,42), overlay_rect, 4)
						else:
							pygame.draw.rect(screen, (43,219,211), rect, 2)
					else:
						pygame.draw.rect(screen, (38,255,38), overlay_rect, 4)

						is_any_description_being_displayed = True

						# LAW DESCRIPTION
						if law.description_complement == None:
							law_description = self.big_scalable_font.render(law.description, True, (255, 255, 255))
						else:
							law_description = self.big_scalable_font.render(law.description + getattr(self.selected_country, law.description_complement), True, (255, 255, 255))
						text_position = (490 * self.factor_x, 508 * self.factor_y - law_description.get_height()/2 + 63 * self.factor_y)						
						pygame.draw.rect(screen, (6,15,20), (480 * self.factor_x, 498 * self.factor_y - law_description.get_height()/2, 538 * self.factor_x, law_description.get_height() + 20 * self.factor_y + 63 * self.factor_y))
						screen.blit(self.laws_description_image, (495 * self.factor_x, 503 * self.factor_y - law_description.get_height()/2))
						
						pygame.draw.rect(screen, (43,219,211), (480 * self.factor_x, 498 * self.factor_y - law_description.get_height()/2, 538 * self.factor_x, law_description.get_height() + 20 * self.factor_y + 63 * self.factor_y), 2)
						screen.blit(law_description, text_position)

					law_opened = self.big_scalable_font.render(law.name, True, (255, 255, 255))
					text_position = (60 * self.factor_x, (start_pos + 120 * index) * self.factor_y + 40 * self.factor_y - law_opened.get_height()/2)
					screen.blit(law_opened, text_position)					

					self.laws_butons_rect.append(rect)

				if is_any_description_being_displayed == False:
					# ACTIVE LAW DESCRIPTION
					if laws_group.active_law.description_complement == None:
						law_description = self.big_scalable_font.render(laws_group.active_law.description, True, (255, 255, 255))
					else:
						law_description = self.big_scalable_font.render(laws_group.active_law.description + getattr(self.selected_country, laws_group.active_law.description_complement), True, (255, 255, 255))
					text_position = (490 * self.factor_x, 508 * self.factor_y - law_description.get_height()/2 + 63 * self.factor_y)						
					pygame.draw.rect(screen, (6,15,20), (480 * self.factor_x, 498 * self.factor_y - law_description.get_height()/2, 538 * self.factor_x, law_description.get_height() + 20 * self.factor_y + 63 * self.factor_y))
					screen.blit(self.laws_description_image, (495 * self.factor_x, 503 * self.factor_y - law_description.get_height()/2))
					
					pygame.draw.rect(screen, (43,219,211), (480 * self.factor_x, 498 * self.factor_y - law_description.get_height()/2, 538 * self.factor_x, law_description.get_height() + 20 * self.factor_y + 63 * self.factor_y), 2)
					screen.blit(law_description, text_position)					

#----------------------------------------------------#

class Game_Screen:
	def __init__(self, screen_width, screen_height, pygame, clock, generic_hover_over_button_sound, generic_click_button_sound, top_bar_right_background, top_bar_game_speed_indicator,
			top_bar_defcon_level, top_bar_left_background, top_bar_flag_overlay, top_bar_flag_overlay_hovering_over, country_overview, popularity_circle_overlay, earth_daymap, 
			earth_political_map, earth_political_map_filled, progressbar_huge, progressbar, progressbar_vertical, progressbar_small, country_laws_background, laws_description_image,
			game_logo, economic_overview_background, poverty_rate_0, poverty_rate_5, poverty_rate_10, poverty_rate_15, poverty_rate_25, poverty_rate_50, poverty_rate_80, credit_ratings,
			economic_warning, economic_freedom_index_green, economic_freedom_index_red, economic_freedom_score_green, economic_freedom_score_red, small_rating_green, small_rating_red,
			intelligence_overview_background, intelligency_agencies_icons_image_dic, research_overview_background, active_research_background, researche_icons_image_dic,
			researche_institute_icons_image_dic, construction_overview_background, production_overview_background, bottom_HUD, law_opinion_survey_icon, law_opinion_survey_menu,
			finances_menu_background, budget_menu, debt_menu, taxation_menu, currency_menu, finance_menu, government_menu_background, head_of_state_menu, cabinet_menu, parliament_menu,
			elections_menu, political_parties_menu):

		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y
		self.factor = self.factor_x * self.factor_y
		
		self.generic_hover_over_button_sound, self.generic_click_button_sound = generic_hover_over_button_sound, generic_click_button_sound

		self.last_hovered_button = None	

		self.PlayerCountry = None

		self.Country_Overview = Country_Overview(self.factor_x, self.factor_y, pygame, top_bar_left_background, top_bar_flag_overlay, top_bar_flag_overlay_hovering_over,
			country_overview, popularity_circle_overlay, self.generic_hover_over_button_sound, progressbar, progressbar_vertical, progressbar_small)
		
		self.Country_Focus_Tree = Country_Focus_Tree(self.factor_x, self.factor_y, screen_width, screen_height, pygame, top_bar_flag_overlay, top_bar_flag_overlay_hovering_over)

		self.Clock_UI = Clock_UI(self.factor_x, self.factor_y, screen_width, screen_height, pygame, clock, top_bar_right_background, top_bar_game_speed_indicator, top_bar_defcon_level)

		self.Bottom_HUD = Bottom_HUD(self.factor_x, self.factor_y, screen_width, screen_height, pygame, bottom_HUD, law_opinion_survey_icon, law_opinion_survey_menu, finances_menu_background, budget_menu, debt_menu, taxation_menu, currency_menu,
			finance_menu, government_menu_background, head_of_state_menu, cabinet_menu, parliament_menu, elections_menu, political_parties_menu)

		self.Earth_Map = Earth_Map(self.factor_x, self.factor_y, screen_width, screen_height, earth_daymap, earth_political_map, earth_political_map_filled, self.Clock_UI)


		self.Decisions_Menu = Decisions_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame)
	
		self.Laws_Menu = Laws_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame, progressbar_huge, country_laws_background, laws_description_image)

		self.Finances_Menu = Finances_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame, economic_overview_background, poverty_rate_0, poverty_rate_5, poverty_rate_10,
			poverty_rate_15, poverty_rate_25, poverty_rate_50, poverty_rate_80, credit_ratings, economic_warning, economic_freedom_index_green, economic_freedom_index_red, economic_freedom_score_green,
			economic_freedom_score_red, small_rating_green, small_rating_red)

		self.intelligence_Menu = intelligence_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame, intelligence_overview_background, intelligency_agencies_icons_image_dic)

		self.Research_Menu = Research_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame, research_overview_background, researche_icons_image_dic,
			researche_institute_icons_image_dic, active_research_background)
		
		self.Global_Market_Menu = Global_Market_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame)

		self.Construction_Menu = Construction_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame, construction_overview_background)

		self.Production_Menu = Production_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame, production_overview_background)

		self.Army_Menu = Army_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame)

		self.Stockpile_Menu = Stockpile_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame)

		self.menu_list = [self.Country_Overview, self.Country_Focus_Tree, self.Decisions_Menu, self.Laws_Menu, self.Finances_Menu, self.intelligence_Menu, self.Research_Menu, self.Global_Market_Menu, self.Construction_Menu, self.Production_Menu, self.Army_Menu, self.Stockpile_Menu]					

		
		self.Game_Introduction_Menu = Game_Introduction_Menu(self.factor_x, self.factor_y, screen_width, screen_height, pygame, game_logo)

		self.County_Overview = County_Overview(self.factor_x, self.factor_y, screen_width, screen_height, pygame)

		#-----------#

		self.Clock_UI.Player_Country_Research_Menu = self.Research_Menu

	def get_button_by_interaction(self, mouse_rect, index):
		if index == 'Country_Overview':
			button = self.Country_Overview.get_button_by_interaction(mouse_rect)
			return button
		elif index == 'Bottom_HUD':
			button = self.Bottom_HUD.get_button_by_interaction(mouse_rect)
			return button
		elif index == 'Country_Focus_Tree':
			button = self.Country_Focus_Tree.get_button_by_interaction(mouse_rect)
			return button	
		elif index == 'Decisions_Menu':
			button = self.Decisions_Menu.get_button_by_interaction(mouse_rect)
			return button				
		elif index == 'Laws_Menu':
			button = self.Laws_Menu.get_button_by_interaction(mouse_rect)
			return button
		elif index == 'Finances_Menu':
			button = self.Finances_Menu.get_button_by_interaction(mouse_rect)
			return button	
		elif index == 'intelligence_Menu':
			button = self.intelligence_Menu.get_button_by_interaction(mouse_rect)
			return button	
		elif index == 'Research_Menu':
			button = self.Research_Menu.get_button_by_interaction(mouse_rect)
			return button				
		elif index == 'Global_Market_Menu':
			button = self.Global_Market_Menu.get_button_by_interaction(mouse_rect)
			return button
		elif index == 'Construction_Menu':
			button = self.Construction_Menu.get_button_by_interaction(mouse_rect)
			return button		
		elif index == 'Production_Menu':
			button = self.Production_Menu.get_button_by_interaction(mouse_rect)
			return button
		elif index == 'Army_Menu':
			button = self.Army_Menu.get_button_by_interaction(mouse_rect)
			return button	
		elif index == 'Stockpile_Menu':
			button = self.Stockpile_Menu.get_button_by_interaction(mouse_rect)
			return button		
		elif index == 'Game_Introduction_Menu':
			button = self.Game_Introduction_Menu.get_button_by_interaction(mouse_rect)
			return button						
		
	def get_clicked_button(self, mouse_rect):
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Country_Overview')
		if clicked_button != None:

			if self.Country_Overview.is_menu_open == False:
				for menu in self.menu_list:
					menu.is_menu_open = False
															
				self.Country_Overview.is_menu_open = True
		
			elif self.Country_Overview.is_menu_open == True:
				self.Country_Overview.is_menu_open = False

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Country_Focus_Tree')
		if clicked_button != None:
			if clicked_button == "focus_tree":
				if self.Country_Focus_Tree.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False					
					self.Country_Focus_Tree.is_menu_open = True
			
				elif self.Country_Focus_Tree.is_menu_open == True:
					self.Country_Focus_Tree.is_menu_open = False	
			elif clicked_button == "choice_button":
				self.Country_Focus_Tree.keep_game_paused = False
				self.Country_Focus_Tree.focus_wating_player_path_selection = None
			elif clicked_button == "accept_button":
				self.Country_Focus_Tree.keep_game_paused = False
				self.Country_Focus_Tree.focus_to_remove.append(self.Country_Focus_Tree.focus_completion_wating_player_visualization.focus_id)
				self.Country_Focus_Tree.focus_completion_wating_player_visualization = None

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button		
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Decisions_Menu')
		if clicked_button != None:
			if clicked_button == "decisions_button":
				if self.Decisions_Menu.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False

					self.Decisions_Menu.is_menu_open = True

				elif self.Decisions_Menu.is_menu_open == True:
					self.Decisions_Menu.is_menu_open = False

			elif clicked_button == "open_decision_tree_button":
				self.Decisions_Menu.is_decision_tree_menu_open = not self.Decisions_Menu.is_decision_tree_menu_open

			elif clicked_button == "decision_button":
				self.Decisions_Menu.clicked_decision_button = True

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Laws_Menu')
		if clicked_button != None:
			if clicked_button == "laws_button":
				if self.Laws_Menu.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False

					self.Laws_Menu.is_menu_open = True
			
				elif self.Laws_Menu.is_menu_open == True:
					self.Laws_Menu.is_menu_open = False
					self.Laws_Menu.selected_law_group_index = None
			elif clicked_button[-1].isalnum():
				self.Laws_Menu.selected_law_group_index = clicked_button

			elif clicked_button == "rect_law_button":
				pass

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Finances_Menu')
		if clicked_button != None:
			if clicked_button == "finances_button":
				if self.Finances_Menu.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False

					self.Finances_Menu.is_menu_open = True

				elif self.Finances_Menu.is_menu_open == True:
					self.Finances_Menu.is_menu_open = False

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'intelligence_Menu')
		if clicked_button != None:
			if clicked_button == "intelligence_button":
				if self.intelligence_Menu.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False

					self.intelligence_Menu.is_menu_open = True

				elif self.intelligence_Menu.is_menu_open == True:
					self.intelligence_Menu.is_menu_open = False

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Research_Menu')
		if clicked_button != None:
			if clicked_button == "research_button":
				if self.Research_Menu.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False

					self.Research_Menu.is_menu_open = True

				elif self.Research_Menu.is_menu_open == True:
					self.Research_Menu.is_menu_open = False
			
			elif clicked_button == "warfare_tech_tree_button":
				self.Research_Menu.open_tech_tree = "warfare_tech_tree_button" if self.Research_Menu.open_tech_tree != "warfare_tech_tree_button" else None
			elif clicked_button == "transport_tech_tree_button":
				self.Research_Menu.open_tech_tree = "transport_tech_tree_button" if self.Research_Menu.open_tech_tree != "transport_tech_tree_button" else None
			elif clicked_button == "science_tech_tree_button":
				self.Research_Menu.open_tech_tree = "science_tech_tree_button" if self.Research_Menu.open_tech_tree != "science_tech_tree_button" else None
			elif clicked_button == "technology_tech_tree_button":
				self.Research_Menu.open_tech_tree = "technology_tech_tree_button" if self.Research_Menu.open_tech_tree != "technology_tech_tree_button" else None
			elif clicked_button == "medical_tech_tree_button":
				self.Research_Menu.open_tech_tree = "medical_tech_tree_button" if self.Research_Menu.open_tech_tree != "medical_tech_tree_button" else None
			elif clicked_button == "society_tech_tree_button":
				self.Research_Menu.open_tech_tree = "society_tech_tree_button" if self.Research_Menu.open_tech_tree != "society_tech_tree_button" else None

			elif type(clicked_button) == tuple:
				if clicked_button[0] == "selected_workers_text_box":
					clicked_button[1].selected_budget_text_box = False
					clicked_button[1].selected_assign_institute_box = False
					clicked_button[1].selected_workers_text_box = True
					self.Research_Menu.receive_player_keybord_input = True
				elif clicked_button[0] == "assign_budget_box_rect":
					clicked_button[1].selected_workers_text_box = False
					clicked_button[1].selected_assign_institute_box = False
					clicked_button[1].selected_budget_text_box = True
					self.Research_Menu.receive_player_keybord_input = True	
				elif clicked_button[0] == "assign_institute_box_rect":
					clicked_button[1].selected_workers_text_box = False
					clicked_button[1].selected_budget_text_box = False
					clicked_button[1].selected_assign_institute_box = not clicked_button[1].selected_assign_institute_box
					self.Research_Menu.research_project_to_assing_institute = clicked_button[1]
					self.Research_Menu.receive_player_keybord_input = False	
					self.Research_Menu.is_assign_institutes_menu_open = not self.Research_Menu.is_assign_institutes_menu_open 		
				elif clicked_button[0] == "selected_research_institute_box":
					clicked_button[1].selected_workers_text_box = False
					clicked_button[1].selected_budget_text_box = False
					clicked_button[1].selected_assign_institute_box = False						
					clicked_button[1].assigned_research_institute = clicked_button[2]	
					clicked_button[1].current_project_workers_amount = 0
					self.Research_Menu.receive_player_keybord_input = False
					self.Research_Menu.is_assign_institutes_menu_open = False		
					self.Research_Menu.research_project_to_assing_institute = None		

			else: # CLICKED ON A RESEARCHE PROJECT
				if clicked_button['available'] == True:
					new_research_projects = Research_Project(clicked_button['name'], clicked_button['type'], clicked_button['icon'])
					self.Research_Menu.active_research_projects.append(new_research_projects)
					self.Research_Menu.open_tech_tree = None
					clicked_button['available'] = False

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Global_Market_Menu')
		if clicked_button != None:
			if clicked_button == "global_market_button":
				if self.Global_Market_Menu.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False

					self.Global_Market_Menu.is_menu_open = True

				elif self.Global_Market_Menu.is_menu_open == True:
					self.Global_Market_Menu.is_menu_open = False

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Construction_Menu')
		if clicked_button != None:
			if clicked_button == "construction_button":
				if self.Construction_Menu.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False

					self.Construction_Menu.is_menu_open = True

				elif self.Construction_Menu.is_menu_open == True:
					self.Construction_Menu.is_menu_open = False

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Production_Menu')
		if clicked_button != None:
			if clicked_button == "production_button":
				if self.Production_Menu.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False

					self.Production_Menu.is_menu_open = True

				elif self.Production_Menu.is_menu_open == True:
					self.Production_Menu.is_menu_open = False

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Army_Menu')
		if clicked_button != None:
			if clicked_button == "army_button":
				if self.Army_Menu.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False

					self.Army_Menu.is_menu_open = True

				elif self.Army_Menu.is_menu_open == True:
					self.Army_Menu.is_menu_open = False

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button	
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Stockpile_Menu')
		if clicked_button != None:
			if clicked_button == "stockpile_button":
				if self.Stockpile_Menu.is_menu_open == False:
					for menu in self.menu_list:
						menu.is_menu_open = False

					self.Stockpile_Menu.is_menu_open = True

				elif self.Stockpile_Menu.is_menu_open == True:
					self.Stockpile_Menu.is_menu_open = False

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Game_Introduction_Menu')
		if clicked_button != None:
			if clicked_button == "close_introduction_button":
				if self.Game_Introduction_Menu.is_menu_open == True:
					self.Game_Introduction_Menu.is_menu_open = False

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button			
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#																					
		clicked_button = self.get_button_by_interaction(mouse_rect, 'Bottom_HUD')
		if clicked_button != None:
			if type(clicked_button) is int:
				self.Earth_Map.map_overlay_index = clicked_button
				self.Bottom_HUD.active_map_overlay = clicked_button
				self.Earth_Map.update_map()

			elif type(clicked_button) is str and clicked_button[0:26] == 'country_legislation_button':
				if clicked_button != self.Bottom_HUD.open_country_legislation:
					self.Bottom_HUD.open_country_legislation = clicked_button
				else:
					self.Bottom_HUD.open_country_legislation = None					


			if self.Bottom_HUD.open_country_legislation == 'country_legislation_button_1' and clicked_button != 'country_legislation_button_1':

				self.Bottom_HUD.Legislative_Government_Menu.open_menu = None # 6

				if clicked_button != self.Bottom_HUD.Legislative_Finances_Menu.open_menu:
					self.Bottom_HUD.Legislative_Finances_Menu.open_menu = clicked_button
				else:
					self.Bottom_HUD.Legislative_Finances_Menu.open_menu = None


			elif self.Bottom_HUD.open_country_legislation == 'country_legislation_button_6' and clicked_button != 'country_legislation_button_6':

				self.Bottom_HUD.Legislative_Finances_Menu.open_menu = None # 1

				if clicked_button in ['head_of_state_menu_button', 'cabinet_menu_button', 'parliament_menu_button', 'elections_menu_button', 'political_parties_menu_button']:
					if clicked_button != self.Bottom_HUD.Legislative_Government_Menu.open_menu:
						self.Bottom_HUD.Legislative_Government_Menu.open_menu = clicked_button
						self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_opinion_civilian = None
						self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_opinion_parliament = None
						self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_opinion_senate = None							
					else:
						self.Bottom_HUD.Legislative_Government_Menu.open_menu = None
				else:
					if self.Bottom_HUD.Legislative_Government_Menu.open_menu == 'head_of_state_menu_button':
						if clicked_button == 'law_opinion_survey_menu_close_button':
							self.Bottom_HUD.Legislative_Government_Menu.is_law_opinion_survey_menu_open = False
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_opinion_civilian = None
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_opinion_parliament = None
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_opinion_senate = None							
						
						elif clicked_button in ['law_change_nomination_of_head_of_state_button', 'law_change_election_of_head_of_state_button']:
							if clicked_button != self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.law_open:
								self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.law_open = clicked_button
							else:
								self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.law_open = None
						
						else:
							if clicked_button == 'law_change_close_button':
								self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.law_change_menu_open = None
								self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_being_survey = None
							elif clicked_button == 'law_change_accept_button':
								law_group_to_be_voted = self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.get_law_group()
								law_to_be_voted = self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.get_law()
								current_date = {
									'day': self.Clock_UI.current_day,
									'month': self.Clock_UI.current_month,
									'year': self.Clock_UI.current_year
								}

								self.PlayerCountry.add_law_to_be_voted(law_group_to_be_voted, law_to_be_voted, current_date)

								self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.law_change_menu_open = None
								self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.law_open = None								

							elif clicked_button == 'law_change_survey_button':
								self.Bottom_HUD.Legislative_Government_Menu.is_law_opinion_survey_menu_open = True
								law_group_to_be_voted = self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.get_law_group()
								law_to_be_voted = self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.get_law()	

								law_group_to_be_voted = getattr(self.PlayerCountry, law_group_to_be_voted)
								if type(law_group_to_be_voted) == CountriesManager.Laws_Group:
									self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_being_survey = law_group_to_be_voted.laws[law_to_be_voted]							

							elif clicked_button == 'simple_population_survey_button':
								self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.calculate_law_opinion_civilian('simple')
							elif clicked_button == 'extensive_population_survey_button':
								self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.calculate_law_opinion_civilian('extensive')
							elif clicked_button == 'parliament_survey_button':
								self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.calculate_law_opinion_parliament(self.PlayerCountry)
							elif clicked_button == 'senate_survey_button':
								self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.calculate_law_opinion_senate(self.PlayerCountry)
							else:
								self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.law_change_menu_open = clicked_button

					elif self.Bottom_HUD.Legislative_Government_Menu.open_menu == 'parliament_menu_button':	
						if clicked_button == 'law_opinion_survey_menu_close_button':
							self.Bottom_HUD.Legislative_Government_Menu.is_law_opinion_survey_menu_open = False
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_opinion_civilian = None
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_opinion_parliament = None
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_opinion_senate = None							
						
						elif type(clicked_button) == CountriesManager.Law_Project:
							self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law = clicked_button

						elif clicked_button == 'law_change_close_button':
							try:
								self.PlayerCountry.laws_being_voted.remove(self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law)
							except:
								pass
							self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law = None

						elif clicked_button == 'law_change_accept_button':
							self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law = None
						
						elif clicked_button == 'law_change_survey_button':
							self.Bottom_HUD.Legislative_Government_Menu.is_law_opinion_survey_menu_open = True	

							law_group_to_be_voted = getattr(self.PlayerCountry, self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law.law_group_being_voted)

							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_being_survey = law_group_to_be_voted.laws[self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law.law_being_suggested]
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.law_opinion_civilian = self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law.survey_civilian_support
							if self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law.survey_parliament_support != None:
								self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.calculate_law_opinion_parliament(self.PlayerCountry, self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law)
							if self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law.survey_senate_support != None:
								self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.calculate_law_opinion_senate(self.PlayerCountry, self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law)

						elif clicked_button == 'simple_population_survey_button':
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.calculate_law_opinion_civilian('simple', self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law)
						elif clicked_button == 'extensive_population_survey_button':
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.calculate_law_opinion_civilian('extensive', self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law)
						elif clicked_button == 'parliament_survey_button':
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.calculate_law_opinion_parliament(self.PlayerCountry, self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law)
						elif clicked_button == 'senate_survey_button':
							self.Bottom_HUD.Legislative_Government_Menu.Law_Opinion_survey_Menu.calculate_law_opinion_senate(self.PlayerCountry, self.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.open_law)															

			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button	
	
	def get_hovered_button(self, mouse_rect):
		any_button_was_hovered = False

		hovered_button = self.get_button_by_interaction(mouse_rect, 'Country_Overview')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.Country_Overview.highlight_button = True

		else:
			self.Country_Overview.highlight_button = False
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Country_Focus_Tree')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			if hovered_button == "focus_tree":
				for menu in self.menu_list:
					menu.highlight_button = False				
				self.Country_Focus_Tree.highlight_button = True
			elif hovered_button == "choice_button":
				self.Country_Focus_Tree.highlight_focus_path_selection_button_index = self.Country_Focus_Tree.focus_wating_player_path_selection.selected_path
			elif hovered_button == "accept_button":
				self.Country_Focus_Tree.highlight_focus_completion_wating_player_visualization_button = True
		
		else:
			self.Country_Focus_Tree.highlight_button = False
			self.Country_Focus_Tree.highlight_focus_completion_wating_player_visualization_button = False
			self.Country_Focus_Tree.highlight_focus_path_selection_button_index = None	
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Decisions_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			if hovered_button == 'decisions_button':
				any_button_was_hovered = True

				for menu in self.menu_list:
					menu.highlight_button = False

				self.Decisions_Menu.highlight_button = True

			elif hovered_button == 'open_decision_tree_button':
				any_button_was_hovered = True

				self.Decisions_Menu.hovered_decision_tree_button = True
			
			elif hovered_button == 'decision_button':
				any_button_was_hovered = True

				self.Decisions_Menu.hovered_decision_button = True

		else:
			self.Decisions_Menu.highlight_button = False
			self.Decisions_Menu.hovered_decision_tree_button = False
			self.Decisions_Menu.hovered_decision_button = False				
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Laws_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.Laws_Menu.highlight_button = True

		else:
			self.Laws_Menu.highlight_button = False				
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#	
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Finances_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.Finances_Menu.highlight_button = True

		else:
			self.Finances_Menu.highlight_button = False				
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#	
		hovered_button = self.get_button_by_interaction(mouse_rect, 'intelligence_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.intelligence_Menu.highlight_button = True

		else:
			self.intelligence_Menu.highlight_button = False				
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#	
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Research_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.Research_Menu.highlight_button = True

			if type(hovered_button) == tuple:
				if hovered_button[0] == "selected_workers_text_box":
					hovered_button[1].hovered_budget_text_box = False
					hovered_button[1].hovered_assign_institute_box = False
					hovered_button[1].hovered_workers_text_box = True
				elif hovered_button[0] == "assign_budget_box_rect":
					hovered_button[1].hovered_workers_text_box = False
					hovered_button[1].hovered_assign_institute_box = False
					hovered_button[1].hovered_budget_text_box = True	
				elif hovered_button[0] == "assign_institute_box_rect":
					hovered_button[1].hovered_workers_text_box = False
					hovered_button[1].hovered_budget_text_box = False	
					hovered_button[1].hovered_assign_institute_box = True
				elif hovered_button[0] == "selected_research_institute_box":
					hovered_button[1].hovered_workers_text_box = False
					hovered_button[1].hovered_budget_text_box = False	
					hovered_button[1].hovered_assign_institute_box = False		
					hovered_button[2].hovered = True											

		else:
			self.Research_Menu.highlight_button = False				
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#	
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Global_Market_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.Global_Market_Menu.highlight_button = True

		else:
			self.Global_Market_Menu.highlight_button = False				
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#	
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Construction_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.Construction_Menu.highlight_button = True

		else:
			self.Construction_Menu.highlight_button = False				
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#	
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Production_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.Production_Menu.highlight_button = True

		else:
			self.Production_Menu.highlight_button = False				
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#	
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Army_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.Army_Menu.highlight_button = True

		else:
			self.Army_Menu.highlight_button = False				
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#	
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Stockpile_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.Stockpile_Menu.highlight_button = True

		else:
			self.Stockpile_Menu.highlight_button = False	
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#	
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Game_Introduction_Menu')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

			for menu in self.menu_list:
				menu.highlight_button = False

			self.Game_Introduction_Menu.highlight_button = True

		else:
			self.Game_Introduction_Menu.highlight_button = False							
		#---------------------------------------------------------------------------------------------------------------------------------------#
		#---------------------------------------------------------------------------------------------------------------------------------------#																											
		hovered_button = self.get_button_by_interaction(mouse_rect, 'Bottom_HUD')
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
			self.last_hovered_button = hovered_button

			any_button_was_hovered = True

		else:
			pass

		#---------------------------------------------------------------------------------------------------------------------------------------#	
		if any_button_was_hovered == False:
			self.last_hovered_button = None
			self.generic_hover_over_button_sound.fadeout(100)
		#---------------------------------------------------------------------------------------------------------------------------------------#	

	def draw(self, screen, mouse_rect):
		self.Earth_Map.draw(screen)		
		self.Country_Overview.draw(screen, mouse_rect)
		self.Country_Focus_Tree.draw(screen)
		self.Clock_UI.draw(screen)
		self.Bottom_HUD.draw(screen)

		self.Decisions_Menu.draw(screen)
		self.Laws_Menu.draw(screen)
		self.Finances_Menu.draw(screen)
		self.intelligence_Menu.draw(screen)
		self.Research_Menu.draw(screen)
		self.Global_Market_Menu.draw(screen)
		self.Construction_Menu.draw(screen)
		self.Production_Menu.draw(screen)
		self.Army_Menu.draw(screen)
		self.Stockpile_Menu.draw(screen)

		self.Game_Introduction_Menu.draw(screen)
		self.County_Overview.draw(screen)

# TIME
class Clock_UI:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, clock, top_bar_right_background, top_bar_game_speed_indicator, top_bar_defcon_level):

		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = None

		self.Player_Country_Research_Menu = None

		self.week = 0

		self.clock = clock

		self.top_bar_right_background = pygame.transform.smoothscale_by(top_bar_right_background, (self.factor_x, self.factor_y))
		self.top_bar_game_speed_indicator = pygame.transform.smoothscale_by(top_bar_game_speed_indicator, (self.factor_x, self.factor_y))
		self.top_bar_defcon_level = pygame.transform.smoothscale_by(top_bar_defcon_level, (self.factor_x, self.factor_y))	


		self.game_speed = 0	
		self.defcon_level = 5

		self.current_year = 1970
		self.current_month = 1
		self.current_day = 1
		self.current_hour = 1
		self.current_minute = 0

		self.days_in_each_mounth = {
			'1': 31,
			'2': 28,
			'3': 31,
			'4': 30,
			'5': 31,
			'6': 30,
			'7': 31,
			'8': 31,
			'9': 30,
			'10': 31,
			'11': 30,
			'12': 31,
		}						
		
		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))	

	def date_tick(self):
		if self.game_speed == 0:
			self.current_minute += 0
		elif self.game_speed == 1:
			self.current_minute += 1
		elif self.game_speed == 2:
			self.current_minute += 5
		elif self.game_speed == 3:
			self.current_minute += 10
		elif self.game_speed == 4:
			self.current_minute += 30
		elif self.game_speed == 5:
			self.current_minute += 120														

		if self.current_minute >= 60:
			self.current_hour += int(self.current_minute/60)

			self.Player_Country_Research_Menu.continue_research_progress += int(self.current_minute/60)
			if self.Player_Country_Research_Menu.is_menu_open == True:
				self.Player_Country_Research_Menu.increase_research_progress()

			self.current_minute = 0			
			if self.current_hour >= 24:

				self.do_daily_calculations()

				self.current_hour = self.current_hour - 24
				self.current_day += 1
				self.week += 1
				if self.week >= 7:

					self.do_weekly_calculations()
					
					self.week -= 7
				if self.current_day == self.days_in_each_mounth[str(self.current_month)] + 1:
					self.current_day = 1
					self.current_month += 1
					if self.current_month == 13:
						self.current_month = 1
						self.current_year += 1

						self.reset_graphs()

	def do_daily_calculations(self):
		if self.Player_Country_Research_Menu.is_menu_open == False:
			self.Player_Country_Research_Menu.increase_research_progress()

		self.PlayerCountry.expenses = sum([
		self.PlayerCountry.agriculture_expense,
		self.PlayerCountry.culture_expense,
		self.PlayerCountry.debt_interest_expense,
		self.PlayerCountry.defense_expense,
		self.PlayerCountry.economy_expense,
		self.PlayerCountry.education_expense,
		self.PlayerCountry.employment_social_expense,
		self.PlayerCountry.energy_expense,
		self.PlayerCountry.environment_expense,
		self.PlayerCountry.family_expense,
		self.PlayerCountry.foreign_affairs_expense,
		self.PlayerCountry.health_expense,
		self.PlayerCountry.homeland_security_expense,
		self.PlayerCountry.housing_expense,
		self.PlayerCountry.industry_expense,
		self.PlayerCountry.information_expense,
		self.PlayerCountry.justice_expense,
		self.PlayerCountry.miscellaneous_expense,
		self.PlayerCountry.religion_expense,
		self.PlayerCountry.research_expense,
		self.PlayerCountry.secret_services_expense,
		self.PlayerCountry.social_security_expense,
		self.PlayerCountry.sport_expense,
		self.PlayerCountry.tourism_expense,
		self.PlayerCountry.transport_expense,
		self.PlayerCountry.treasury_expense,
		self.PlayerCountry.unemployment_insurance_expense
		])

		for law in self.PlayerCountry.laws_being_voted:
			if law.voting_day >= self.current_day and law.voting_month >= self.current_month and law.voting_year >= self.current_year:
				self.PlayerCountry.vote_a_law(law)

	def do_weekly_calculations(self):
		self.PlayerCountry.weekly_inflation_data.append(self.PlayerCountry.inflation)

		self.PlayerCountry.weekly_currency_interest_rate_data.append(self.PlayerCountry.currency_interest_rate)

		self.PlayerCountry.weekly_country_GDP_data.append(self.PlayerCountry.country_GDP)

		debt_to_gdp = round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2)
		self.PlayerCountry.weekly_debt_to_gdp_data.append(debt_to_gdp)

		self.PlayerCountry.weekly_head_of_state_popularity_data.append(self.PlayerCountry.country_party_popularity)

	def reset_graphs(self):
		self.PlayerCountry.weekly_inflation_data = [self.PlayerCountry.inflation]

		self.PlayerCountry.weekly_currency_interest_rate_data = [self.PlayerCountry.currency_interest_rate]

		self.PlayerCountry.weekly_country_GDP_data = [self.PlayerCountry.country_GDP]

		debt_to_gdp = round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2)
		self.PlayerCountry.weekly_debt_to_gdp_data = [debt_to_gdp]	

		self.PlayerCountry.weekly_head_of_state_popularity_data = [self.PlayerCountry.country_party_popularity]

	def draw(self, screen):
		screen.blit(self.top_bar_right_background, (self.screen_width - self.top_bar_right_background.get_width(), 0))

		# SPEED
		speed_indicator_alignment_offset = 8 * self.factor_x
		speed_indicator_sprite_width = 43 * self.factor_x * self.game_speed

		top_bar_game_speed_indicator_surface = self.pygame.Surface((speed_indicator_sprite_width, self.top_bar_game_speed_indicator.get_height()), self.pygame.SRCALPHA)	
		top_bar_game_speed_indicator_surface.blit(self.top_bar_game_speed_indicator, (0, 0), self.pygame.Rect(0, 0, speed_indicator_sprite_width, self.top_bar_game_speed_indicator.get_height()))		

		screen.blit(top_bar_game_speed_indicator_surface, (self.screen_width - self.top_bar_right_background.get_width() + 62 * self.factor_x + speed_indicator_alignment_offset, 42 * self.factor_y))	

		# DEFCON
		top_bar_defcon_level_height = (18.4 * (self.defcon_level - 1) * self.factor_y)

		top_bar_defcon_level_surface = self.pygame.Surface((self.top_bar_defcon_level.get_width(), 92 * self.factor_y), self.pygame.SRCALPHA)	
		top_bar_defcon_level_surface.blit(self.top_bar_defcon_level, (0, top_bar_defcon_level_height), self.pygame.Rect(0, top_bar_defcon_level_height, self.top_bar_defcon_level.get_width(), 18.4 * self.factor_y))		

		screen.blit(top_bar_defcon_level_surface, (self.screen_width - self.top_bar_right_background.get_width() + 300 * self.factor_x, 9 * self.factor_y))	

		# DATE
		date_font_color = (255,255,255) if self.game_speed != 0 else (255,40,40)	

		hour_date_text = f"{self.current_hour:02d}H"
		day_date_text = f"{self.current_day:02d}D"
		month_date_text = f"{self.current_month:02d}M"
		year_date_text = f"{self.current_year:04d}Y"

		hour_date_render = self.medium_scalable_font.render(hour_date_text, True, date_font_color)
		day_date_render = self.medium_scalable_font.render(day_date_text, True, date_font_color)
		month_date_render = self.medium_scalable_font.render(month_date_text, True, date_font_color)
		year_date_render = self.medium_scalable_font.render(year_date_text, True, date_font_color)

		date_x_position = self.screen_width - 312 * self.factor_x
		date_y_position = 17 * self.factor_y

		screen.blit(hour_date_render, (date_x_position + (-2 + max(0, 38 - hour_date_render.get_width()))* self.factor_x, date_y_position))
		screen.blit(day_date_render, (date_x_position + (48 + max(0, 38 * self.factor_x - day_date_render.get_width()))* self.factor_x, date_y_position))
		screen.blit(month_date_render, (date_x_position + (86 + max(0, 41 * self.factor_x - month_date_render.get_width()))* self.factor_x, date_y_position))
		screen.blit(year_date_render, (date_x_position + (135 + max(0, 49 * self.factor_x - year_date_render.get_width()))* self.factor_x, date_y_position))	

		# FPS
		FPS_render = self.medium_scalable_font.render(' FPS:\n' + str(round(self.clock.get_fps(), 2)), True, (255, 255, 255))
		screen.blit(FPS_render, (self.screen_width - 190 * self.factor_x, 75 * self.factor_y))

# MAP
class Earth_Map:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, earth_daymap, earth_political_map, earth_political_map_filled, Clock_UI):
		self.factor_x = factor_x
		self.factor_y = factor_y

		self.last_zoom_factor = 1
		self.zoom_factor = 1

		self.screen_width = screen_width
		self.screen_height = screen_height

		self.Clock_UI = Clock_UI

		self.map_overlay_index = 1

		self.source_earth_daymap = earth_daymap
		self.source_earth_political_map = earth_political_map
		self.source_earth_political_map_filled = earth_political_map_filled

		self.earth_daymap = earth_daymap.copy()
		self.earth_political_map = earth_political_map.copy()
		self.earth_political_map_filled = earth_political_map_filled.copy()

		self.screen_sized_map_surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
		self._8k_sized_map_surface = pygame.Surface((self.source_earth_daymap.get_width(), self.source_earth_daymap.get_height()), pygame.SRCALPHA)	

		self.time_zone = 6.1 # 6.1 == Greenwich

		self.map_position = [0, 0]
		self.offset_y = 0

		self.update_map()

	def scale_map(self, zoom_factor_change, fps_freezing_avoidance, zoom_type):
		if fps_freezing_avoidance > 10:
			self.zoom_factor += zoom_factor_change
			if self.zoom_factor < 0.30:
				self.zoom_factor = 0.30
			if self.zoom_factor > 1.10:
				self.zoom_factor = 1.10

			if self.last_zoom_factor != self.zoom_factor:
				self.update_map()
				
				# DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER
				# DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER

				if zoom_type == 'zoom_out':
					pass
				if zoom_type == 'zoom_in':
					pass

			self.last_zoom_factor = self.zoom_factor

	def update_map(self):
		if self.map_overlay_index != None:

			if self.map_overlay_index == 1:
				self.earth_political_map = pygame.transform.smoothscale_by(self.source_earth_political_map, (self.zoom_factor))

				result_surface = pygame.Surface((self.earth_political_map.get_width(), self.earth_political_map.get_height()), pygame.SRCALPHA)

				result_surface.blit(pygame.transform.smoothscale_by(self.source_earth_daymap, (self.zoom_factor)), (0, 0))
				
				result_surface.blit(self.earth_political_map, (0, 0))
			elif self.map_overlay_index == 2:
				self.earth_political_map_filled = pygame.transform.smoothscale_by(self.source_earth_political_map_filled, (self.zoom_factor))	
				
				result_surface = pygame.Surface((self.earth_political_map_filled.get_width(), self.earth_political_map_filled.get_height()), pygame.SRCALPHA)

				result_surface.blit(pygame.transform.smoothscale_by(self.source_earth_daymap, (self.zoom_factor)), (0, 0))
				
				result_surface.blit(self.earth_political_map_filled, (0, 0))

			self.earth_daymap = result_surface.convert_alpha().copy()
			del result_surface			

	def draw(self, screen):
		self.screen_sized_map_surface.fill((0, 0, 0, 0), (0, 0, self.screen_width, self.screen_height))
		self._8k_sized_map_surface.fill((0, 0, 0, 0), (0, 0, self.screen_width, self.screen_height))

		# HEIGHT
		self.offset_y = abs(self.map_position[1]) if abs(self.map_position[1]) <  self.earth_daymap.get_height() else self.earth_daymap.get_height() - 1
		#--------------#
				

		# DAYMAP	
			
		try:
			if self.map_position[0] == 0:
				start = 0
				width = self.screen_width
				height = self.screen_height if self.screen_height + self.offset_y <= self.earth_daymap.get_height() else self.earth_daymap.get_height()
				
				if start + width > self.earth_daymap.get_width():
					width = self.earth_daymap.get_width() - start			
				if self.offset_y + height > self.earth_daymap.get_height():
					height = self.earth_daymap.get_height() - self.offset_y

				if height > 0 and width > 0:
					self.screen_sized_map_surface.blit(self.earth_daymap.subsurface((start, self.offset_y, width, height)), (0, 0))

					if self.earth_daymap.get_width() < self.screen_width:
						difference = self.screen_width - self.earth_daymap.get_width()
						width = difference
						self.screen_sized_map_surface.blit(self.earth_daymap.subsurface((0, self.offset_y, width, height)), (self.screen_width - difference, 0))
			
			if self.map_position[0] > 0:
				start = self.earth_daymap.get_width() - self.map_position[0]
				width = min(self.screen_width, self.map_position[0])
				height = self.screen_height if self.screen_height + self.offset_y <= self.earth_daymap.get_height() else self.earth_daymap.get_height()
				
				if start + width > self.earth_daymap.get_width():
					width = self.earth_daymap.get_width() - start
				if self.offset_y + height > self.earth_daymap.get_height():
					height = self.earth_daymap.get_height() - self.offset_y	

				if height > 0 and width > 0:			
					self.screen_sized_map_surface.blit(self.earth_daymap.subsurface((start, self.offset_y, width, height)), (0, 0))			
					
					if self.screen_width - self.map_position[0] > 0:
						self.screen_sized_map_surface.blit(self.earth_daymap.subsurface((0, self.offset_y, self.screen_width - self.map_position[0], height)), (abs(self.map_position[0]), 0))
			
			if self.map_position[0] < 0:
				start = max(self.screen_width, abs(self.map_position[0]))
				width = min(abs(self.map_position[0]), min(self.screen_width, self.earth_daymap.get_width() - abs(self.map_position[0])))
				height = self.screen_height if self.screen_height + self.offset_y <= self.earth_daymap.get_height() else self.earth_daymap.get_height()
				
				if start + width > self.earth_daymap.get_width():
					width = self.earth_daymap.get_width() - start
				if self.offset_y + height > self.earth_daymap.get_height():
					height = self.earth_daymap.get_height() - self.offset_y

				if height > 0 and width > 0:		
					self.screen_sized_map_surface.blit(self.earth_daymap.subsurface((start, self.offset_y, width, height)), (max(0, self.screen_width - abs(self.map_position[0])), 0))
					
					if self.screen_width - abs(self.map_position[0]) > 0:
						self.screen_sized_map_surface.blit(self.earth_daymap.subsurface((abs(self.map_position[0]), self.offset_y, self.screen_width - abs(self.map_position[0]), height)), (0, 0))
					
					if self.earth_daymap.get_width() - abs(self.map_position[0]) < self.screen_width:
						self.screen_sized_map_surface.blit(self.earth_daymap.subsurface((0, self.offset_y, self.screen_width - (self.earth_daymap.get_width() - abs(self.map_position[0])), height)), (self.earth_daymap.get_width() - abs(self.map_position[0]), 0))
		
		except:
			pass
		#--------------------------------------------------------------------------------------------------------#
		
		self._8k_sized_map_surface.blit(self.screen_sized_map_surface, (0, 0))

		screen.blit(self._8k_sized_map_surface, (0, 0))

# TOP BAR MENUS:
class Country_Overview:
	def __init__(self, factor_x, factor_y, pygame, top_bar_left_background, top_bar_flag_overlay, top_bar_flag_overlay_hovering_over, country_overview, popularity_circle_overlay,
			generic_hover_over_button_sound, progressbar, progressbar_vertical, progressbar_small):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.pygame = pygame

		self.PlayerCountry = None

		self.top_bar_left_background = pygame.transform.smoothscale_by(top_bar_left_background, (self.factor_x, self.factor_y))
		self.top_bar_left_background_rect = self.top_bar_left_background.get_rect()

		self.top_bar_flag_overlay = pygame.transform.smoothscale_by(top_bar_flag_overlay, (self.factor_x, self.factor_y))
		self.top_bar_flag_overlay_hovering_over	= pygame.transform.smoothscale_by(top_bar_flag_overlay_hovering_over, (self.factor_x, self.factor_y))	
		self.progressbar = pygame.transform.smoothscale_by(progressbar, (self.factor_x, self.factor_y))
		self.progressbar_vertical = pygame.transform.smoothscale_by(progressbar_vertical, (self.factor_x, self.factor_y))
		self.progressbar_small = pygame.transform.smoothscale_by(progressbar_small, (self.factor_x, self.factor_y))

		self.highlight_button = False
		self.is_menu_open = False

		self.country_overview = pygame.transform.smoothscale_by(country_overview, (self.factor_x, self.factor_y))
		self.popularity_circle_overlay = pygame.transform.smoothscale_by(popularity_circle_overlay, (self.factor_x, self.factor_y))
		self.country_overview_position = (0, 158 * self.factor_y)
		self.national_spirits_display_rects = []
		self.hovered_national_spirit = None	
		self.last_hovered_national_spirit = None	

		self.last_hovered_button = None

		self.hovered_rect = None
		self.last_hovered_rect = None

		self.generic_hover_over_button_sound = generic_hover_over_button_sound

		self.update_parties_pie_chart = False
		self.parties_pie_chart_surface = pygame.Surface((603 * self.factor_x, 301 * self.factor_y), pygame.SRCALPHA)

		self.official_parties_names_surface = pygame.Surface((295 * self.factor_x, 187 * self.factor_y), pygame.SRCALPHA)

		# COLORS ------------#	

		# POLITICS
		red_base = (255, 0, 0)
		blue_base =  (89, 200, 234)
		yellow_base = (255, 255, 0)
		green_base = (0, 255, 16)

		red_values = GenericUtilitys.generate_fading_colors(6, red_base)
		blue_values = GenericUtilitys.generate_fading_colors(7, blue_base)
		yellow_values = GenericUtilitys.generate_fading_colors(7, yellow_base) 
		green_values = GenericUtilitys.generate_fading_colors(4, green_base)

		self.politics_segment_colors = red_values + blue_values + yellow_values + green_values
		self.politics_popularity = None

		self.ideologies = [
			'Marxist Leninism',
			'Command Socialism',
			'Consumer Socialism',
			'Authoritarian Market Socialism',
			'Democratic Socialism',
			'Social Democracy',

			'Absolute Monarchism',
			'National Syndicalism',
			'Corporautocracy',
			'Social Statism',
			'Pinochetism',
			'Keynesianism',
			'Chicago School',

			'Social Liberalism',
			'Classical Liberalism',	
			'Social Libertarianism',
			'Libertarian Capitalism',
			'Minarcho Capitalism',
			'Voluntaryism',
			'Anarcho Capitalism',

			'Libertarian Socialism',
			'Libertarian Market Socialism',
			'Mutualism',
			'Anarcho Communism'
			]	


		# CULTURE
		redish_base = (227, 52, 47)
		gray_base = (220, 220, 220)
		blue_base = (89, 200, 234)

		red_values = GenericUtilitys.generate_fading_colors(6, redish_base)
		blue_values = GenericUtilitys.generate_fading_colors(2, gray_base)
		yellow_values = GenericUtilitys.generate_fading_colors(6, blue_base)

		self.culture_segment_colors = red_values + blue_values + yellow_values + green_values
		self.culture_popularity = None

		self.cultures = [
			'Accelerationism',
			'Ultraprogressive',
			'Progressive',
			'Environmentalism',
			'Globalism',
			'Multiculturalism',
			
			'Secularism',
			'Centrist',
			
			'Liberal',
			'Neoconservatism',
			'Conservative',
			'Reactionary',
			'Traditionalist',
			'Nationalism'
		]

		# RELIGION
		self.religion_segment_colors = [(227, 52, 47),  (246, 153, 63), (255, 237, 74),  (56, 193, 114),  (77, 192, 181),
			(52, 144, 220), (101, 116, 205),  (149, 97, 226), (246, 109, 155)]

		self.religion_popularity = None

		self.religions = [
			'Christianity',
			'Judaism',
			'Islam',
			'Hinduism',
			'Buddhism',
			'Taoism',
			'Shintoism',
			'Indigenous',
			'Atheism'
		]				

		# COLORS ------------#

		self.is_touching_cicle_rects = False
		self.politics_cicle_rects = [[(0, 0), (0, 1080), (1920, 0)]]
		
		self.culture_cicle_rects = [[(0, 0), (0, 1080), (1920, 0)]]
		
		self.religion_cicle_rects = [[(0, 0), (0, 1080), (1920, 0)]]

		self.hitted_rect = None

		self.top_bar_country_viewer_button = GenericUtilitys.Button(2 * self.factor_x, 2 * self.factor_y, 123 * self.factor_x, 74 * self.factor_y)

		self.info_height = 9 * self.factor_y

		# INFORMATION ------------#

		self.hovering_diplomatic_information_rect = False
		self.hovering_military_information_rect = False
		self.hovering_economic_information_rect = False
		self.hovering_domestic_information_rect = False	

		size_x = 168 * self.factor_x
		size_y = 14 * self.factor_y		

		self.diplomatic_information_rect = 	self.pygame.Rect(135 * self.factor_x, 38 * self.factor_y, size_x, size_y)
		self.military_information_rect = 	self.pygame.Rect(135 * self.factor_x, 57 * self.factor_y, size_x, size_y)
		self.economic_information_rect = 	self.pygame.Rect(311 * self.factor_x, 38 * self.factor_y, 160 * self.factor_x, size_y)
		self.domestic_information_rect = 	self.pygame.Rect(311 * self.factor_x, 57 * self.factor_y, 160 * self.factor_x, size_y)			


		self.hovering_military_approval_rating_rect = False
		self.hovering_domestic_approval_rating_rect = False
		self.hovering_midia_approval_rating_rect = False
		self.hovering_secret_service_approval_rating_rect = False
		self.hovering_politics_approval_rating_rect = False
		
		self.hovering_internal_and_external_market_approval_rating_rect = False

		size_x = 43 * self.factor_x
		size_y = 25 * self.factor_y
		height = 76 * self.factor_y

		self.military_approval_rating_rect = 		self.pygame.Rect(136 * self.factor_x, height, size_x, size_y)
		self.domestic_approval_rating_rect = 		self.pygame.Rect(182 * self.factor_x, height, size_x, size_y)
		self.midia_approval_rating_rect = 			self.pygame.Rect(228 * self.factor_x, height, size_x, size_y)
		self.secret_service_approval_rating_rect = 	self.pygame.Rect(274 * self.factor_x, height, size_x, size_y)
		self.politics_approval_rating_rect = 		self.pygame.Rect(320 * self.factor_x, height, size_x, size_y)

		self.internal_and_external_market_approval_rating_rect = self.pygame.Rect(370 * self.factor_x, 74 * self.factor_y, 101 * self.factor_x, 28 * self.factor_y)	

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(13 * self.factor_y))	

	def get_button_by_interaction(self, mouse_rect):
		if self.top_bar_country_viewer_button.rect.colliderect(mouse_rect):
			return "country_viewer"							

		return None																													

	def get_hovered_rect(self, mouse_rect):
		if self.top_bar_left_background_rect.colliderect(mouse_rect):
			self.hovered_rect = None

			if self.diplomatic_information_rect.colliderect(mouse_rect):
				self.hovered_rect = 1
				self.hovering_diplomatic_information_rect = True
			elif self.military_information_rect.colliderect(mouse_rect):	
				self.hovered_rect = 2
				self.hovering_military_information_rect = True
			elif self.economic_information_rect.colliderect(mouse_rect):
				self.hovered_rect = 3	
				self.hovering_economic_information_rect = True
			elif self.domestic_information_rect.colliderect(mouse_rect):
				self.hovered_rect = 4									
				self.hovering_domestic_information_rect = True

			elif self.internal_and_external_market_approval_rating_rect.colliderect(mouse_rect):
				self.hovered_rect = 5
				self.hovering_internal_and_external_market_approval_rating_rect = True

			elif self.military_approval_rating_rect.colliderect(mouse_rect):
				self.hovered_rect = 6
				self.hovering_military_approval_rating_rect = True
			elif self.domestic_approval_rating_rect.colliderect(mouse_rect):
				self.hovered_rect = 7
				self.hovering_domestic_approval_rating_rect = True
			elif self.midia_approval_rating_rect.colliderect(mouse_rect):
				self.hovered_rect = 8
				self.hovering_midia_approval_rating_rect = True
			elif self.secret_service_approval_rating_rect.colliderect(mouse_rect):
				self.hovered_rect = 9
				self.hovering_secret_service_approval_rating_rect = True
			elif self.politics_approval_rating_rect.colliderect(mouse_rect):	
				self.hovered_rect = 10											
				self.hovering_politics_approval_rating_rect = True

			if self.hovered_rect != None:
				if self.last_hovered_rect != self.hovered_rect:
					self.generic_hover_over_button_sound.play()
					self.last_hovered_rect = self.hovered_rect
			else:
				self.last_hovered_rect = None
				self.generic_hover_over_button_sound.fadeout(100)

		if self.is_menu_open == True:
			self.is_touching_cicle_rects = False
			if mouse_rect[1] - self.country_overview_position[1] > 441 * self.factor_y and mouse_rect[1] - self.country_overview_position[1] < 608 * self.factor_y:
				if  mouse_rect[0] > 60 * self.factor_x and  mouse_rect[0] < 227 * self.factor_x:
					for index, rect in enumerate(self.politics_cicle_rects):
						if GenericUtilitys.polygon_intersects_rectangle(rect, mouse_rect):
							self.hitted_rect = [index, 'politics']
							self.is_touching_cicle_rects = True
							return
				elif  mouse_rect[0] > 350 * self.factor_x and  mouse_rect[0] < 517 * self.factor_x:
					for index, rect in enumerate(self.culture_cicle_rects):
						if GenericUtilitys.polygon_intersects_rectangle(rect, mouse_rect):
							self.hitted_rect = [index, 'culture']
							self.is_touching_cicle_rects = True
							return	
				elif  mouse_rect[0] > 637 * self.factor_x and  mouse_rect[0] < 804 * self.factor_x:			
					for index, rect in enumerate(self.religion_cicle_rects):
						if GenericUtilitys.polygon_intersects_rectangle(rect, mouse_rect):
							self.hitted_rect = [index, 'religion']
							self.is_touching_cicle_rects = True
							return	

			for rect, national_spirit in self.national_spirits_display_rects:
				if rect.colliderect(mouse_rect):
					self.hovered_national_spirit = national_spirit
					if national_spirit != self.last_hovered_national_spirit:
						self.last_hovered_national_spirit = national_spirit
						self.generic_hover_over_button_sound.play()
					return national_spirit
			self.last_hovered_national_spirit = None
			self.hovered_national_spirit = None													

		else:
			self.is_touching_politics_cicle_rects = False
			self.is_touching_culture_cicle_rects = False
			self.is_touching_religion_cicle_rects = False

	def draw(self, screen, mouse_rect):
		screen.blit(self.top_bar_left_background, (0 * self.factor_x, 0 * self.factor_y))
		if self.PlayerCountry.country_flag_image.get_size() != self.top_bar_flag_overlay.get_size():
			self.PlayerCountry.country_flag_image = self.pygame.transform.smoothscale(self.PlayerCountry.country_flag_image, (115 * self.factor_x, 66 * self.factor_y))
		screen.blit(self.PlayerCountry.country_flag_image, (5 * self.factor_x, 5 * self.factor_y))

		if self.highlight_button == False and self.is_menu_open == False:
			screen.blit(self.top_bar_flag_overlay, (2 * self.factor_x, 2 * self.factor_y))
		else:
			screen.blit(self.top_bar_flag_overlay_hovering_over, (2 * self.factor_x, 2 * self.factor_y))

		#----------------------------------------------------------------------------------------------------------------------------------------#
		# TOP BAR INFOS
			
		diplomacy_rating = int((self.progressbar.get_width()/100) * self.PlayerCountry.diplomacy_rating)
		screen.blit(self.progressbar.subsurface((0, 0, diplomacy_rating, self.progressbar.get_height())), (210 * self.factor_x, 41 * self.factor_y))

		military_rating = int((self.progressbar.get_width()/100) * self.PlayerCountry.military_rating)	
		screen.blit(self.progressbar.subsurface((0, 0, military_rating, self.progressbar.get_height())), (210 * self.factor_x, 60 * self.factor_y))
		
		economy_rating = int((self.progressbar.get_width()/100) * self.PlayerCountry.economy_rating)
		screen.blit(self.progressbar.subsurface((0, 0, economy_rating, self.progressbar.get_height())), (378 * self.factor_x, 41 * self.factor_y))

		domestic_rating = int((self.progressbar.get_width()/100) * self.PlayerCountry.domestic_rating)	
		screen.blit(self.progressbar.subsurface((0, 0, domestic_rating, self.progressbar.get_height())), (378 * self.factor_x, 60 * self.factor_y))		


		internal_economy_rating = int((self.progressbar_small.get_width()/100) * self.PlayerCountry.internal_economy_rating)
		screen.blit(self.progressbar_small.subsurface((0, 0, internal_economy_rating, self.progressbar_small.get_height())), (401 * self.factor_x, 76 * self.factor_y))

		external_economy_rating = int((self.progressbar_small.get_width()/100) * self.PlayerCountry.external_economy_rating)	
		screen.blit(self.progressbar_small.subsurface((0, 0, external_economy_rating, self.progressbar_small.get_height())), (401 * self.factor_x, 91 * self.factor_y))

			# 	VERTICAL
		height = 77 * self.factor_y
		military_approval_rating = int((self.progressbar_vertical.get_height()/100) * self.PlayerCountry.military_approval_rating)	
		screen.blit(self.progressbar_vertical.subsurface((0, self.progressbar_vertical.get_height() - military_approval_rating, self.progressbar_vertical.get_width(), military_approval_rating)), (173 * self.factor_x, height + self.progressbar_vertical.get_height() - military_approval_rating))

		domestic_approval_rating = int((self.progressbar_vertical.get_height()/100) * self.PlayerCountry.domestic_approval_rating)	
		screen.blit(self.progressbar_vertical.subsurface((0, self.progressbar_vertical.get_height() - domestic_approval_rating, self.progressbar_vertical.get_width(), domestic_approval_rating)), (219 * self.factor_x, height + self.progressbar_vertical.get_height() - domestic_approval_rating))
		
		midia_approval_rating = int((self.progressbar_vertical.get_height()/100) * self.PlayerCountry.midia_approval_rating)
		screen.blit(self.progressbar_vertical.subsurface((0, self.progressbar_vertical.get_height() - midia_approval_rating, self.progressbar_vertical.get_width(), midia_approval_rating)), (265 * self.factor_x, height + self.progressbar_vertical.get_height() - midia_approval_rating))

		secret_service_approval_rating = int((self.progressbar_vertical.get_height()/100) * self.PlayerCountry.secret_service_approval_rating)	
		screen.blit(self.progressbar_vertical.subsurface((0, self.progressbar_vertical.get_height() - secret_service_approval_rating, self.progressbar_vertical.get_width(), secret_service_approval_rating)), (311 * self.factor_x, height + self.progressbar_vertical.get_height() - secret_service_approval_rating))	

		politics_approval_rating = int((self.progressbar_vertical.get_height()/100) * self.PlayerCountry.politics_approval_rating)	
		screen.blit(self.progressbar_vertical.subsurface((0, self.progressbar_vertical.get_height() - politics_approval_rating, self.progressbar_vertical.get_width(), politics_approval_rating)), (357 * self.factor_x, height + self.progressbar_vertical.get_height() - politics_approval_rating))				


		## STABILITY
		text_country_stability = self.small_scalable_font.render(str(self.PlayerCountry.country_stability)+'%', True, (255, 255, 255))
		text_country_stability_position = (165 * self.factor_x, self.info_height)	
		screen.blit(text_country_stability, text_country_stability_position)
		## WAR SUPPORT
		text_country_war_support = self.small_scalable_font.render(str(self.PlayerCountry.country_war_support)+'%', True, (255, 255, 255))
		text_country_war_support_position = (265 * self.factor_x, self.info_height)	
		screen.blit(text_country_war_support, text_country_war_support_position)
		## PARTY POPULARITY
		text_country_party_popularity = self.small_scalable_font.render(str(self.PlayerCountry.country_party_popularity)+'%', True, (255, 255, 255))
		text_country_party_popularity_position = (350 * self.factor_x, self.info_height)	
		screen.blit(text_country_party_popularity, text_country_party_popularity_position)	

		## LAND MANPOWER
		manpower = self.PlayerCountry.country_land_manpower
		if manpower >= 1000000:
			formatted_manpower = f'{manpower / 1000000:.1f} M'
		elif manpower >= 1000:
			formatted_manpower = f'{manpower / 1000:.1f} K'
		else:
			formatted_manpower = str(manpower)
	
		text_country_land_manpower = self.small_scalable_font.render(formatted_manpower, True, (255, 255, 255))
		text_country_land_manpower_position = (451 * self.factor_x, self.info_height)	
		screen.blit(text_country_land_manpower, text_country_land_manpower_position)
		
		## AIR MANPOWER
		manpower = self.PlayerCountry.country_air_manpower
		if manpower >= 1000000:
			formatted_manpower = f'{manpower / 1000000:.1f} M'
		elif manpower >= 1000:
			formatted_manpower = f'{manpower / 1000:.1f} K'
		else:
			formatted_manpower = str(manpower)

		text_country_air_manpower = self.small_scalable_font.render(formatted_manpower, True, (255, 255, 255))
		text_country_air_manpower_position = (568 * self.factor_x, self.info_height)	
		screen.blit(text_country_air_manpower, text_country_air_manpower_position)

		## COUNTRY GDP
		GDP = self.PlayerCountry.country_GDP
		if abs(GDP) < 1e6:
			formatted_GDP = f"GDP:  ${GDP:,.2f}"
		elif abs(GDP) < 1e9:
			formatted_GDP = f"GDP:  ${GDP / 1e6:.3f} M"
		elif abs(GDP) < 1e12:
			formatted_GDP = f"GDP:  ${GDP / 1e9:.3f} B"
		elif abs(GDP) < 1e15:
			formatted_GDP = f"GDP:  ${GDP / 1e12:.3f} T"
		else:
			formatted_GDP = f"GDP:  ${GDP:.2f}"
			
		text_country_GDP = self.small_scalable_font.render(formatted_GDP, True, (255, 255, 255))
		text_country_GDP_position = (718 * self.factor_x, self.info_height)	
		screen.blit(text_country_GDP, text_country_GDP_position)	


		## INCOME
		income = self.PlayerCountry.income
		if abs(income) < 1e6:
			formatted_money = f"INCO:  ${income:,.2f}"
		elif abs(income) < 1e9:
			formatted_money = f"INCO:  ${income / 1e6:.3f} M"
		elif abs(income) < 1e12:
			formatted_money = f"INCO:  ${income / 1e9:.3f} B"
		elif abs(income) < 1e15:
			formatted_money = f"INCO:  ${income / 1e12:.3f} T"
		else:
			formatted_money = f"INCO:  ${income:.2f}"
		
		text_income = self.small_scalable_font.render(formatted_money, True, (255, 255, 255))
		text_income_position = (748 * self.factor_x, 40 * self.factor_y)	
		screen.blit(text_income, text_income_position)

		## EXPENSES
		expenses = self.PlayerCountry.expenses
		if abs(expenses) < 1e6:
			formatted_money = f"EXPE:  ${expenses:,.2f}"
		elif abs(expenses) < 1e9:
			formatted_money = f"EXPE:  ${expenses / 1e6:.3f} M"
		elif abs(expenses) < 1e12:
			formatted_money = f"EXPE:  ${expenses / 1e9:.3f} B"
		elif abs(expenses) < 1e15:
			formatted_money = f"EXPE:  ${expenses / 1e12:.3f} T"
		else:
			formatted_money = f"EXPE:  ${expenses:.2f}"
		
		text_expenses = self.small_scalable_font.render(formatted_money, True, (255, 255, 255))
		text_expenses_position = (748 * self.factor_x, 59 * self.factor_y)	
		screen.blit(text_expenses, text_expenses_position)	


		if self.hovering_diplomatic_information_rect == True:
			pygame.draw.rect(screen, (255,255,255), self.diplomatic_information_rect, 2)
			hovering_diplomatic_information_description_title_text = self.small_scalable_font.render("DIPLOMATIC INFORMATION", True, (255, 255, 255))
			text_position = (mouse_rect[0]+20 * self.factor_x + hovering_diplomatic_information_description_title_text.get_width(), mouse_rect[1] + 20)

			hovering_diplomatic_information_description_text = self.tiny_scalable_font.render("\n\n    SOMETHING: 100% \n\n    SOMETHING: 80% \n\n    SOMETHING: 60%", True, (255, 255, 255))	
			
			pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x - hovering_diplomatic_information_description_title_text.get_width(), text_position[1], hovering_diplomatic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_diplomatic_information_description_title_text.get_height()+30 * self.factor_y + hovering_diplomatic_information_description_text.get_height()))
			pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x - hovering_diplomatic_information_description_title_text.get_width(), text_position[1], hovering_diplomatic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_diplomatic_information_description_title_text.get_height()+30 * self.factor_y + hovering_diplomatic_information_description_text.get_height()), 4)				
			
			screen.blit(hovering_diplomatic_information_description_title_text, (text_position[0] - hovering_diplomatic_information_description_title_text.get_width()/2 +10 * self.factor_x, text_position[1]+12 * self.factor_y))
			screen.blit(hovering_diplomatic_information_description_text, (text_position[0] - hovering_diplomatic_information_description_title_text.get_width(), text_position[1]+15 * self.factor_y + hovering_diplomatic_information_description_title_text.get_height()))	
		if self.hovering_military_information_rect == True:
			pygame.draw.rect(screen, (255,255,255), self.military_information_rect, 2)
			hovering_military_information_description_title_text = self.small_scalable_font.render("MILITARY INFORMATION", True, (255, 255, 255))
			text_position = (mouse_rect[0]+20 * self.factor_x + hovering_military_information_description_title_text.get_width(), mouse_rect[1] + 20)

			manpower = self.PlayerCountry.army_staff
			if manpower >= 1000000:
				formatted_manpower = f'{manpower / 1000000:.1f} M'
			elif manpower >= 1000:
				formatted_manpower = f'{manpower / 1000:.1f} K'
			else:
				formatted_manpower = str(manpower)
			hovering_military_information_description_text = self.tiny_scalable_font.render(f"\n\n    ARMY STAFF: \n\n    PRODUCTION CAPACITY: ", True, (255, 255, 255))	
			hovering_military_information_description_values_text = self.tiny_scalable_font.render(f"\n\n                {formatted_manpower} \n\n                {self.PlayerCountry.production_capacity_total}", True, (255, 255, 255))	

			pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x - hovering_military_information_description_title_text.get_width(), text_position[1], hovering_military_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_military_information_description_title_text.get_height()+30 * self.factor_y + hovering_military_information_description_text.get_height()))
			pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x - hovering_military_information_description_title_text.get_width(), text_position[1], hovering_military_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_military_information_description_title_text.get_height()+30 * self.factor_y + hovering_military_information_description_text.get_height()), 4)				
			
			screen.blit(hovering_military_information_description_title_text, (text_position[0] - hovering_military_information_description_title_text.get_width()/2 +10 * self.factor_x, text_position[1]+12 * self.factor_y))
			screen.blit(hovering_military_information_description_text, (text_position[0] - hovering_military_information_description_title_text.get_width(), text_position[1]+15 * self.factor_y + hovering_military_information_description_title_text.get_height()))
			screen.blit(hovering_military_information_description_values_text, (text_position[0] - hovering_military_information_description_title_text.get_width() + 140 * self.factor_x, text_position[1]+15 * self.factor_y + hovering_military_information_description_title_text.get_height()))								
		if self.hovering_economic_information_rect == True:
			pygame.draw.rect(screen, (255,255,255), self.economic_information_rect, 2)
			hovering_economic_information_description_title_text = self.small_scalable_font.render("ECONOMIC INFORMATION", True, (255, 255, 255))
			text_position = (mouse_rect[0]+20 * self.factor_x + hovering_economic_information_description_title_text.get_width(), mouse_rect[1] + 20)

			treasury = self.PlayerCountry.treasury
			if abs(treasury) < 1e6:
				formatted_treasury = f"${treasury:,.3f}"
			elif abs(treasury) < 1e9:
				formatted_treasury = f"${treasury / 1e6:.3f} M"
			elif abs(treasury) < 1e12:
				formatted_treasury = f"${treasury / 1e9:.3f} B"
			elif abs(treasury) < 1e15:
				formatted_treasury = f"${treasury / 1e12:.3f} T"
			else:
				formatted_treasury = f"${treasury:.3f}"

			debt = self.PlayerCountry.debt
			if abs(debt) < 1e6:
				formatted_debt = f"${debt:,.3f}"
			elif abs(debt) < 1e9:
				formatted_debt = f"${debt / 1e6:.3f} M"
			elif abs(debt) < 1e12:
				formatted_debt = f"${debt / 1e9:.3f} B"
			elif abs(debt) < 1e15:
				formatted_debt = f"${debt / 1e12:.3f} T"
			else:
				formatted_debt = f"${debt:.3f}"				

			hovering_economic_information_description_text = self.tiny_scalable_font.render(f"\n\n    TREASURY: \n\n    GDP/c: \n\n    DEBT: \n\n\n        CREDIT RATING: \n\n        INFLATION: \n\n        UNEMPLOYMENT: ", True, (255, 255, 255))	
			hovering_economic_information_description_values_text = self.tiny_scalable_font.render(f"\n\n{formatted_treasury} \n\n${self.PlayerCountry.country_GDP/self.PlayerCountry.country_population:,.2f}\n\n{formatted_debt}\n\n\n        {self.PlayerCountry.credit_rating}%\n\n        {self.PlayerCountry.inflation}%\n\n        {self.PlayerCountry.unemployment}%", True, (255, 255, 255))
			
			pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x - hovering_economic_information_description_title_text.get_width(), text_position[1], hovering_economic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_economic_information_description_title_text.get_height()+30 * self.factor_y + hovering_economic_information_description_text.get_height()))
			pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x - hovering_economic_information_description_title_text.get_width(), text_position[1], hovering_economic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_economic_information_description_title_text.get_height()+30 * self.factor_y + hovering_economic_information_description_text.get_height()), 4)				
			
			screen.blit(hovering_economic_information_description_title_text, (text_position[0] - hovering_economic_information_description_title_text.get_width()/2 +10 * self.factor_x, text_position[1]+12 * self.factor_y))
			screen.blit(hovering_economic_information_description_text, (text_position[0] - hovering_economic_information_description_title_text.get_width(), text_position[1]+15 * self.factor_y + hovering_economic_information_description_title_text.get_height()))
			screen.blit(hovering_economic_information_description_values_text, (text_position[0] - hovering_economic_information_description_title_text.get_width() + 135 * self.factor_x, text_position[1]+15 * self.factor_y + hovering_economic_information_description_title_text.get_height()))
		if self.hovering_domestic_information_rect == True:
			pygame.draw.rect(screen, (255,255,255), self.domestic_information_rect, 2)
			hovering_domestic_information_description_title_text = self.small_scalable_font.render("DOMESTIC INFORMATION", True, (255, 255, 255))
			text_position = (mouse_rect[0]+20 * self.factor_x + hovering_domestic_information_description_title_text.get_width(), mouse_rect[1] + 20)

			population_formated = locale.format_string("%d", self.PlayerCountry.country_population, grouping=True)
			country_immigration_formated = locale.format_string("%d", self.PlayerCountry.country_immigration, grouping=True)
			country_emigration_formated = locale.format_string("%d", self.PlayerCountry.country_emigration, grouping=True)
			country_births_formated = locale.format_string("%d", self.PlayerCountry.country_births, grouping=True)			
			country_deaths_formated = locale.format_string("%d", self.PlayerCountry.country_deaths, grouping=True)
			
			hovering_domestic_information_description_text = self.tiny_scalable_font.render(f"\n\n    POPULATION: \n\n      IMMIGRATION: \n\n      EMIGRATION: \n\n      BIRTHS: \n\n      DEATHS: \n\n      LITERACY RATE: \n\n\n    POPULATION POLITICAL LEANING: ", True, (255, 255, 255))	
			hovering_domestic_information_description_values_text = self.tiny_scalable_font.render(f"\n\n{population_formated} \n\n    {country_immigration_formated} \n\n    {country_emigration_formated} \n\n    {country_births_formated} \n\n    {country_deaths_formated} \n\n    {self.PlayerCountry.country_literacy_rate}% \n\n\n                        {self.PlayerCountry.population_political_leaning}", True, (255, 255, 255))
			
			pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x - hovering_domestic_information_description_title_text.get_width(), text_position[1], hovering_domestic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_domestic_information_description_title_text.get_height()+30 * self.factor_y + hovering_domestic_information_description_text.get_height()))
			pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x - hovering_domestic_information_description_title_text.get_width(), text_position[1], hovering_domestic_information_description_title_text.get_width()*2 + 24 * self.factor_x, hovering_domestic_information_description_title_text.get_height()+30 * self.factor_y + hovering_domestic_information_description_text.get_height()), 4)				
			
			screen.blit(hovering_domestic_information_description_title_text, (text_position[0] - hovering_domestic_information_description_title_text.get_width()/2 +10 * self.factor_x, text_position[1]+12 * self.factor_y))
			screen.blit(hovering_domestic_information_description_text, (text_position[0] - hovering_domestic_information_description_title_text.get_width(), text_position[1]+15 * self.factor_y + hovering_domestic_information_description_title_text.get_height()))			
			screen.blit(hovering_domestic_information_description_values_text, (text_position[0] - hovering_domestic_information_description_title_text.get_width() + 160 * self.factor_x, text_position[1]+15 * self.factor_y + hovering_domestic_information_description_title_text.get_height()))			
		
		self.hovering_diplomatic_information_rect = False
		self.hovering_military_information_rect = False
		self.hovering_economic_information_rect = False
		self.hovering_domestic_information_rect = False	


		if self.hovering_internal_and_external_market_approval_rating_rect == True:
			pygame.draw.rect(screen, (255,255,255), self.internal_and_external_market_approval_rating_rect, 3)
			hovering_internal_and_external_market_approval_rating_rect = self.small_scalable_font.render(f"INTERNAL MARKET APPROVAL RATING:  {self.PlayerCountry.internal_economy_rating}%\n\nEXTERNAL MARKET APPROVAL RATING:  {self.PlayerCountry.external_economy_rating}%", True, (255, 255, 255))
			text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
			
			pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_internal_and_external_market_approval_rating_rect.get_width()+24 * self.factor_x, hovering_internal_and_external_market_approval_rating_rect.get_height()+10 * self.factor_y))
			pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_internal_and_external_market_approval_rating_rect.get_width()+24 * self.factor_x, hovering_internal_and_external_market_approval_rating_rect.get_height()+10 * self.factor_y), 2)				
			
			screen.blit(hovering_internal_and_external_market_approval_rating_rect, (text_position[0], text_position[1]+6 * self.factor_y))	
		self.hovering_internal_and_external_market_approval_rating_rect = False


		if self.hovering_military_approval_rating_rect == True:
			pygame.draw.rect(screen, (255,255,255), self.military_approval_rating_rect, 3)
			hovering_military_approval_rating_description_text = self.small_scalable_font.render(f"MILITARY APPROVAL RATING:  {self.PlayerCountry.military_approval_rating}%", True, (255, 255, 255))
			text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
			
			pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_military_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_military_approval_rating_description_text.get_height()+10 * self.factor_y))
			pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_military_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_military_approval_rating_description_text.get_height()+10 * self.factor_y), 3)				
			
			screen.blit(hovering_military_approval_rating_description_text, (text_position[0], text_position[1]+6 * self.factor_y))	
		if self.hovering_domestic_approval_rating_rect == True:
			pygame.draw.rect(screen, (255,255,255), self.domestic_approval_rating_rect, 3)
			hovering_domestic_approval_rating_description_text = self.small_scalable_font.render(f"DOMESTIC APPROVAL RATING:  {self.PlayerCountry.domestic_approval_rating}%", True, (255, 255, 255))
			text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
			
			pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_domestic_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_domestic_approval_rating_description_text.get_height()+10 * self.factor_y))
			pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_domestic_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_domestic_approval_rating_description_text.get_height()+10 * self.factor_y), 3)				
			
			screen.blit(hovering_domestic_approval_rating_description_text, (text_position[0], text_position[1]+6 * self.factor_y))	
		if self.hovering_midia_approval_rating_rect == True:
			pygame.draw.rect(screen, (255,255,255), self.midia_approval_rating_rect, 3)
			hovering_midia_approval_rating_description_text = self.small_scalable_font.render(f"MIDIA APPROVAL RATING:  {self.PlayerCountry.midia_approval_rating}%", True, (255, 255, 255))
			text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
			
			pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_midia_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_midia_approval_rating_description_text.get_height()+10 * self.factor_y))
			pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_midia_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_midia_approval_rating_description_text.get_height()+10 * self.factor_y), 3)				
			
			screen.blit(hovering_midia_approval_rating_description_text, (text_position[0], text_position[1]+6 * self.factor_y))	
		if self.hovering_secret_service_approval_rating_rect == True:
			pygame.draw.rect(screen, (255,255,255), self.secret_service_approval_rating_rect, 3)
			hovering_secret_service_approval_description_text = self.small_scalable_font.render(f"SECRET SERVICE APPROVAL RATING:  {self.PlayerCountry.secret_service_approval_rating}%", True, (255, 255, 255))
			text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
			
			pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_secret_service_approval_description_text.get_width()+24 * self.factor_x, hovering_secret_service_approval_description_text.get_height()+10 * self.factor_y))
			pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_secret_service_approval_description_text.get_width()+24 * self.factor_x, hovering_secret_service_approval_description_text.get_height()+10 * self.factor_y), 3)				
			
			screen.blit(hovering_secret_service_approval_description_text, (text_position[0], text_position[1]+6 * self.factor_y))	
		if self.hovering_politics_approval_rating_rect == True:
			pygame.draw.rect(screen, (255,255,255), self.politics_approval_rating_rect, 3)
			hovering_politics_approval_rating_description_text = self.small_scalable_font.render(f"POLITICIANS APPROVAL RATING:  {self.PlayerCountry.politics_approval_rating}%", True, (255, 255, 255))
			text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
			
			pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_politics_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_politics_approval_rating_description_text.get_height()+10 * self.factor_y))
			pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_politics_approval_rating_description_text.get_width()+24 * self.factor_x, hovering_politics_approval_rating_description_text.get_height()+10 * self.factor_y), 3)				
			
			screen.blit(hovering_politics_approval_rating_description_text, (text_position[0], text_position[1]+6 * self.factor_y))													


		self.hovering_military_approval_rating_rect = False
		self.hovering_domestic_approval_rating_rect = False
		self.hovering_midia_approval_rating_rect = False
		self.hovering_secret_service_approval_rating_rect = False
		self.hovering_politics_approval_rating_rect = False	

		#----------------------------------------------------------------------------------------------------------------------------------------#

		#----------------------------------------------------------------------------------------------------------------------------------------#
		# COUNTRY VIEWER

		if self.is_menu_open == True:
			if self.update_parties_pie_chart == True:
				self.parties_pie_chart_surface.fill((0, 0, 0, 0))
				self.official_parties_names_surface.fill((0, 0, 0, 0))
				last_angle = 180
				for index, official_party in enumerate(self.PlayerCountry.country_official_parties):
					end_angle = 180 * (official_party.parliament_seats / self.PlayerCountry.total_parliament_seats)
					GenericUtilitys.draw_pie(self.parties_pie_chart_surface, official_party.party_color, (302 * self.factor_x, 300 * self.factor_y), 300 * self.factor_x, last_angle, end_angle + last_angle)
					last_angle = end_angle + last_angle

					party_name_text = self.small_scalable_font.render(official_party.party_name, True, (255, 255, 255))

					self.pygame.draw.rect(self.official_parties_names_surface, official_party.party_color, (5 * self.factor_x, (party_name_text.get_height()*1.2) * index + 5 * self.factor_y, party_name_text.get_height(), party_name_text.get_height()))

					text_position = (5 * self.factor_x + party_name_text.get_height()*1.1, (party_name_text.get_height()*1.2) * index + 5 * self.factor_y)
					self.official_parties_names_surface.blit(party_name_text, text_position)			

				self.update_parties_pie_chart = False						

			
			screen.blit(self.PlayerCountry.country_leader_image, (12 * self.factor_x, 27 * self.factor_y + self.country_overview_position[1]))
			screen.blit(self.country_overview, self.country_overview_position)

			screen.blit(self.PlayerCountry.country_capital_image, (160 * self.factor_x, 90 * self.factor_y + self.country_overview_position[1]))
			screen.blit(self.country_overview, self.country_overview_position)			

			# PARTIES
			screen.blit(self.parties_pie_chart_surface, (876 * self.factor_x, 82 * self.factor_y + self.country_overview_position[1]))

			screen.blit(self.official_parties_names_surface, (879 * self.factor_x, 418 * self.factor_y + self.country_overview_position[1]))

			# COUNTRY NAME
			country_name_text = self.big_scalable_font.render(self.PlayerCountry.country_name, True, (255, 255, 255))
			text_position = (165 * self.factor_x, 39 * self.factor_y + self.country_overview_position[1])	
			screen.blit(country_name_text, text_position)

			# LEADER NAME
			leader_name_text = self.huge_scalable_font.render(self.PlayerCountry.country_leader_name, True, (255, 255, 255))
			if leader_name_text.get_width() > 350 * self.factor_x:
				leader_name_text = self.big_scalable_font.render(self.PlayerCountry.country_leader_name, True, (255, 255, 255))
			
			text_position = (24 * self.factor_x, 226 * self.factor_y + self.country_overview_position[1])	
			screen.blit(leader_name_text, text_position)

			# GOVERNMENT
			government_name_text = self.huge_scalable_font.render(self.PlayerCountry.country_government, True, (255, 255, 255))
			text_position = (25 * self.factor_x, 293 * self.factor_y + self.country_overview_position[1])	
			
			if government_name_text.get_width() > 250 * self.factor_x:
				government_name_text = self.big_scalable_font.render(self.PlayerCountry.country_government, True, (255, 255, 255))	
				text_position = (25 * self.factor_x, 293 * self.factor_y + self.country_overview_position[1])
				if government_name_text.get_width() > 250 * self.factor_x:	
					government_name_text = self.medium_scalable_font.render(self.PlayerCountry.country_government, True, (255, 255, 255))	
					text_position = (25 * self.factor_x, 293 * self.factor_y + self.country_overview_position[1])					

			screen.blit(government_name_text, text_position)	

			# RULING PARTY
			ruling_party_name_text = self.huge_scalable_font.render(self.PlayerCountry.country_ruling_party, True, (255, 255, 255))
			text_position = (299 * self.factor_x, 293 * self.factor_y + self.country_overview_position[1])	

			if ruling_party_name_text.get_width() > 250 * self.factor_x:
				ruling_party_name_text = self.big_scalable_font.render(self.PlayerCountry.country_ruling_party, True, (255, 255, 255))	
				text_position = (299 * self.factor_x, 293 * self.factor_y + self.country_overview_position[1])
				if ruling_party_name_text.get_width() > 250 * self.factor_x:
					ruling_party_name_text = self.medium_scalable_font.render(self.PlayerCountry.country_ruling_party, True, (255, 255, 255))	
					text_position = (299 * self.factor_x, 293 * self.factor_y + self.country_overview_position[1])										

			screen.blit(ruling_party_name_text, text_position)

			# ELECTIONS
			elections_text = self.huge_scalable_font.render(self.PlayerCountry.country_elections, True, (255, 255, 255))
			text_position = (586 * self.factor_x, 293 * self.factor_y + self.country_overview_position[1])	
			screen.blit(elections_text, text_position)	


			#-----------------------------------------------------------------------------------------------------------------------------------------------------#
			# POPULARITY CIRCLES

			# POLITICS
			chart_position = (143 * self.factor_x, 525 * self.factor_y + self.country_overview_position[1]) 
			chart_radius = 80 * self.factor_y

			self.politics_cicle_rects = GenericUtilitys.draw_pie_chart(screen, chart_position, chart_radius, self.politics_popularity, self.politics_segment_colors)	

			screen.blit(self.popularity_circle_overlay, (chart_position[0]-85 * self.factor_x, chart_position[1]-85 * self.factor_y))

			# CULTURE
			chart_position = (433 * self.factor_x, 525 * self.factor_y + self.country_overview_position[1]) 
			chart_radius = 80 * self.factor_y

			rects_info = GenericUtilitys.draw_pie_chart(screen, chart_position, chart_radius, self.culture_popularity, self.culture_segment_colors)		
			self.culture_cicle_rects = rects_info

			screen.blit(self.popularity_circle_overlay, (chart_position[0]-85 * self.factor_x, chart_position[1]-85 * self.factor_y))			

			# RELIGION
			chart_position = (720 * self.factor_x, 525 * self.factor_y + self.country_overview_position[1]) 
			chart_radius = 80 * self.factor_y  

			rects_info = GenericUtilitys.draw_pie_chart(screen, chart_position, chart_radius, self.religion_popularity, self.religion_segment_colors)
			self.religion_cicle_rects = rects_info

			screen.blit(self.popularity_circle_overlay, (chart_position[0]-85 * self.factor_x, chart_position[1]-85 * self.factor_y))	

			# POPULARITY TEXT INFO
			if self.is_touching_cicle_rects == True:
				if self.hitted_rect[1] == 'politics':
					ideology_name = self.ideologies[self.hitted_rect[0]] + ":   " + str(self.politics_popularity[self.hitted_rect[0]]) + '%'
				elif self.hitted_rect[1] == 'culture':
					ideology_name = self.cultures[self.hitted_rect[0]] + ":   " + str(self.culture_popularity[self.hitted_rect[0]]) + '%'
				elif self.hitted_rect[1] == 'religion':
					ideology_name = self.religions[self.hitted_rect[0]] + ":   " + str(self.religion_popularity[self.hitted_rect[0]]) + '%'

				ideology_name_text = self.medium_scalable_font.render(ideology_name, True, (255, 255, 255))
				text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1])	
				
				pygame.draw.rect(screen, (6,15,20), (text_position[0]-20 * self.factor_x, text_position[1], ideology_name_text.get_width()+24 * self.factor_x, ideology_name_text.get_height()+10 * self.factor_y))
				pygame.draw.rect(screen, (43,219,211), (text_position[0]-20 * self.factor_x, text_position[1], ideology_name_text.get_width()+24 * self.factor_x, ideology_name_text.get_height()+10 * self.factor_y), 2)				
				
				screen.blit(ideology_name_text, (text_position[0], text_position[1]+6 * self.factor_y))	

			#-----------------------------------------------------------------------------------------------------------------------------------------------------#
			# NATIONAL SPIRITS

			self.national_spirits_display_rects = []
			national_spirits_position = [382 * self.factor_x, 110 * self.factor_y + self.country_overview_position[1]]
			x_index = 0
			y_index = 0			

			if len(self.PlayerCountry.country_national_spirits) > 14:
				for national_spirit in self.PlayerCountry.country_national_spirits:
					scaled_national_spirit_icon = pygame.transform.smoothscale(national_spirit.national_spirit_icon, (48 * self.factor_x, 48 * self.factor_y))

					scaled_national_spirit_icon = pygame.transform.smoothscale_by(scaled_national_spirit_icon, 0.8)

					x_offset = scaled_national_spirit_icon.get_width() * 1.20
					y_offset = scaled_national_spirit_icon.get_height() * 1.1
					
					screen.blit(scaled_national_spirit_icon, (national_spirits_position[0] + x_offset*x_index, national_spirits_position[1] -5 * self.factor_y + y_offset*y_index))
					
					national_spirit.rect = self.pygame.Rect(national_spirits_position[0] + x_offset*x_index, national_spirits_position[1] -5 * self.factor_y  + y_offset*y_index,
														scaled_national_spirit_icon.get_width(), scaled_national_spirit_icon.get_height())
					self.national_spirits_display_rects.append([national_spirit.rect, national_spirit])	

					if x_index < 8:
						x_index += 1
					else:
						x_index = 0
						y_index += 1							
			else:	
				for national_spirit in self.PlayerCountry.country_national_spirits:
					scaled_national_spirit_icon = pygame.transform.smoothscale(national_spirit.national_spirit_icon, (48 * self.factor_x, 48 * self.factor_y))	
						
					x_offset = scaled_national_spirit_icon.get_width() * 1.23
					y_offset = scaled_national_spirit_icon.get_height()	* 1.26		
					
					screen.blit(scaled_national_spirit_icon, (national_spirits_position[0] + x_offset*x_index, national_spirits_position[1] + y_offset*y_index))
					
					national_spirit.rect = self.pygame.Rect(national_spirits_position[0] + x_offset*x_index, national_spirits_position[1] + y_offset*y_index,
														scaled_national_spirit_icon.get_width(), scaled_national_spirit_icon.get_height())
					self.national_spirits_display_rects.append([national_spirit.rect, national_spirit])	

					if x_index < 6:
						x_index += 1
					else:
						x_index = 0
						y_index += 1

			if self.hovered_national_spirit != None:
				pygame.draw.rect(screen, (255,255,255), self.hovered_national_spirit.rect, 2)

				national_spirit_description_text = self.medium_scalable_font.render(self.hovered_national_spirit.national_spirit_description, True, (255, 255, 255))
				text_position = (382 * self.factor_x, 238 * self.factor_y + self.country_overview_position[1])

				pygame.draw.rect(screen, (6,15,20), (376 * self.factor_x, 230 * self.factor_y + self.country_overview_position[1], 484 * self.factor_x, national_spirit_description_text.get_height() + 10 * self.factor_y))
				pygame.draw.rect(screen, (43,219,211), (376 * self.factor_x, 230 * self.factor_y + self.country_overview_position[1], 484 * self.factor_x, national_spirit_description_text.get_height() + 10 * self.factor_y), 2)

				screen.blit(national_spirit_description_text, text_position)


			# CULTURE
			culture_national_spirit = self.PlayerCountry.country_culture
			screen.blit(culture_national_spirit.national_spirit_icon, (792 * self.factor_x, 104 * self.factor_y + self.country_overview_position[1]))
			
			culture_national_spirit.rect = self.pygame.Rect(792 * self.factor_x, 103 * self.factor_y + self.country_overview_position[1],
					culture_national_spirit.national_spirit_icon.get_width(), culture_national_spirit.national_spirit_icon.get_height())					
			
			self.national_spirits_display_rects.append([culture_national_spirit.rect, culture_national_spirit])						
			
			# RELIGION	
			religion_national_spirit = self.PlayerCountry.country_religion
			screen.blit(religion_national_spirit.national_spirit_icon, (792 * self.factor_x, 103 * self.factor_y + religion_national_spirit.national_spirit_icon.get_height() + self.country_overview_position[1]))
			
			religion_national_spirit.rect = self.pygame.Rect(792 * self.factor_x, 103 * self.factor_y + religion_national_spirit.national_spirit_icon.get_height() + self.country_overview_position[1],
					religion_national_spirit.national_spirit_icon.get_width(), religion_national_spirit.national_spirit_icon.get_height())					
			
			self.national_spirits_display_rects.append([religion_national_spirit.rect, religion_national_spirit])	

		else:
			self.update_parties_pie_chart = True
		# country_viewer_open	

class Country_Focus_Tree:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, top_bar_flag_overlay, top_bar_flag_overlay_hovering_over):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.focus_tree_surface = pygame.Surface((self.screen_width, self.screen_height - (158 + 110) * self.factor_y), pygame.SRCALPHA)
		self.focus_to_remove = []

		self.focus_wating_player_path_selection = None
		self.focus_completion_wating_player_visualization = None
		self.highlight_focus_completion_wating_player_visualization_button = False

		self.PlayerCountry = None

		self.current_year = 1970
		self.current_month = 1
		self.current_day = 1	

		self.keep_game_paused = False	

		self.focus_movement_x = 0
		self.focus_movement_y = 0

		self.highlight_focus_path_selection_button_index = None
		self.highlight_button = False
		self.is_menu_open = False

		self.top_bar_flag_overlay = pygame.transform.smoothscale_by(top_bar_flag_overlay, (self.factor_x, self.factor_y))
		self.top_bar_flag_overlay_hovering_over = pygame.transform.smoothscale_by(top_bar_flag_overlay_hovering_over, (self.factor_x, self.factor_y))	

		self.top_bar_focus_tree_button = GenericUtilitys.Button(2 * self.factor_x, 81 * self.factor_y, 123 * self.factor_x, 74 * self.factor_y)

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_focus_tree_button.rect.colliderect(mouse_rect):
			return "focus_tree"

		if self.focus_wating_player_path_selection:
			for index, choice in enumerate(self.focus_wating_player_path_selection.next_focus): 
				if getattr(self, f'choice_button_{index}').rect.colliderect(mouse_rect):
					# Inverted so player chooses what path to keep instead of choosing what path to vanish
					if index == 0:
						index = 1
					elif index == 1:
						index = 0
					self.focus_wating_player_path_selection.selected_path = index
					return 'choice_button'
				
		if self.focus_completion_wating_player_visualization:
			if getattr(self, 'accept_button').rect.colliderect(mouse_rect):
				return 'accept_button'

		return None		

	def deactivate_branch(self, focus):
		focus.is_active = False
		self.focus_to_remove.append(focus.focus_id)

		if len(focus.next_focus) > 0:
			for next_focus_index in focus.next_focus:
				next_focus = self.PlayerCountry.country_focus_tree[next_focus_index]
				self.deactivate_branch(next_focus)

	def draw(self, screen):

		if len(self.focus_to_remove) > 0:
			for focus in self.focus_to_remove:
				try:
					self.PlayerCountry.country_focus_tree.pop(focus)
				except:
					pass
			self.focus_to_remove.clear()

		self.focus_tree_surface.fill((0, 0, 0, 0), (0, 0, self.screen_width, self.screen_height - (158 + 110) * self.factor_y))
		
		#screen.blit(next(iter(self.PlayerCountry.country_focus_tree.values())).national_focus_icon, (5 * self.factor_x, 84 * self.factor_y))	

		if self.highlight_button == False and self.is_menu_open == False:
			screen.blit(self.top_bar_flag_overlay, (2 * self.factor_x, 81 * self.factor_y))
		else:
			screen.blit(self.top_bar_flag_overlay_hovering_over, (2 * self.factor_x, 81 * self.factor_y))


		for focus in self.PlayerCountry.country_focus_tree.values():
			if focus.is_active == True:
				if focus.completion_time['day'] <= self.current_day and focus.completion_time['month'] <= self.current_month and focus.completion_time['year'] <= self.current_year:
					focus.is_active = False
					self.keep_game_paused = True
					self.focus_completion_wating_player_visualization = focus
					setattr(self, 'accept_button', GenericUtilitys.Button(self.screen_width/2 - self.screen_width/8, self.screen_height - (180 + 55) * self.factor_y, self.screen_width/4, 75 * self.factor_y))
					if len(focus.next_focus) > 1:
						focus.next_focus = [focus.next_focus[focus.selected_path]]
						self.deactivate_branch(focus)
					continue
				elif focus.decision_time:
					if focus.decision_time['day'] <= self.current_day and focus.decision_time['month'] <= self.current_month and focus.decision_time['year'] <= self.current_year and self.keep_game_paused == False:
						self.keep_game_paused = True
						focus.decision_time = None
						self.focus_wating_player_path_selection = focus
						for index, choice in enumerate(focus.next_focus):
							setattr(self, f'choice_button_{index}', GenericUtilitys.Button(self.screen_width/2 - self.screen_width/8, self.screen_height - (180 + 55 + (95 * index)) * self.factor_y, self.screen_width/4, 75 * self.factor_y))

				if self.is_menu_open == True:	
					self.pygame.draw.rect(screen, (6,15,20), (0, 158 * self.factor_y, self.screen_width, self.screen_height - (158 + 110) * self.factor_y))

					current_focus_position = (self.screen_width/2 + (focus.x_offset + self.focus_movement_x) * self.factor_x + focus.national_focus_icon.get_width()/2, (focus.y_offset + self.focus_movement_y) * self.factor_y - focus.national_focus_icon.get_height()/2)
					if focus.next_focus:
						for focus_id in focus.next_focus:
							next_focus_position = (self.screen_width/2 + (self.PlayerCountry.country_focus_tree[focus_id].x_offset + self.focus_movement_x) * self.factor_x + focus.national_focus_icon.get_width()/2, (self.PlayerCountry.country_focus_tree[focus_id].y_offset + self.focus_movement_y) * self.factor_y - focus.national_focus_icon.get_height()/2)					
							self.pygame.draw.line(self.focus_tree_surface, (255, 255, 255), current_focus_position, next_focus_position, 2)

					self.pygame.draw.rect(self.focus_tree_surface, (6,15,20), (self.screen_width/2 + (focus.x_offset + self.focus_movement_x - 40) * self.factor_x, (focus.y_offset + self.focus_movement_y - 5) * self.factor_y - focus.national_focus_icon.get_height(), focus.national_focus_icon.get_width() + 80 * self.factor_x, focus.national_focus_icon.get_height() + 40 * self.factor_y))

					self.focus_tree_surface.blit(focus.national_focus_icon, (self.screen_width/2 + (focus.x_offset + self.focus_movement_x) * self.factor_x, (focus.y_offset + self.focus_movement_y) * self.factor_y - focus.national_focus_icon.get_height()))

					focus_name = self.medium_scalable_font.render(focus.national_focus_name, True, (255, 255, 255))
					self.focus_tree_surface.blit(focus_name, (self.screen_width/2 + (focus.x_offset + self.focus_movement_x) * self.factor_x - focus_name.get_width()/2 + focus.national_focus_icon.get_width()/2, (focus.y_offset + self.focus_movement_y) * self.factor_y + 10 * self.factor_y))

					self.pygame.draw.rect(self.focus_tree_surface, (43,219,211), (self.screen_width/2 + (focus.x_offset + self.focus_movement_x - 40) * self.factor_x, (focus.y_offset + self.focus_movement_y - 5) * self.factor_y - focus.national_focus_icon.get_height(), focus.national_focus_icon.get_width() + 80 * self.factor_x, focus.national_focus_icon.get_height() + 40 * self.factor_y), 2)
		if self.is_menu_open == True:
			for month in range(4):
				years_offset = 0

				months_offset = int(abs(self.focus_movement_y)/300)
				months = month + 1 + months_offset
			
				years_offset = int((months-1)/12)
				total_months = months - 12 * int((months-1)/12)		
		
				dates_name = self.big_scalable_font.render(str(1970+years_offset)+ ' - ' + str(total_months), True, (255, 255, 255))
				self.focus_tree_surface.blit(dates_name, (15 * self.factor_x, (self.focus_movement_y + ((total_months + (years_offset*12)) * 300) + 35) * self.factor_y))

			current_date_line_height = (self.current_day * 10 + ((self.current_month + (years_offset*12)) * 300) + self.focus_movement_y) * self.factor_y
			self.pygame.draw.line(self.focus_tree_surface, (255, 0, 0), (0, current_date_line_height + 35 * self.factor_y), (self.screen_width, current_date_line_height + 35 * self.factor_y), 1)

			screen.blit(self.focus_tree_surface, (0, 158 * self.factor_y))

			self.pygame.draw.rect(screen, (43,219,211), (0, 158 * self.factor_y, self.screen_width, self.screen_height - (158 + 110) * self.factor_y), 2)			

		#----------------------------------------------------------------#
		# FOCUS SELECT PATH POP UP
		#----------------------------------------------------------------#
		if self.focus_wating_player_path_selection:
			self.pygame.draw.rect(screen, (6,15,20), (self.screen_width/2 - self.screen_width/4, 170 * self.factor_y, self.screen_width/2, self.screen_height - (180 + 110) * self.factor_y))
			self.pygame.draw.rect(screen, (43,219,211), (self.screen_width/2 - self.screen_width/4, 170 * self.factor_y, self.screen_width/2, self.screen_height - (180 + 110) * self.factor_y), 2)
			for index, choice in enumerate(self.focus_wating_player_path_selection.next_focus):
				self.pygame.draw.rect(screen, (255,255,255), getattr(self, f'choice_button_{index}').rect, 2)
				button_text = self.big_scalable_font.render('Choose Path: ' + str(index), True, (255, 255, 255))
				screen.blit(button_text, (self.screen_width/2 - button_text.get_width()/2, self.screen_height - (180 + 55 + (95 * index)) * self.factor_y - button_text.get_height()/2 + 37.5 * self.factor_y))


			if self.highlight_focus_path_selection_button_index != None:
				# Inverted so player chooses what path to keep instead of choosing what path to vanish
				if self.highlight_focus_path_selection_button_index == 0:
					self.highlight_focus_path_selection_button_index = 1
				elif self.highlight_focus_path_selection_button_index == 1:
					self.highlight_focus_path_selection_button_index = 0
				self.pygame.draw.rect(screen, (0,255,0), getattr(self, f'choice_button_{self.highlight_focus_path_selection_button_index}').rect, 4)


			focus_selection_description_text = self.big_scalable_font.render(self.focus_wating_player_path_selection.national_focus_path_selection_description, True, (255, 255, 255))
			screen.blit(focus_selection_description_text, (self.screen_width/2 - focus_selection_description_text.get_width()/2, 180 * self.factor_y))				
			

		#----------------------------------------------------------------#
		# FOCUS COMPLETION
		#----------------------------------------------------------------#
		if self.focus_completion_wating_player_visualization:
			self.pygame.draw.rect(screen, (6,15,20), (self.screen_width/2 - self.screen_width/4, 170 * self.factor_y, self.screen_width/2, self.screen_height - (180 + 110) * self.factor_y))
			self.pygame.draw.rect(screen, (43,219,211), (self.screen_width/2 - self.screen_width/4, 170 * self.factor_y, self.screen_width/2, self.screen_height - (180 + 110) * self.factor_y), 2)			

			self.pygame.draw.rect(screen, (255,255,255), getattr(self, 'accept_button').rect, 2)

			button_text = self.big_scalable_font.render('Accept', True, (255, 255, 255))
			screen.blit(button_text, (self.screen_width/2 - button_text.get_width()/2, self.screen_height - (180 + 55) * self.factor_y - button_text.get_height()/2 + 37.5 * self.factor_y))		

			focus_description_text = self.big_scalable_font.render(self.focus_completion_wating_player_visualization.national_focus_description, True, (255, 255, 255))
			screen.blit(focus_description_text, (self.screen_width/2 - focus_description_text.get_width()/2, 180 * self.factor_y))		

			if self.highlight_focus_completion_wating_player_visualization_button == True:
				self.pygame.draw.rect(screen, (0,255,0), getattr(self, 'accept_button').rect, 4)

# 	TOP BAR BUTTONS
class Decisions_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = None

		self.is_menu_open = False
		self.highlight_button = False

		self.is_decision_tree_menu_open = False
		self.hovered_decision_tree_button = False
		self.hovered_decision_button = False
		self.clicked_decision_button = False

		self.interected_decision_button = None

		self.active_decisions_surface = pygame.Surface((self.screen_width/2, 3000 * self.factor_y), pygame.SRCALPHA)

		self.tree_icons_offset_x = 0
		self.tree_icons_offset_y = 0
		self.decisions_tree_surface = pygame.Surface((3000 * self.factor_x, 3000 * self.factor_y), pygame.SRCALPHA)		

		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_decisions_button = GenericUtilitys.Button(129 * self.factor_x, height, button_size[0], button_size[1])
		
		self.decision_buttons_rect_list = []
		self.decision_buttons_lits = []

		button_size = ((self.screen_width/2) * 0.6, 60 * self.factor_y)
		self.open_decision_tree_button = GenericUtilitys.Button(self.screen_width/4 - button_size[0]/2, 178 * self.factor_y, button_size[0], button_size[1])

		self.text_scroll_bar = GenericUtilitys.Scroll_Bar(6, 164  * self.factor_y, self.screen_height - (158 + 110 + 10) * self.factor_y, 3000 * self.factor_y - (self.screen_height - (158 + 120) * self.factor_y), (255,255,255), (255,0,0), 10 * self.factor_x)

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))	

		self.open_active_decisions_text_render = self.huge_scalable_font.render('OPEN DECISIONS TREE', False, (255,255,255))	

	def generate_decisions_tree(self):
		# REQUIREMENTS LINES
		for decision in self.PlayerCountry.country_decisions_tree.values():
			size_x = 50
			size_y = 50

			icon_image = getattr(decision, 'decision_on_tree_menu_icon', None)
			if icon_image:
				size_x = icon_image.get_width()
				size_y = icon_image.get_height()

			if decision.requirements:
				for requirement_decision in decision.requirements:
					requirement_decision = self.PlayerCountry.country_decisions_tree[requirement_decision]
					pygame.draw.line(self.decisions_tree_surface, (255,255,255), ((decision.x_pos + size_x/2) * self.factor_x, (decision.y_pos + size_y/2) * self.factor_y), ((requirement_decision.x_pos + size_x/2) * self.factor_x, (requirement_decision.y_pos + size_y/2) * self.factor_y), 2)	

		# ICONS
		for decision in self.PlayerCountry.country_decisions_tree.values():
			size_x = 50
			size_y = 50

			icon_image = getattr(decision, 'decision_on_tree_menu_icon', None)
			if icon_image:
				size_x = icon_image.get_width()
				size_y = icon_image.get_height()

				self.pygame.draw.rect(self.decisions_tree_surface, (0,0,0), (decision.x_pos * self.factor_x, decision.y_pos * self.factor_y, size_x, size_y))
				self.pygame.draw.rect(self.decisions_tree_surface, (43,219,211), (decision.x_pos * self.factor_x, decision.y_pos * self.factor_y, size_x, size_y), 2)

				self.decisions_tree_surface.blit(icon_image, (decision.x_pos, decision.y_pos))			

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_decisions_button.rect.colliderect(mouse_rect):
			return "decisions_button"
		
		if self.is_menu_open == True:
			if self.open_decision_tree_button.rect.colliderect(mouse_rect):
				return "open_decision_tree_button"	

			elif mouse_rect[1] > 258 * self.factor_y and mouse_rect[1] < (self.screen_height - (258 + 120) * self.factor_y) + 258 * self.factor_y:
				for index, rect in enumerate(self.decision_buttons_rect_list):
					if rect.colliderect(mouse_rect):
						self.interected_decision_button = self.decision_buttons_lits[index]
						return "decision_button"
		
		return None

	def draw(self, screen):
		if self.is_menu_open == True:
			self.decision_buttons_rect_list.clear()
			self.decision_buttons_lits.clear()

			self.active_decisions_surface.fill((0, 0, 0, 0), (0, 0, self.active_decisions_surface.get_width(), self.screen_height - (258 + 120) * self.factor_y))

			self.pygame.draw.rect(screen, (6,15,20), (0, 158 * self.factor_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y))
			self.pygame.draw.rect(screen, (43,219,211), (0, 158 * self.factor_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y), 2)		

			self.text_scroll_bar.draw(screen)

			if self.hovered_decision_tree_button == False:
				self.pygame.draw.rect(screen, (255,255,255), self.open_decision_tree_button.rect, 2)
			else:
				self.pygame.draw.rect(screen, (0,255,0), self.open_decision_tree_button.rect, 2)	

			screen.blit(self.open_active_decisions_text_render, (self.screen_width/4 - self.open_active_decisions_text_render.get_width()/2, (60 * self.factor_y)/2 - self.open_active_decisions_text_render.get_height()/2 + 178 * self.factor_y))		


			if self.is_decision_tree_menu_open == True:
				self.pygame.draw.rect(screen, (6,15,20), (self.screen_width/2, 158 * self.factor_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y))
				self.pygame.draw.rect(screen, (43,219,211), (self.screen_width/2, 158 * self.factor_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y), 2)	


				screen.blit(self.decisions_tree_surface.subsurface(self.tree_icons_offset_x, self.tree_icons_offset_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y), (self.screen_width/2, 158 * self.factor_y))				


			offset_y = self.text_scroll_bar.get_scroll_position()
			for index, decision in enumerate(self.PlayerCountry.country_active_decisions.values()):
				if index > 0:
					last_decision_menu = list(self.PlayerCountry.country_active_decisions.values())[index-1]
					last_decision_height = last_decision_menu.last_height + 25 * self.factor_y
				else:
					last_decision_height = 0
					
				self.pygame.draw.rect(self.active_decisions_surface, (43,219,211), (self.screen_width/2 * 0.05, last_decision_height, self.screen_width/2 * 0.9, decision.main_image.get_height()*1.2), 2)	
				self.active_decisions_surface.blit(decision.main_image, (self.screen_width/2 * 0.07, decision.main_image.get_height()*0.1 + last_decision_height))

				decision_description_text_render = self.huge_scalable_font.render(decision.decision_description, False, (255,255,255))	
				self.active_decisions_surface.blit(decision_description_text_render, (self.screen_width/2 * 0.09 + decision.main_image.get_width(), decision.main_image.get_height()*0.1 + last_decision_height))

				for button_index, button in enumerate(decision.buttons):
					button_x = button.x * self.factor_x
					button_y = button.y * self.factor_y + last_decision_height
					button_width = button.width * self.factor_x
					button_height = button.height * self.factor_y
				
					button_position_y = button_y + decision.main_image.get_height()*1.3 + button_index*(button_height*1.25) + 258 * self.factor_y - offset_y

					if button_position_y + button_height < 258 * self.factor_y or button_position_y > (self.screen_height - (258 + 120) * self.factor_y) + 258 * self.factor_y:
						button_position_y = -1000

					self.decision_buttons_rect_list.append(self.pygame.Rect((self.screen_width/2 * 0.05 + button_x, button_position_y, button_width, button_height)))
					self.decision_buttons_lits.append(button)

					self.active_decisions_surface.blit(decision.buttons_icons[button_index], (self.screen_width/2 * 0.05 + button_x, button_y + decision.main_image.get_height()*1.3 + button_index*(button_height*1.25)))

					if self.hovered_decision_button == False or self.interected_decision_button != button:
						self.pygame.draw.rect(self.active_decisions_surface, (43,219,211), (self.screen_width/2 * 0.05 + button_x, button_y + decision.main_image.get_height()*1.3 + button_index*(button_height*1.25), button_width, button_height), 2)
					elif self.hovered_decision_button == True and self.interected_decision_button == button:
						self.pygame.draw.rect(self.active_decisions_surface, (0,255,0), (self.screen_width/2 * 0.05 + button_x, button_y + decision.main_image.get_height()*1.3 + button_index*(button_height*1.25), button_width, button_height), 2)

					if self.interected_decision_button == button and self.clicked_decision_button == True:
						self.pygame.draw.rect(self.active_decisions_surface, (255,0,0), (self.screen_width/2 * 0.05 + button_x, button_y + decision.main_image.get_height()*1.3 + button_index*(button_height*1.25), button_width, button_height), 2)
						self.clicked_decision_button = False

					button_description_text_render = self.huge_scalable_font.render(decision.buttons_descriptions[button_index], False, (255,255,255))
					self.active_decisions_surface.blit(button_description_text_render, (self.screen_width/2 * 0.05 + button_x + button_width*1.1, button_y + decision.main_image.get_height()*1.3 + button_height/2 - button_description_text_render.get_height()/2 + button_index*(button_height*1.25)))

				decision.last_height = button_y + decision.main_image.get_height()*1.3 + button_index*(button_height*1.25) + button_height

			screen.blit(self.active_decisions_surface.subsurface(0, offset_y, self.active_decisions_surface.get_width(), self.screen_height - (258 + 120) * self.factor_y), (0, 258 * self.factor_y))


		if self.highlight_button == True or self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,255,255), self.top_bar_decisions_button.rect, 2)		

class Laws_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, progressbar_huge, country_laws_background, laws_description_image):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.is_menu_open = False
		self.highlight_button = False
		self.selected_law_group_index = None

		self.hovered_law_button = None

		self.laws_butons_rect = []
		self.hovered_rect = None

		self.PlayerCountry = None

		self.progressbar_huge 			= pygame.transform.smoothscale_by(progressbar_huge, (self.factor_x, self.factor_y))	
		self.country_laws_background 	= pygame.transform.smoothscale_by(country_laws_background, (self.factor_x, self.factor_y))
		self.laws_description_image		= pygame.transform.smoothscale_by(laws_description_image, (self.factor_x, self.factor_y))

		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_laws_button = GenericUtilitys.Button(188 * self.factor_x, height, button_size[0], button_size[1])

		#### LAWS BUTTONS
		law_button_width = 208 * self.factor_x
		law_button_height = 27 * self.factor_y		

		x_offset = 15
		y_offset = 60 + 158

		### FIRST ROW
		self.first_row_law_button_y_offset_1 = (50 + y_offset) * self.factor_y
		self.first_row_law_button_y_offset_2 = (83 + y_offset) * self.factor_y
		self.first_row_law_button_y_offset_3 = (116 + y_offset) * self.factor_y
		self.first_row_law_button_y_offset_4 = (149 + y_offset) * self.factor_y
		self.first_row_law_button_y_offset_5 = (182 + y_offset) * self.factor_y
		self.first_row_law_button_y_offset_6 = (215 + y_offset) * self.factor_y
		self.first_row_law_button_y_offset_7 = (248 + y_offset) * self.factor_y
		self.first_row_law_button_y_offset_8 = (281 + y_offset) * self.factor_y
		self.first_row_law_button_y_offset_9 = (314 + y_offset) * self.factor_y	
		
		## POLITICAL LAWS
		self.political_law_button_x_offset = (214 + x_offset) * self.factor_x
		
		self.political_law_button_1 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.political_law_button_2 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.political_law_button_3 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.political_law_button_4 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.political_law_button_5 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.political_law_button_6 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.political_law_button_7 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.political_law_button_8 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_8, law_button_width, law_button_height)
		self.political_law_button_9 = GenericUtilitys.Button(self.political_law_button_x_offset, self.first_row_law_button_y_offset_9, law_button_width, law_button_height)				
		##

		## MILITARY LAWS
		self.military_law_button_x_offset = (646 + x_offset) * self.factor_x

		self.military_law_button_1 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.military_law_button_2 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.military_law_button_3 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.military_law_button_4 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.military_law_button_5 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.military_law_button_6 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.military_law_button_7 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.military_law_button_8 = GenericUtilitys.Button(self.military_law_button_x_offset, (294 + y_offset) * self.factor_y, law_button_width, law_button_height)		
		##
		###

		### SECOND ROW
		self.second_row_law_button_y_offset_1 = (401 + y_offset) * self.factor_y
		self.second_row_law_button_y_offset_2 = (434 + y_offset) * self.factor_y
		self.second_row_law_button_y_offset_3 = (467 + y_offset) * self.factor_y
		self.second_row_law_button_y_offset_4 = (500 + y_offset) * self.factor_y
		self.second_row_law_button_y_offset_5 = (533 + y_offset) * self.factor_y
		self.second_row_law_button_y_offset_6 = (566 + y_offset) * self.factor_y
		self.second_row_law_button_y_offset_7 = (599 + y_offset) * self.factor_y
		self.second_row_law_button_y_offset_8 = (632 + y_offset) * self.factor_y
		self.second_row_law_button_y_offset_9 = (665 + y_offset) * self.factor_y	
		
		## ECONOMIC LAWS
		self.economical_law_button_x_offset = (214 + x_offset) * self.factor_x
		
		self.economical_law_button_1 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.economical_law_button_2 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.economical_law_button_3 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.economical_law_button_4 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.economical_law_button_5 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.economical_law_button_6 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.economical_law_button_7 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.economical_law_button_8 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_8, law_button_width, law_button_height)
		self.economical_law_button_9 = GenericUtilitys.Button(self.economical_law_button_x_offset, self.second_row_law_button_y_offset_9, law_button_width, law_button_height)				
		##

		## SOCIAL LAWS
		self.social_law_button_x_offset = (646 + x_offset) * self.factor_x

		self.social_law_button_1 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.social_law_button_2 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.social_law_button_3 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.social_law_button_4 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.social_law_button_5 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.social_law_button_6 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.social_law_button_7 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.social_law_button_8 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_8, law_button_width, law_button_height)
		self.social_law_button_9 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_9, law_button_width, law_button_height)			

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_laws_button.rect.colliderect(mouse_rect):
			return "laws_button"
		
		elif self.is_menu_open == True:
			self.hovered_law_button = None
			self.hovered_rect = None
			for number in range(9):
				button = getattr(self, f'political_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					self.hovered_law_button = f'political_law_button_{str(number+1)}'
					return f'political_law_button_{str(number+1)}'
			
			for number in range(8):
				button = getattr(self, f'military_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					self.hovered_law_button = f'military_law_button_{str(number+1)}'
					return f'military_law_button_{str(number+1)}'

			for number in range(9):
				button = getattr(self, f'economical_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					self.hovered_law_button = f'economical_law_button_{str(number+1)}'
					return f'economical_law_button_{str(number+1)}'
			
			for number in range(9):
				button = getattr(self, f'social_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					self.hovered_law_button = f'social_law_button_{str(number+1)}'
					return f'social_law_button_{str(number+1)}'

			for index, rect in enumerate(self.laws_butons_rect):
				if self.pygame.Rect(rect).colliderect(mouse_rect):
					self.hovered_rect = rect
					return f'rect_law_button{index}'

		return None

	def draw(self, screen):		

		if self.highlight_button == True or self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,255,255), self.top_bar_laws_button.rect, 2)	

		if self.is_menu_open == True:
			self.pygame.draw.rect(screen, (0,0,0), (0, 158 * self.factor_y, self.country_laws_background.get_width() + 30 * self.factor_x, self.screen_height - (158 + 110) * self.factor_y))
			self.pygame.draw.rect(screen, (43,219,211), (0, 158 * self.factor_y, self.country_laws_background.get_width() + 30 * self.factor_x, self.screen_height - (158 + 110) * self.factor_y), 2)	

			screen.blit(self.country_laws_background, (15 * self.factor_x, 158 * self.factor_y + 15 * self.factor_y))				

			# LAWS PROGRESS BAR	
			for number in range(9):
				button = getattr(self, f'political_law_button_{str(number+1)}', None)
				law_rating = int((self.progressbar_huge.get_width()/100) * self.PlayerCountry.political_laws_groups[number].active_law_rating)
				screen.blit(self.progressbar_huge.subsurface((0, 0, law_rating, self.progressbar_huge.get_height())), (button.rect[:2]))
			
			for number in range(8):
				button = getattr(self, f'military_law_button_{str(number+1)}', None)
				law_rating = int((self.progressbar_huge.get_width()/100) * self.PlayerCountry.military_laws_groups[number].active_law_rating)
				screen.blit(self.progressbar_huge.subsurface((0, 0, law_rating, self.progressbar_huge.get_height())), (button.rect[:2]))	
			
			for number in range(9):
				button = getattr(self, f'economical_law_button_{str(number+1)}', None)
				law_rating = int((self.progressbar_huge.get_width()/100) * self.PlayerCountry.economical_laws_groups[number].active_law_rating)
				screen.blit(self.progressbar_huge.subsurface((0, 0, law_rating, self.progressbar_huge.get_height())), (button.rect[:2]))
			
			for number in range(9):
				button = getattr(self, f'social_law_button_{str(number+1)}', None)
				law_rating = int((self.progressbar_huge.get_width()/100) * self.PlayerCountry.social_laws_groups[number].active_law_rating)
				screen.blit(self.progressbar_huge.subsurface((0, 0, law_rating, self.progressbar_huge.get_height())), (button.rect[:2]))	


			if self.hovered_law_button != None or self.selected_law_group_index != None:
				if self.hovered_law_button != None:
					splited = self.hovered_law_button.split('_')
					button = getattr(self, self.hovered_law_button, None)	
				elif self.selected_law_group_index != None:
					splited = self.selected_law_group_index.split('_')
					button = getattr(self, self.selected_law_group_index, None)

				if button != None:
					self.pygame.draw.rect(screen, (6,15,20), (self.country_laws_background.get_width() + 30 * self.factor_x, 158 * self.factor_y, self.screen_width - (self.country_laws_background.get_width() + 30 * self.factor_x), self.screen_height - (158 + 110) * self.factor_y))
					self.pygame.draw.rect(screen, (43,219,211), (self.country_laws_background.get_width() + 30 * self.factor_x, 158 * self.factor_y, self.screen_width - (self.country_laws_background.get_width() + 30 * self.factor_x), self.screen_height - (158 + 110) * self.factor_y), 2)	

					self.pygame.draw.rect(screen, (0,255,0), button.rect, 4)					

					laws_group = None
					if splited[0] == 'political':
						laws_group = self.PlayerCountry.political_laws_groups[int(splited[-1]) - 1]
					elif splited[0] == 'military':
						laws_group = self.PlayerCountry.military_laws_groups[int(splited[-1]) - 1]
					elif splited[0] == 'economical':
						laws_group = self.PlayerCountry.economical_laws_groups[int(splited[-1]) - 1]
					elif splited[0] == 'social':
						laws_group = self.PlayerCountry.social_laws_groups[int(splited[-1]) - 1]											

					laws = laws_group.laws

					height = (95 * self.factor_y) * len(laws) + (95 * self.factor_y)
					start_pos = self.screen_height/2 - height/2 + (158 * self.factor_y)/2
					
					self.laws_butons_rect = []
					show_description = False
					for index, law in enumerate(laws):
						rect = (self.country_laws_background.get_width() + 30 * self.factor_x + 40 * self.factor_x, start_pos + (95 * index) * self.factor_y, 424 * self.factor_x, 80 * self.factor_y)
						overlay_rect = (self.country_laws_background.get_width() + 30 * self.factor_x + 39 * self.factor_x, start_pos-1 + (95 * index) * self.factor_y, 426 * self.factor_x, 82 * self.factor_y)

						self.pygame.draw.rect(screen, (6,15,20), rect)

						show_description = False
						if index == laws_group.active_law_index:
							self.pygame.draw.rect(screen, (255,38,42), overlay_rect, 4)
							if self.hovered_rect == None:
								show_description = True
						if self.hovered_rect == rect:
							self.pygame.draw.rect(screen, (0,255,0), overlay_rect, 4)
							show_description = True
						if index != laws_group.active_law_index and self.hovered_rect != rect:
							self.pygame.draw.rect(screen, (43,219,211), overlay_rect, 2)
							show_description = False

						if show_description == True:
							# LAW DESCRIPTION
							if law.description_complement == None:
								law_description = self.big_scalable_font.render(law.description, True, (255, 255, 255))
							else:
								law_description = self.big_scalable_font.render(law.description + getattr(self.PlayerCountry, law.description_complement), True, (255, 255, 255))
							text_position = (self.country_laws_background.get_width() + 30 * self.factor_x + 490 * self.factor_x, start_pos + 63 * self.factor_y)						
							self.pygame.draw.rect(screen, (6,15,20), (self.country_laws_background.get_width() + 30 * self.factor_x + 480 * self.factor_x, start_pos-1, 538 * self.factor_x, law_description.get_height() + 20 * self.factor_y + 65 * self.factor_y))
							screen.blit(self.laws_description_image, (self.country_laws_background.get_width() + 30 * self.factor_x + 495 * self.factor_x, start_pos))
							
							self.pygame.draw.rect(screen, (255,255,255), (self.country_laws_background.get_width() + 30 * self.factor_x + 480 * self.factor_x, start_pos-1, 538 * self.factor_x, law_description.get_height() + 20 * self.factor_y + 65 * self.factor_y), 2)
							screen.blit(law_description, text_position)

						law_opened = self.big_scalable_font.render(law.name, True, (255, 255, 255))
						text_position = (self.country_laws_background.get_width() + 30 * self.factor_x + 60 * self.factor_x, start_pos + (95 * index) * self.factor_y + 40 * self.factor_y - law_opened.get_height()/2)
						screen.blit(law_opened, text_position)	

						self.laws_butons_rect.append(rect)

class Finances_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, economic_overview_background, poverty_rate_0, poverty_rate_5, poverty_rate_10,
			poverty_rate_15, poverty_rate_25, poverty_rate_50, poverty_rate_80, credit_ratings, economic_warning, economic_freedom_index_green, economic_freedom_index_red,
			economic_freedom_score_green, economic_freedom_score_red, small_rating_green, small_rating_red):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = None		

		self.economic_overview_background = pygame.transform.smoothscale_by(economic_overview_background, (self.factor_x, self.factor_y))	
		
		self.poverty_rate_0 	= pygame.transform.smoothscale_by(poverty_rate_0, (self.factor_x, self.factor_y))
		self.poverty_rate_5 	= pygame.transform.smoothscale_by(poverty_rate_5, (self.factor_x, self.factor_y))
		self.poverty_rate_10 	= pygame.transform.smoothscale_by(poverty_rate_10, (self.factor_x, self.factor_y))
		self.poverty_rate_15 	= pygame.transform.smoothscale_by(poverty_rate_15, (self.factor_x, self.factor_y))
		self.poverty_rate_25	= pygame.transform.smoothscale_by(poverty_rate_25, (self.factor_x, self.factor_y))
		self.poverty_rate_50 	= pygame.transform.smoothscale_by(poverty_rate_50, (self.factor_x, self.factor_y))
		self.poverty_rate_80 	= pygame.transform.smoothscale_by(poverty_rate_80, (self.factor_x, self.factor_y))		

		self.credit_ratings		= pygame.transform.smoothscale_by(credit_ratings, (self.factor_x, self.factor_y))
		self.economic_warning	= pygame.transform.smoothscale_by(economic_warning, (self.factor_x, self.factor_y))

		self.economic_freedom_index_green		= pygame.transform.smoothscale_by(economic_freedom_index_green, (self.factor_x, self.factor_y))
		self.economic_freedom_index_red			= pygame.transform.smoothscale_by(economic_freedom_index_red, (self.factor_x, self.factor_y))
		self.economic_freedom_score_green		= pygame.transform.smoothscale_by(economic_freedom_score_green, (self.factor_x, self.factor_y))
		self.economic_freedom_score_red			= pygame.transform.smoothscale_by(economic_freedom_score_red, (self.factor_x, self.factor_y))
		self.small_rating_green					= pygame.transform.smoothscale_by(small_rating_green, (self.factor_x, self.factor_y))
		self.small_rating_red					= pygame.transform.smoothscale_by(small_rating_red, (self.factor_x, self.factor_y))


		self.is_menu_open = False
		self.highlight_button = False


		self.poverty_rate_image_pos_x = 340 * self.factor_x
		self.poverty_rate_image_pos_y = 692 * self.factor_y + 158 * self.factor_y	
		

		self.credit_rating_image_pos_x = 293 * self.factor_x
		self.credit_rating_image_pos_y = 584 * self.factor_y + 158 * self.factor_y

		self.credit_rating_image_size_x = 125 * self.factor_x
		self.credit_rating_image_size_y = 64 * self.factor_y


		self.economic_warnings_image_pos_x = 17 * self.factor_x
		self.economic_warnings_image_pos_y = 559 * self.factor_y + 158 * self.factor_y

		self.economic_warnings_image_size_x = 124 * self.factor_x
		self.economic_warnings_image_size_y = 58 * self.factor_y		


		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_finances_button = GenericUtilitys.Button(247 * self.factor_x, height, button_size[0], button_size[1])

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_finances_button.rect.colliderect(mouse_rect):
			return "finances_button"
		
		return None

	def draw(self, screen):
		if self.is_menu_open == True:
			screen.blit(self.economic_overview_background, (0, 158 * self.factor_y))

			country_poverty_rate = (self.PlayerCountry.country_poverty_rate[0] * 100)

			if country_poverty_rate < 5:
				screen.blit(self.poverty_rate_0, (self.poverty_rate_image_pos_x, self.poverty_rate_image_pos_y))	
			elif country_poverty_rate < 10:
				screen.blit(self.poverty_rate_5, (self.poverty_rate_image_pos_x, self.poverty_rate_image_pos_y))		
			elif country_poverty_rate < 15:
				screen.blit(self.poverty_rate_10, (self.poverty_rate_image_pos_x, self.poverty_rate_image_pos_y))	
			elif country_poverty_rate < 25:
				screen.blit(self.poverty_rate_15, (self.poverty_rate_image_pos_x, self.poverty_rate_image_pos_y))	
			elif country_poverty_rate < 50:
				screen.blit(self.poverty_rate_25, (self.poverty_rate_image_pos_x, self.poverty_rate_image_pos_y))	
			elif country_poverty_rate < 80:
				screen.blit(self.poverty_rate_50, (self.poverty_rate_image_pos_x, self.poverty_rate_image_pos_y))	
			elif country_poverty_rate <= 100:
				screen.blit(self.poverty_rate_80, (self.poverty_rate_image_pos_x, self.poverty_rate_image_pos_y))	


			country_credit_rating = self.PlayerCountry.credit_rating

			if country_credit_rating < 10:																							
				screen.blit(self.credit_ratings.subsurface(0, 0, self.credit_rating_image_size_x, self.credit_rating_image_size_y), (self.credit_rating_image_pos_x, self.credit_rating_image_pos_y))
			elif country_credit_rating < 20:																							
				screen.blit(self.credit_ratings.subsurface(125 * self.factor_x, 0, self.credit_rating_image_size_x, self.credit_rating_image_size_y), (self.credit_rating_image_pos_x, self.credit_rating_image_pos_y))	
			elif country_credit_rating < 30:																							
				screen.blit(self.credit_ratings.subsurface(250 * self.factor_x, 0, self.credit_rating_image_size_x, self.credit_rating_image_size_y), (self.credit_rating_image_pos_x, self.credit_rating_image_pos_y))	
			elif country_credit_rating < 40:																							
				screen.blit(self.credit_ratings.subsurface(375 * self.factor_x, 0, self.credit_rating_image_size_x, self.credit_rating_image_size_y), (self.credit_rating_image_pos_x, self.credit_rating_image_pos_y))	
			elif country_credit_rating < 50:																							
				screen.blit(self.credit_ratings.subsurface(500 * self.factor_x, 0, self.credit_rating_image_size_x, self.credit_rating_image_size_y), (self.credit_rating_image_pos_x, self.credit_rating_image_pos_y))	
			elif country_credit_rating < 60:																							
				screen.blit(self.credit_ratings.subsurface(625 * self.factor_x, 0, self.credit_rating_image_size_x, self.credit_rating_image_size_y), (self.credit_rating_image_pos_x, self.credit_rating_image_pos_y))	
			elif country_credit_rating < 70:																							
				screen.blit(self.credit_ratings.subsurface(750 * self.factor_x, 0, self.credit_rating_image_size_x, self.credit_rating_image_size_y), (self.credit_rating_image_pos_x, self.credit_rating_image_pos_y))	
			elif country_credit_rating < 80:																							
				screen.blit(self.credit_ratings.subsurface(875 * self.factor_x, 0, self.credit_rating_image_size_x, self.credit_rating_image_size_y), (self.credit_rating_image_pos_x, self.credit_rating_image_pos_y))	
			elif country_credit_rating < 90:																							
				screen.blit(self.credit_ratings.subsurface(1000 * self.factor_x, 0, self.credit_rating_image_size_x, self.credit_rating_image_size_y), (self.credit_rating_image_pos_x, self.credit_rating_image_pos_y))	
			elif country_credit_rating <= 100:																							
				screen.blit(self.credit_ratings.subsurface(1125 * self.factor_x, 0, self.credit_rating_image_size_x, self.credit_rating_image_size_y), (self.credit_rating_image_pos_x, self.credit_rating_image_pos_y))	


			country_economic_warnings = [1, 2, 3, 4, 5, 6]

			if len(country_economic_warnings) > 0:
				for economic_warning in country_economic_warnings:
					if economic_warning == 1:
						screen.blit(self.economic_warning.subsurface(7 * self.factor_x, 27 * self.factor_y, self.economic_warnings_image_size_x, self.economic_warnings_image_size_y), (self.economic_warnings_image_pos_x + 7 * self.factor_x, self.economic_warnings_image_pos_y + 27 * self.factor_y))
					elif economic_warning == 2:
						screen.blit(self.economic_warning.subsurface(141 * self.factor_x, 27 * self.factor_y, self.economic_warnings_image_size_x, self.economic_warnings_image_size_y), (self.economic_warnings_image_pos_x + 141 * self.factor_x, self.economic_warnings_image_pos_y + 27 * self.factor_y))
					elif economic_warning == 3:
						screen.blit(self.economic_warning.subsurface(7 * self.factor_x, 93 * self.factor_y, self.economic_warnings_image_size_x, self.economic_warnings_image_size_y), (self.economic_warnings_image_pos_x + 7 * self.factor_x, self.economic_warnings_image_pos_y + 93 * self.factor_y))
					elif economic_warning == 4:
						screen.blit(self.economic_warning.subsurface(141 * self.factor_x, 93 * self.factor_y, self.economic_warnings_image_size_x, self.economic_warnings_image_size_y), (self.economic_warnings_image_pos_x + 141 * self.factor_x, self.economic_warnings_image_pos_y + 93 * self.factor_y))
					elif economic_warning == 5:
						screen.blit(self.economic_warning.subsurface(7 * self.factor_x, 159 * self.factor_y, self.economic_warnings_image_size_x, self.economic_warnings_image_size_y), (self.economic_warnings_image_pos_x + 7 * self.factor_x, self.economic_warnings_image_pos_y + 159 * self.factor_y))
					elif economic_warning == 6:
						screen.blit(self.economic_warning.subsurface(141 * self.factor_x, 159 * self.factor_y, self.economic_warnings_image_size_x, self.economic_warnings_image_size_y), (self.economic_warnings_image_pos_x + 141 * self.factor_x, self.economic_warnings_image_pos_y + 159 * self.factor_y))


			# INFLATION
			country_inflation_text_render = self.medium_scalable_font.render(str(round(self.PlayerCountry.inflation, 3))+' %', False, (255,255,255))	
			screen.blit(country_inflation_text_render, (294 * self.factor_x, 39 * self.factor_y + 158 * self.factor_y))

			# GDP
			GDP = self.PlayerCountry.country_GDP
			if abs(GDP) < 1e6:
				formatted_GDP = f"${GDP:,.2f}"
			elif abs(GDP) < 1e9:
				formatted_GDP = f"${GDP / 1e6:.3f} M"
			elif abs(GDP) < 1e12:
				formatted_GDP = f"${GDP / 1e9:.3f} B"
			elif abs(GDP) < 1e15:
				formatted_GDP = f"${GDP / 1e12:.3f} T"
			else:
				formatted_GDP = f"${GDP:.2f}"
						
			country_gdp_text_render = self.medium_scalable_font.render(formatted_GDP, False, (255,255,255))	
			screen.blit(country_gdp_text_render, (228 * self.factor_x, 203 * self.factor_y + 158 * self.factor_y))

			# DEBT-TO-GDP
			country_debt_to_gdp_text_render = self.medium_scalable_font.render(str(round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2))+' %', False, (255,255,255))	
			screen.blit(country_debt_to_gdp_text_render, (329 * self.factor_x, 367 * self.factor_y + 158 * self.factor_y))


			# FREEDOM INDEX
			x_offset = 439 * self.factor_x
			for freedom_index in range(12):
				green_ammount = self.economic_freedom_index_green.get_width() * 0.4
				screen.blit(self.economic_freedom_index_green.subsurface(0, 0, green_ammount, self.economic_freedom_index_green.get_height()), (x_offset, (150 + (34 * freedom_index)) * self.factor_y + 158 * self.factor_y))
				
				red_ammount = self.economic_freedom_index_red.get_width() * 0.4
				screen.blit(self.economic_freedom_index_red.subsurface(0, 0, red_ammount, self.economic_freedom_index_red.get_height()), (x_offset + (self.economic_freedom_index_red.get_width() - red_ammount), (150 + (34 * freedom_index)) * self.factor_y + 158 * self.factor_y))
			
			#	SCORE
			green_ammount = self.economic_freedom_score_green.get_width() * 0.4
			screen.blit(self.economic_freedom_score_green.subsurface(0, 0, green_ammount, self.economic_freedom_score_green.get_height()), (x_offset, (98 * self.factor_y + 158 * self.factor_y)))
			
			red_ammount = self.economic_freedom_score_red.get_width() * 0.4
			screen.blit(self.economic_freedom_score_red.subsurface(0, 0, red_ammount, self.economic_freedom_score_red.get_height()), (x_offset + (self.economic_freedom_score_red.get_width() - red_ammount), (98 * self.factor_y + 158 * self.factor_y)))

			# CREDIT RATING
			x_offset = 297 * self.factor_x

			credit_stability = self.PlayerCountry.credit_stability

			green_ammount = self.small_rating_green.get_width() * ((self.PlayerCountry.credit_rating/100) * credit_stability)
			screen.blit(self.small_rating_green.subsurface(0, 0, green_ammount, self.small_rating_green.get_height()), (x_offset, (653 * self.factor_y + 158 * self.factor_y)))
			
			red_ammount = self.small_rating_red.get_width() * (1  * credit_stability - (self.PlayerCountry.credit_rating/100))
			screen.blit(self.small_rating_red.subsurface(0, 0, red_ammount, self.small_rating_red.get_height()), (x_offset + (self.small_rating_red.get_width() - red_ammount), (653 * self.factor_y + 158 * self.factor_y)))

			# POVERTY
			green_ammount = self.small_rating_green.get_width() * self.PlayerCountry.country_poverty_rate[2]
			screen.blit(self.small_rating_green.subsurface(0, 0, green_ammount, self.small_rating_green.get_height()), (x_offset, (758 * self.factor_y + 158 * self.factor_y)))
			
			red_ammount = self.small_rating_red.get_width() * self.PlayerCountry.country_poverty_rate[0]
			screen.blit(self.small_rating_red.subsurface(0, 0, red_ammount, self.small_rating_red.get_height()), (x_offset + (self.small_rating_red.get_width() - red_ammount), (758 * self.factor_y + 158 * self.factor_y)))


			# GRAPHS

			#	INFLATION
			country_inflation_high_end_text_render = self.small_scalable_font.render(str(round(self.PlayerCountry.inflation + self.PlayerCountry.inflation*0.15, 3))+' %', False, (255,255,255))	
			screen.blit(country_inflation_high_end_text_render, (140 * self.factor_x - country_inflation_high_end_text_render.get_width(), 63 * self.factor_y + 158 * self.factor_y - country_inflation_high_end_text_render.get_height()/2))
			
			country_inflation_low_end_text_render = self.small_scalable_font.render(str(round(self.PlayerCountry.inflation - self.PlayerCountry.inflation*0.15, 3))+' %', False, (255,255,255))	
			screen.blit(country_inflation_low_end_text_render, (140 * self.factor_x - country_inflation_low_end_text_render.get_width(), 163 * self.factor_y + 158 * self.factor_y - country_inflation_low_end_text_render.get_height()/2))

			graph_dots = []
			for index, weekly_data in enumerate(self.PlayerCountry.weekly_inflation_data):
				if weekly_data > self.PlayerCountry.inflation:
					height = 113 - (50 * (min(1, (weekly_data/(self.PlayerCountry.inflation + 0.01)) - 1)))
				else:
					height = 113 + (50 * (min(1, (self.PlayerCountry.inflation/(weekly_data + 0.01)) - 1)))
				
				graph_dots.append(((3.855 * index + 173) * self.factor_x, (height + 158) * self.factor_y))

			if len(graph_dots) > 1:
				self.pygame.draw.lines(screen, (255,0,0), False, graph_dots, 3)
			else:
				self.pygame.draw.line(screen, (255,0,0), graph_dots[0], (graph_dots[0][0], (113 + 158) * self.factor_y), 3)				

			#	GDP
			GDP = self.PlayerCountry.country_GDP + self.PlayerCountry.country_GDP*0.15

			if abs(GDP) < 1e6:
				high_end_formatted_GDP = f"${GDP:,.2f}"
			elif abs(GDP) < 1e9:
				high_end_formatted_GDP = f"${GDP / 1e6:.3f} M"
			elif abs(GDP) < 1e12:
				high_end_formatted_GDP = f"${GDP / 1e9:.3f} B"
			elif abs(GDP) < 1e15:
				high_end_formatted_GDP = f"${GDP / 1e12:.3f} T"
			else:
				high_end_formatted_GDP = f"${GDP:.2f}"

			country_gdp_high_end_text_render = self.small_scalable_font.render(high_end_formatted_GDP, False, (255,255,255))	
			screen.blit(country_gdp_high_end_text_render, (140 * self.factor_x - country_gdp_high_end_text_render.get_width(), 227 * self.factor_y + 158 * self.factor_y - country_gdp_high_end_text_render.get_height()/2))
			
			GDP = self.PlayerCountry.country_GDP - self.PlayerCountry.country_GDP*0.15

			if abs(GDP) < 1e6:
				low_end_formatted_GDP = f"${GDP:,.2f}"
			elif abs(GDP) < 1e9:
				low_end_formatted_GDP = f"${GDP / 1e6:.3f} M"
			elif abs(GDP) < 1e12:
				low_end_formatted_GDP = f"${GDP / 1e9:.3f} B"
			elif abs(GDP) < 1e15:
				low_end_formatted_GDP = f"${GDP / 1e12:.3f} T"
			else:
				low_end_formatted_GDP = f"${GDP:.2f}"

			country_gdp_low_end_text_render = self.small_scalable_font.render(low_end_formatted_GDP, False, (255,255,255))	
			screen.blit(country_gdp_low_end_text_render, (140 * self.factor_x - country_gdp_low_end_text_render.get_width(), 327 * self.factor_y + 158 * self.factor_y - country_gdp_low_end_text_render.get_height()/2))

			graph_dots = []
			for index, weekly_data in enumerate(self.PlayerCountry.weekly_country_GDP_data):
				if weekly_data > self.PlayerCountry.country_GDP:
					height = 277 - (50 * (min(1, (weekly_data/(self.PlayerCountry.country_GDP + 0.01)) - 1)))
				else:
					height = 277 + (50 * (min(1, (self.PlayerCountry.country_GDP/(weekly_data + 0.01)) - 1)))
				
				graph_dots.append(((3.855 * index + 173) * self.factor_x, (height + 158) * self.factor_y))

			if len(graph_dots) > 1:
				self.pygame.draw.lines(screen, (0,255,0), False, graph_dots, 3)
			else:
				self.pygame.draw.line(screen, (0,255,0), graph_dots[0], (graph_dots[0][0], (277 + 158) * self.factor_y), 3)				

			#	DEBT-TO-GDP
			debt_to_gdp = round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2)

			debt_to_gdp_high_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp + debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
			screen.blit(debt_to_gdp_high_end_text_render, (140 * self.factor_x - debt_to_gdp_high_end_text_render.get_width(), 391 * self.factor_y + 158 * self.factor_y - debt_to_gdp_high_end_text_render.get_height()/2))
			
			debt_to_gdp_low_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp - debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
			screen.blit(debt_to_gdp_low_end_text_render, (140 * self.factor_x - debt_to_gdp_low_end_text_render.get_width(), 491 * self.factor_y + 158 * self.factor_y - debt_to_gdp_low_end_text_render.get_height()/2))

			graph_dots = []
			for index, weekly_data in enumerate(self.PlayerCountry.weekly_debt_to_gdp_data):
				if weekly_data > debt_to_gdp:
					height = 441 - (50 * (min(1, (weekly_data/(debt_to_gdp + 0.01)) - 1)))
				else:
					height = 441 + (50 * (min(1, (debt_to_gdp/(weekly_data + 0.01)) - 1)))
				
				graph_dots.append(((3.855 * index + 173) * self.factor_x, (height + 158) * self.factor_y))

			if len(graph_dots) > 1:
				self.pygame.draw.lines(screen, (255,0,0), False, graph_dots, 3)
			else:
				self.pygame.draw.line(screen, (255,0,0), graph_dots[0], (graph_dots[0][0], (441 + 158) * self.factor_y), 3)

			# BUDGET
				
			# EXPENDITURES
			expenses = self.PlayerCountry.expenses

			if abs(expenses) < 1e6:
				formatted_expenses = f"${expenses:,.2f}"
			elif abs(expenses) < 1e9:
				formatted_expenses = f"${expenses / 1e6:.3f} M"
			elif abs(expenses) < 1e12:
				formatted_expenses = f"${expenses / 1e9:.3f} B"
			elif abs(expenses) < 1e15:
				formatted_expenses = f"${expenses / 1e12:.3f} T"
			else:
				formatted_expenses = f"${expenses:.2f}"

			expenses_text_render = self.small_scalable_font.render(formatted_expenses, False, (255,255,255))	
			screen.blit(expenses_text_render, (519 * self.factor_x, 738 * self.factor_y + 158 * self.factor_y))

			# REVENUE
			income = self.PlayerCountry.income

			if abs(income) < 1e6:
				formatted_income = f"${income:,.2f}"
			elif abs(income) < 1e9:
				formatted_income = f"${income / 1e6:.3f} M"
			elif abs(income) < 1e12:
				formatted_income = f"${income / 1e9:.3f} B"
			elif abs(income) < 1e15:
				formatted_income = f"${income / 1e12:.3f} T"
			else:
				formatted_income = f"${income:.2f}"

			income_text_render = self.small_scalable_font.render(formatted_income, False, (255,255,255))	
			screen.blit(income_text_render, (720 * self.factor_x, 738 * self.factor_y + 158 * self.factor_y))			


			# DIFFERENCE

			difference = income - expenses

			if abs(difference) < 1e6:
				formatted_difference = f"${difference:,.2f}"
			elif abs(difference) < 1e9:
				formatted_difference = f"${difference / 1e6:.3f} M"
			elif abs(difference) < 1e12:
				formatted_difference = f"${difference / 1e9:.3f} B"
			elif abs(difference) < 1e15:
				formatted_difference = f"${difference / 1e12:.3f} T"
			else:
				formatted_difference = f"${difference:.2f}"

			if income > expenses:
				difference_text_render = self.medium_scalable_font.render(formatted_difference, False, (0,255,0))
			else:	
				difference_text_render = self.medium_scalable_font.render(formatted_difference, False, (255,0,0))

			screen.blit(difference_text_render, (641 * self.factor_x - difference_text_render.get_width()/2, 597 * self.factor_y + 158 * self.factor_y - difference_text_render.get_height()/2))
			#---------------------------------------------------------------------------------------------------------------------------------#	

		if self.highlight_button == True or self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,255,255), self.top_bar_finances_button.rect, 2)		

class intelligence_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, intelligence_overview_background, intelligency_agencies_icons_image_dic):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = None

		self.is_menu_open = False
		self.highlight_button = False

		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_intelligence_button = GenericUtilitys.Button(306 * self.factor_x, height, button_size[0], button_size[1])

		self.intelligence_overview_background = pygame.transform.smoothscale_by(intelligence_overview_background, (self.factor_x, self.factor_y))

		self.intelligency_agencies_icons_image_dic = intelligency_agencies_icons_image_dic

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_intelligence_button.rect.colliderect(mouse_rect):
			return "intelligence_button"
		
		return None

	def draw(self, screen):
		if self.is_menu_open == True:
			screen.blit(self.intelligence_overview_background, (0, 158 * self.factor_y))

			screen.blit(self.intelligency_agencies_icons_image_dic[self.PlayerCountry.country_intelligency_agency.icon_image_name], (18 * self.factor_x, 174 * self.factor_y))	

			intelligency_agency_name_text_render = self.huge_scalable_font.render(self.PlayerCountry.country_intelligency_agency.name, False, (255,255,255))	
			screen.blit(intelligency_agency_name_text_render, (106 * self.factor_x, 208 * self.factor_y))				

		if self.highlight_button == True or self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,255,255), self.top_bar_intelligence_button.rect, 2)

class Research_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, research_overview_background, researche_icons_image_dic, researche_institute_icons_image_dic,
		active_research_background):

		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = None

		self.is_menu_open = False
		self.highlight_button = False

		self.receive_player_keybord_input = False
		self.received_player_keybord_input = ''
		self.apply_received_player_keybord_input = False

		self.is_assign_institutes_menu_open = False
		self.research_project_to_assing_institute = None

		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_research_button = GenericUtilitys.Button(365 * self.factor_x, height, button_size[0], button_size[1])

		self.researche_institute_icons_image_dic = researche_institute_icons_image_dic

		# TECH TREES
		self.continue_research_progress = 0

		x_pos = 92 * self.factor_x
		button_size = (248 * self.factor_x, 69 * self.factor_y)
		self.warfare_tech_tree_button 		= GenericUtilitys.Button(x_pos, 67 * self.factor_y + 158 * self.factor_y, button_size[0], button_size[1])
		self.transport_tech_tree_button 	= GenericUtilitys.Button(x_pos, 146 * self.factor_y + 158 * self.factor_y, button_size[0], button_size[1])
		self.science_tech_tree_button 		= GenericUtilitys.Button(x_pos, 225 * self.factor_y + 158 * self.factor_y, button_size[0], button_size[1])
		self.technology_tech_tree_button 	= GenericUtilitys.Button(x_pos, 304 * self.factor_y + 158 * self.factor_y, button_size[0], button_size[1])
		self.medical_tech_tree_button 		= GenericUtilitys.Button(x_pos, 383 * self.factor_y + 158 * self.factor_y, button_size[0], button_size[1])
		self.society_tech_tree_button 		= GenericUtilitys.Button(x_pos, 462 * self.factor_y + 158 * self.factor_y, button_size[0], button_size[1])

		self.hovered_tech_tree_button = None
		self.open_tech_tree = None

		self.active_research_projects = []

		self.icons_offset_x = 0
		self.icons_offset_y = 0

		self.surface_size_x = 2000
		self.surface_size_y = 2000
		self.Warfare_Tech_Tree 		= Warfare_Tech_Tree(factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, self.surface_size_x, self.surface_size_x)
		self.Transport_Tech_Tree 	= Transport_Tech_Tree(factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, self.surface_size_x, self.surface_size_x)
		self.Science_Tech_Tree 		= Science_Tech_Tree(factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, self.surface_size_x, self.surface_size_x)
		self.Technology_Tech_Tree 	= Technology_Tech_Tree(factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, self.surface_size_x, self.surface_size_x)
		self.Medical_Tech_Tree 		= Medical_Tech_Tree(factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, self.surface_size_x, self.surface_size_x)
		self.Society_Tech_Tree 		= Society_Tech_Tree(factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, self.surface_size_x, self.surface_size_x)

		self.research_overview_background = pygame.transform.smoothscale_by(research_overview_background, (self.factor_x, self.factor_y))
		self.active_research_background = pygame.transform.smoothscale_by(active_research_background, (self.factor_x, self.factor_y))

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(13 * self.factor_y))		

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_research_button.rect.colliderect(mouse_rect):
			return "research_button"
		
		if self.is_menu_open == True:
			self.hovered_tech_tree_button = None
			if self.is_assign_institutes_menu_open == False:
				if self.warfare_tech_tree_button.rect.colliderect(mouse_rect):
					self.hovered_tech_tree_button = self.warfare_tech_tree_button
					return "warfare_tech_tree_button"
				elif self.transport_tech_tree_button.rect.colliderect(mouse_rect):
					self.hovered_tech_tree_button = self.transport_tech_tree_button
					return "transport_tech_tree_button"
				elif self.science_tech_tree_button.rect.colliderect(mouse_rect):
					self.hovered_tech_tree_button = self.science_tech_tree_button
					return "science_tech_tree_button"
				elif self.technology_tech_tree_button.rect.colliderect(mouse_rect):
					self.hovered_tech_tree_button = self.technology_tech_tree_button
					return "technology_tech_tree_button"
				elif self.medical_tech_tree_button.rect.colliderect(mouse_rect):
					self.hovered_tech_tree_button = self.medical_tech_tree_button
					return "medical_tech_tree_button"
				elif self.society_tech_tree_button.rect.colliderect(mouse_rect):
					self.hovered_tech_tree_button = self.society_tech_tree_button
					return "society_tech_tree_button"
			else:
				for index, research_institute in enumerate(self.PlayerCountry.research_institutes):
					research_institute_box_rect = self.pygame.Rect(7 * self.factor_x, 158 * self.factor_y + 7 * self.factor_y + (index * (110 * self.factor_y)), 657 * self.factor_x, 100 * self.factor_y)
					if research_institute_box_rect.colliderect(mouse_rect):
						return ('selected_research_institute_box', self.research_project_to_assing_institute, research_institute)
					else:
						research_institute.hovered = False

			if mouse_rect[0] >= 701 * self.factor_x and mouse_rect[1] >= 160 * self.factor_y and mouse_rect[1] <= 800 * self.factor_y:
				if self.open_tech_tree == "warfare_tech_tree_button":
					for rect, researche in self.Warfare_Tech_Tree.researches_rects:
						rect = self.pygame.Rect(rect[0]-self.icons_offset_x, rect[1]-self.icons_offset_y, rect[2], rect[3])
						if rect.colliderect(mouse_rect):
							self.Warfare_Tech_Tree.hovered_researche = (rect, researche)
							return researche
				elif self.open_tech_tree == "transport_tech_tree_button":
					for rect, researche in self.Transport_Tech_Tree.researches_rects:
						rect = self.pygame.Rect(rect[0]-self.icons_offset_x, rect[1]-self.icons_offset_y, rect[2], rect[3])
						if rect.colliderect(mouse_rect):
							self.Transport_Tech_Tree.hovered_researche = (rect, researche)
							return researche
				elif self.open_tech_tree == "science_tech_tree_button":
					for rect, researche in self.Science_Tech_Tree.researches_rects:
						rect = self.pygame.Rect(rect[0]-self.icons_offset_x, rect[1]-self.icons_offset_y, rect[2], rect[3])
						if rect.colliderect(mouse_rect):
							self.Science_Tech_Tree.hovered_researche = (rect, researche)
							return researche
				elif self.open_tech_tree == "technology_tech_tree_button":
					for rect, researche in self.Technology_Tech_Tree.researches_rects:
						rect = self.pygame.Rect(rect[0]-self.icons_offset_x, rect[1]-self.icons_offset_y, rect[2], rect[3])
						if rect.colliderect(mouse_rect):
							self.Technology_Tech_Tree.hovered_researche = (rect, researche)
							return researche
				elif self.open_tech_tree == "medical_tech_tree_button":
					for rect, researche in self.Medical_Tech_Tree.researches_rects:
						rect = self.pygame.Rect(rect[0]-self.icons_offset_x, rect[1]-self.icons_offset_y, rect[2], rect[3])
						if rect.colliderect(mouse_rect):
							self.Medical_Tech_Tree.hovered_researche = (rect, researche)
							return researche
				elif self.open_tech_tree == "society_tech_tree_button":
					for rect, researche in self.Society_Tech_Tree.researches_rects:
						rect = self.pygame.Rect(rect[0]-self.icons_offset_x, rect[1]-self.icons_offset_y, rect[2], rect[3])
						if rect.colliderect(mouse_rect):
							self.Society_Tech_Tree.hovered_researche = (rect, researche)
							return researche	
			
			for index, active_research_project in enumerate(self.active_research_projects):
				assign_workers_box_rect = self.pygame.Rect(709 * self.factor_x + 669 * self.factor_x, 149 * self.factor_y + 20 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y, 129 * self.factor_x, 24 * self.factor_y)
				if assign_workers_box_rect.colliderect(mouse_rect):
					return ('selected_workers_text_box', active_research_project)
				else:
					active_research_project.selected_workers_text_box = False

				assign_budget_box_rect = self.pygame.Rect(709 * self.factor_x + 972 * self.factor_x, 149 * self.factor_y + 41 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y, 206 * self.factor_x, 24 * self.factor_y)
				if assign_budget_box_rect.colliderect(mouse_rect):
					return ('assign_budget_box_rect', active_research_project)
				else:
					active_research_project.selected_budget_text_box = False					

				assign_institute_box_rect = self.pygame.Rect(709 * self.factor_x + 255 * self.factor_x, 149 * self.factor_y + 31 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y, 128 * self.factor_x, 64 * self.factor_y)
				if assign_institute_box_rect.colliderect(mouse_rect):
					return ('assign_institute_box_rect', active_research_project)
				elif self.is_assign_institutes_menu_open == False:
					active_research_project.selected_assign_institute_box = False

		return None

	def calculate_research_progress_increase(self, current_project_monthly_budget, necessary_budget, current_project_workers_amount, workers_quality):
		base_progress_rate = 0.01

		# Budget Efficiency Factor
		budget_efficiency_factor = 1 + ((current_project_monthly_budget/necessary_budget) * math.sqrt(current_project_monthly_budget))

		# Workers Efficiency Factor
		if current_project_workers_amount > 0:
			workers_efficiency_factor = 1 + (workers_quality * math.sqrt(current_project_workers_amount))
		else:
			workers_efficiency_factor = 0

		# Calculate Progress Increase Hourly
		progress_increase_hourly = (base_progress_rate * budget_efficiency_factor) * (base_progress_rate * workers_efficiency_factor)

		return progress_increase_hourly

	def increase_research_progress(self):
		if self.continue_research_progress != 0:
			for active_research_project in self.active_research_projects:
				for progress in range(self.continue_research_progress):
					workers_quality = active_research_project.assigned_research_institute.workforce_quality if active_research_project.assigned_research_institute else 0
					progress_increase_hourly = self.calculate_research_progress_increase(active_research_project.current_project_monthly_budget, active_research_project.necessary_budget, active_research_project.current_project_workers_amount, workers_quality)
					active_research_project.completion_progress += progress_increase_hourly	

					active_research_project.days_until_completion = round(((active_research_project.total_duration - active_research_project.completion_progress) / (progress_increase_hourly+0.000001)) / 24, 1)

					if active_research_project.completion_progress >= active_research_project.total_duration:
						active_research_project.assigned_research_institute.workers_assigned[active_research_project] = 0

						if active_research_project.type == 'warfare_researche':
							self.PlayerCountry.known_warfare_researches.append(active_research_project.name)
							self.Warfare_Tech_Tree.generate_researche_images(self.PlayerCountry)
						
						elif active_research_project.type == 'transport_researche':
							self.PlayerCountry.known_transport_researches.append(active_research_project.name)
							self.Transport_Tech_Tree.generate_researche_images(self.PlayerCountry)
						
						elif active_research_project.type == 'science_researche':
							self.PlayerCountry.known_science_researches.append(active_research_project.name)
							self.Science_Tech_Tree.generate_researche_images(self.PlayerCountry)
						
						elif active_research_project.type == 'technology_researche':
							self.PlayerCountry.known_technology_researches.append(active_research_project.name)
							self.Technology_Tech_Tree.generate_researche_images(self.PlayerCountry)
						
						elif active_research_project.type == 'medical_researche':
							self.PlayerCountry.known_medical_researches.append(active_research_project.name)
							self.Medical_Tech_Tree.generate_researche_images(self.PlayerCountry)
						
						elif active_research_project.type == 'society_researche':
							self.PlayerCountry.known_society_researches.append(active_research_project.name)
							self.Society_Tech_Tree.generate_researche_images(self.PlayerCountry)																																			
						
						try:
							self.active_research_projects.remove(active_research_project)
							break
						except:
							pass # SOMEHOW ALREADY REMOVED

		self.continue_research_progress = 0						

	def draw(self, screen):
		if self.is_menu_open == True:
			screen.blit(self.research_overview_background, (0, 158 * self.factor_y))

			# KNOWN TECHNOLOGIES
			x_pos = 630 * self.factor_x

			known_warfare_researches_text_render = self.big_scalable_font.render(str(len(self.PlayerCountry.known_warfare_researches)), False, (255,255,255))	
			screen.blit(known_warfare_researches_text_render, (x_pos, 93 * self.factor_y + 158 * self.factor_y))

			known_transport_researches_text_render = self.big_scalable_font.render(str(len(self.PlayerCountry.known_transport_researches)), False, (255,255,255))	
			screen.blit(known_transport_researches_text_render, (x_pos, 172 * self.factor_y + 158 * self.factor_y))

			known_science_researches_text_render = self.big_scalable_font.render(str(len(self.PlayerCountry.known_science_researches)), False, (255,255,255))	
			screen.blit(known_science_researches_text_render, (x_pos, 251 * self.factor_y + 158 * self.factor_y))

			known_technology_researches_text_render = self.big_scalable_font.render(str(len(self.PlayerCountry.known_technology_researches)), False, (255,255,255))	
			screen.blit(known_technology_researches_text_render, (x_pos, 330 * self.factor_y + 158 * self.factor_y))

			known_medical_researches_text_render = self.big_scalable_font.render(str(len(self.PlayerCountry.known_medical_researches)), False, (255,255,255))	
			screen.blit(known_medical_researches_text_render, (x_pos, 409 * self.factor_y + 158 * self.factor_y))

			known_society_researches_text_render = self.big_scalable_font.render(str(len(self.PlayerCountry.known_society_researches)), False, (255,255,255))	
			screen.blit(known_society_researches_text_render, (x_pos, 488 * self.factor_y + 158 * self.factor_y))															
			
			# TECH TREE BUTTONS
			if self.hovered_tech_tree_button:
				self.pygame.draw.rect(screen, (0,255,0), self.hovered_tech_tree_button.rect, 2)

			# OPEN TECH TREE
			if self.open_tech_tree:
				self.pygame.draw.rect(screen, (6,15,20), (701 * self.factor_x, 160 * self.factor_y, 1217 * self.factor_x, 796 * self.factor_y))

				if self.open_tech_tree == "warfare_tech_tree_button":
					self.pygame.draw.rect(screen, (255,255,255), self.warfare_tech_tree_button.rect, 4)
					self.Warfare_Tech_Tree.draw(screen, self.icons_offset_x, self.icons_offset_y)
				elif self.open_tech_tree == "transport_tech_tree_button":
					self.pygame.draw.rect(screen, (255,255,255), self.transport_tech_tree_button.rect, 4)
					self.Transport_Tech_Tree.draw(screen, self.icons_offset_x, self.icons_offset_y)
				elif self.open_tech_tree == "science_tech_tree_button":
					self.pygame.draw.rect(screen, (255,255,255), self.science_tech_tree_button.rect, 4)
					self.Science_Tech_Tree.draw(screen, self.icons_offset_x, self.icons_offset_y)
				elif self.open_tech_tree == "technology_tech_tree_button":
					self.pygame.draw.rect(screen, (255,255,255), self.technology_tech_tree_button.rect, 4)
					self.Technology_Tech_Tree.draw(screen, self.icons_offset_x, self.icons_offset_y)
				elif self.open_tech_tree == "medical_tech_tree_button":
					self.pygame.draw.rect(screen, (255,255,255), self.medical_tech_tree_button.rect, 4)
					self.Medical_Tech_Tree.draw(screen, self.icons_offset_x, self.icons_offset_y)
				elif self.open_tech_tree == "society_tech_tree_button":
					self.pygame.draw.rect(screen, (255,255,255), self.society_tech_tree_button.rect, 4)
					self.Society_Tech_Tree.draw(screen, self.icons_offset_x, self.icons_offset_y)
			
			else:
				is_player_typing_on_any_research_project = False
				for index, active_research_project in enumerate(self.active_research_projects):
					screen.blit(self.active_research_background, (709 * self.factor_x, 149 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y))

					self.pygame.draw.rect(screen, (255,0,0), (961 * self.factor_x, 263 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y, (942 * self.factor_x) * (active_research_project.completion_progress / active_research_project.total_duration), 10 * self.factor_y))
					
					screen.blit(active_research_project.icon, (709 * self.factor_x + 119 * self.factor_x - active_research_project.icon.get_width()/2, 149 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y + 58 * self.factor_y - active_research_project.icon.get_height()/2))
					
					active_research_project_name_text_render = self.medium_scalable_font.render(active_research_project.name, False, (255,255,255))	
					screen.blit(active_research_project_name_text_render, (709 * self.factor_x + 119 * self.factor_x - active_research_project_name_text_render.get_width()/2, 149 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y + 58 * self.factor_y - active_research_project_name_text_render.get_height()/2 + 52 * self.factor_y))					

					if active_research_project.assigned_research_institute:
						screen.blit(self.researche_institute_icons_image_dic[active_research_project.assigned_research_institute.icon_image_name], (709 * self.factor_x + 255 * self.factor_x, 149 * self.factor_y + 31 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y))

						total_workers_already_being_used = 0
						for key, workers_already_being_used in active_research_project.assigned_research_institute.workers_assigned.items():
							if key == active_research_project:
								continue
							total_workers_already_being_used += workers_already_being_used

						total_available_workers = active_research_project.assigned_research_institute.total_workers_amount - total_workers_already_being_used
					else:
						total_available_workers = 0
					
					active_research_workers_amount_text_render = self.tiny_scalable_font.render(str(total_available_workers), True, (255,127,127))	
					screen.blit(active_research_workers_amount_text_render, (709 * self.factor_x + 506 * self.factor_x, 149 * self.factor_y + 58 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y))	
					
					active_research_workers_amount_text_render = self.tiny_scalable_font.render(str(active_research_project.current_project_workers_amount), True, (127,201,255))	
					screen.blit(active_research_workers_amount_text_render, (709 * self.factor_x + 506 * self.factor_x, 149 * self.factor_y + 76 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y))	

					if active_research_project.hovered_workers_text_box == True:
						self.pygame.draw.rect(screen, (255,255,255), (709 * self.factor_x + 669 * self.factor_x, 149 * self.factor_y + 20 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y, 129 * self.factor_x, 24 * self.factor_y), 1)
						active_research_project.hovered_workers_text_box = False
					elif active_research_project.hovered_budget_text_box == True:
						self.pygame.draw.rect(screen, (255,255,255), (709 * self.factor_x + 972 * self.factor_x, 149 * self.factor_y + 41 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y, 206 * self.factor_x, 24 * self.factor_y), 1)
						active_research_project.hovered_budget_text_box = False		
					elif active_research_project.hovered_assign_institute_box == True or active_research_project.selected_assign_institute_box == True:
						self.pygame.draw.rect(screen, (105,233,127), (709 * self.factor_x + 255 * self.factor_x, 149 * self.factor_y + 31 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y, 128 * self.factor_x, 64 * self.factor_y), 3)
						active_research_project.hovered_assign_institute_box = False													

					if active_research_project.selected_workers_text_box == True or active_research_project.selected_budget_text_box == True:
						is_player_typing_on_any_research_project = True
						if self.apply_received_player_keybord_input == True:
							self.apply_received_player_keybord_input = False
							self.receive_player_keybord_input = False
							
							if active_research_project.selected_workers_text_box == True:
								active_research_project.selected_workers_text_box = False
								try:
									active_research_project.current_project_workers_amount = min(total_available_workers, int(self.received_player_keybord_input))
									active_research_project.assigned_research_institute.workers_assigned[active_research_project] = active_research_project.current_project_workers_amount
								except:
									pass
								self.received_player_keybord_input = ''
							
							if active_research_project.selected_budget_text_box == True:
								active_research_project.selected_budget_text_box = False
								try:
									active_research_project.current_project_monthly_budget = int(self.received_player_keybord_input)
								except:
									pass
								self.received_player_keybord_input = ''								
						
						
						wating_player_keybord_input_text_render = self.medium_scalable_font.render('|', True, (255,255,255))

						if active_research_project.selected_workers_text_box == True:
							received_player_keybord_input_text_render = self.medium_scalable_font.render(str(self.received_player_keybord_input), True, (255,255,255))
							text_pos = (709 * self.factor_x + 675 * self.factor_x, 149 * self.factor_y + 26 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y)
						else:
							if len(self.received_player_keybord_input) > 0:
								received_player_keybord_input_text_render = self.medium_scalable_font.render(f' ${int(self.received_player_keybord_input):,.2f}', True, (255,255,255))
							
							text_pos = (709 * self.factor_x + 978 * self.factor_x, 149 * self.factor_y + 47 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y)
						
						if len(self.received_player_keybord_input) > 0:
							screen.blit(received_player_keybord_input_text_render, text_pos)
						else:
							screen.blit(wating_player_keybord_input_text_render, text_pos)							

					active_research_current_budget_text_render = self.small_scalable_font.render(f' ${active_research_project.current_project_monthly_budget:,.2f}', True, (165,255,127))	
					screen.blit(active_research_current_budget_text_render, (709 * self.factor_x + 954 * self.factor_x, 149 * self.factor_y + 74 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y))

					active_research_days_until_completion_text_render = self.tiny_scalable_font.render(str(active_research_project.days_until_completion), True, (255,255,255))	
					screen.blit(active_research_days_until_completion_text_render, (709 * self.factor_x + 1029 * self.factor_x, 149 * self.factor_y + 101 * self.factor_y + (index * (142 * self.factor_y)) + 158 * self.factor_y))					
				
				if is_player_typing_on_any_research_project == False:
					self.apply_received_player_keybord_input = False
					self.receive_player_keybord_input = False		
					self.received_player_keybord_input = ''		

				active_research_amount_text_render = self.medium_scalable_font.render('RESEARCHES: ' + str(len(self.active_research_projects)), True, (255,255,255))	
				screen.blit(active_research_amount_text_render, (1715 * self.factor_x, 22 * self.factor_y + 158 * self.factor_y))		

				if self.is_assign_institutes_menu_open == True:
					self.pygame.draw.rect(screen, (6,15,20), (2 * self.factor_x, 160 * self.factor_y, 697 * self.factor_x, 796 * self.factor_y))
					for index, research_institute in enumerate(self.PlayerCountry.research_institutes):
						research_institute_box_rect = self.pygame.Rect(7 * self.factor_x, 158 * self.factor_y + 7 * self.factor_y + (index * (110 * self.factor_y)), 657 * self.factor_x, 100 * self.factor_y)		
						if research_institute.hovered:
							self.pygame.draw.rect(screen, (105,233,127), research_institute_box_rect, 3)	
							research_institute.hovered = False	
						else:
							self.pygame.draw.rect(screen, (255,255,255), research_institute_box_rect, 2)

						screen.blit(self.researche_institute_icons_image_dic[research_institute.icon_image_name], (17 * self.factor_x, 158 * self.factor_y + 17 * self.factor_y + (index * (110 * self.factor_y))))

						research_institute_name_text_render = self.small_scalable_font.render(research_institute.name, True, (255,255,255))	
						screen.blit(research_institute_name_text_render, (17 * self.factor_x, 158 * self.factor_y + 107 * self.factor_y + (index * (110 * self.factor_y)) - research_institute_name_text_render.get_height()*1.4))			

						research_institute_workforce_amount_text_render = self.small_scalable_font.render('WORKERS AMOUNT:             ' + str(research_institute.total_workers_amount), True, (255,255,255))	
						screen.blit(research_institute_workforce_amount_text_render, (155 * self.factor_x, 158 * self.factor_y + 20 * self.factor_y + (index * (110 * self.factor_y))))		

						research_institute_workforce_quality_text_render = self.small_scalable_font.render('WORKFORCE QUALITY:        ' + str(research_institute.workforce_quality*100) + '%', True, (255,255,255))	
						screen.blit(research_institute_workforce_quality_text_render, (155 * self.factor_x, 158 * self.factor_y + 45 * self.factor_y + (index * (110 * self.factor_y))))															
		
		if self.highlight_button == True or self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,255,255), self.top_bar_research_button.rect, 2)
class Research_Project:
	def __init__(self, name, type, icon):
		self.name = name
		self.type = type
		self.icon = icon

		self.total_duration = 100
		self.completion_progress = 0

		self.current_project_monthly_budget = 0
		self.current_project_workers_amount = 0

		self.necessary_budget = 1_000_000_000

		self.days_until_completion = 0

		self.assigned_research_institute = None

		# TEXT BOX
		self.hovered_workers_text_box = False
		self.selected_workers_text_box = False

		self.hovered_budget_text_box = False
		self.selected_budget_text_box = False

		# ASSIGNED INSTITUTE
		self.hovered_assign_institute_box = False
		self.selected_assign_institute_box = False
class Warfare_Tech_Tree:
	def __init__(self,factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, surface_size_x, surface_size_y):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.researche_icons_image_dic = researche_icons_image_dic

		self.background = pygame.Surface((1217 * self.factor_x, 796 * self.factor_y), pygame.SRCALPHA)
		self.background.blit(researche_icons_image_dic['warfare_tree_background'], (0,0))

		self.researches_surface = pygame.Surface((surface_size_x * self.factor_x, surface_size_y * self.factor_y), pygame.SRCALPHA)

		self.researches_lines_connection_surface = pygame.Surface((2000 * self.factor_x, 2000 * self.factor_y), pygame.SRCALPHA)

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))

		self.researches_rects = []

		self.hovered_researche = None

		self.researches = {
			'tech 1': {
				'name': 'TECH NAME 1',
				'position': (150, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': None,
				'available': None,
				'type': 'warfare_researche'
			},
			'tech 2': {
				'name': 'TECH NAME 2',
				'position': (150, 450),
				'icon': researche_icons_image_dic['tech_M-190_Cipher_Machine'],
				'requirements': None,
				'available': None,
				'type': 'warfare_researche'
			},
			'tech 3': {
				'name': 'TECH NAME 3',
				'position': (500, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': ['tech 1', 'tech 2'],
				'available': None,
				'type': 'warfare_researche'
			}						
		}

	def generate_researche_images(self, PlayerCountry):
		self.researches_rects = []

		self.researches_surface.fill((0, 0, 0, 0))
		self.researches_lines_connection_surface.fill((0, 0, 0, 0))

		for researche in self.researches.values():
			if researche['requirements']:
				is_research_available = True
				for requirement in researche['requirements']:
					self.pygame.draw.line(self.researches_lines_connection_surface, (255,255,255), (researche['position']), (self.researches[requirement]['position']), 2)
					if self.researches[requirement]['name'] not in PlayerCountry.known_warfare_researches:
						is_research_available = False
				
				if researche['name'] in PlayerCountry.known_warfare_researches:
					image = self.researche_icons_image_dic['technology_researched']	
					researche['available'] = False
				else:					
					if is_research_available:
						image = self.researche_icons_image_dic['technology_available']
						researche['available'] = True
					else:
						image = self.researche_icons_image_dic['technology_unavailable']
						researche['available'] = False
			else:
				if researche['name'] in PlayerCountry.known_warfare_researches:
					image = self.researche_icons_image_dic['technology_researched']
					researche['available'] = False	
				else:
					image = self.researche_icons_image_dic['technology_available']	
					researche['available'] = True						

			researche_rect = pygame.Rect(0,0, 239 * self.factor_x, 117 * self.factor_y)
			researche_rect.center = (researche['position'][0] * self.factor_x, researche['position'][1] * self.factor_y)

			self.researches_rects.append((pygame.Rect(researche_rect[0] + 701 * self.factor_x, researche_rect[1] + 160 * self.factor_y, researche_rect[2], researche_rect[3]), researche))
	
			self.researches_surface.blit(image, (researche_rect.center[0] - image.get_width()/2, researche_rect.center[1] - image.get_height()/2))

			self.researches_surface.blit(researche['icon'], (researche_rect.center[0] - researche['icon'].get_width()/2, researche_rect.center[1] - researche['icon'].get_height()/2))

			researche_name_text_render = self.medium_scalable_font.render(researche['name'], False, (255,255,255))	
			self.researches_surface.blit(researche_name_text_render, (researche_rect.center[0] - researche_name_text_render.get_width()/2, researche_rect.center[1] + 56 * self.factor_y - researche_name_text_render.get_height()))

	def draw(self, screen, offset_x, offset_y):
		screen.blit(self.background, (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_lines_connection_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		if self.hovered_researche:
			rect = self.hovered_researche[0].copy()
			rect = (max(701 * self.factor_x, rect[0]), max(160 * self.factor_y, rect[1]), min(rect[0]-(701 * self.factor_x)+rect[2],rect[2]), min(rect[1]-(160 * self.factor_y)+rect[3],rect[3]))
			self.pygame.draw.rect(screen, (255,255,255), rect, 3)
			self.hovered_researche = None
class Transport_Tech_Tree:
	def __init__(self,factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, surface_size_x, surface_size_y):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.researche_icons_image_dic = researche_icons_image_dic

		self.background = pygame.Surface((1217 * self.factor_x, 796 * self.factor_y), pygame.SRCALPHA)
		self.background.blit(researche_icons_image_dic['transport_tree_background'], (0,0))

		self.researches_surface = pygame.Surface((surface_size_x * self.factor_x, surface_size_y * self.factor_y), pygame.SRCALPHA)

		self.researches_lines_connection_surface = pygame.Surface((2000 * self.factor_x, 2000 * self.factor_y), pygame.SRCALPHA)

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))

		self.researches_rects = []

		self.hovered_researche = None

		self.researches = {
			'tech 1': {
				'name': 'TECH NAME 1',
				'position': (150, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': None,
				'available': None,
				'type': 'transport_researche'
			},
			'tech 2': {
				'name': 'TECH NAME 2',
				'position': (150, 450),
				'icon': researche_icons_image_dic['tech_M-190_Cipher_Machine'],
				'requirements': None,
				'available': None,
				'type': 'transport_researche'
			},
			'tech 3': {
				'name': 'TECH NAME 3',
				'position': (500, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': ['tech 1', 'tech 2'],
				'available': None,
				'type': 'transport_researche'
			}						
		}

	def generate_researche_images(self, PlayerCountry):
		self.researches_rects = []

		self.researches_surface.fill((0, 0, 0, 0))
		self.researches_lines_connection_surface.fill((0, 0, 0, 0))

		for researche in self.researches.values():
			if researche['requirements']:
				is_research_available = True
				for requirement in researche['requirements']:
					self.pygame.draw.line(self.researches_lines_connection_surface, (255,255,255), (researche['position']), (self.researches[requirement]['position']), 2)
					if self.researches[requirement]['name'] not in PlayerCountry.known_transport_researches:
						is_research_available = False
				
				if researche['name'] in PlayerCountry.known_transport_researches:
					image = self.researche_icons_image_dic['technology_researched']	
					researche['available'] = False
				else:					
					if is_research_available:
						image = self.researche_icons_image_dic['technology_available']
						researche['available'] = True
					else:
						image = self.researche_icons_image_dic['technology_unavailable']
						researche['available'] = False
			else:
				if researche['name'] in PlayerCountry.known_transport_researches:
					image = self.researche_icons_image_dic['technology_researched']
					researche['available'] = False	
				else:
					image = self.researche_icons_image_dic['technology_available']	
					researche['available'] = True						

			researche_rect = pygame.Rect(0,0, 239 * self.factor_x, 117 * self.factor_y)
			researche_rect.center = (researche['position'][0] * self.factor_x, researche['position'][1] * self.factor_y)

			self.researches_rects.append((pygame.Rect(researche_rect[0] + 701 * self.factor_x, researche_rect[1] + 160 * self.factor_y, researche_rect[2], researche_rect[3]), researche))
	
			self.researches_surface.blit(image, (researche_rect.center[0] - image.get_width()/2, researche_rect.center[1] - image.get_height()/2))

			self.researches_surface.blit(researche['icon'], (researche_rect.center[0] - researche['icon'].get_width()/2, researche_rect.center[1] - researche['icon'].get_height()/2))

			researche_name_text_render = self.medium_scalable_font.render(researche['name'], False, (255,255,255))	
			self.researches_surface.blit(researche_name_text_render, (researche_rect.center[0] - researche_name_text_render.get_width()/2, researche_rect.center[1] + 56 * self.factor_y - researche_name_text_render.get_height()))

	def draw(self, screen, offset_x, offset_y):
		screen.blit(self.background, (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_lines_connection_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		if self.hovered_researche:
			rect = self.hovered_researche[0].copy()
			rect = (max(701 * self.factor_x, rect[0]), max(160 * self.factor_y, rect[1]), min(rect[0]-(701 * self.factor_x)+rect[2],rect[2]), min(rect[1]-(160 * self.factor_y)+rect[3],rect[3]))
			self.pygame.draw.rect(screen, (255,255,255), rect, 3)
			self.hovered_researche = None
class Science_Tech_Tree:
	def __init__(self,factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, surface_size_x, surface_size_y):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.researche_icons_image_dic = researche_icons_image_dic

		self.background = pygame.Surface((1217 * self.factor_x, 796 * self.factor_y), pygame.SRCALPHA)
		self.background.blit(researche_icons_image_dic['science_tree_background'], (0,0))

		self.researches_surface = pygame.Surface((surface_size_x * self.factor_x, surface_size_y * self.factor_y), pygame.SRCALPHA)

		self.researches_lines_connection_surface = pygame.Surface((2000 * self.factor_x, 2000 * self.factor_y), pygame.SRCALPHA)

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))

		self.researches_rects = []

		self.hovered_researche = None

		self.researches = {
			'tech 1': {
				'name': 'TECH NAME 1',
				'position': (150, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': None,
				'available': None,
				'type': 'science_researche'
			},
			'tech 2': {
				'name': 'TECH NAME 2',
				'position': (150, 450),
				'icon': researche_icons_image_dic['tech_M-190_Cipher_Machine'],
				'requirements': None,
				'available': None,
				'type': 'science_researche'
			},
			'tech 3': {
				'name': 'TECH NAME 3',
				'position': (500, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': ['tech 1', 'tech 2'],
				'available': None,
				'type': 'science_researche'
			}						
		}

	def generate_researche_images(self, PlayerCountry):
		self.researches_rects = []

		self.researches_surface.fill((0, 0, 0, 0))
		self.researches_lines_connection_surface.fill((0, 0, 0, 0))

		for researche in self.researches.values():
			if researche['requirements']:
				is_research_available = True
				for requirement in researche['requirements']:
					self.pygame.draw.line(self.researches_lines_connection_surface, (255,255,255), (researche['position']), (self.researches[requirement]['position']), 2)
					if self.researches[requirement]['name'] not in PlayerCountry.known_science_researches:
						is_research_available = False
				
				if researche['name'] in PlayerCountry.known_science_researches:
					image = self.researche_icons_image_dic['technology_researched']	
					researche['available'] = False
				else:					
					if is_research_available:
						image = self.researche_icons_image_dic['technology_available']
						researche['available'] = True
					else:
						image = self.researche_icons_image_dic['technology_unavailable']
						researche['available'] = False
			else:
				if researche['name'] in PlayerCountry.known_science_researches:
					image = self.researche_icons_image_dic['technology_researched']
					researche['available'] = False	
				else:
					image = self.researche_icons_image_dic['technology_available']	
					researche['available'] = True						

			researche_rect = pygame.Rect(0,0, 239 * self.factor_x, 117 * self.factor_y)
			researche_rect.center = (researche['position'][0] * self.factor_x, researche['position'][1] * self.factor_y)

			self.researches_rects.append((pygame.Rect(researche_rect[0] + 701 * self.factor_x, researche_rect[1] + 160 * self.factor_y, researche_rect[2], researche_rect[3]), researche))
	
			self.researches_surface.blit(image, (researche_rect.center[0] - image.get_width()/2, researche_rect.center[1] - image.get_height()/2))

			self.researches_surface.blit(researche['icon'], (researche_rect.center[0] - researche['icon'].get_width()/2, researche_rect.center[1] - researche['icon'].get_height()/2))

			researche_name_text_render = self.medium_scalable_font.render(researche['name'], False, (255,255,255))	
			self.researches_surface.blit(researche_name_text_render, (researche_rect.center[0] - researche_name_text_render.get_width()/2, researche_rect.center[1] + 56 * self.factor_y - researche_name_text_render.get_height()))

	def draw(self, screen, offset_x, offset_y):
		screen.blit(self.background, (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_lines_connection_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		if self.hovered_researche:
			rect = self.hovered_researche[0].copy()
			rect = (max(701 * self.factor_x, rect[0]), max(160 * self.factor_y, rect[1]), min(rect[0]-(701 * self.factor_x)+rect[2],rect[2]), min(rect[1]-(160 * self.factor_y)+rect[3],rect[3]))
			self.pygame.draw.rect(screen, (255,255,255), rect, 3)
			self.hovered_researche = None
class Technology_Tech_Tree:
	def __init__(self,factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, surface_size_x, surface_size_y):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.researche_icons_image_dic = researche_icons_image_dic

		self.background = pygame.Surface((1217 * self.factor_x, 796 * self.factor_y), pygame.SRCALPHA)
		self.background.blit(researche_icons_image_dic['technology_tree_background'], (0,0))

		self.researches_surface = pygame.Surface((surface_size_x * self.factor_x, surface_size_y * self.factor_y), pygame.SRCALPHA)

		self.researches_lines_connection_surface = pygame.Surface((2000 * self.factor_x, 2000 * self.factor_y), pygame.SRCALPHA)

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))

		self.researches_rects = []

		self.hovered_researche = None

		self.researches = {
			'tech 1': {
				'name': 'TECH NAME 1',
				'position': (150, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': None,
				'available': None,
				'type': 'technology_researche'
			},
			'tech 2': {
				'name': 'TECH NAME 2',
				'position': (150, 450),
				'icon': researche_icons_image_dic['tech_M-190_Cipher_Machine'],
				'requirements': None,
				'available': None,
				'type': 'technology_researche'
			},
			'tech 3': {
				'name': 'TECH NAME 3',
				'position': (500, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': ['tech 1', 'tech 2'],
				'available': None,
				'type': 'technology_researche'
			}						
		}

	def generate_researche_images(self, PlayerCountry):
		self.researches_rects = []

		self.researches_surface.fill((0, 0, 0, 0))
		self.researches_lines_connection_surface.fill((0, 0, 0, 0))

		for researche in self.researches.values():
			if researche['requirements']:
				is_research_available = True
				for requirement in researche['requirements']:
					self.pygame.draw.line(self.researches_lines_connection_surface, (255,255,255), (researche['position']), (self.researches[requirement]['position']), 2)
					if self.researches[requirement]['name'] not in PlayerCountry.known_technology_researches:
						is_research_available = False
				
				if researche['name'] in PlayerCountry.known_technology_researches:
					image = self.researche_icons_image_dic['technology_researched']	
					researche['available'] = False
				else:					
					if is_research_available:
						image = self.researche_icons_image_dic['technology_available']
						researche['available'] = True
					else:
						image = self.researche_icons_image_dic['technology_unavailable']
						researche['available'] = False
			else:
				if researche['name'] in PlayerCountry.known_technology_researches:
					image = self.researche_icons_image_dic['technology_researched']
					researche['available'] = False	
				else:
					image = self.researche_icons_image_dic['technology_available']	
					researche['available'] = True						

			researche_rect = pygame.Rect(0,0, 239 * self.factor_x, 117 * self.factor_y)
			researche_rect.center = (researche['position'][0] * self.factor_x, researche['position'][1] * self.factor_y)

			self.researches_rects.append((pygame.Rect(researche_rect[0] + 701 * self.factor_x, researche_rect[1] + 160 * self.factor_y, researche_rect[2], researche_rect[3]), researche))
	
			self.researches_surface.blit(image, (researche_rect.center[0] - image.get_width()/2, researche_rect.center[1] - image.get_height()/2))

			self.researches_surface.blit(researche['icon'], (researche_rect.center[0] - researche['icon'].get_width()/2, researche_rect.center[1] - researche['icon'].get_height()/2))

			researche_name_text_render = self.medium_scalable_font.render(researche['name'], False, (255,255,255))	
			self.researches_surface.blit(researche_name_text_render, (researche_rect.center[0] - researche_name_text_render.get_width()/2, researche_rect.center[1] + 56 * self.factor_y - researche_name_text_render.get_height()))

	def draw(self, screen, offset_x, offset_y):
		screen.blit(self.background, (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_lines_connection_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		if self.hovered_researche:
			rect = self.hovered_researche[0].copy()
			rect = (max(701 * self.factor_x, rect[0]), max(160 * self.factor_y, rect[1]), min(rect[0]-(701 * self.factor_x)+rect[2],rect[2]), min(rect[1]-(160 * self.factor_y)+rect[3],rect[3]))
			self.pygame.draw.rect(screen, (255,255,255), rect, 3)
			self.hovered_researche = None
class Medical_Tech_Tree:
	def __init__(self,factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, surface_size_x, surface_size_y):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.researche_icons_image_dic = researche_icons_image_dic

		self.background = pygame.Surface((1217 * self.factor_x, 796 * self.factor_y), pygame.SRCALPHA)
		self.background.blit(researche_icons_image_dic['medical_tree_background'], (0,0))

		self.researches_surface = pygame.Surface((surface_size_x * self.factor_x, surface_size_y * self.factor_y), pygame.SRCALPHA)

		self.researches_lines_connection_surface = pygame.Surface((2000 * self.factor_x, 2000 * self.factor_y), pygame.SRCALPHA)

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))

		self.researches_rects = []

		self.hovered_researche = None

		self.researches = {
			'tech 1': {
				'name': 'TECH NAME 1',
				'position': (150, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': None,
				'available': None,
				'type': 'medical_researche'
			},
			'tech 2': {
				'name': 'TECH NAME 2',
				'position': (150, 450),
				'icon': researche_icons_image_dic['tech_M-190_Cipher_Machine'],
				'requirements': None,
				'available': None,
				'type': 'medical_researche'
			},
			'tech 3': {
				'name': 'TECH NAME 3',
				'position': (500, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': ['tech 1', 'tech 2'],
				'available': None,
				'type': 'medical_researche'
			}						
		}

	def generate_researche_images(self, PlayerCountry):
		self.researches_rects = []

		self.researches_surface.fill((0, 0, 0, 0))
		self.researches_lines_connection_surface.fill((0, 0, 0, 0))

		for researche in self.researches.values():
			if researche['requirements']:
				is_research_available = True
				for requirement in researche['requirements']:
					self.pygame.draw.line(self.researches_lines_connection_surface, (255,255,255), (researche['position']), (self.researches[requirement]['position']), 2)
					if self.researches[requirement]['name'] not in PlayerCountry.known_medical_researches:
						is_research_available = False
				
				if researche['name'] in PlayerCountry.known_medical_researches:
					image = self.researche_icons_image_dic['technology_researched']	
					researche['available'] = False
				else:					
					if is_research_available:
						image = self.researche_icons_image_dic['technology_available']
						researche['available'] = True
					else:
						image = self.researche_icons_image_dic['technology_unavailable']
						researche['available'] = False
			else:
				if researche['name'] in PlayerCountry.known_medical_researches:
					image = self.researche_icons_image_dic['technology_researched']
					researche['available'] = False	
				else:
					image = self.researche_icons_image_dic['technology_available']	
					researche['available'] = True						

			researche_rect = pygame.Rect(0,0, 239 * self.factor_x, 117 * self.factor_y)
			researche_rect.center = (researche['position'][0] * self.factor_x, researche['position'][1] * self.factor_y)

			self.researches_rects.append((pygame.Rect(researche_rect[0] + 701 * self.factor_x, researche_rect[1] + 160 * self.factor_y, researche_rect[2], researche_rect[3]), researche))
	
			self.researches_surface.blit(image, (researche_rect.center[0] - image.get_width()/2, researche_rect.center[1] - image.get_height()/2))

			self.researches_surface.blit(researche['icon'], (researche_rect.center[0] - researche['icon'].get_width()/2, researche_rect.center[1] - researche['icon'].get_height()/2))

			researche_name_text_render = self.medium_scalable_font.render(researche['name'], False, (255,255,255))	
			self.researches_surface.blit(researche_name_text_render, (researche_rect.center[0] - researche_name_text_render.get_width()/2, researche_rect.center[1] + 56 * self.factor_y - researche_name_text_render.get_height()))

	def draw(self, screen, offset_x, offset_y):
		screen.blit(self.background, (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_lines_connection_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		if self.hovered_researche:
			rect = self.hovered_researche[0].copy()
			rect = (max(701 * self.factor_x, rect[0]), max(160 * self.factor_y, rect[1]), min(rect[0]-(701 * self.factor_x)+rect[2],rect[2]), min(rect[1]-(160 * self.factor_y)+rect[3],rect[3]))
			self.pygame.draw.rect(screen, (255,255,255), rect, 3)
			self.hovered_researche = None
class Society_Tech_Tree:
	def __init__(self,factor_x, factor_y, screen_width, screen_height, pygame, researche_icons_image_dic, surface_size_x, surface_size_y):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.researche_icons_image_dic = researche_icons_image_dic

		self.background = pygame.Surface((1217 * self.factor_x, 796 * self.factor_y), pygame.SRCALPHA)
		self.background.blit(researche_icons_image_dic['society_tree_background'], (0,0))

		self.researches_surface = pygame.Surface((surface_size_x * self.factor_x, surface_size_y * self.factor_y), pygame.SRCALPHA)

		self.researches_lines_connection_surface = pygame.Surface((2000 * self.factor_x, 2000 * self.factor_y), pygame.SRCALPHA)

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))

		self.researches_rects = []

		self.hovered_researche = None

		self.researches = {
			'tech 1': {
				'name': 'TECH NAME 1',
				'position': (150, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': None,
				'available': None,
				'type': 'society_researche'
			},
			'tech 2': {
				'name': 'TECH NAME 2',
				'position': (150, 450),
				'icon': researche_icons_image_dic['tech_M-190_Cipher_Machine'],
				'requirements': None,
				'available': None,
				'type': 'society_researche'
			},
			'tech 3': {
				'name': 'TECH NAME 3',
				'position': (500, 250),
				'icon': researche_icons_image_dic['industry_tech_social_construction_3'],
				'requirements': ['tech 1', 'tech 2'],
				'available': None,
				'type': 'society_researche'
			}						
		}

	def generate_researche_images(self, PlayerCountry):
		self.researches_rects = []

		self.researches_surface.fill((0, 0, 0, 0))
		self.researches_lines_connection_surface.fill((0, 0, 0, 0))

		for researche in self.researches.values():
			if researche['requirements']:
				is_research_available = True
				for requirement in researche['requirements']:
					self.pygame.draw.line(self.researches_lines_connection_surface, (255,255,255), (researche['position']), (self.researches[requirement]['position']), 2)
					if self.researches[requirement]['name'] not in PlayerCountry.known_society_researches:
						is_research_available = False
				
				if researche['name'] in PlayerCountry.known_society_researches:
					image = self.researche_icons_image_dic['technology_researched']	
					researche['available'] = False
				else:					
					if is_research_available:
						image = self.researche_icons_image_dic['technology_available']
						researche['available'] = True
					else:
						image = self.researche_icons_image_dic['technology_unavailable']
						researche['available'] = False
			else:
				if researche['name'] in PlayerCountry.known_society_researches:
					image = self.researche_icons_image_dic['technology_researched']
					researche['available'] = False	
				else:
					image = self.researche_icons_image_dic['technology_available']	
					researche['available'] = True						

			researche_rect = pygame.Rect(0,0, 239 * self.factor_x, 117 * self.factor_y)
			researche_rect.center = (researche['position'][0] * self.factor_x, researche['position'][1] * self.factor_y)

			self.researches_rects.append((pygame.Rect(researche_rect[0] + 701 * self.factor_x, researche_rect[1] + 160 * self.factor_y, researche_rect[2], researche_rect[3]), researche))
	
			self.researches_surface.blit(image, (researche_rect.center[0] - image.get_width()/2, researche_rect.center[1] - image.get_height()/2))

			self.researches_surface.blit(researche['icon'], (researche_rect.center[0] - researche['icon'].get_width()/2, researche_rect.center[1] - researche['icon'].get_height()/2))

			researche_name_text_render = self.medium_scalable_font.render(researche['name'], False, (255,255,255))	
			self.researches_surface.blit(researche_name_text_render, (researche_rect.center[0] - researche_name_text_render.get_width()/2, researche_rect.center[1] + 56 * self.factor_y - researche_name_text_render.get_height()))

	def draw(self, screen, offset_x, offset_y):
		screen.blit(self.background, (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_lines_connection_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		screen.blit(self.researches_surface.subsurface(offset_x, offset_y, 1217 * self.factor_x, 796 * self.factor_y), (701 * self.factor_x, 160 * self.factor_y))

		if self.hovered_researche:
			rect = self.hovered_researche[0].copy()
			rect = (max(701 * self.factor_x, rect[0]), max(160 * self.factor_y, rect[1]), min(rect[0]-(701 * self.factor_x)+rect[2],rect[2]), min(rect[1]-(160 * self.factor_y)+rect[3],rect[3]))
			self.pygame.draw.rect(screen, (255,255,255), rect, 3)
			self.hovered_researche = None

class Global_Market_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.is_menu_open = False
		self.highlight_button = False

		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_global_market_button = GenericUtilitys.Button(424 * self.factor_x, height, button_size[0], button_size[1])

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_global_market_button.rect.colliderect(mouse_rect):
			return "global_market_button"
		
		return None

	def draw(self, screen):
		if self.is_menu_open == True:
			self.pygame.draw.rect(screen, (6,15,20), (0, 158 * self.factor_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y))
			self.pygame.draw.rect(screen, (43,219,211), (0, 158 * self.factor_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y), 2)			

		if self.highlight_button == True or self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,255,255), self.top_bar_global_market_button.rect, 2)

class Construction_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, construction_overview_background):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.is_menu_open = False
		self.highlight_button = False

		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_construction_button = GenericUtilitys.Button(483 * self.factor_x, height, button_size[0], button_size[1])

		self.construction_overview_background = pygame.transform.smoothscale_by(construction_overview_background, (self.factor_x, self.factor_y))

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_construction_button.rect.colliderect(mouse_rect):
			return "construction_button"
		
		return None

	def draw(self, screen):
		if self.is_menu_open == True:
			screen.blit(self.construction_overview_background, (0, 158 * self.factor_y))			

		if self.highlight_button == True or self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,255,255), self.top_bar_construction_button.rect, 2)

class Production_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, production_overview_background):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.is_menu_open = False
		self.highlight_button = False

		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_production_button = GenericUtilitys.Button(542 * self.factor_x, height, button_size[0], button_size[1])

		self.production_overview_background = pygame.transform.smoothscale_by(production_overview_background, (self.factor_x, self.factor_y))

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_production_button.rect.colliderect(mouse_rect):
			return "production_button"
		
		return None

	def draw(self, screen):
		if self.is_menu_open == True:
			screen.blit(self.production_overview_background, (0, 158 * self.factor_y))		

		if self.highlight_button == True or self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,255,255), self.top_bar_production_button.rect, 2)

class Army_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.is_menu_open = False
		self.highlight_button = False

		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_army_button = GenericUtilitys.Button(601 * self.factor_x, height, button_size[0], button_size[1])

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_army_button.rect.colliderect(mouse_rect):
			return "army_button"
		
		return None

	def draw(self, screen):
		if self.is_menu_open == True:
			self.pygame.draw.rect(screen, (6,15,20), (0, 158 * self.factor_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y))
			self.pygame.draw.rect(screen, (43,219,211), (0, 158 * self.factor_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y), 2)			

		if self.highlight_button == True or self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,255,255), self.top_bar_army_button.rect, 2)

class Stockpile_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.is_menu_open = False
		self.highlight_button = False

		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_stockpile_button = GenericUtilitys.Button(660 * self.factor_x, height, button_size[0], button_size[1])

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

	def get_button_by_interaction(self, mouse_rect):	
		if self.top_bar_stockpile_button.rect.colliderect(mouse_rect):
			return "stockpile_button"
		
		return None

	def draw(self, screen):
		if self.is_menu_open == True:
			self.pygame.draw.rect(screen, (6,15,20), (0, 158 * self.factor_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y))
			self.pygame.draw.rect(screen, (43,219,211), (0, 158 * self.factor_y, self.screen_width/2, self.screen_height - (158 + 110) * self.factor_y), 2)			

		if self.highlight_button == True or self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,255,255), self.top_bar_stockpile_button.rect, 2)

# BOTTOM BAR MENUS:
class Law_Opinion_survey_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, law_opinion_survey_menu):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame	

		self.law_opinion_survey_menu = law_opinion_survey_menu

		self.hovered_button = None

		self.law_opinion_survey_menu_close_button = GenericUtilitys.Button(1703 * self.factor_x, 660 * self.factor_y + 158 * self.factor_y, 199 * self.factor_x, 66 * self.factor_y)


		self.simple_population_survey_button 	= GenericUtilitys.Button(1247 * self.factor_x, 14 * self.factor_y + 158 * self.factor_y, 659 * self.factor_x, 40 * self.factor_y)
		self.extensive_population_survey_button = GenericUtilitys.Button(1247 * self.factor_x, 58 * self.factor_y + 158 * self.factor_y, 659 * self.factor_x, 40 * self.factor_y)

		self.parliament_survey_button 			= GenericUtilitys.Button(1247 * self.factor_x, 107 * self.factor_y + 158 * self.factor_y, 659 * self.factor_x, 40 * self.factor_y)
		self.senate_survey_button 				= GenericUtilitys.Button(1247 * self.factor_x, 151 * self.factor_y + 158 * self.factor_y, 659 * self.factor_x, 40 * self.factor_y)	

		self.law_being_survey = None	

		self.law_opinion_civilian = None
		self.law_opinion_parliament = None
		self.law_opinion_senate = None

		self.parliament_pie_chart_surface = pygame.Surface((603 * self.factor_x, 301 * self.factor_y), pygame.SRCALPHA)		
		self.senate_pie_chart_surface = pygame.Surface((603 * self.factor_x, 301 * self.factor_y), pygame.SRCALPHA)			

	def calculate_law_opinion_civilian(self, complexity = 'simple', law_project_being_survey = None):
		if complexity == 'simple':
			if law_project_being_survey != None:
				law_project_being_survey.opinion_surveyed = True
			
			if 'left' in self.law_being_survey.law_ideology:
				self.law_opinion_civilian = ([10, 25, 12], [23, 8, 22])

				if law_project_being_survey != None:
					law_project_being_survey.survey_civilian_support = ([10, 25, 12], [23, 8, 22])

	def calculate_law_opinion_parliament(self, PlayerCountry, law_project_being_survey = None):
		if law_project_being_survey != None:
			law_project_being_survey.opinion_surveyed = True
			law_project_being_survey.survey_parliament_support = 0

		self.parliament_pie_chart_surface.fill((0, 0, 0, 0))
		
		last_parliament_angle = 180
		for official_party in PlayerCountry.country_official_parties:

			law_disaproval_parliament = 0
			law_approval_parliament = 0
			
			if self.law_being_survey.law_ideology[0] in official_party.ideology:
				law_approval_parliament = 1
			else:
				law_disaproval_parliament = 1

			red_amount = int(255 * law_disaproval_parliament)
			green_amount = int(255 * law_approval_parliament)
			seats_color = (red_amount,green_amount,0)
			parliament_end_angle = 180 * (official_party.parliament_seats / PlayerCountry.total_parliament_seats)
			GenericUtilitys.draw_pie(self.parliament_pie_chart_surface, seats_color, (302 * self.factor_x, 300 * self.factor_y), 300 * self.factor_x, last_parliament_angle, parliament_end_angle + last_parliament_angle)
			last_parliament_angle = parliament_end_angle + last_parliament_angle

			if law_project_being_survey != None:
				law_project_being_survey.survey_parliament_support += (law_approval_parliament*100) * (official_party.parliament_seats / PlayerCountry.total_parliament_seats)

		self.law_opinion_parliament = 'Done'

	def calculate_law_opinion_senate(self, PlayerCountry, law_project_being_survey = None):
		if law_project_being_survey != None:
			law_project_being_survey.opinion_surveyed = True
			law_project_being_survey.survey_senate_support = 0			

		self.senate_pie_chart_surface.fill((0, 0, 0, 0))

		last_senate_angle = 180
		for official_party in PlayerCountry.country_official_parties:
			
			law_disaproval_senate = 0
			law_approval_senate = 0
			
			if self.law_being_survey.law_ideology[0] in official_party.ideology:
				law_approval_senate = 1
			else:
				law_disaproval_senate = 1

			red_amount = int(255 * law_disaproval_senate)
			green_amount = int(255 * law_approval_senate)
			seats_color = (red_amount,green_amount,0)	

			senate_end_angle = 180 * (official_party.senate_seats / PlayerCountry.total_senate_seats)
			GenericUtilitys.draw_pie(self.senate_pie_chart_surface, seats_color, (302 * self.factor_x, 300 * self.factor_y), 300 * self.factor_x, last_senate_angle, senate_end_angle + last_senate_angle)
			last_senate_angle = senate_end_angle + last_senate_angle

			if law_project_being_survey != None:
				law_project_being_survey.survey_senate_support += (law_approval_senate*100) * (official_party.senate_seats / PlayerCountry.total_senate_seats)

		self.law_opinion_senate = 'Done'												

	def get_button_by_interaction(self, mouse_rect):
		if self.law_opinion_survey_menu_close_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'law_opinion_survey_menu_close_button'
			return 'law_opinion_survey_menu_close_button'
		
		elif self.simple_population_survey_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'simple_population_survey_button'
			return 'simple_population_survey_button'			
		elif self.extensive_population_survey_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'extensive_population_survey_button'
			return 'extensive_population_survey_button'			
		elif self.parliament_survey_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'parliament_survey_button'
			return 'parliament_survey_button'			
		elif self.senate_survey_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'senate_survey_button'
			return 'senate_survey_button'			
		
		return None

	def draw(self, screen):
		screen.blit(self.law_opinion_survey_menu, (0, 158 * self.factor_y))

		if self.hovered_button == 'law_opinion_survey_menu_close_button':
			self.hovered_button = None
			self.pygame.draw.rect(screen, (255,0,0), self.law_opinion_survey_menu_close_button.rect, 2)
		
		elif self.hovered_button == 'simple_population_survey_button':
			self.hovered_button = None
			self.pygame.draw.rect(screen, (255,255,255), self.simple_population_survey_button.rect, 3)
		elif self.hovered_button == 'extensive_population_survey_button':
			self.hovered_button = None
			self.pygame.draw.rect(screen, (255,255,255), self.extensive_population_survey_button.rect, 3)		
		elif self.hovered_button == 'parliament_survey_button':
			self.hovered_button = None
			self.pygame.draw.rect(screen, (255,255,255), self.parliament_survey_button.rect, 3)		
		elif self.hovered_button == 'senate_survey_button':
			self.hovered_button = None
			self.pygame.draw.rect(screen, (255,255,255), self.senate_survey_button.rect, 3)	


		if self.law_opinion_civilian != None:
			# CIVILIAN CHART
			chart_position = (932 * self.factor_x, 456 * self.factor_y) 
			chart_radius = 249 * self.factor_y

			popularities = self.law_opinion_civilian[1].copy()
			popularities.extend(self.law_opinion_civilian[0].copy())

			GenericUtilitys.draw_pie_chart(screen, chart_position, chart_radius, popularities, [
			(255, 0, 0),
			(200, 0, 0),
			(150, 0, 0),
			(0, 255, 0),
			(0, 200, 0),
			(0, 150, 0)])	
			
		if self.law_opinion_parliament == 'Done':
			screen.blit(self.parliament_pie_chart_surface, (12 * self.factor_x, 223 * self.factor_y))	

		if self.law_opinion_senate == 'Done':
			screen.blit(self.senate_pie_chart_surface, (12 * self.factor_x, 587 * self.factor_y))				

class Bottom_HUD:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, bottom_HUD, law_opinion_survey_icon, law_opinion_survey_menu, finances_menu_background, budget_menu,
		debt_menu, taxation_menu, currency_menu, finance_menu, government_menu_background, head_of_state_menu, cabinet_menu, parliament_menu, elections_menu, political_parties_menu):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.bottom_HUD 			 = pygame.transform.smoothscale(bottom_HUD, (self.screen_width, bottom_HUD.get_height() * self.factor_y))

		self.law_opinion_survey_icon = pygame.transform.smoothscale_by(law_opinion_survey_icon, (self.factor_x, self.factor_y))
		self.law_opinion_survey_menu = pygame.transform.smoothscale_by(law_opinion_survey_menu, (self.factor_x, self.factor_y))

		# 1 
		self.finances_menu_background, self.budget_menu, self.debt_menu, self.taxation_menu, self.currency_menu, self.finance_menu = finances_menu_background, budget_menu, debt_menu, taxation_menu, currency_menu, finance_menu
		# 6
		self.government_menu_background, self.head_of_state_menu, self.cabinet_menu, self.parliament_menu, self.elections_menu, self.political_parties_menu = government_menu_background, head_of_state_menu, cabinet_menu, parliament_menu, elections_menu, political_parties_menu

		self.selected_map_overlay = 0
		self.active_map_overlay = 1

		offset_y = 	self.screen_height - self.bottom_HUD.get_height()

		self.bottom_HUD_rect = self.pygame.Rect(0, offset_y, 1920 * self.factor_x, 110 * self.factor_y)

		self.map_overlay_1 = GenericUtilitys.Button(1776 * self.factor_x, 12 * self.factor_y + offset_y, 59 * self.factor_x, 43 * self.factor_y)
		self.map_overlay_2 = GenericUtilitys.Button(1845 * self.factor_x, 12 * self.factor_y + offset_y, 59 * self.factor_x, 43 * self.factor_y)

		country_legislation_size_x = 210 * self.factor_x
		country_legislation_size_y = 86 * self.factor_y
		country_legislation_height = 12 * self.factor_y + offset_y
		self.country_legislation_1 = GenericUtilitys.Button(12 * self.factor_x, country_legislation_height, country_legislation_size_x, country_legislation_size_y)
		self.country_legislation_2 = GenericUtilitys.Button(240 * self.factor_x, country_legislation_height, country_legislation_size_x, country_legislation_size_y)
		self.country_legislation_3 = GenericUtilitys.Button(468 * self.factor_x, country_legislation_height, country_legislation_size_x, country_legislation_size_y)
		self.country_legislation_4 = GenericUtilitys.Button(696 * self.factor_x, country_legislation_height, country_legislation_size_x, country_legislation_size_y)
		self.country_legislation_5 = GenericUtilitys.Button(924 * self.factor_x, country_legislation_height, country_legislation_size_x, country_legislation_size_y)
		self.country_legislation_6 = GenericUtilitys.Button(1152 * self.factor_x, country_legislation_height, country_legislation_size_x, country_legislation_size_y)
		self.country_legislation_7 = GenericUtilitys.Button(1380 * self.factor_x, country_legislation_height, country_legislation_size_x, country_legislation_size_y)

		self.collided_country_legislation_button = None
		self.open_country_legislation = None
	
	def start_menus(self, PlayerCountry):	
		self.Law_Opinion_survey_Menu = Law_Opinion_survey_Menu(self.factor_x, self.factor_y, self.screen_width, self.screen_height, self.pygame, self.law_opinion_survey_menu)

		self.Legislative_Finances_Menu = Legislative_Finances_Menu(self.factor_x, self.factor_y, self.screen_width, self.screen_height, self.pygame, PlayerCountry, self.law_opinion_survey_icon, self.finances_menu_background, self.budget_menu, self.debt_menu, self.taxation_menu, self.currency_menu, self.finance_menu)		
		self.Legislative_Government_Menu = Legislative_Government_Menu(self.factor_x, self.factor_y, self.screen_width, self.screen_height, self.pygame, PlayerCountry, self.law_opinion_survey_icon, self.government_menu_background, self.head_of_state_menu, self.cabinet_menu, self.parliament_menu, self.elections_menu, self.political_parties_menu, self.Law_Opinion_survey_Menu)		

	def get_button_by_interaction(self, mouse_rect):
		if self.bottom_HUD_rect.colliderect(mouse_rect):
			self.Legislative_Finances_Menu.hovered_button = None
			self.Legislative_Government_Menu.hovered_button = None

			if self.map_overlay_1.rect.colliderect(mouse_rect):
				self.selected_map_overlay = 1
				return 1
			elif self.map_overlay_2.rect.colliderect(mouse_rect):
				self.selected_map_overlay = 2
				return 2

			self.collided_country_legislation_button = None
			for button in range(7):
				button_rect = getattr(self, 'country_legislation_'+str(button+1)).rect
				if button_rect.colliderect(mouse_rect):
					self.collided_country_legislation_button = button+1
					return 'country_legislation_button_'+str(button+1)
		else:
			if self.open_country_legislation == 'country_legislation_button_1': # FINANCES
				return self.Legislative_Finances_Menu.get_button_by_interaction(mouse_rect)
			elif self.open_country_legislation == 'country_legislation_button_6': # GOVERNMENT
				return self.Legislative_Government_Menu.get_button_by_interaction(mouse_rect)			
		
		self.selected_map_overlay = 0
		self.collided_country_legislation_button = None
		return None

	def draw(self, screen):		
		screen.blit(self.bottom_HUD, (0, self.screen_height - self.bottom_HUD.get_height()))

		self.pygame.draw.rect(screen, (0, 255, 0), getattr(self, 'map_overlay_'+str(self.active_map_overlay)).rect, 2)	

		if self.selected_map_overlay > 0:
			self.pygame.draw.rect(screen, (255, 255, 255), getattr(self, 'map_overlay_'+str(self.selected_map_overlay)).rect, 2)

		if self.collided_country_legislation_button != None:
			self.pygame.draw.rect(screen, (255, 255, 255), getattr(self, 'country_legislation_'+str(self.collided_country_legislation_button)).rect, 2)
		
		if self.open_country_legislation != None:
			self.pygame.draw.rect(screen, (255, 255, 255), getattr(self, 'country_legislation_'+str(self.open_country_legislation[-1])).rect, 2)
			if self.open_country_legislation == 'country_legislation_button_1': # FINANCES
				self.Legislative_Finances_Menu.draw(screen)
			elif self.open_country_legislation == 'country_legislation_button_6': # GOVERNMENT
				self.Legislative_Government_Menu.draw(screen)				

class Legislative_Finances_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, law_opinion_survey_icon, finances_menu_background, budget_menu, debt_menu, taxation_menu, currency_menu, finance_menu):

		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame		
		
		self.finances_menu_background 			= pygame.transform.smoothscale_by(finances_menu_background, (self.factor_x, self.factor_y))		

		self.Legislative_Finances_Budget_Menu = Legislative_Finances_Budget_Menu(factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, budget_menu)
		self.budget_menu_button = GenericUtilitys.Button(5 * self.factor_x, 741 * self.factor_y + 158 * self.factor_y, 380 * self.factor_x, 64 * self.factor_y)

		self.Legislative_Finances_Debt_Menu = Legislative_Finances_Debt_Menu(factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, debt_menu)
		self.debt_menu_button = GenericUtilitys.Button(387 * self.factor_x, 741 * self.factor_y + 158 * self.factor_y, 380 * self.factor_x, 64 * self.factor_y)

		self.Legislative_Finances_Taxation_Menu = Legislative_Finances_Taxation_Menu(factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, taxation_menu)
		self.taxation_menu_button = GenericUtilitys.Button(769 * self.factor_x, 741 * self.factor_y + 158 * self.factor_y, 380 * self.factor_x, 64 * self.factor_y)

		self.Legislative_Finances_Currency_Menu = Legislative_Finances_Currency_Menu(factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, currency_menu)
		self.currency_menu_button = GenericUtilitys.Button(1151 * self.factor_x, 741 * self.factor_y + 158 * self.factor_y, 380 * self.factor_x, 64 * self.factor_y)	

		self.Legislative_Finances_Finance_Menu = Legislative_Finances_Finance_Menu(factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, finance_menu)
		self.finance_menu_button = GenericUtilitys.Button(1533 * self.factor_x, 741 * self.factor_y + 158 * self.factor_y, 380 * self.factor_x, 64 * self.factor_y)				

		self.hovered_button = None

		self.open_menu = None

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(13 * self.factor_y))			

	def get_button_by_interaction(self, mouse_rect):
		if self.budget_menu_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'budget_menu_button'
			return 'budget_menu_button'
		elif self.debt_menu_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'debt_menu_button'
			return 'debt_menu_button'
		elif self.taxation_menu_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'taxation_menu_button'
			return 'taxation_menu_button'	
		elif self.currency_menu_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'currency_menu_button'
			return 'currency_menu_button'			
		elif self.finance_menu_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'finance_menu_button'
			return 'finance_menu_button'			
		else:
			if self.open_menu == 'budget_menu_button':
				Legislative_Finances_Budget_Menu_button = self.Legislative_Finances_Budget_Menu.get_button_by_interaction(mouse_rect)
				if Legislative_Finances_Budget_Menu_button:
					return Legislative_Finances_Budget_Menu_button

		self.hovered_button = None
		return None		

	def draw(self, screen):
		screen.blit(self.finances_menu_background, (0, 158 * self.factor_y))

		if self.hovered_button == 'budget_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.budget_menu_button.rect, 2)
		elif self.hovered_button == 'debt_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.debt_menu_button.rect, 2)
		elif self.hovered_button == 'taxation_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.taxation_menu_button.rect, 2)	
		elif self.hovered_button == 'currency_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.currency_menu_button.rect, 2)		
		elif self.hovered_button == 'finance_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.finance_menu_button.rect, 2)								

		if self.open_menu == 'budget_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.budget_menu_button.rect, 3)
			self.Legislative_Finances_Budget_Menu.draw(screen)
		elif self.open_menu == 'debt_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.debt_menu_button.rect, 3)
			self.Legislative_Finances_Debt_Menu.draw(screen)
		elif self.open_menu == 'taxation_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.taxation_menu_button.rect, 3)
			self.Legislative_Finances_Taxation_Menu.draw(screen)		
		elif self.open_menu == 'currency_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.currency_menu_button.rect, 3)
			self.Legislative_Finances_Currency_Menu.draw(screen)		
		elif self.open_menu == 'finance_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.finance_menu_button.rect, 3)
			self.Legislative_Finances_Finance_Menu.draw(screen)							
class Legislative_Finances_Budget_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, budget_menu):

		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = PlayerCountry

		self.budget_menu = pygame.transform.smoothscale_by(budget_menu, (self.factor_x, self.factor_y))

		self.PlayerCountry_expenses_dict = {
		'0': self.PlayerCountry.agriculture_expense,
		'1': self.PlayerCountry.culture_expense,
		'2': self.PlayerCountry.debt_interest_expense,
		'3': self.PlayerCountry.defense_expense,
		'4': self.PlayerCountry.economy_expense,
		'5': self.PlayerCountry.education_expense,
		'6': self.PlayerCountry.employment_social_expense,
		'7': self.PlayerCountry.energy_expense,
		'8': self.PlayerCountry.environment_expense,
		'9': self.PlayerCountry.family_expense,
		'10': self.PlayerCountry.foreign_affairs_expense,
		'11': self.PlayerCountry.health_expense,
		'12': self.PlayerCountry.homeland_security_expense,
		'13': self.PlayerCountry.housing_expense,
		'14': self.PlayerCountry.industry_expense,
		'15': self.PlayerCountry.information_expense,
		'16': self.PlayerCountry.justice_expense,
		'17': self.PlayerCountry.miscellaneous_expense,
		'18': self.PlayerCountry.religion_expense,
		'19': self.PlayerCountry.research_expense,
		'20': self.PlayerCountry.secret_services_expense,
		'21': self.PlayerCountry.social_security_expense,
		'22': self.PlayerCountry.sport_expense,
		'23': self.PlayerCountry.tourism_expense,
		'24': self.PlayerCountry.transport_expense,
		'25': self.PlayerCountry.treasury_expense,
		'26': self.PlayerCountry.unemployment_insurance_expense			
		}

		self.PlayerCountry_expenses_name_dict = {
		0: 'Agriculture Expense',
		1: 'Culture Expense',
		2: 'Debt Interest Expense',
		3: 'Defense Expense',
		4: 'Economy Expense',
		5: 'Education Expense',
		6: 'Employment Social Expense',
		7: 'Energy Expense',
		8: 'Environment Expense',
		9: 'Family Expense',
		10: 'Foreign Affairs Expense',
		11: 'Health Expense',
		12: 'Homeland Security Expense',
		13: 'Housing Expense',
		14: 'Industry Expense',
		15: 'Information Expense',
		16: 'Justice Expense',
		17: 'Miscellaneous Expense',
		18: 'Religion Expense',
		19: 'Research Expense',
		20: 'Secret Services Expense',
		21: 'Social Security Expense',
		22: 'Sport Expense',
		23: 'Tourism Expense',
		24: 'Transport Expense',
		25: 'Treasury Expense',
		26: 'Unemployment Insurance Expense'			
		}		

		self.expenses_cicle_rects = []
		self.hitted_rect = None

		self.mouse_rect = (0,0,0,0)

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))

	def get_button_by_interaction(self, mouse_rect):
		self.mouse_rect = mouse_rect
		try:
			for index, rect in enumerate(self.expenses_cicle_rects):
				if GenericUtilitys.polygon_intersects_rectangle(rect, mouse_rect):
					self.hitted_rect = [index, rect]
					return rect	
		except:
			pass
		
		self.hitted_rect = None
		return None

	def draw(self, screen):
		
		# CHART
		chart_position = (450 * self.factor_x, 529 * self.factor_y) 
		chart_radius = 360 * self.factor_y

		expenses_porcentages = []
		for expense in self.PlayerCountry_expenses_dict.values():
			expenses_porcentages.append((expense / self.PlayerCountry.expenses) * 100)

		self.expenses_cicle_rects = GenericUtilitys.draw_pie_chart(screen, chart_position, chart_radius, expenses_porcentages, [
		(0, 0, 0),
		(255, 255, 255),
		(255, 0, 0),
		(0, 255, 0),
		(0, 0, 255),
		(255, 255, 0),
		(0, 255, 255),
		(255, 0, 255),
		(128, 128, 128),
		(128, 0, 0),
		(128, 128, 0),
		(0, 128, 0),
		(0, 0, 128),
		(128, 0, 128),
		(0, 128, 128),
		(192, 192, 192),
		(169, 169, 169),
		(139, 0, 0),
		(165, 42, 42),
		(0, 0, 139),
		(255, 165, 0),
		(255, 192, 203),
		(255, 215, 0),
		(230, 230, 250),
		(107, 142, 35),
		(135, 206, 235),
		(112, 128, 144)
		])		

		screen.blit(self.budget_menu, (0, 158 * self.factor_y))

		# EXPENDITURES
		pygame.draw.line(screen, (0,0,0), (1248 * self.factor_x, 300 * self.factor_y), (1248 * self.factor_x, 321 * self.factor_y), 5)
		pygame.draw.line(screen, (255,255,255), (1248 * self.factor_x, 301 * self.factor_y), (1248 * self.factor_x, 320 * self.factor_y), 3)
		
		expenses = self.PlayerCountry.expenses
		if abs(expenses) < 1e6:
			formatted_expenses = f"${expenses:,.2f}"
		elif abs(expenses) < 1e9:
			formatted_expenses = f"${expenses / 1e6:.3f} M"
		elif abs(expenses) < 1e12:
			formatted_expenses = f"${expenses / 1e9:.3f} B"
		elif abs(expenses) < 1e15:
			formatted_expenses = f"${expenses / 1e12:.3f} T"
		else:
			formatted_expenses = f"${expenses:.2f}"			
		expense_text = self.small_scalable_font.render(formatted_expenses, True, (255,255,255))
		screen.blit(expense_text, (1248 * self.factor_x - expense_text.get_width()/2, 327 * self.factor_y))		

		# REVENUES
		pygame.draw.line(screen, (0,0,0), (1687 * self.factor_x, 300 * self.factor_y), (1687 * self.factor_x, 321 * self.factor_y), 5)
		pygame.draw.line(screen, (255,255,255), (1687 * self.factor_x, 301 * self.factor_y), (1687 * self.factor_x, 320 * self.factor_y), 3)
		
		income = self.PlayerCountry.income
		if abs(income) < 1e6:
			formatted_income = f"${income:,.2f}"
		elif abs(income) < 1e9:
			formatted_income = f"${income / 1e6:.3f} M"
		elif abs(income) < 1e12:
			formatted_income = f"${income / 1e9:.3f} B"
		elif abs(income) < 1e15:
			formatted_income = f"${income / 1e12:.3f} T"
		else:
			formatted_income = f"${income:.2f}"			
		expense_text = self.small_scalable_font.render(formatted_income, True, (255,255,255))
		screen.blit(expense_text, (1687 * self.factor_x - expense_text.get_width()/2, 327 * self.factor_y))				


		x_expense_index = 0
		y_expense_index = 0
		for expense_index in range(24):
			pygame.draw.line(screen, (0,0,0), ((1176 + (x_expense_index*195)) * self.factor_x, (397 + (y_expense_index*69)) * self.factor_y), ((1176 + (x_expense_index*195)) * self.factor_x, (420 + (y_expense_index*69)) * self.factor_y), 5)
			pygame.draw.line(screen, (255,255,255), ((1176 + (x_expense_index*195)) * self.factor_x, (398 + (y_expense_index*69)) * self.factor_y), ((1176 + (x_expense_index*195)) * self.factor_x, (419 + (y_expense_index*69)) * self.factor_y), 3)
			
			expense = self.PlayerCountry_expenses_dict[str(expense_index)]
			if abs(expense) < 1e6:
				formatted_expense = f"${expense:,.2f}"
			elif abs(expense) < 1e9:
				formatted_expense = f"${expense / 1e6:.3f} M"
			elif abs(expense) < 1e12:
				formatted_expense = f"${expense / 1e9:.3f} B"
			elif abs(expense) < 1e15:
				formatted_expense = f"${expense / 1e12:.3f} T"
			else:
				formatted_expense = f"${expense:.2f}"			
			expense_text = self.small_scalable_font.render(formatted_expense, True, (255,255,255))
			screen.blit(expense_text, ((1176 + (x_expense_index*195)) * self.factor_x - expense_text.get_width()/2, (425 + (y_expense_index*69)) * self.factor_y))

			x_expense_index += 1
			if x_expense_index > 3:
				x_expense_index = 0
				y_expense_index += 1			

		x_expense_index = 0
		for expense_index in range(3):
			pygame.draw.line(screen, (0,0,0), ((1273 + (x_expense_index*195)) * self.factor_x, 812 * self.factor_y), ((1273 + (x_expense_index*195)) * self.factor_x, 833 * self.factor_y), 5)
			pygame.draw.line(screen, (255,255,255), ((1273 + (x_expense_index*195)) * self.factor_x, 813 * self.factor_y), ((1273 + (x_expense_index*195)) * self.factor_x, 832 * self.factor_y), 3)
			
			expense = self.PlayerCountry_expenses_dict[str(expense_index + 24)]
			if abs(expense) < 1e6:
				formatted_expense = f"${expense:,.2f}"
			elif abs(expense) < 1e9:
				formatted_expense = f"${expense / 1e6:.3f} M"
			elif abs(expense) < 1e12:
				formatted_expense = f"${expense / 1e9:.3f} B"
			elif abs(expense) < 1e15:
				formatted_expense = f"${expense / 1e12:.3f} T"
			else:
				formatted_expense = f"${expense:.2f}"			
			expense_text = self.small_scalable_font.render(formatted_expense, True, (255,255,255))
			screen.blit(expense_text, ((1273 + (x_expense_index*195)) * self.factor_x - expense_text.get_width()/2, 838 * self.factor_y))			

			x_expense_index += 1		

		if self.hitted_rect:
			pygame.draw.polygon(screen, (0,0,0), self.hitted_rect[1], 14)
			pygame.draw.polygon(screen, (255,255,255), self.hitted_rect[1], 5)

			expense_description_text = self.huge_scalable_font.render(self.PlayerCountry_expenses_name_dict[self.hitted_rect[0]] + ': ' + str((self.PlayerCountry_expenses_dict[str(self.hitted_rect[0])]/ self.PlayerCountry.expenses )*100) + '%', True, (255,255,255))
			pygame.draw.rect(screen, (6,17,21), (self.mouse_rect[0], self.mouse_rect[1], expense_description_text.get_width() * 1.5, expense_description_text.get_height() * 1.5))
			pygame.draw.rect(screen, (23,255,255), (self.mouse_rect[0], self.mouse_rect[1], expense_description_text.get_width() * 1.5, expense_description_text.get_height() * 1.5), 2)
			
			screen.blit(expense_description_text, (self.mouse_rect[0] + expense_description_text.get_width() * 0.25, self.mouse_rect[1] +  expense_description_text.get_height() * 0.25))			
class Legislative_Finances_Debt_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, debt_menu):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = PlayerCountry

		self.debt_menu = pygame.transform.smoothscale_by(debt_menu, (self.factor_x, self.factor_y))

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

	def draw(self, screen):		
		screen.blit(self.debt_menu, (0, 158 * self.factor_y))

		#	DEBT-TO-GDP
		graph_pos_x = 1029
		graph_pos_y = 155

		country_debt_to_gdp_text_render = self.medium_scalable_font.render(str(round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2))+' %', False, (255,255,255))	
		screen.blit(country_debt_to_gdp_text_render, (1216 * self.factor_x, 81 * self.factor_y + 158 * self.factor_y))

		debt_to_gdp = round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2)

		debt_to_gdp_high_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp + debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(debt_to_gdp_high_end_text_render, ((graph_pos_x - 39) * self.factor_x - debt_to_gdp_high_end_text_render.get_width(), (graph_pos_y - 50) * self.factor_y + 158 * self.factor_y - debt_to_gdp_high_end_text_render.get_height()/2))
		
		debt_to_gdp_low_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp - debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(debt_to_gdp_low_end_text_render, ((graph_pos_x - 39) * self.factor_x - debt_to_gdp_low_end_text_render.get_width(), (graph_pos_y + 50) * self.factor_y + 158 * self.factor_y - debt_to_gdp_low_end_text_render.get_height()/2))

		graph_dots = []
		for index, weekly_data in enumerate(self.PlayerCountry.weekly_debt_to_gdp_data):
			if weekly_data > debt_to_gdp:
				height = graph_pos_y - (50 * (min(1, (weekly_data/(debt_to_gdp + 0.01)) - 1)))
			else:
				height = graph_pos_y + (50 * (min(1, (debt_to_gdp/(weekly_data + 0.01)) - 1)))
			
			graph_dots.append(((3.855 * index + graph_pos_x) * self.factor_x, (height + 158) * self.factor_y))

		if len(graph_dots) > 1:
			self.pygame.draw.lines(screen, (255,0,0), False, graph_dots, 3)
		else:
			self.pygame.draw.line(screen, (255,0,0), graph_dots[0], (graph_dots[0][0], (graph_pos_y + 158) * self.factor_y), 3)	


		#	BUDGET DEFICIT
		graph_pos_x = 1534
		graph_pos_y = 155

		budget_deficit = round(self.PlayerCountry.debt - self.PlayerCountry.income, 2)

		if abs(budget_deficit) < 1e6:
			budget_deficit_formatted = f"${budget_deficit:,.2f}"
		elif abs(budget_deficit) < 1e9:
			budget_deficit_formatted = f"${budget_deficit / 1e6:.3f} M"
		elif abs(budget_deficit) < 1e12:
			budget_deficit_formatted = f"${budget_deficit / 1e9:.3f} B"
		elif abs(budget_deficit) < 1e15:
			budget_deficit_formatted = f"${budget_deficit / 1e12:.3f} T"
		else:
			budget_deficit_formatted = f"${budget_deficit:.2f}"		

		if budget_deficit <= 0:
			color = (165,255,127)
		else:
			color = (255,127,127)
		
		country_budget_deficit_text_render = self.medium_scalable_font.render(budget_deficit_formatted, False, color)	
		screen.blit(country_budget_deficit_text_render, (1724 * self.factor_x, 81 * self.factor_y + 158 * self.factor_y))


		high_end_budget_deficit = budget_deficit * 1.15

		if abs(high_end_budget_deficit) < 1e6:
			high_end_formatted_budget_deficit = f"${high_end_budget_deficit:,.2f}"
		elif abs(high_end_budget_deficit) < 1e9:
			high_end_formatted_budget_deficit = f"${high_end_budget_deficit / 1e6:.3f} M"
		elif abs(high_end_budget_deficit) < 1e12:
			high_end_formatted_budget_deficit = f"${high_end_budget_deficit / 1e9:.3f} B"
		elif abs(high_end_budget_deficit) < 1e15:
			high_end_formatted_budget_deficit = f"${high_end_budget_deficit / 1e12:.3f} T"
		else:
			high_end_formatted_budget_deficit = f"${high_end_budget_deficit:.2f}"

		budget_deficit_high_end_text_render = self.small_scalable_font.render(high_end_formatted_budget_deficit, False, (255,255,255))	
		screen.blit(budget_deficit_high_end_text_render, ((graph_pos_x - 39) * self.factor_x - budget_deficit_high_end_text_render.get_width(), (graph_pos_y - 50) * self.factor_y + 158 * self.factor_y - budget_deficit_high_end_text_render.get_height()/2))
		

		low_end_budget_deficit = budget_deficit * 0.85

		if abs(low_end_budget_deficit) < 1e6:
			low_end_formatted_budget_deficit = f"${low_end_budget_deficit:,.2f}"
		elif abs(low_end_budget_deficit) < 1e9:
			low_end_formatted_budget_deficit = f"${low_end_budget_deficit / 1e6:.3f} M"
		elif abs(low_end_budget_deficit) < 1e12:
			low_end_formatted_budget_deficit = f"${low_end_budget_deficit / 1e9:.3f} B"
		elif abs(low_end_budget_deficit) < 1e15:
			low_end_formatted_budget_deficit = f"${low_end_budget_deficit / 1e12:.3f} T"
		else:
			low_end_formatted_budget_deficit = f"${low_end_budget_deficit:.2f}"

		budget_deficit_low_end_text_render = self.small_scalable_font.render(low_end_formatted_budget_deficit, False, (255,255,255))	
		screen.blit(budget_deficit_low_end_text_render, ((graph_pos_x - 39) * self.factor_x - budget_deficit_low_end_text_render.get_width(), (graph_pos_y + 50) * self.factor_y + 158 * self.factor_y - budget_deficit_low_end_text_render.get_height()/2))

		graph_dots = []
		for index, weekly_data in enumerate(self.PlayerCountry.weekly_debt_to_gdp_data):
			if weekly_data > debt_to_gdp:
				height = graph_pos_y - (50 * (min(1, (weekly_data/(debt_to_gdp + 0.01)) - 1)))
			else:
				height = graph_pos_y + (50 * (min(1, (debt_to_gdp/(weekly_data + 0.01)) - 1)))
			
			graph_dots.append(((3.855 * index + graph_pos_x) * self.factor_x, (height + 158) * self.factor_y))

		if budget_deficit <= 0:
			graph_color = (0,255,0)
		else:
			graph_color = (255,0,0)

		if len(graph_dots) > 1:
			self.pygame.draw.lines(screen, graph_color, False, graph_dots, 3)
		else:
			self.pygame.draw.line(screen, graph_color, graph_dots[0], (graph_dots[0][0], (graph_pos_y + 158) * self.factor_y), 3)	


		#	STRUCTURAL DEFICIT-TO-GDP
		graph_pos_x = 1029
		graph_pos_y = 394

		country_debt_to_gdp_text_render = self.medium_scalable_font.render(str(round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2))+' %', False, (255,255,255))	
		screen.blit(country_debt_to_gdp_text_render, (1216 * self.factor_x, 320 * self.factor_y + 158 * self.factor_y))

		debt_to_gdp = round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2)

		debt_to_gdp_high_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp + debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(debt_to_gdp_high_end_text_render, ((graph_pos_x - 39) * self.factor_x - debt_to_gdp_high_end_text_render.get_width(), (graph_pos_y - 50) * self.factor_y + 158 * self.factor_y - debt_to_gdp_high_end_text_render.get_height()/2))
		
		debt_to_gdp_low_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp - debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(debt_to_gdp_low_end_text_render, ((graph_pos_x - 39) * self.factor_x - debt_to_gdp_low_end_text_render.get_width(), (graph_pos_y + 50) * self.factor_y + 158 * self.factor_y - debt_to_gdp_low_end_text_render.get_height()/2))

		graph_dots = []
		for index, weekly_data in enumerate(self.PlayerCountry.weekly_debt_to_gdp_data):
			if weekly_data > debt_to_gdp:
				height = graph_pos_y - (50 * (min(1, (weekly_data/(debt_to_gdp + 0.01)) - 1)))
			else:
				height = graph_pos_y + (50 * (min(1, (debt_to_gdp/(weekly_data + 0.01)) - 1)))
			
			graph_dots.append(((3.855 * index + graph_pos_x) * self.factor_x, (height + 158) * self.factor_y))

		if len(graph_dots) > 1:
			self.pygame.draw.lines(screen, (255,0,0), False, graph_dots, 3)
		else:
			self.pygame.draw.line(screen, (255,0,0), graph_dots[0], (graph_dots[0][0], (graph_pos_y + 158) * self.factor_y), 3)	


		#	NATIONALIZED SECTOR DEBT
		graph_pos_x = 1534
		graph_pos_y = 394

		country_debt_to_gdp_text_render = self.medium_scalable_font.render(str(round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2))+' %', False, (255,255,255))	
		screen.blit(country_debt_to_gdp_text_render, (1711 * self.factor_x, 320 * self.factor_y + 158 * self.factor_y))

		debt_to_gdp = round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2)

		debt_to_gdp_high_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp + debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(debt_to_gdp_high_end_text_render, ((graph_pos_x - 39) * self.factor_x - debt_to_gdp_high_end_text_render.get_width(), (graph_pos_y - 50) * self.factor_y + 158 * self.factor_y - debt_to_gdp_high_end_text_render.get_height()/2))
		
		debt_to_gdp_low_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp - debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(debt_to_gdp_low_end_text_render, ((graph_pos_x - 39) * self.factor_x - debt_to_gdp_low_end_text_render.get_width(), (graph_pos_y + 50) * self.factor_y + 158 * self.factor_y - debt_to_gdp_low_end_text_render.get_height()/2))

		graph_dots = []
		for index, weekly_data in enumerate(self.PlayerCountry.weekly_debt_to_gdp_data):
			if weekly_data > debt_to_gdp:
				height = graph_pos_y - (50 * (min(1, (weekly_data/(debt_to_gdp + 0.01)) - 1)))
			else:
				height = graph_pos_y + (50 * (min(1, (debt_to_gdp/(weekly_data + 0.01)) - 1)))
			
			graph_dots.append(((3.855 * index + graph_pos_x) * self.factor_x, (height + 158) * self.factor_y))

		if len(graph_dots) > 1:
			self.pygame.draw.lines(screen, (255,0,0), False, graph_dots, 3)
		else:
			self.pygame.draw.line(screen, (255,0,0), graph_dots[0], (graph_dots[0][0], (graph_pos_y + 158) * self.factor_y), 3)		


		#	PUBLIC DEBT-TO-GDP
		graph_pos_x = 1029
		graph_pos_y = 633

		country_debt_to_gdp_text_render = self.medium_scalable_font.render(str(round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2))+' %', False, (255,255,255))	
		screen.blit(country_debt_to_gdp_text_render, (1273 * self.factor_x, 559 * self.factor_y + 158 * self.factor_y))

		debt_to_gdp = round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2)

		debt_to_gdp_high_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp + debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(debt_to_gdp_high_end_text_render, ((graph_pos_x - 39) * self.factor_x - debt_to_gdp_high_end_text_render.get_width(), (graph_pos_y - 50) * self.factor_y + 158 * self.factor_y - debt_to_gdp_high_end_text_render.get_height()/2))
		
		debt_to_gdp_low_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp - debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(debt_to_gdp_low_end_text_render, ((graph_pos_x - 39) * self.factor_x - debt_to_gdp_low_end_text_render.get_width(), (graph_pos_y + 50) * self.factor_y + 158 * self.factor_y - debt_to_gdp_low_end_text_render.get_height()/2))

		graph_dots = []
		for index, weekly_data in enumerate(self.PlayerCountry.weekly_debt_to_gdp_data):
			if weekly_data > debt_to_gdp:
				height = graph_pos_y - (50 * (min(1, (weekly_data/(debt_to_gdp + 0.01)) - 1)))
			else:
				height = graph_pos_y + (50 * (min(1, (debt_to_gdp/(weekly_data + 0.01)) - 1)))
			
			graph_dots.append(((3.855 * index + graph_pos_x) * self.factor_x, (height + 158) * self.factor_y))

		if len(graph_dots) > 1:
			self.pygame.draw.lines(screen, (255,0,0), False, graph_dots, 3)
		else:
			self.pygame.draw.line(screen, (255,0,0), graph_dots[0], (graph_dots[0][0], (graph_pos_y + 158) * self.factor_y), 3)	


		#	PUBLIC DEBT
		graph_pos_x = 1534
		graph_pos_y = 633

		country_debt_to_gdp_text_render = self.medium_scalable_font.render(str(round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2))+' %', False, (255,255,255))	
		screen.blit(country_debt_to_gdp_text_render, (1686 * self.factor_x, 559 * self.factor_y + 158 * self.factor_y))

		debt_to_gdp = round((self.PlayerCountry.debt/self.PlayerCountry.country_GDP)*100, 2)

		debt_to_gdp_high_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp + debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(debt_to_gdp_high_end_text_render, ((graph_pos_x - 39) * self.factor_x - debt_to_gdp_high_end_text_render.get_width(), (graph_pos_y - 50) * self.factor_y + 158 * self.factor_y - debt_to_gdp_high_end_text_render.get_height()/2))
		
		debt_to_gdp_low_end_text_render = self.small_scalable_font.render(str(round(debt_to_gdp - debt_to_gdp*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(debt_to_gdp_low_end_text_render, ((graph_pos_x - 39) * self.factor_x - debt_to_gdp_low_end_text_render.get_width(), (graph_pos_y + 50) * self.factor_y + 158 * self.factor_y - debt_to_gdp_low_end_text_render.get_height()/2))

		graph_dots = []
		for index, weekly_data in enumerate(self.PlayerCountry.weekly_debt_to_gdp_data):
			if weekly_data > debt_to_gdp:
				height = graph_pos_y - (50 * (min(1, (weekly_data/(debt_to_gdp + 0.01)) - 1)))
			else:
				height = graph_pos_y + (50 * (min(1, (debt_to_gdp/(weekly_data + 0.01)) - 1)))
			
			graph_dots.append(((3.855 * index + graph_pos_x) * self.factor_x, (height + 158) * self.factor_y))

		if len(graph_dots) > 1:
			self.pygame.draw.lines(screen, (255,0,0), False, graph_dots, 3)
		else:
			self.pygame.draw.line(screen, (255,0,0), graph_dots[0], (graph_dots[0][0], (graph_pos_y + 158) * self.factor_y), 3)										
class Legislative_Finances_Taxation_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, taxation_menu):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = PlayerCountry

		self.taxation_menu = pygame.transform.smoothscale_by(taxation_menu, (self.factor_x, self.factor_y))

		self.tax_creation_surface = pygame.Surface((616 * self.factor_x, 2000 * self.factor_y), pygame.SRCALPHA)
		self.active_tax_surface = pygame.Surface((616 * self.factor_x, 2000 * self.factor_y), pygame.SRCALPHA)

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))	

	def draw(self, screen):
		screen.blit(self.taxation_menu, (0, 158 * self.factor_y))

		self.tax_creation_surface.fill((0, 0, 0, 0))
		self.active_tax_surface.fill((0, 0, 0, 0))

		total_revenue = 0

		active_index = 0
		creation_index = 0
		for tax_name, info in self.PlayerCountry.country_taxation_laws_values.items():
			is_law_active = False
			for value in info['value']:
				if value == 0:
					is_law_active = False
				else:
					is_law_active = True

			if is_law_active == False: 	# LAWS TO CREATE
				self.pygame.draw.rect(self.tax_creation_surface, (255,255,255), (3 * self.factor_x, (creation_index * 35) * self.factor_y, 580 * self.factor_x, 30 * self.factor_y), 1)

				law_name_text = self.medium_scalable_font.render(tax_name, True, (255,255,255))
				self.tax_creation_surface.blit(law_name_text, (13 * self.factor_x, ((creation_index * 35) + 16) * self.factor_y - law_name_text.get_height()/2))

				creation_index += 1
			else:						# ACTIVE LAWS
				self.pygame.draw.rect(self.active_tax_surface, (255,255,255), (7 * self.factor_x, (active_index * 35) * self.factor_y, 576 * self.factor_x, 30 * self.factor_y), 1)
				
				law_name_text = self.small_scalable_font.render(tax_name, True, (255,255,255))
				self.active_tax_surface.blit(law_name_text, (17 * self.factor_x, ((active_index * 35) + 16)  * self.factor_y - law_name_text.get_height()/2))		

				if len(info['value']) == 1:
					if info['value_type'] == 'porcentage':
						law_value_text = self.small_scalable_font.render(str(info['value'][0]) + '%', True, (255,127,127))
						self.active_tax_surface.blit(law_value_text, (305 * self.factor_x, ((active_index * 35) + 16) * self.factor_y - law_value_text.get_height()/2))

				tax_revenue = info['monthly_revenue']
				total_revenue += tax_revenue

				if abs(tax_revenue) < 1e6:
					formatted_tax_revenue = f"REVENUE:  ${tax_revenue:,.2f}"
				elif abs(tax_revenue) < 1e9:
					formatted_tax_revenue = f"REVENUE:  ${tax_revenue / 1e6:.3f} M"
				elif abs(tax_revenue) < 1e12:
					formatted_tax_revenue = f"REVENUE:  ${tax_revenue / 1e9:.3f} B"
				elif abs(tax_revenue) < 1e15:
					formatted_tax_revenue = f"REVENUE:  ${tax_revenue / 1e12:.3f} T"
				else:
					formatted_tax_revenue = f"REVENUE:  ${tax_revenue:.2f}"	

				law_revenue_text = self.small_scalable_font.render(formatted_tax_revenue, True, (165,255,127))
				self.active_tax_surface.blit(law_revenue_text, (400 * self.factor_x, ((active_index * 35) + 16) * self.factor_y - law_value_text.get_height()/2))							

				active_index += 1

		screen.blit(self.tax_creation_surface.subsurface(0, 0, 616 * self.factor_x, 670 * self.factor_y), (652 * self.factor_x, 218 * self.factor_y))
		screen.blit(self.active_tax_surface.subsurface(0, 0, 616 * self.factor_x, 622 * self.factor_y), (21 * self.factor_x, 221 * self.factor_y))


		if abs(total_revenue) < 1e6:
			formatted_total_revenue = f"${total_revenue:,.2f}"
		elif abs(total_revenue) < 1e9:
			formatted_total_revenue = f"${total_revenue / 1e6:.3f} M"
		elif abs(total_revenue) < 1e12:
			formatted_total_revenue = f"${total_revenue / 1e9:.3f} B"
		elif abs(total_revenue) < 1e15:
			formatted_total_revenue = f"${total_revenue / 1e12:.3f} T"
		else:
			formatted_total_revenue = f"${total_revenue:.2f}"			

		total_revenue_text = self.big_scalable_font.render(formatted_total_revenue, True, (165,255,127))
		screen.blit(total_revenue_text, (450 * self.factor_x, 870 * self.factor_y - total_revenue_text.get_height()/2))			
class Legislative_Finances_Currency_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, currency_menu):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = PlayerCountry

		self.currency_menu = pygame.transform.smoothscale_by(currency_menu, (self.factor_x, self.factor_y))

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))			

	def draw(self, screen):
		screen.blit(self.currency_menu, (0, 158 * self.factor_y))	

		#	INFLATION
		graph_pos_x = 302
		graph_pos_y = 188

		inflation_text_render = self.small_scalable_font.render(str(round(self.PlayerCountry.inflation, 2))+' %', False, (255,255,255))	
		screen.blit(inflation_text_render, (1818 * self.factor_x, 55 * self.factor_y + 158 * self.factor_y))


		inflation = round(self.PlayerCountry.inflation, 3)


		inflation_15_high_end_text_render = self.small_scalable_font.render(str(round(inflation + inflation*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(inflation_15_high_end_text_render, ((graph_pos_x - 45) * self.factor_x - inflation_15_high_end_text_render.get_width(), (graph_pos_y - 158) * self.factor_y + 158 * self.factor_y - inflation_15_high_end_text_render.get_height()/2))
		
		inflation_1125_high_end_text_render = self.small_scalable_font.render(str(round(inflation + inflation*0.1125, 2))+' %', False, (255,255,255))	
		screen.blit(inflation_1125_high_end_text_render, ((graph_pos_x - 45) * self.factor_x - inflation_1125_high_end_text_render.get_width(), (graph_pos_y - 113) * self.factor_y + 158 * self.factor_y - inflation_1125_high_end_text_render.get_height()/2))	

		inflation_75_high_end_text_render = self.small_scalable_font.render(str(round(inflation + inflation*0.075, 2))+' %', False, (255,255,255))	
		screen.blit(inflation_75_high_end_text_render, ((graph_pos_x - 45) * self.factor_x - inflation_75_high_end_text_render.get_width(), (graph_pos_y - 68) * self.factor_y + 158 * self.factor_y - inflation_75_high_end_text_render.get_height()/2))

		inflation_375_high_end_text_render = self.small_scalable_font.render(str(round(inflation + inflation*0.0375, 2))+' %', False, (255,255,255))	
		screen.blit(inflation_375_high_end_text_render, ((graph_pos_x - 45) * self.factor_x - inflation_375_high_end_text_render.get_width(), (graph_pos_y - 23) * self.factor_y + 158 * self.factor_y - inflation_375_high_end_text_render.get_height()/2))	


		inflation_15_low_end_text_render = self.small_scalable_font.render(str(round(inflation - inflation*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(inflation_15_low_end_text_render, ((graph_pos_x - 45) * self.factor_x - inflation_15_low_end_text_render.get_width(), (graph_pos_y + 158) * self.factor_y + 158 * self.factor_y - inflation_15_low_end_text_render.get_height()/2))
		
		inflation_1125_low_end_text_render = self.small_scalable_font.render(str(round(inflation - inflation*0.1125, 2))+' %', False, (255,255,255))	
		screen.blit(inflation_1125_low_end_text_render, ((graph_pos_x - 45) * self.factor_x - inflation_1125_low_end_text_render.get_width(), (graph_pos_y + 113) * self.factor_y + 158 * self.factor_y - inflation_1125_low_end_text_render.get_height()/2))	

		inflation_75_low_end_text_render = self.small_scalable_font.render(str(round(inflation - inflation*0.075, 2))+' %', False, (255,255,255))	
		screen.blit(inflation_75_low_end_text_render, ((graph_pos_x - 45) * self.factor_x - inflation_75_low_end_text_render.get_width(), (graph_pos_y + 68) * self.factor_y + 158 * self.factor_y - inflation_75_low_end_text_render.get_height()/2))

		inflation_375_low_end_text_render = self.small_scalable_font.render(str(round(inflation - inflation*0.0375, 2))+' %', False, (255,255,255))	
		screen.blit(inflation_375_low_end_text_render, ((graph_pos_x - 45) * self.factor_x - inflation_375_low_end_text_render.get_width(), (graph_pos_y + 23) * self.factor_y + 158 * self.factor_y - inflation_375_low_end_text_render.get_height()/2))			


		graph_dots = []
		for index, weekly_data in enumerate(self.PlayerCountry.weekly_inflation_data):
			if weekly_data > inflation:
				height = graph_pos_y - (158 * (min(1, (weekly_data/(inflation + 0.01)) - 1)))
			else:
				height = graph_pos_y + (158 * (min(1, (inflation/(weekly_data + 0.01)) - 1)))
			
			graph_dots.append(((26.557 * index + graph_pos_x) * self.factor_x, (height + 158) * self.factor_y))

		if len(graph_dots) > 1:
			self.pygame.draw.lines(screen, (255,0,0), False, graph_dots, 3)
		else:
			self.pygame.draw.line(screen, (255,0,0), graph_dots[0], (graph_dots[0][0], (graph_pos_y + 158) * self.factor_y), 3)	

		#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#	
		#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#	

		#	INTEREST RATE
		graph_pos_x = 302
		graph_pos_y = 540

		interest_rate_text_render = self.small_scalable_font.render(str(round(self.PlayerCountry.currency_interest_rate, 2))+' %', False, (255,255,255))	
		screen.blit(interest_rate_text_render, (1818 * self.factor_x, 408 * self.factor_y + 158 * self.factor_y))


		interest_rate = round(self.PlayerCountry.currency_interest_rate, 3)
		if interest_rate == 0:
			interest_rate = 0.01


		interest_rate_15_high_end_text_render = self.small_scalable_font.render(str(round(interest_rate + interest_rate*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(interest_rate_15_high_end_text_render, ((graph_pos_x - 45) * self.factor_x - interest_rate_15_high_end_text_render.get_width(), (graph_pos_y - 158) * self.factor_y + 158 * self.factor_y - interest_rate_15_high_end_text_render.get_height()/2))
		
		interest_rate_1125_high_end_text_render = self.small_scalable_font.render(str(round(interest_rate + interest_rate*0.1125, 2))+' %', False, (255,255,255))	
		screen.blit(interest_rate_1125_high_end_text_render, ((graph_pos_x - 45) * self.factor_x - interest_rate_1125_high_end_text_render.get_width(), (graph_pos_y - 113) * self.factor_y + 158 * self.factor_y - interest_rate_1125_high_end_text_render.get_height()/2))	

		interest_rate_75_high_end_text_render = self.small_scalable_font.render(str(round(interest_rate + interest_rate*0.075, 2))+' %', False, (255,255,255))	
		screen.blit(interest_rate_75_high_end_text_render, ((graph_pos_x - 45) * self.factor_x - interest_rate_75_high_end_text_render.get_width(), (graph_pos_y - 68) * self.factor_y + 158 * self.factor_y - interest_rate_75_high_end_text_render.get_height()/2))

		interest_rate_375_high_end_text_render = self.small_scalable_font.render(str(round(interest_rate + interest_rate*0.0375, 2))+' %', False, (255,255,255))	
		screen.blit(interest_rate_375_high_end_text_render, ((graph_pos_x - 45) * self.factor_x - interest_rate_375_high_end_text_render.get_width(), (graph_pos_y - 23) * self.factor_y + 158 * self.factor_y - interest_rate_375_high_end_text_render.get_height()/2))	


		interest_rate_15_low_end_text_render = self.small_scalable_font.render(str(round(interest_rate - interest_rate*0.15, 2))+' %', False, (255,255,255))	
		screen.blit(interest_rate_15_low_end_text_render, ((graph_pos_x - 45) * self.factor_x - interest_rate_15_low_end_text_render.get_width(), (graph_pos_y + 158) * self.factor_y + 158 * self.factor_y - interest_rate_15_low_end_text_render.get_height()/2))
		
		interest_rate_1125_low_end_text_render = self.small_scalable_font.render(str(round(interest_rate - interest_rate*0.1125, 2))+' %', False, (255,255,255))	
		screen.blit(interest_rate_1125_low_end_text_render, ((graph_pos_x - 45) * self.factor_x - interest_rate_1125_low_end_text_render.get_width(), (graph_pos_y + 113) * self.factor_y + 158 * self.factor_y - interest_rate_1125_low_end_text_render.get_height()/2))	

		interest_rate_75_low_end_text_render = self.small_scalable_font.render(str(round(interest_rate - interest_rate*0.075, 2))+' %', False, (255,255,255))	
		screen.blit(interest_rate_75_low_end_text_render, ((graph_pos_x - 45) * self.factor_x - interest_rate_75_low_end_text_render.get_width(), (graph_pos_y + 68) * self.factor_y + 158 * self.factor_y - interest_rate_75_low_end_text_render.get_height()/2))

		interest_rate_375_low_end_text_render = self.small_scalable_font.render(str(round(interest_rate - interest_rate*0.0375, 2))+' %', False, (255,255,255))	
		screen.blit(interest_rate_375_low_end_text_render, ((graph_pos_x - 45) * self.factor_x - interest_rate_375_low_end_text_render.get_width(), (graph_pos_y + 23) * self.factor_y + 158 * self.factor_y - interest_rate_375_low_end_text_render.get_height()/2))			


		graph_dots = []
		for index, weekly_data in enumerate(self.PlayerCountry.weekly_currency_interest_rate_data):
			if weekly_data > interest_rate:
				height = graph_pos_y - (158 * (min(1, (weekly_data/(interest_rate + 0.01)) - 1)))
			else:
				height = graph_pos_y + (158 * (min(1, (interest_rate/(weekly_data + 0.01)) - 1)))
			
			graph_dots.append(((26.557 * index + graph_pos_x) * self.factor_x, (height + 158) * self.factor_y))

		if len(graph_dots) > 1:
			self.pygame.draw.lines(screen, (255,0,0), False, graph_dots, 3)
		else:
			self.pygame.draw.line(screen, (255,0,0), graph_dots[0], (graph_dots[0][0], (graph_pos_y + 158) * self.factor_y), 3)	

		#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#	
		#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#					
class Legislative_Finances_Finance_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, finance_menu):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = PlayerCountry

		self.finance_menu = pygame.transform.smoothscale_by(finance_menu, (self.factor_x, self.factor_y))

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))			

	def draw(self, screen):
		screen.blit(self.finance_menu, (0, 158 * self.factor_y))	

class Legislative_Government_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, law_opinion_survey_icon, government_menu_background, head_of_state_menu, cabinet_menu, parliament_menu, elections_menu, political_parties_menu, Law_Opinion_survey_Menu):

		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame	

		self.Law_Opinion_survey_Menu = Law_Opinion_survey_Menu
		
		self.government_menu_background 			= pygame.transform.smoothscale_by(government_menu_background, (self.factor_x, self.factor_y))	

		self.is_law_opinion_survey_menu_open = False

		self.Legislative_Government_Head_Of_State_Menu = Legislative_Government_Head_Of_State_Menu(factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, law_opinion_survey_icon, head_of_state_menu)
		self.head_of_state_menu_button = GenericUtilitys.Button(5 * self.factor_x, 741 * self.factor_y + 158 * self.factor_y, 380 * self.factor_x, 64 * self.factor_y)

		self.Legislative_Government_Cabinet_Menu = Legislative_Government_Cabinet_Menu(factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, cabinet_menu)
		self.cabinet_menu_button = GenericUtilitys.Button(387 * self.factor_x, 741 * self.factor_y + 158 * self.factor_y, 380 * self.factor_x, 64 * self.factor_y)

		self.Legislative_Government_Parliament_Menu = Legislative_Government_Parliament_Menu(factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, law_opinion_survey_icon, parliament_menu)
		self.parliament_menu_button = GenericUtilitys.Button(769 * self.factor_x, 741 * self.factor_y + 158 * self.factor_y, 380 * self.factor_x, 64 * self.factor_y)

		self.Legislative_Government_Elections_Menu = Legislative_Government_Elections_Menu(factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, elections_menu)
		self.elections_menu_button = GenericUtilitys.Button(1151 * self.factor_x, 741 * self.factor_y + 158 * self.factor_y, 380 * self.factor_x, 64 * self.factor_y)	

		self.Legislative_Government_Political_Parties_Menu = Legislative_Government_Political_Parties_Menu(factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, political_parties_menu)
		self.political_parties_menu_button = GenericUtilitys.Button(1533 * self.factor_x, 741 * self.factor_y + 158 * self.factor_y, 380 * self.factor_x, 64 * self.factor_y)				

		self.hovered_button = None

		self.open_menu = None

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(13 * self.factor_y))			

	def get_button_by_interaction(self, mouse_rect):
		if self.is_law_opinion_survey_menu_open == False:
			if self.head_of_state_menu_button.rect.colliderect(mouse_rect):
				self.hovered_button = 'head_of_state_menu_button'
				return 'head_of_state_menu_button'
			elif self.cabinet_menu_button.rect.colliderect(mouse_rect):
				self.hovered_button = 'cabinet_menu_button'
				return 'cabinet_menu_button'
			elif self.parliament_menu_button.rect.colliderect(mouse_rect):
				self.hovered_button = 'parliament_menu_button'
				return 'parliament_menu_button'	
			elif self.elections_menu_button.rect.colliderect(mouse_rect):
				self.hovered_button = 'elections_menu_button'
				return 'elections_menu_button'			
			elif self.political_parties_menu_button.rect.colliderect(mouse_rect):
				self.hovered_button = 'political_parties_menu_button'
				return 'political_parties_menu_button'			
			else:
				if self.open_menu == 'head_of_state_menu_button':
					Legislative_Government_Head_Of_State_Menu = self.Legislative_Government_Head_Of_State_Menu.get_button_by_interaction(mouse_rect)
					if Legislative_Government_Head_Of_State_Menu:
						return Legislative_Government_Head_Of_State_Menu
				elif self.open_menu == 'parliament_menu_button':
					Legislative_Government_Parliament_Menu = self.Legislative_Government_Parliament_Menu.get_button_by_interaction(mouse_rect)
					if Legislative_Government_Parliament_Menu:
						return Legislative_Government_Parliament_Menu
		else:
			return self.Law_Opinion_survey_Menu.get_button_by_interaction(mouse_rect)

		self.hovered_button = None
		return None		

	def draw(self, screen):
		screen.blit(self.government_menu_background, (0, 158 * self.factor_y))

		if self.hovered_button == 'head_of_state_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.head_of_state_menu_button.rect, 2)
		elif self.hovered_button == 'cabinet_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.cabinet_menu_button.rect, 2)
		elif self.hovered_button == 'parliament_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.parliament_menu_button.rect, 2)	
		elif self.hovered_button == 'elections_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.elections_menu_button.rect, 2)		
		elif self.hovered_button == 'political_parties_menu_button':
			self.pygame.draw.rect(screen, (255,255,255), self.political_parties_menu_button.rect, 2)								

		if self.is_law_opinion_survey_menu_open == False:
			if self.open_menu == 'head_of_state_menu_button':
				self.pygame.draw.rect(screen, (255,255,255), self.head_of_state_menu_button.rect, 3)
				self.Legislative_Government_Head_Of_State_Menu.draw(screen)
			elif self.open_menu == 'cabinet_menu_button':
				self.pygame.draw.rect(screen, (255,255,255), self.cabinet_menu_button.rect, 3)
				self.Legislative_Government_Cabinet_Menu.draw(screen)
			elif self.open_menu == 'parliament_menu_button':
				self.pygame.draw.rect(screen, (255,255,255), self.parliament_menu_button.rect, 3)
				self.Legislative_Government_Parliament_Menu.draw(screen)		
			elif self.open_menu == 'elections_menu_button':
				self.pygame.draw.rect(screen, (255,255,255), self.elections_menu_button.rect, 3)
				self.Legislative_Government_Elections_Menu.draw(screen)		
			elif self.open_menu == 'political_parties_menu_button':
				self.pygame.draw.rect(screen, (255,255,255), self.political_parties_menu_button.rect, 3)
				self.Legislative_Government_Political_Parties_Menu.draw(screen)

		if self.open_menu != None and self.is_law_opinion_survey_menu_open == True:
			self.Law_Opinion_survey_Menu.draw(screen)

class Legislative_Government_Head_Of_State_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, law_opinion_survey_icon, head_of_state_menu):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = PlayerCountry

		self.law_opinion_survey_icon = law_opinion_survey_icon

		self.head_of_state_menu = pygame.transform.smoothscale_by(head_of_state_menu, (self.factor_x, self.factor_y))


		self.law_open = None
		self.law_open_menu_rect = (655 * self.factor_x, 478 * self.factor_y, 610 * self.factor_x, 409 * self.factor_y)

		self.law_change_menu_open = None
		self.law_change_close_button = GenericUtilitys.Button(680 * self.factor_x, 827 * self.factor_y, 250 * self.factor_x, 50 * self.factor_y)
		self.law_change_accept_button = GenericUtilitys.Button(990 * self.factor_x, 827 * self.factor_y, 250 * self.factor_x, 50 * self.factor_y)
		self.law_change_survey_button = GenericUtilitys.Button(1176 * self.factor_x, 713 * self.factor_y, 64 * self.factor_x, 64 * self.factor_y)		

		self.hovered_button = None



		self.law_change_nomination_of_head_of_state_button = GenericUtilitys.Button(655 * self.factor_x, 218 * self.factor_y, 610 * self.factor_x, 50 * self.factor_y)
		self.law_change_nomination_of_head_of_state_by_election_button = GenericUtilitys.Button(835 * self.factor_x, 763 * self.factor_y, 250 * self.factor_x, 50 * self.factor_y)
		self.law_change_nomination_of_head_of_state_dictator_button = GenericUtilitys.Button(835 * self.factor_x, 823 * self.factor_y, 250 * self.factor_x, 50 * self.factor_y)

		self.law_change_election_of_head_of_state_button = GenericUtilitys.Button(655 * self.factor_x, 270 * self.factor_y, 610 * self.factor_x, 50 * self.factor_y)
		self.law_change_election_of_head_of_state_1_button = GenericUtilitys.Button(835 * self.factor_x, 763 * self.factor_y, 250 * self.factor_x, 50 * self.factor_y)
		self.law_change_election_of_head_of_state_2_button = GenericUtilitys.Button(835 * self.factor_x, 823 * self.factor_y, 250 * self.factor_x, 50 * self.factor_y)

		self.law_change_mandates_limit_of_head_of_state_button = GenericUtilitys.Button(655 * self.factor_x, 322 * self.factor_y, 610 * self.factor_x, 50 * self.factor_y)

		self.law_change_lenght_of_head_of_state_rule_button = GenericUtilitys.Button(655 * self.factor_x, 270 * self.factor_y, 610 * self.factor_x, 50 * self.factor_y)

		self.law_change_salary_of_head_of_state_button = GenericUtilitys.Button(655 * self.factor_x, 270 * self.factor_y, 610 * self.factor_x, 50 * self.factor_y)


		self.law_being_voted_description_surface = pygame.Surface((496 * self.factor_x, 850 * self.factor_y), pygame.SRCALPHA)
		self.text_scroll_bar = GenericUtilitys.Scroll_Bar(660 * self.factor_x, 481 * self.factor_x, 403 * self.factor_y, 850 * self.factor_y - 336 * self.factor_y, (255,255,255), (255,0,0), 10 * self.factor_x)				

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))			

	def get_button_by_interaction(self, mouse_rect):
		if self.law_change_nomination_of_head_of_state_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'law_change_nomination_of_head_of_state_button'
			return 'law_change_nomination_of_head_of_state_button'
		
		elif self.law_change_election_of_head_of_state_button.rect.colliderect(mouse_rect):
			self.hovered_button = 'law_change_election_of_head_of_state_button'
			return 'law_change_election_of_head_of_state_button'

		
		if self.law_change_menu_open == None:
			
			if self.law_open == 'law_change_nomination_of_head_of_state_button':
				if self.law_change_nomination_of_head_of_state_by_election_button.rect.colliderect(mouse_rect) and self.PlayerCountry.head_of_state_apointment.active_law_index != 0:
					self.hovered_button = 'law_change_nomination_of_head_of_state_by_election_button'
					return 'law_change_nomination_of_head_of_state_by_election_button'
				elif self.law_change_nomination_of_head_of_state_dictator_button.rect.colliderect(mouse_rect) and self.PlayerCountry.head_of_state_apointment.active_law_index != 1:
					self.hovered_button = 'law_change_nomination_of_head_of_state_dictator_button'
					return 'law_change_nomination_of_head_of_state_dictator_button'
			
			elif self.law_open == 'law_change_election_of_head_of_state_button':
				if self.law_change_election_of_head_of_state_1_button.rect.colliderect(mouse_rect) and self.PlayerCountry.head_of_state_election.active_law_index != 0:
					self.hovered_button = 'law_change_election_of_head_of_state_1_button'
					return 'law_change_election_of_head_of_state_1_button'
				elif self.law_change_election_of_head_of_state_2_button.rect.colliderect(mouse_rect) and self.PlayerCountry.head_of_state_election.active_law_index != 1:
					self.hovered_button = 'law_change_election_of_head_of_state_2_button'
					return 'law_change_election_of_head_of_state_2_button'				


		else:
			if self.law_change_close_button.rect.colliderect(mouse_rect):
				self.hovered_button = 'law_change_close_button'
				return 'law_change_close_button'	
			elif self.law_change_accept_button.rect.colliderect(mouse_rect):
				self.hovered_button = 'law_change_accept_button'
				return 'law_change_accept_button'		
			elif self.law_change_survey_button.rect.colliderect(mouse_rect):
				self.hovered_button = 'law_change_survey_button'
				return 'law_change_survey_button'											

		self.hovered_button = None
		return None			

	def get_law_group(self):
		if self.law_open == 'law_change_nomination_of_head_of_state_button':
			return 'head_of_state_apointment'
		elif self.law_open == 'law_change_election_of_head_of_state_button':
			return 'head_of_state_election'

	def get_law(self):
		if self.law_change_menu_open == 'law_change_nomination_of_head_of_state_by_election_button':
			return 0
		elif self.law_change_menu_open == 'law_change_nomination_of_head_of_state_dictator_button':
			return 1

		elif self.law_change_menu_open == 'law_change_election_of_head_of_state_1_button':
			return 0
		elif self.law_change_menu_open == 'law_change_election_of_head_of_state_2_button':
			return 1			

	def draw(self, screen):
		screen.blit(self.PlayerCountry.country_leader_image, (72 * self.factor_x, 268 * self.factor_y))

		index_x = 0
		index_y = 0
		for person in self.PlayerCountry.head_of_state_close_people:
			if index_x >= 3:
				index_x = 0
				index_y += 1

			screen.blit(person.portrait, ((1330 + (190 * index_x)) * self.factor_x, (239 + (215 * index_y)) * self.factor_y))
			
			index_x += 1

		screen.blit(self.head_of_state_menu, (0, 158 * self.factor_y))

		head_of_state_title_text = self.medium_scalable_font.render(self.PlayerCountry.country_leader_title, True, (255,255,255))
		screen.blit(head_of_state_title_text, (304 * self.factor_x, 271 * self.factor_y))		

		head_of_state_name_text = self.medium_scalable_font.render(self.PlayerCountry.country_leader_name, True, (255,255,255))
		screen.blit(head_of_state_name_text, (304 * self.factor_x, 296 * self.factor_y))	

		next_election_text = self.medium_scalable_font.render(self.PlayerCountry.country_next_presidential_election, True, (255,255,255))
		screen.blit(next_election_text, (410 * self.factor_x, 346 * self.factor_y))	

		head_of_state_popularity_text = self.medium_scalable_font.render(str(self.PlayerCountry.country_party_popularity) + '%', True, (255,255,255))
		screen.blit(head_of_state_popularity_text, (375 * self.factor_x, 441 * self.factor_y))	

		#	HEAD OF STATE POPULARITY
		graph_pos_x = 106
		graph_pos_y = 518

		head_of_state_popularity = round(self.PlayerCountry.country_party_popularity, 1)

		head_of_state_popularity_15_high_end_text_render = self.small_scalable_font.render(str(round(head_of_state_popularity + head_of_state_popularity*0.15, 1))+' %', False, (255,255,255))	
		screen.blit(head_of_state_popularity_15_high_end_text_render, ((graph_pos_x - 25) * self.factor_x - head_of_state_popularity_15_high_end_text_render.get_width(), (graph_pos_y - 158) * self.factor_y + 158 * self.factor_y - head_of_state_popularity_15_high_end_text_render.get_height()/2))
		
		head_of_state_popularity_1125_high_end_text_render = self.small_scalable_font.render(str(round(head_of_state_popularity + head_of_state_popularity*0.1125, 1))+' %', False, (255,255,255))	
		screen.blit(head_of_state_popularity_1125_high_end_text_render, ((graph_pos_x - 25) * self.factor_x - head_of_state_popularity_1125_high_end_text_render.get_width(), (graph_pos_y - 113) * self.factor_y + 158 * self.factor_y - head_of_state_popularity_1125_high_end_text_render.get_height()/2))	

		head_of_state_popularity_75_high_end_text_render = self.small_scalable_font.render(str(round(head_of_state_popularity + head_of_state_popularity*0.075, 1))+' %', False, (255,255,255))	
		screen.blit(head_of_state_popularity_75_high_end_text_render, ((graph_pos_x - 25) * self.factor_x - head_of_state_popularity_75_high_end_text_render.get_width(), (graph_pos_y - 68) * self.factor_y + 158 * self.factor_y - head_of_state_popularity_75_high_end_text_render.get_height()/2))

		head_of_state_popularity_375_high_end_text_render = self.small_scalable_font.render(str(round(head_of_state_popularity + head_of_state_popularity*0.0375, 1))+' %', False, (255,255,255))	
		screen.blit(head_of_state_popularity_375_high_end_text_render, ((graph_pos_x - 25) * self.factor_x - head_of_state_popularity_375_high_end_text_render.get_width(), (graph_pos_y - 23) * self.factor_y + 158 * self.factor_y - head_of_state_popularity_375_high_end_text_render.get_height()/2))	


		head_of_state_popularity_15_low_end_text_render = self.small_scalable_font.render(str(round(head_of_state_popularity - head_of_state_popularity*0.15, 1))+' %', False, (255,255,255))	
		screen.blit(head_of_state_popularity_15_low_end_text_render, ((graph_pos_x - 25) * self.factor_x - head_of_state_popularity_15_low_end_text_render.get_width(), (graph_pos_y + 158) * self.factor_y + 158 * self.factor_y - head_of_state_popularity_15_low_end_text_render.get_height()/2))
		
		head_of_state_popularity_1125_low_end_text_render = self.small_scalable_font.render(str(round(head_of_state_popularity - head_of_state_popularity*0.1125, 1))+' %', False, (255,255,255))	
		screen.blit(head_of_state_popularity_1125_low_end_text_render, ((graph_pos_x - 25) * self.factor_x - head_of_state_popularity_1125_low_end_text_render.get_width(), (graph_pos_y + 113) * self.factor_y + 158 * self.factor_y - head_of_state_popularity_1125_low_end_text_render.get_height()/2))	

		head_of_state_popularity_75_low_end_text_render = self.small_scalable_font.render(str(round(head_of_state_popularity - head_of_state_popularity*0.075, 1))+' %', False, (255,255,255))	
		screen.blit(head_of_state_popularity_75_low_end_text_render, ((graph_pos_x - 25) * self.factor_x - head_of_state_popularity_75_low_end_text_render.get_width(), (graph_pos_y + 68) * self.factor_y + 158 * self.factor_y - head_of_state_popularity_75_low_end_text_render.get_height()/2))

		head_of_state_popularity_375_low_end_text_render = self.small_scalable_font.render(str(round(head_of_state_popularity - head_of_state_popularity*0.0375, 1))+' %', False, (255,255,255))	
		screen.blit(head_of_state_popularity_375_low_end_text_render, ((graph_pos_x - 25) * self.factor_x - head_of_state_popularity_375_low_end_text_render.get_width(), (graph_pos_y + 23) * self.factor_y + 158 * self.factor_y - head_of_state_popularity_375_low_end_text_render.get_height()/2))			


		graph_dots = []
		for index, weekly_data in enumerate(self.PlayerCountry.weekly_head_of_state_popularity_data):
			if weekly_data > head_of_state_popularity:
				height = graph_pos_y - (158 * (min(1, (weekly_data/(head_of_state_popularity + 0.01)) - 1)))
			else:
				height = graph_pos_y + (158 * (min(1, (head_of_state_popularity/(weekly_data + 0.01)) - 1)))
			
			graph_dots.append(((9.79999 * index + graph_pos_x) * self.factor_x, (height + 158) * self.factor_y))

		if len(graph_dots) > 1:
			self.pygame.draw.lines(screen, (218,255,127), False, graph_dots, 3)
		else:
			self.pygame.draw.line(screen, (218,255,127), graph_dots[0], (graph_dots[0][0], (graph_pos_y + 158) * self.factor_y), 3)


		if self.law_open != None:
			pygame.draw.rect(screen, (255,255,255), self.law_open_menu_rect, 1)
			if self.law_open == 'law_change_nomination_of_head_of_state_button':
				pygame.draw.rect(screen, (255,255,255), self.law_change_nomination_of_head_of_state_button.rect, 3)


				pygame.draw.rect(screen, (255,255,255), self.law_change_nomination_of_head_of_state_by_election_button.rect, 1)

				pygame.draw.rect(screen, (255,255,255), self.law_change_nomination_of_head_of_state_dictator_button.rect, 1)	
				

				text_render = self.medium_scalable_font.render('BY ELECTION', True, (255,255,255))
				screen.blit(text_render, (self.law_change_nomination_of_head_of_state_by_election_button.x + self.law_change_nomination_of_head_of_state_by_election_button.width/2 - text_render.get_width()/2, self.law_change_nomination_of_head_of_state_by_election_button.y + self.law_change_nomination_of_head_of_state_by_election_button.height/2 - text_render.get_height()/2))

				text_render = self.medium_scalable_font.render('RULE FOR LIFE', True, (255,255,255))
				screen.blit(text_render, (self.law_change_nomination_of_head_of_state_dictator_button.x + self.law_change_nomination_of_head_of_state_dictator_button.width/2 - text_render.get_width()/2, self.law_change_nomination_of_head_of_state_dictator_button.y + self.law_change_nomination_of_head_of_state_dictator_button.height/2 - text_render.get_height()/2))

				
				if self.hovered_button == 'law_change_nomination_of_head_of_state_by_election_button':
					pygame.draw.rect(screen, (0,255,0), self.law_change_nomination_of_head_of_state_by_election_button.rect, 3)
					self.hovered_button = None
				elif self.hovered_button == 'law_change_nomination_of_head_of_state_dictator_button':
					pygame.draw.rect(screen, (0,255,0), self.law_change_nomination_of_head_of_state_dictator_button.rect, 3)
					self.hovered_button = None

				if self.PlayerCountry.head_of_state_apointment.active_law_index == 0:
					pygame.draw.rect(screen, (255,0,0), self.law_change_nomination_of_head_of_state_by_election_button.rect, 3)
				elif self.PlayerCountry.head_of_state_apointment.active_law_index == 1:
					pygame.draw.rect(screen, (255,0,0), self.law_change_nomination_of_head_of_state_dictator_button.rect, 3)

			elif self.law_open == 'law_change_election_of_head_of_state_button':
				pygame.draw.rect(screen, (255,255,255), self.law_change_election_of_head_of_state_button.rect, 3)


				pygame.draw.rect(screen, (255,255,255), self.law_change_election_of_head_of_state_1_button.rect, 1)

				pygame.draw.rect(screen, (255,255,255), self.law_change_election_of_head_of_state_2_button.rect, 1)


				text_render = self.medium_scalable_font.render('1', True, (255,255,255))
				screen.blit(text_render, (self.law_change_election_of_head_of_state_1_button.x + self.law_change_election_of_head_of_state_1_button.width/2 - text_render.get_width()/2, self.law_change_election_of_head_of_state_1_button.y + self.law_change_election_of_head_of_state_1_button.height/2 - text_render.get_height()/2))

				text_render = self.medium_scalable_font.render('2', True, (255,255,255))
				screen.blit(text_render, (self.law_change_election_of_head_of_state_2_button.x + self.law_change_election_of_head_of_state_2_button.width/2 - text_render.get_width()/2, self.law_change_election_of_head_of_state_2_button.y + self.law_change_election_of_head_of_state_2_button.height/2 - text_render.get_height()/2))

				
				if self.hovered_button == 'law_change_election_of_head_of_state_1_button':
					pygame.draw.rect(screen, (0,255,0), self.law_change_election_of_head_of_state_1_button.rect, 3)
					self.hovered_button = None
				elif self.hovered_button == 'law_change_election_of_head_of_state_2_button':
					pygame.draw.rect(screen, (0,255,0), self.law_change_election_of_head_of_state_2_button.rect, 3)
					self.hovered_button = None

				if self.PlayerCountry.head_of_state_election.active_law_index == 0:
					pygame.draw.rect(screen, (255,0,0), self.law_change_election_of_head_of_state_1_button.rect, 3)
				elif self.PlayerCountry.head_of_state_election.active_law_index == 1:
					pygame.draw.rect(screen, (255,0,0), self.law_change_election_of_head_of_state_2_button.rect, 3)					

		if self.hovered_button == 'law_change_nomination_of_head_of_state_button':
			pygame.draw.rect(screen, (0,255,0), self.law_change_nomination_of_head_of_state_button.rect, 3)
			self.hovered_button = None		
		elif self.hovered_button == 'law_change_election_of_head_of_state_button':
			pygame.draw.rect(screen, (0,255,0), self.law_change_election_of_head_of_state_button.rect, 3)
			self.hovered_button = None				

		if self.law_change_menu_open != None:
			pygame.draw.rect(screen, (6,17,21), self.law_open_menu_rect)
			pygame.draw.rect(screen, (255,233,127), self.law_open_menu_rect, 2)	

			law_group = getattr(self.PlayerCountry, self.get_law_group())

			law = self.get_law()

			self.text_offset_y = self.text_scroll_bar.get_scroll_position()	

			if type(law_group) == CountriesManager.Laws_Group:
				self.law_being_voted_description_surface.fill((0,0,0,0))
				text_render = self.medium_scalable_font.render(' '.join(law_group.group_name.split('_')).upper() + ' - ' + ' '.join(law_group.laws[law].name.split('_')).upper() + ':\n\n' + law_group.laws[law].description, False, (255,255,255))
				self.law_being_voted_description_surface.blit(text_render, (0, 0))
				screen.blit(self.law_being_voted_description_surface.subsurface(0, self.text_offset_y, self.law_being_voted_description_surface.get_width(), 336 * self.factor_y), (680 * self.factor_x, 486 * self.factor_y))

			elif type(law_group) == dict:
				law_group[law.law_being_suggested['key']] = law.law_being_suggested['value']

			self.text_scroll_bar.draw(screen)			

			pygame.draw.rect(screen, (255,255,255), self.law_change_close_button.rect, 1)
			pygame.draw.rect(screen, (255,255,255), self.law_change_accept_button.rect, 1)
			pygame.draw.rect(screen, (255,255,255), self.law_change_survey_button.rect, 1)	

			text_render = self.medium_scalable_font.render('CANCEL', True, (255,0,0))
			screen.blit(text_render, (self.law_change_close_button.x + self.law_change_close_button.width/2 - text_render.get_width()/2, self.law_change_close_button.y + self.law_change_close_button.height/2 - text_render.get_height()/2 + 1))
			
			text_render = self.medium_scalable_font.render('VOTE LAW', True, (0,255,0))
			screen.blit(text_render, (self.law_change_accept_button.x + self.law_change_accept_button.width/2 - text_render.get_width()/2, self.law_change_accept_button.y + self.law_change_accept_button.height/2 - text_render.get_height()/2 + 1))


			screen.blit(self.law_opinion_survey_icon, (self.law_change_survey_button.x, self.law_change_survey_button.y))

			text_render = self.tiny_scalable_font.render('SURVEY', True, (255,255,255))
			screen.blit(text_render, (self.law_change_survey_button.x + self.law_change_survey_button.width/2 - text_render.get_width()/2, self.law_change_survey_button.y + self.law_change_survey_button.height - text_render.get_height()*1.1))			

			if self.hovered_button == 'law_change_close_button':
				pygame.draw.rect(screen, (255,0,0), self.law_change_close_button.rect, 3)
				self.hovered_button = None
			elif self.hovered_button == 'law_change_accept_button':
				pygame.draw.rect(screen, (0,255,0), self.law_change_accept_button.rect, 3)
				self.hovered_button = None			
			elif self.hovered_button == 'law_change_survey_button':
				pygame.draw.rect(screen, (0,255,0), self.law_change_survey_button.rect, 3)
				self.hovered_button = None						
class Legislative_Government_Cabinet_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, cabinet_menu):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = PlayerCountry

		self.cabinet_menu = pygame.transform.smoothscale_by(cabinet_menu, (self.factor_x, self.factor_y))

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))			

	def draw(self, screen):
		index_x = 0
		index_y = 0
		for person in self.PlayerCountry.country_government_gabinet:
			if index_x >= 10:
				index_x = 0
				index_y += 1

			screen.blit(person.portrait, ((34 + (190 * index_x)) * self.factor_x, (228 + (215 * index_y)) * self.factor_y))
			
			index_x += 1

		screen.blit(self.cabinet_menu, (0, 158 * self.factor_y))
class Legislative_Government_Parliament_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, law_opinion_survey_icon, parliament_menu):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = PlayerCountry

		self.law_opinion_survey_icon = law_opinion_survey_icon

		self.parliament_menu = pygame.transform.smoothscale_by(parliament_menu, (self.factor_x, self.factor_y))

		self.update_pie_chart = True

		self.parliament_pie_chart_surface = pygame.Surface((603 * self.factor_x, 301 * self.factor_y), pygame.SRCALPHA)		
		self.senate_pie_chart_surface = pygame.Surface((603 * self.factor_x, 301 * self.factor_y), pygame.SRCALPHA)	

		self.law_being_voted_surface = pygame.Surface((638 * self.factor_x, 469 * self.factor_y), pygame.SRCALPHA)	

		self.laws_being_voted_rects = []	
		self.open_law = None

		self.hovered_rect = None

		self.law_being_voted_description_surface = pygame.Surface((496 * self.factor_x, 850 * self.factor_y), pygame.SRCALPHA)		

		self.law_open_menu_rect = (1262 * self.factor_x, 375 * self.factor_y, 642 * self.factor_x, 500 * self.factor_y)
		self.law_change_close_button = GenericUtilitys.Button(1303 * self.factor_x, 794 * self.factor_y, 250 * self.factor_x, 50 * self.factor_y)
		self.law_change_accept_button = GenericUtilitys.Button(1613 * self.factor_x, 794 * self.factor_y, 250 * self.factor_x, 50 * self.factor_y)
		self.law_change_survey_button = GenericUtilitys.Button(1799 * self.factor_x, 680 * self.factor_y, 64 * self.factor_x, 64 * self.factor_y)	

		self.text_scroll_bar = GenericUtilitys.Scroll_Bar(1268 * self.factor_x, 378 * self.factor_x, 494 * self.factor_y, 850 * self.factor_y - 494 * self.factor_y, (255,255,255), (255,0,0), 10 * self.factor_x)				

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))			

	def get_button_by_interaction(self, mouse_rect):
		if self.open_law != None:
			if self.law_change_close_button.rect.colliderect(mouse_rect):
				self.hovered_rect = self.law_change_close_button.rect
				return 'law_change_close_button'	
			elif self.law_change_accept_button.rect.colliderect(mouse_rect):
				self.hovered_rect = self.law_change_accept_button.rect
				return 'law_change_accept_button'		
			elif self.law_change_survey_button.rect.colliderect(mouse_rect):
				self.hovered_rect = self.law_change_survey_button.rect
				return 'law_change_survey_button'
		else:
			for rect in self.laws_being_voted_rects:
				if rect[0].colliderect(mouse_rect):									
					self.hovered_rect = rect[0]
					return rect[1]		

			
		self.hovered_button = None
		return None			

	def draw(self, screen):

		height = (519 + 158) * self.factor_y
		screen.blit(self.PlayerCountry.parliament_head.portrait, (156 * self.factor_x, height))
		screen.blit(self.PlayerCountry.parliament_parties_head.portrait, (346 * self.factor_x, height))

		screen.blit(self.PlayerCountry.senate_head.portrait, (774 * self.factor_x, height))
		screen.blit(self.PlayerCountry.senate_parties_head.portrait, (964 * self.factor_x, height))


		screen.blit(self.parliament_menu, (0, 158 * self.factor_y))

		if self.update_pie_chart == True:
			self.parliament_pie_chart_surface.fill((0, 0, 0, 0))
			self.senate_pie_chart_surface.fill((0, 0, 0, 0))
			
			last_parliament_angle = 180
			last_senate_angle = 180
			for official_party in self.PlayerCountry.country_official_parties:
				parliament_end_angle = 180 * (official_party.parliament_seats / self.PlayerCountry.total_parliament_seats)
				GenericUtilitys.draw_pie(self.parliament_pie_chart_surface, official_party.party_color, (302 * self.factor_x, 300 * self.factor_y), 300 * self.factor_x, last_parliament_angle, parliament_end_angle + last_parliament_angle)
				last_parliament_angle = parliament_end_angle + last_parliament_angle

				senate_end_angle = 180 * (official_party.senate_seats / self.PlayerCountry.total_senate_seats)
				GenericUtilitys.draw_pie(self.senate_pie_chart_surface, official_party.party_color, (302 * self.factor_x, 300 * self.factor_y), 300 * self.factor_x, last_senate_angle, senate_end_angle + last_senate_angle)
				last_senate_angle = senate_end_angle + last_senate_angle				

			self.update_pie_chart = False

		height = (137 + 158) * self.factor_y
		screen.blit(self.parliament_pie_chart_surface, (21 * self.factor_x, height))
		screen.blit(self.senate_pie_chart_surface, (639 * self.factor_x, height))

		if self.open_law == None:
			self.law_being_voted_surface.fill((0,0,0,0))
			self.laws_being_voted_rects = []

			if len(self.PlayerCountry.laws_being_voted) >= 1:
				support_explanation_text = self.small_scalable_font.render("P.S. = POLITICAL SUPPORT  |  C.S. = CIVILIAN SUPPORT", True, (240,233,115))
				screen.blit(support_explanation_text, (1480 * self.factor_x, 382 * self.factor_y))

			for index, law in enumerate(self.PlayerCountry.laws_being_voted):
				Law_name_text = self.small_scalable_font.render(' '.join(law.law_group_being_voted.split('_')).upper(), True, (255,255,255))

				Law_election_date_text = self.tiny_scalable_font.render(f'WILL BE VOTED ON: {law.voting_day:02d}/{law.voting_month:02d}/{law.voting_year:04d}', True, (165,255,127))

				height_offset = (index * 50) * self.factor_y

				self.law_being_voted_surface.blit(Law_name_text, (15 * self.factor_x, 17 * self.factor_y + height_offset))
				self.law_being_voted_surface.blit(Law_election_date_text, (100 * self.factor_x + Law_name_text.get_width(), 17 * self.factor_y + height_offset + Law_name_text.get_height()))

				pygame.draw.rect(self.law_being_voted_surface, (255,255,255), (5 * self.factor_x, height_offset, 628 * self.factor_x, Law_name_text.get_height() + 35 * self.factor_y), 1)
				self.laws_being_voted_rects.append((pygame.Rect((5 + 1264) * self.factor_x, 404 * self.factor_y + height_offset, 628 * self.factor_x, Law_name_text.get_height() + 35 * self.factor_y), law))

				if law.opinion_surveyed == False:
					accuracy_color = (255,90,90)
				else:
					accuracy_color = (127,255,197)

				if law.survey_parliament_support != None and law.survey_senate_support != None:
					law_survey_political_support = round((law.survey_parliament_support + law.survey_senate_support)/2, 1)
				elif law.survey_parliament_support != None:
					law_survey_political_support = round(law.survey_parliament_support, 1)
				elif law.survey_senate_support != None:
					law_survey_political_support = round(law.survey_senate_support, 1)
				else:
					law_survey_political_support = 'None'

				law_survey_civilian_support = law.survey_civilian_support
				if law.survey_civilian_support == None:
					law_survey_civilian_support = ['None']					

				Law_political_support_text = self.tiny_scalable_font.render('P.S.: ' + str(law_survey_political_support) + '%  /  ', True, accuracy_color)
				self.law_being_voted_surface.blit(Law_political_support_text, (100 * self.factor_x + Law_name_text.get_width(), 10 * self.factor_y + height_offset))

				Law_civilian_support_text = self.tiny_scalable_font.render('C.S.: ' + str(law_survey_civilian_support[0]) + '%', True, accuracy_color)
				self.law_being_voted_surface.blit(Law_civilian_support_text, (100 * self.factor_x + Law_name_text.get_width() + Law_political_support_text.get_width(), 10 * self.factor_y + height_offset))

			screen.blit(self.law_being_voted_surface, (1264 * self.factor_x, 404 * self.factor_y))
		else:
			self.law_being_voted_description_surface.fill((0,0,0,0))

			pygame.draw.rect(screen, (6,17,21), self.law_open_menu_rect)
			pygame.draw.rect(screen, (255,233,127), self.law_open_menu_rect, 2)

			law_group = getattr(self.PlayerCountry, self.open_law.law_group_being_voted)

			self.text_offset_y = self.text_scroll_bar.get_scroll_position()	

			if type(law_group) == CountriesManager.Laws_Group:
				text_render = self.big_scalable_font.render(' '.join(self.open_law.law_group_being_voted.split('_')).upper() + ':\n\n' + law_group.laws[self.open_law.law_being_suggested].description, True, (255,255,255))
				self.law_being_voted_description_surface.blit(text_render, (0, 0))
				screen.blit(self.law_being_voted_description_surface.subsurface(0, self.text_offset_y, self.law_being_voted_description_surface.get_width(), 405 * self.factor_y), (1303 * self.factor_x, 385 * self.factor_y))

			elif type(law_group) == dict:
				law_group[law.law_being_suggested['key']] = law.law_being_suggested['value']

			self.text_scroll_bar.draw(screen)

			pygame.draw.rect(screen, (255,255,255), self.law_change_close_button.rect, 1)
			pygame.draw.rect(screen, (255,255,255), self.law_change_accept_button.rect, 1)
			pygame.draw.rect(screen, (255,255,255), self.law_change_survey_button.rect, 1)	

			text_render = self.medium_scalable_font.render('CANCEL VOTING', True, (255,0,0))
			screen.blit(text_render, (self.law_change_close_button.x + self.law_change_close_button.width/2 - text_render.get_width()/2, self.law_change_close_button.y + self.law_change_close_button.height/2 - text_render.get_height()/2 + 1))
			
			text_render = self.medium_scalable_font.render('KEEP VOTING', True, (0,255,0))
			screen.blit(text_render, (self.law_change_accept_button.x + self.law_change_accept_button.width/2 - text_render.get_width()/2, self.law_change_accept_button.y + self.law_change_accept_button.height/2 - text_render.get_height()/2 + 1))
			
			screen.blit(self.law_opinion_survey_icon, (self.law_change_survey_button.x, self.law_change_survey_button.y))

			text_render = self.tiny_scalable_font.render('SURVEY', True, (255,255,255))
			screen.blit(text_render, (self.law_change_survey_button.x + self.law_change_survey_button.width/2 - text_render.get_width()/2, self.law_change_survey_button.y + self.law_change_survey_button.height - text_render.get_height()*1.1))		
		
		if self.hovered_rect != None:
			if self.hovered_rect != self.law_change_close_button.rect:
				pygame.draw.rect(screen, (0,255,0), self.hovered_rect, 2)
			else:
				pygame.draw.rect(screen, (255,0,0), self.hovered_rect, 2)
			self.hovered_rect = None
class Legislative_Government_Elections_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, elections_menu):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = PlayerCountry

		self.elections_menu = pygame.transform.smoothscale_by(elections_menu, (self.factor_x, self.factor_y))

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))			

	def draw(self, screen):
		# CHART
		chart_position = (511 * self.factor_x, 530 * self.factor_y) 
		chart_radius = 360 * self.factor_y

		parties_popularity_porcentages = []
		for party in self.PlayerCountry.country_official_parties:
			parties_popularity_porcentages.append(party.popularity)

		self.expenses_cicle_rects = GenericUtilitys.draw_pie_chart(screen, chart_position, chart_radius, parties_popularity_porcentages, [
		(0, 15, 0),
		(255, 255, 255),
		(255, 0, 0),
		(0, 255, 0),
		(0, 0, 255),
		(255, 255, 0),
		(0, 255, 255),
		(255, 0, 255),
		(128, 128, 128),
		(128, 0, 0),
		(128, 128, 0),
		(0, 128, 0),
		(0, 0, 128),
		(128, 0, 128),
		(0, 128, 128),
		(192, 192, 192),
		(169, 169, 169),
		(139, 0, 0),
		(165, 42, 42),
		(0, 0, 139),
		(255, 165, 0),
		(255, 192, 203),
		(255, 215, 0),
		(230, 230, 250),
		(107, 142, 35),
		(135, 206, 235),
		(112, 128, 144)
		])		
		#----------------------#

		screen.blit(self.elections_menu, (0, 158 * self.factor_y))

		next_presidential_election_text = self.medium_scalable_font.render(self.PlayerCountry.country_next_presidential_election, True, (255,255,255))
		screen.blit(next_presidential_election_text, (144 * self.factor_x, 808 * self.factor_y))	

		next_congessional_election_text = self.medium_scalable_font.render(self.PlayerCountry.country_next_congessional_election, True, (255,255,255))
		screen.blit(next_congessional_election_text, (144 * self.factor_x, 862 * self.factor_y))		
class Legislative_Government_Political_Parties_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, PlayerCountry, political_parties_menu):
		
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.PlayerCountry = PlayerCountry

		self.political_parties_menu = pygame.transform.smoothscale_by(political_parties_menu, (self.factor_x, self.factor_y))

		self.update_parties_pie_chart = True

		self.parties_pie_chart_surface = pygame.Surface((603 * self.factor_x, 301 * self.factor_y), pygame.SRCALPHA)
		self.official_parties_names_surface = pygame.Surface((295 * self.factor_x, 187 * self.factor_y), pygame.SRCALPHA)		

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))			

	def draw(self, screen):
		screen.blit(self.political_parties_menu, (0, 158 * self.factor_y))								

		if self.update_parties_pie_chart == True:
			self.parties_pie_chart_surface.fill((0, 0, 0, 0))
			self.official_parties_names_surface.fill((0, 0, 0, 0))
			last_angle = 180
			for index, official_party in enumerate(self.PlayerCountry.country_official_parties):
				end_angle = 180 * (official_party.parliament_seats / self.PlayerCountry.total_parliament_seats)
				GenericUtilitys.draw_pie(self.parties_pie_chart_surface, official_party.party_color, (302, 300), 300, last_angle, end_angle + last_angle)
				last_angle = end_angle + last_angle

				party_name_text = self.small_scalable_font.render(official_party.party_name, True, (255, 255, 255))

				self.pygame.draw.rect(self.official_parties_names_surface, official_party.party_color, (5 * self.factor_x, (party_name_text.get_height()*1.2) * index + 5 * self.factor_y, party_name_text.get_height(), party_name_text.get_height()))

				text_position = (5 * self.factor_x + party_name_text.get_height()*1.1, (party_name_text.get_height()*1.2) * index + 5 * self.factor_y)
				self.official_parties_names_surface.blit(party_name_text, text_position)			

			self.update_parties_pie_chart = False

		# PARTIES
		screen.blit(self.parties_pie_chart_surface, (15 * self.factor_x, 229 * self.factor_y))

		screen.blit(self.official_parties_names_surface, (18 * self.factor_x, 565 * self.factor_y))				

# POP UP
class Game_Introduction_Menu:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, game_logo):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.game_logo = pygame.transform.smoothscale_by(game_logo, (self.factor_x, self.factor_y))			

		self.is_menu_open = True
		self.highlight_button = False

		self.height = self.screen_height - (158 + 35) * self.factor_y
		self.button_size = (self.screen_width/4, 60 * self.factor_y)

		self.close_introduction_button = GenericUtilitys.Button(self.screen_width/2 - self.button_size[0]/2, self.height, self.button_size[0], self.button_size[1])

		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(12 * self.factor_y))		

		# TEXT
		self.text_scroll_bar = GenericUtilitys.Scroll_Bar(6, 164  * self.factor_y, self.screen_height - (158 + 110 + 10) * self.factor_y, 2250 * self.factor_y - (self.height-(198 * self.factor_y)) + self.game_logo.get_height()*1.1, (255,255,255), (255,0,0), 10 * self.factor_x)

		self.text_offset_y = 0

		self.introduction_text = """
ACT I - 1943-1947


In the tumultuous year of 1943, Mussolini's audacious betrayal shattered the Axis alliance, leaving chaos in its wake.
As the Mediterranean theater became the epicenter of conflict, the Allies, bolstered by Italian southern forces, launched a daring offensive into German-occupied Italy.
The German High Command, already stretched thin on the Eastern Front against the relentless Soviet advance, now faced
a three-front war. By 1945, the Allies began to emerge totally victorious.

In the wake of the uneasy peace, the Allies faced a growing unease regarding the Soviet threat, their leadership grew
wary of the growing influence of the Soviet Union in Eastern Europe.
As Soviet troops and their American counterparts stood on the outskirts of Berlin, with remnants of the defeated Axis now as allies, the Allies launched a surprise
offensive against the Soviet Union. The Eastern Front, weakened by the relentless Soviet advance, presented an opportunity to challenge the Soviet might.

As the conflict raged on, the Soviets managed to push the Western Allies back. The vast expanse of Eastern Europe witnessed the ebb and flow of armies, with cities
changing hands multiple times. The Allies made a final stand at the Rhine River and the formidable Alps. In a desperate gambit to stop the Soviet onslaught and end
the escalating conflict, the Allies turned to a weapon initially planned for use against Japan - nuclear weapons:

The first nuclear strike, unleashed upon Soviet military concentrations near the Rhine River, sent shockwaves through the conflict zone. The devastating power of the
explosion caught the Soviet forces off guard, disrupting their advance and causing significant casualties.
Simultaneously, the second nuclear strike, strategically aimed at military troops entrenched in the formidable Alps, further underscored the Allies' resolve to halt
the Soviet onslaught. 

The world watched with bated breath the conflict in Europe reaching a stalemate, as the nuclear strikes brought the conflict to a halt, the subsequent diplomatic
negotiations aimed to reshape the political landscape of post-war Europe:

Among the notable changes was the unification of Belgium with the remaining Allied-held parts of the Netherlands west of the Rhine. However, such geopolitical
realignments were not without challenges. The integration of two distinct nations into a unified entity demanded careful navigation of cultural, administrative, and
political differences.

Another notable development unfolded in the heart of the continent. Switzerland, known for its neutrality during World War II, entered into diplomatic discussions with
the Allied powers.
In a strategic move to strengthen the region against potential future threats, Switzerland unified with the remaining parts of the Austrian Alps.

However, a shadow lurked in the corner…

Mussolini, after a strategic shift in alliances during the war, found himself in a precarious position as the dust settled. Understanding the intricate nature of the
situation, Allied leaders carefully weighed the potential ramifications of totally ousting Mussolini from power.
The Allies harbored concerns that removing Mussolini abruptly might create a power vacuum, leading to political instability, internal strife, and the risk of an upsurge
in more radical statism, potentially inclining towards socialism.

Despite these reservations, the decision to allow Mussolini to retain power came with certain stipulations. The Allies, keenly aware of the delicate balance required in
post-war Italy, instituted a system of close monitoring over Italian political developments. Mussolini, granted the latitude to remain in a position of authority, was
compelled to navigate a nuanced path. 


ACT II - 1947-1970


In the wake of the nuclear stalemate, as the dust of global uncertainty settled, an ominous shadow descended upon the world. The Soviets, lurking in the sinister aftermath,
seized the opportunity to mold the very fabric of reality.

Embracing the tools of subversion, espionage, and political manipulation, the Soviets ushered in a chilling era, a clandestine war fought in the obscurity of shadows.
The Cold War, now transformed into a macabre dance orchestrated by intelligence agencies and covert operatives, wove a sinister tapestry of deceit that ensnared nations in
a malevolent embrace.

As the world watched, unaware of the unseen puppeteers pulling the strings, this dark ballet of silent malevolence tightened, the KGB emerged as an unholy force, spreading
its dark influence across the globe, like a malignant web ensnaring the unsuspecting prey of Western powers.

The Soviets, architects of a malevolent symphony, understood the potency of ideas. A sinister campaign of ideological subversion unfolded, infiltrating the sanctuaries of 
knowledge; academic institutions, media citadels, and the very soul of culture. A toxic brew of false narratives, fabricated stories, and deceitful information oozed forth,
creating a miasma of confusion and manipulating the fragile tapestry of public opinion.

Within the realm of culture, the Soviets wielded a malevolent brush, supporting artists, writers, and filmmakers whose creations resonated with their dark ideology.
The narratives that unfolded became insidious whispers, seeping into the collective consciousness, like a slow poison corrupting the very essence of truth.

Through a network of faceless proxies, they orchestrated conflicts in far-flung realms; Southeast Asia, Africa, and Latin America. Movements and governments, puppets of a
malevolent force, danced to the tune of communism, expanding the Soviet sphere without the need for the overt clash of armies.

The absence of thundering tanks and warring armies did not herald an era of tranquility, but rather a shift to a covert and ideological battleground, where minds were the
weapons, and truth became a casualty.

The second act of the Cold War was defined not by the roar of tanks and the clash of armies but by the quiet and persistent erosion of the values that had once defined the
Western world.


	The silent war of ideologies had begun, and its effects would reverberate for decades to come...
"""

		self.introduction_text_surface = pygame.Surface((self.screen_width, 2250 * self.factor_y + self.game_logo.get_height()*1.1), pygame.SRCALPHA)
		self.introduction_text_surface.blit(self.game_logo, (self.screen_width/2 - self.game_logo.get_width()/2, 0))

		introduction_text_render = self.big_scalable_font.render(self.introduction_text, False, (255,255,255))
		self.introduction_text_surface.blit(introduction_text_render, (0, self.game_logo.get_height()*1.1))

	def get_button_by_interaction(self, mouse_rect):	
		if self.close_introduction_button.rect.colliderect(mouse_rect) and self.is_menu_open == True:
			return "close_introduction_button"
		
		return None

	def draw(self, screen):
		if self.is_menu_open == True:
			self.pygame.draw.rect(screen, (6,15,20), (0, 158 * self.factor_y, self.screen_width, self.screen_height - (158 + 110) * self.factor_y))
			self.pygame.draw.rect(screen, (43,219,211), (0, 158 * self.factor_y, self.screen_width, self.screen_height - (158 + 110) * self.factor_y), 2)

			self.text_scroll_bar.draw(screen)

			self.text_offset_y = self.text_scroll_bar.get_scroll_position()

			screen.blit(self.introduction_text_surface.subsurface(0, self.text_offset_y, self.screen_width, self.height-(198 * self.factor_y)), (20, 178 * self.factor_y))

			self.pygame.draw.rect(screen, (255,255,255), self.close_introduction_button.rect, 2)	

			close_text_render = self.huge_scalable_font.render('CLOSE', False, (255,0,0))
			screen.blit(close_text_render, (self.screen_width/2 - close_text_render.get_width()/2, (self.height) + (self.button_size[1])/2 - close_text_render.get_height()/2 + 2))		

		if self.highlight_button == True:
			self.pygame.draw.rect(screen, (255,0,0), self.close_introduction_button.rect, 3)

class County_Overview:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame):
		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.is_menu_open = False

	def draw(self, screen):
		if self.is_menu_open == True:
			self.pygame.draw.rect(screen, (255,0,0), (500, 500, 100, 100))  # (x, y, width, height)

#----------------------------------------------------#

























