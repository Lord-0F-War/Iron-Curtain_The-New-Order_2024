
import GenericUtilitys
from PygameManager import pygame
from pyvidplayer import Video
import random

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

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

		self.main_menu_intro_video = Video("Know Your History.mp4", size=(936 * self.factor_x, 378 * self.factor_y))
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

		screen.blit(self.game_logo, (60 * self.factor_x, 0))	
		
		if self.is_in_new_game_menu == False:
			self.main_menu_intro_video.draw(screen, (self.menu_gui_middle_x + 2 * self.factor_x, self.menu_gui_middle_y + 2 * self.factor_y))

			if self.main_menu_intro_video.frames >= 1674:
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

		screen.blit(self.game_logo, (60 * self.factor_x, 0))

		if self.hovered_button != 'none':
			if self.hovered_button == 'start':
				screen.blit(self.hovered_select_scenario_button_menu_image, self.start_button.rect)
			if self.hovered_button == 'back':
				screen.blit(self.hovered_back_button_menu_image, self.back_button.rect)
		else:
			self.hover_over_button_sound.fadeout(200)	


class Country_Selection_Screen:
	def __init__(self,
				screen_width, screen_height, pygame, countries, generic_hover_over_button_sound, generic_click_button_sound, 
				country_selection_background, country_info_display_background, political_compass_image, ideologies_CRT_overlay_effect,
				hovered_start_game_button, hovered_select_national_spirit_button_image, hovered_select_country_button_image, 
				hovered_laws_button_image, generic_leader, CRT_flag_overlay_effect, blocked_select_national_spirit_button, 
				blocked_select_country_button, blocked_start_game_button, blocked_full_right_side, blocked_all_laws, national_spirits_background,
				generic_national_spirits, progressbar, progressbar_vertical, progressbar_small, progressbar_huge):	
		
		self.Country_Selection_Menu = Country_Selection_Menu(
				screen_width, screen_height, pygame, generic_hover_over_button_sound, generic_click_button_sound, 
				country_selection_background, political_compass_image, ideologies_CRT_overlay_effect,
				hovered_start_game_button, hovered_select_national_spirit_button_image, hovered_select_country_button_image, 
				hovered_laws_button_image, generic_leader, CRT_flag_overlay_effect, blocked_select_national_spirit_button, 
				blocked_select_country_button, blocked_start_game_button, blocked_full_right_side, blocked_all_laws, progressbar, progressbar_vertical,
				progressbar_small, progressbar_huge)		
		
		self.Flag_Selection_Menu = Flag_Selection_Menu(screen_width, screen_height, pygame, countries, 
				generic_hover_over_button_sound, generic_click_button_sound, country_info_display_background)
		
		self.National_Spirits_Selection_Menu = National_Spirits_Selection_Menu(screen_width, screen_height,
				national_spirits_background, generic_national_spirits, generic_hover_over_button_sound, generic_click_button_sound, political_compass_image)
		
		self.selected_flag_image = None

	def get_clicked_button(self, mouse_rect):
		if self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == False:
			clicked_button = self.Country_Selection_Menu.get_clicked_ideology(mouse_rect)
			if clicked_button != None:
				return clicked_button			
		
			clicked_button = self.Flag_Selection_Menu.get_clicked_button(mouse_rect)
			if clicked_button != None:
				pygame.mixer.music.fadeout(200)
				self.Flag_Selection_Menu.flag_rects = []
				self.Country_Selection_Menu.flag_size = None
				self.Country_Selection_Menu.is_flag_selection_menu_open = False
				self.selected_flag_image = clicked_button
				self.Country_Selection_Menu.selected_flag_image = self.selected_flag_image
				self.Country_Selection_Menu.selected_selectable_national_spirits = []
				self.National_Spirits_Selection_Menu.selected_country = self.Flag_Selection_Menu.selected_country		
				self.Country_Selection_Menu.selected_country = self.Flag_Selection_Menu.selected_country		
				return clicked_button
			
		clicked_button = self.Country_Selection_Menu.get_clicked_button(mouse_rect)
		if clicked_button != None and (self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == False and clicked_button != 'select_country'):
			return clicked_button		
		
		clicked_button = self.National_Spirits_Selection_Menu.get_clicked_national_spirit(mouse_rect)
		if clicked_button != None:
			return clicked_button	

	def get_hovered_button(self, mouse_rect):	
		if self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == False:
			hovered_button = self.Country_Selection_Menu.get_hovered_button(mouse_rect)
			if hovered_button != None:
				return hovered_button	

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

		hovered_button = self.National_Spirits_Selection_Menu.get_hovered_national_spirit(mouse_rect)
		if hovered_button != None:
			self.National_Spirits_Selection_Menu.hovered_national_spirit = hovered_button
			return hovered_button
		else:
			self.National_Spirits_Selection_Menu.hovered_national_spirit = hovered_button
	
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

class Country_Selection_Menu:
	def __init__(self, screen_width, screen_height, pygame, 
		generic_hover_over_button_sound, generic_click_menu_sound, country_selection_background, political_compass_image, 
		ideologies_CRT_overlay_effect, hovered_start_game_button, hovered_select_national_spirit_button_image, hovered_select_country_button_image, 
		hovered_laws_button_image, generic_leader, CRT_flag_overlay_effect, blocked_select_national_spirit_button, blocked_select_country_button, blocked_start_game_button, 
		blocked_full_right_side, blocked_all_laws, progressbar, progressbar_vertical, progressbar_small, progressbar_huge):
		
		self.national_spirits_display_rects = []
		self.hovered_national_spirit = None
		self.last_hovered_national_spirit = None

		self.selected_country = None

		self.selected_selectable_national_spirits = []

		self.mouse_pos = [0, 0]
		
		self.hovered_ideology_rect = None
		self.last_hovered_ideology = None
		
		self.hovered_button = 'none'
		self.last_hovered_button ='none'
		
		self.is_flag_selection_menu_open = False
		self.selected_flag_image = None
		self.flag_size = None

		self.is_flag_national_spirits_selection_menu_open = False
		
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
		self.hovered_laws_button_image = pygame.transform.smoothscale_by(hovered_laws_button_image, (self.factor_x, self.factor_y))

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
		self.country_flag_position = (1209 * self.factor_x, 89 * self.factor_y)

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

		select_flag_style_button_width = 362 * self.factor_x
		select_flag_style_button_height = 70 * self.factor_y
		self.select_flag_style_button_x_offset = 1059 * self.factor_x
		self.select_flag_style_button_y_offset = 248 * self.factor_y		
		self.select_flag_style_button = GenericUtilitys.Button(self.select_flag_style_button_x_offset, self.select_flag_style_button_y_offset, select_flag_style_button_width, select_flag_style_button_height)					
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
		self.economic_law_button_x_offset = 1269 * self.factor_x
		
		self.economic_law_button_1 = GenericUtilitys.Button(self.economic_law_button_x_offset, self.second_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.economic_law_button_2 = GenericUtilitys.Button(self.economic_law_button_x_offset, self.second_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.economic_law_button_3 = GenericUtilitys.Button(self.economic_law_button_x_offset, self.second_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.economic_law_button_4 = GenericUtilitys.Button(self.economic_law_button_x_offset, self.second_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.economic_law_button_5 = GenericUtilitys.Button(self.economic_law_button_x_offset, self.second_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.economic_law_button_6 = GenericUtilitys.Button(self.economic_law_button_x_offset, self.second_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.economic_law_button_7 = GenericUtilitys.Button(self.economic_law_button_x_offset, self.second_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.economic_law_button_8 = GenericUtilitys.Button(self.economic_law_button_x_offset, self.second_row_law_button_y_offset_8, law_button_width, law_button_height)
		self.economic_law_button_9 = GenericUtilitys.Button(self.economic_law_button_x_offset, self.second_row_law_button_y_offset_9, law_button_width, law_button_height)				
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
		elif self.select_flag_style_button.rect.colliderect(mouse_rect) and self.clicked_ideology != None:
			return 'select_country'				
		elif self.selected_country != None:
			
			for number in range(9):
				button = getattr(self, f'political_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					return f'political_law_button_{str(number+1)}'
			
			for number in range(8):
				button = getattr(self, f'military_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					return f'military_law_button_{str(number+1)}'	

			for number in range(9):
				button = getattr(self, f'economic_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					return f'economic_law_button_{str(number+1)}'
			
			for number in range(9):
				button = getattr(self, f'social_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					return f'social_law_button_{str(number+1)}'						

		return None

	def get_clicked_button(self, mouse_rect):
		if self.is_flag_selection_menu_open == False:
			clicked_button = self.get_button_by_interaction(mouse_rect)
			if clicked_button != None:
				self.hover_over_button_sound.fadeout(50)
				self.click_menu_sound.play()

				if clicked_button == 'select_country' and self.is_flag_national_spirits_selection_menu_open == False:
					self.is_flag_selection_menu_open = True

				if clicked_button == 'select_national_spirit' and self.is_flag_selection_menu_open == False:
					self.is_flag_national_spirits_selection_menu_open = not self.is_flag_national_spirits_selection_menu_open

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
				if self.hovered_button != self.last_hovered_button:
					self.hover_over_button_sound.play()
					self.last_hovered_button = self.hovered_button
			else:
				self.last_hovered_button = self.hovered_button

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

			return self.hovered_button
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
			if self.flag_size == None:
				self.selected_flag_image = pygame.transform.scale(self.selected_country.country_flag_image, (208, 126))
				self.selected_flag_image = pygame.transform.smoothscale_by(self.selected_flag_image, (self.factor_x, self.factor_y))
				self.flag_size = self.selected_flag_image.get_size()
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
					button = getattr(self, f'economic_law_button_{str(number+1)}', None)
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
				
				self.hovering_diplomatic_information_rect = False
				self.hovering_military_information_rect = False
				self.hovering_economic_information_rect = False
				self.hovering_domestic_information_rect = False	


				if self.hovering_internal_and_external_market_approval_rating_rect == True:
					pygame.draw.rect(screen, (255,255,255), self.internal_and_external_market_approval_rating_rect, 3)
					hovering_internal_and_external_market_approval_rating_rect = self.small_scalable_font.render(f"INTERNAL MARKET APPROVAL RATING:  {self.selected_country.internal_economy_rating}%\n\nEXTERNAL MARKET APPROVAL RATING:  {self.selected_country.external_economy_rating}%", True, (255, 255, 255))
					text_position = (mouse_rect[0]+20 * self.factor_x, mouse_rect[1] + 10)	
					
					pygame.draw.rect(screen, (6,15,20), (text_position[0]-5 * self.factor_x, text_position[1], hovering_internal_and_external_market_approval_rating_rect.get_width()+24 * self.factor_x, hovering_internal_and_external_market_approval_rating_rect.get_height()+10 * self.factor_y))
					pygame.draw.rect(screen, (43,219,211), (text_position[0]-5 * self.factor_x, text_position[1], hovering_internal_and_external_market_approval_rating_rect.get_width()+24 * self.factor_x, hovering_internal_and_external_market_approval_rating_rect.get_height()+10 * self.factor_y), 2)				
					
					screen.blit(hovering_internal_and_external_market_approval_rating_rect, (text_position[0], text_position[1]+6 * self.factor_y))	
				self.hovering_internal_and_external_market_approval_rating_rect = False


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


				self.hovering_military_approval_rating_rect = False
				self.hovering_domestic_approval_rating_rect = False
				self.hovering_midia_approval_rating_rect = False
				self.hovering_secret_service_approval_rating_rect = False
				self.hovering_politics_approval_rating_rect = False	


		if self.clicked_ideology == None: # Blocked Buttons
			screen.blit(self.blocked_select_country_button, (self.select_flag_style_button_x_offset, self.select_flag_style_button_y_offset))
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

		if self.hovered_button != None: # Buttons Selection 
			
			if self.hovered_button == 'start_game':
				screen.blit(self.hovered_start_game_button, (self.start_game_button_x_offset, self.start_game_button_y_offset))
			
			elif self.hovered_button == 'select_national_spirit':
				screen.blit(self.hovered_select_national_spirit_button_image, (self.select_national_spirit_button_x_offset, self.select_national_spirit_button_y_offset))
			
			elif self.hovered_button == 'select_country':
				screen.blit(self.hovered_select_country_button_image, (self.select_flag_style_button_x_offset, self.select_flag_style_button_y_offset))				

			else:
				button = getattr(self, self.hovered_button, None)
				if button:
					screen.blit(self.hovered_laws_button_image, (button.rect[:2]))
		
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
		self.selected_country_name = None

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
					pygame.draw.rect(screen, (255,40,30), rect[0], 4)
					
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
	def __init__(self, screen_width, screen_height, national_spirits_background, selectable_national_spirits_list, hover_over_button_sound, click_sound, political_compass_image) -> None:
		self.screen_width = screen_width
		self.screen_height = screen_height
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y	

		self.political_compass_image = political_compass_image
		political_compass_image_rect = self.political_compass_image.get_rect()
		political_compass_image_rect[0] += 15 * self.factor_x
		political_compass_image_rect[1] += 31 * self.factor_y
		self.background_position = [political_compass_image_rect[0]*0.65, political_compass_image_rect[1]*0.95]

		self.national_spirits_background = national_spirits_background
		
		self.selectable_national_spirits_list = selectable_national_spirits_list
		self.selectable_national_spirits_rects = []
		
		self.selected_country = None

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
		else:
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


class Game_Screen:
	def __init__(self, screen_width, screen_height, pygame, generic_hover_over_button_sound, generic_click_button_sound, top_bar_right_background, top_bar_game_speed_indicator,
			top_bar_defcon_level, top_bar_left_background, top_bar_flag_overlay, top_bar_flag_overlay_hovering_over, country_overview, popularity_circle_overlay, earth_daymap, earth_nightmap, 
			progressbar, progressbar_vertical, progressbar_small):

		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y
		self.factor = self.factor_x * self.factor_y
		
		self.generic_hover_over_button_sound, self.generic_click_button_sound = generic_hover_over_button_sound, generic_click_button_sound

		self.last_hovered_button = None
		self.is_top_bar_country_viewer_open = False	


		self.Country_Overview = Country_Overview(self.factor_x, self.factor_y, pygame, top_bar_left_background, top_bar_flag_overlay, top_bar_flag_overlay_hovering_over,
			country_overview, popularity_circle_overlay, generic_hover_over_button_sound, progressbar, progressbar_vertical, progressbar_small)
		
		self.Clock_UI = Clock_UI(self.factor_x, self.factor_y, screen_width, screen_height, pygame, top_bar_right_background, top_bar_game_speed_indicator, top_bar_defcon_level)

		self.Earth_Map = Earth_Map(self.factor_x, self.factor_y, screen_width, screen_height, earth_daymap, earth_nightmap, self.Clock_UI)
	
	def get_button_by_interaction(self, mouse_rect):
		button = self.Country_Overview.get_button_by_interaction(mouse_rect)
		return button

	def get_clicked_button(self, mouse_rect):
		clicked_button = self.get_button_by_interaction(mouse_rect)
		
		if clicked_button != None:
			if clicked_button == "country_viewer":
				self.is_top_bar_country_viewer_open = not self.is_top_bar_country_viewer_open
				self.Country_Overview.is_top_bar_country_viewer_open = not self.Country_Overview.is_top_bar_country_viewer_open
			self.generic_hover_over_button_sound.fadeout(100)
			self.generic_click_button_sound.play()
			return clicked_button	

	def get_hovered_button(self, mouse_rect):
		hovered_button = self.get_button_by_interaction(mouse_rect)
		if hovered_button != None:
			if self.last_hovered_button != hovered_button:
				self.generic_hover_over_button_sound.play()
				if hovered_button == "country_viewer":
					self.Country_Overview.highlight_country_viewer_button = True
			self.last_hovered_button = hovered_button
			return hovered_button
		else:
			self.Country_Overview.highlight_country_viewer_button = False
			self.last_hovered_button = None
			self.generic_hover_over_button_sound.fadeout(100)	

	def draw(self, screen, mouse_rect):
		self.Earth_Map.draw(screen)		
		self.Country_Overview.draw(screen, mouse_rect)
		self.Clock_UI.draw(screen)


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

		self.highlight_country_viewer_button = False
		self.is_top_bar_country_viewer_open = False

		self.country_overview = pygame.transform.smoothscale_by(country_overview, (self.factor_x, self.factor_y))
		self.popularity_circle_overlay = pygame.transform.smoothscale_by(popularity_circle_overlay, (self.factor_x, self.factor_y))
		self.country_overview_position = (0, 159 * self.factor_y)
		self.national_spirits_display_rects = []
		self.hovered_national_spirit = None	
		self.last_hovered_national_spirit = None	

		self.last_hovered_button = None

		self.hovered_rect = None
		self.last_hovered_rect = None

		self.generic_hover_over_button_sound = generic_hover_over_button_sound

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

		# INFORMATION ------------#

		# UI BUTTONS ------------#
		self.hovered_top_bar_UI_button = None

		height = 112 * self.factor_y
		button_size = (57 * self.factor_x, 41 * self.factor_y)

		self.top_bar_decisions_button = 		GenericUtilitys.Button(129 * self.factor_x, height, button_size[0], button_size[1])
		self.top_bar_laws_button = 				GenericUtilitys.Button(188 * self.factor_x, height, button_size[0], button_size[1])
		self.top_bar_finances_button = 			GenericUtilitys.Button(247 * self.factor_x, height, button_size[0], button_size[1])
		self.top_bar_inteligence_button = 		GenericUtilitys.Button(306 * self.factor_x, height, button_size[0], button_size[1])
		self.top_bar_research_button = 			GenericUtilitys.Button(365 * self.factor_x, height, button_size[0], button_size[1])
		self.top_bar_global_market_button = 	GenericUtilitys.Button(424 * self.factor_x, height, button_size[0], button_size[1])
		self.top_bar_construction_button = 		GenericUtilitys.Button(483 * self.factor_x, height, button_size[0], button_size[1])
		self.top_bar_production_button = 		GenericUtilitys.Button(542 * self.factor_x, height, button_size[0], button_size[1])
		self.top_bar_army_button = 				GenericUtilitys.Button(601 * self.factor_x, height, button_size[0], button_size[1])
		self.top_bar_stockpile_button = 		GenericUtilitys.Button(660 * self.factor_x, height, button_size[0], button_size[1])


		self.huge_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(24 * self.factor_y))
		self.big_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(21 * self.factor_y))
		self.medium_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))	
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(13 * self.factor_y))	

	def get_button_by_interaction(self, mouse_rect):
		self.hovered_top_bar_UI_button = None
		if self.top_bar_left_background_rect.colliderect(mouse_rect):		
			if self.top_bar_country_viewer_button.rect.colliderect(mouse_rect):
				return "country_viewer"	
			
			elif self.top_bar_decisions_button.rect.colliderect(mouse_rect):
				self.hovered_top_bar_UI_button = "decisions_button"
				return "decisions_button"	
			elif self.top_bar_laws_button.rect.colliderect(mouse_rect):
				self.hovered_top_bar_UI_button = "laws_button"
				return "laws_button"	
			elif self.top_bar_finances_button.rect.colliderect(mouse_rect):
				self.hovered_top_bar_UI_button = "finances_button"
				return "finances_button"	
			elif self.top_bar_inteligence_button.rect.colliderect(mouse_rect):
				self.hovered_top_bar_UI_button = "inteligence_button"
				return "inteligence_button"	
			elif self.top_bar_research_button.rect.colliderect(mouse_rect):
				self.hovered_top_bar_UI_button = "research_button"
				return "research_button"	
			elif self.top_bar_global_market_button.rect.colliderect(mouse_rect):
				self.hovered_top_bar_UI_button = "global_market_button"
				return "global_market_button"	
			elif self.top_bar_construction_button.rect.colliderect(mouse_rect):
				self.hovered_top_bar_UI_button = "construction_button"
				return "construction_button"	
			elif self.top_bar_production_button.rect.colliderect(mouse_rect):
				self.hovered_top_bar_UI_button = "production_button"
				return "production_button"	
			elif self.top_bar_army_button.rect.colliderect(mouse_rect):
				self.hovered_top_bar_UI_button = "army_button"
				return "army_button"	
			elif self.top_bar_stockpile_button.rect.colliderect(mouse_rect):
				self.hovered_top_bar_UI_button = "stockpile_button"
				return "stockpile_button"	

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


		if self.is_top_bar_country_viewer_open == True:
			self.is_touching_cicle_rects = False
			if mouse_rect[1] - self.country_overview_position[1] > 308 * self.factor_y and mouse_rect[1] - self.country_overview_position[1] < 475 * self.factor_y:
				if  mouse_rect[0] > 60 * self.factor_x and  mouse_rect[0] < 227 * self.factor_x:
					for index, rect in enumerate(self.politics_cicle_rects):
						if GenericUtilitys.polygon_intersects_rectangle(rect, mouse_rect):
							self.hitted_rect = [index, 'politics']
							self.is_touching_cicle_rects = True
							break
				elif  mouse_rect[0] > 350 * self.factor_x and  mouse_rect[0] < 517 * self.factor_x:
					for index, rect in enumerate(self.culture_cicle_rects):
						if GenericUtilitys.polygon_intersects_rectangle(rect, mouse_rect):
							self.hitted_rect = [index, 'culture']
							self.is_touching_cicle_rects = True
							break	
				elif  mouse_rect[0] > 637 * self.factor_x and  mouse_rect[0] < 804 * self.factor_x:			
					for index, rect in enumerate(self.religion_cicle_rects):
						if GenericUtilitys.polygon_intersects_rectangle(rect, mouse_rect):
							self.hitted_rect = [index, 'religion']
							self.is_touching_cicle_rects = True
							break							

		else:
			self.is_touching_politics_cicle_rects = False
			self.is_touching_culture_cicle_rects = False
			self.is_touching_religion_cicle_rects = False

		for rect, national_spirit in self.national_spirits_display_rects:
			if rect.colliderect(mouse_rect):
				self.hovered_national_spirit = national_spirit
				if national_spirit != self.last_hovered_national_spirit:
					self.last_hovered_national_spirit = national_spirit
					self.generic_hover_over_button_sound.play()
				return national_spirit
		self.last_hovered_national_spirit = None
		self.hovered_national_spirit = None	

	def draw(self, screen, mouse_rect):
		screen.blit(self.top_bar_left_background, (0 * self.factor_x, 0 * self.factor_y))
		if self.PlayerCountry.country_flag_image.get_size() != self.top_bar_flag_overlay.get_size():
			self.PlayerCountry.country_flag_image = self.pygame.transform.smoothscale(self.PlayerCountry.country_flag_image, (115 * self.factor_x, 66 * self.factor_y))
		screen.blit(self.PlayerCountry.country_flag_image, (6 * self.factor_x, 6 * self.factor_y))

		if self.highlight_country_viewer_button == False and self.is_top_bar_country_viewer_open == False:
			screen.blit(self.top_bar_flag_overlay, (2 * self.factor_x, 2 * self.factor_y))
		else:
			screen.blit(self.top_bar_flag_overlay_hovering_over, (2 * self.factor_x, 2 * self.factor_y))

		if self.hovered_top_bar_UI_button != None:
			if self.hovered_top_bar_UI_button == "decisions_button":
				pygame.draw.rect(screen, (255,255,255), self.top_bar_decisions_button.rect, 2)
			elif self.hovered_top_bar_UI_button == "laws_button":
				pygame.draw.rect(screen, (255,255,255), self.top_bar_laws_button.rect, 2)
			elif self.hovered_top_bar_UI_button == "finances_button":
				pygame.draw.rect(screen, (255,255,255), self.top_bar_finances_button.rect, 2)
			elif self.hovered_top_bar_UI_button == "inteligence_button":
				pygame.draw.rect(screen, (255,255,255), self.top_bar_inteligence_button.rect, 2)
			elif self.hovered_top_bar_UI_button == "research_button":
				pygame.draw.rect(screen, (255,255,255), self.top_bar_research_button.rect, 2)
			elif self.hovered_top_bar_UI_button == "global_market_button":
				pygame.draw.rect(screen, (255,255,255), self.top_bar_global_market_button.rect, 2)
			elif self.hovered_top_bar_UI_button == "construction_button":
				pygame.draw.rect(screen, (255,255,255), self.top_bar_construction_button.rect, 2)
			elif self.hovered_top_bar_UI_button == "production_button":
				pygame.draw.rect(screen, (255,255,255), self.top_bar_production_button.rect, 2)
			elif self.hovered_top_bar_UI_button == "army_button":
				pygame.draw.rect(screen, (255,255,255), self.top_bar_army_button.rect, 2)
			elif self.hovered_top_bar_UI_button == "stockpile_button":																																				
				pygame.draw.rect(screen, (255,255,255), self.top_bar_stockpile_button.rect, 2)

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
			formatted_GDP = f"GDP:  ${GDP:,.3f}"
		elif abs(GDP) < 1e9:
			formatted_GDP = f"GDP:  ${GDP / 1e6:.3f} M"
		elif abs(GDP) < 1e12:
			formatted_GDP = f"GDP:  ${GDP / 1e9:.3f} B"
		elif abs(GDP) < 1e15:
			formatted_GDP = f"GDP:  ${GDP / 1e12:.3f} T"
		else:
			formatted_GDP = f"GDP:  ${GDP:.3f}"
			
		text_country_GDP = self.small_scalable_font.render(formatted_GDP, True, (255, 255, 255))
		text_country_GDP_position = (718 * self.factor_x, self.info_height)	
		screen.blit(text_country_GDP, text_country_GDP_position)	


		## INCOME
		income = self.PlayerCountry.income
		if abs(income) < 1e6:
			formatted_money = f"INCO:  ${income:,.3f}"
		elif abs(income) < 1e9:
			formatted_money = f"INCO:  ${income / 1e6:.3f} M"
		elif abs(income) < 1e12:
			formatted_money = f"INCO:  ${income / 1e9:.3f} B"
		elif abs(income) < 1e15:
			formatted_money = f"INCO:  ${income / 1e12:.3f} T"
		else:
			formatted_money = f"INCO:  ${income:.3f}"
		
		text_income = self.small_scalable_font.render(formatted_money, True, (255, 255, 255))
		text_income_position = (748 * self.factor_x, 40 * self.factor_y)	
		screen.blit(text_income, text_income_position)

		## EXPENSES
		expenses = self.PlayerCountry.expenses
		if abs(expenses) < 1e6:
			formatted_money = f"EXPE:  ${expenses:,.3f}"
		elif abs(expenses) < 1e9:
			formatted_money = f"EXPE:  ${expenses / 1e6:.3f} M"
		elif abs(expenses) < 1e12:
			formatted_money = f"EXPE:  ${expenses / 1e9:.3f} B"
		elif abs(expenses) < 1e15:
			formatted_money = f"EXPE:  ${expenses / 1e12:.3f} T"
		else:
			formatted_money = f"EXPE:  ${expenses:.3f}"
		
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
		# COUNTRY VIWER

		if self.is_top_bar_country_viewer_open == True:
			screen.blit(self.PlayerCountry.country_leader_image, (12 * self.factor_x, 27 * self.factor_y + self.country_overview_position[1]))
			screen.blit(self.country_overview, self.country_overview_position)

			screen.blit(self.PlayerCountry.country_capital_image, (160 * self.factor_x, 90 * self.factor_y + self.country_overview_position[1]))
			screen.blit(self.country_overview, self.country_overview_position)			

			# COUNTRY NAME
			country_name_text = self.big_scalable_font.render(self.PlayerCountry.country_name, True, (255, 255, 255))
			text_position = (165 * self.factor_x, 39 * self.factor_y + self.country_overview_position[1])	
			screen.blit(country_name_text, text_position)

			# LEADER NAME
			leader_name_text = self.huge_scalable_font.render(self.PlayerCountry.country_leader_name, True, (255, 255, 255))
			if leader_name_text.get_width() > 350:
				leader_name_text = self.big_scalable_font.render(self.PlayerCountry.country_leader_name, True, (255, 255, 255))
			
			text_position = (24 * self.factor_x, 226 * self.factor_y + self.country_overview_position[1])	
			screen.blit(leader_name_text, text_position)

			# GOVERNMENT
			government_name_text = self.huge_scalable_font.render(self.PlayerCountry.country_government, True, (255, 255, 255))
			text_position = (12 * self.factor_x, 512 * self.factor_y + self.country_overview_position[1])	
			
			if government_name_text.get_width() > 250:
				government_name_text = self.big_scalable_font.render(self.PlayerCountry.country_government, True, (255, 255, 255))	
				text_position = (12 * self.factor_x, 512 * self.factor_y + self.country_overview_position[1])
				if government_name_text.get_width() > 250:	
					government_name_text = self.medium_scalable_font.render(self.PlayerCountry.country_government, True, (255, 255, 255))	
					text_position = (12 * self.factor_x, 512 * self.factor_y + self.country_overview_position[1])					

			screen.blit(government_name_text, text_position)	

			# RULING PARTY
			ruling_party_name_text = self.huge_scalable_font.render(self.PlayerCountry.country_ruling_party, True, (255, 255, 255))
			text_position = (299 * self.factor_x, 512 * self.factor_y + self.country_overview_position[1])	

			if ruling_party_name_text.get_width() > 250:
				ruling_party_name_text = self.big_scalable_font.render(self.PlayerCountry.country_ruling_party, True, (255, 255, 255))	
				text_position = (299 * self.factor_x, 512 * self.factor_y + self.country_overview_position[1])
				if ruling_party_name_text.get_width() > 250:
					ruling_party_name_text = self.medium_scalable_font.render(self.PlayerCountry.country_ruling_party, True, (255, 255, 255))	
					text_position = (299 * self.factor_x, 512 * self.factor_y + self.country_overview_position[1])										

			screen.blit(ruling_party_name_text, text_position)

			# ELECTIONS
			elections_text = self.huge_scalable_font.render(self.PlayerCountry.country_elections, True, (255, 255, 255))
			text_position = (586 * self.factor_x, 512 * self.factor_y + self.country_overview_position[1])	
			screen.blit(elections_text, text_position)	


			#-----------------------------------------------------------------------------------------------------------------------------------------------------#
			# POPULARITY CIRCLES

			# POLITICS
			chart_position = (143 * self.factor_x, 391 * self.factor_y + self.country_overview_position[1]) 
			chart_radius = 80 * self.factor_y

			self.politics_cicle_rects = GenericUtilitys.draw_pie_chart(screen, chart_position, chart_radius, self.politics_popularity, self.politics_segment_colors)	

			screen.blit(self.popularity_circle_overlay, (chart_position[0]-85 * self.factor_x, chart_position[1]-85 * self.factor_y))

			# CULTURE
			chart_position = (433 * self.factor_x, 391 * self.factor_y + self.country_overview_position[1]) 
			chart_radius = 80 * self.factor_y

			rects_info = GenericUtilitys.draw_pie_chart(screen, chart_position, chart_radius, self.culture_popularity, self.culture_segment_colors)		
			self.culture_cicle_rects = rects_info

			screen.blit(self.popularity_circle_overlay, (chart_position[0]-85 * self.factor_x, chart_position[1]-85 * self.factor_y))			

			# RELIGION
			chart_position = (720 * self.factor_x, 391 * self.factor_y + self.country_overview_position[1]) 
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

		# country_viewer_open
		else:
			pass	
class Clock_UI:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, pygame, top_bar_right_background, top_bar_game_speed_indicator, top_bar_defcon_level):

		self.factor_x, self.factor_y = factor_x, factor_y	
		self.screen_width = screen_width 
		self.screen_height = screen_height

		self.pygame = pygame

		self.top_bar_right_background = pygame.transform.smoothscale_by(top_bar_right_background, (self.factor_x, self.factor_y))
		self.top_bar_game_speed_indicator = pygame.transform.smoothscale_by(top_bar_game_speed_indicator, (self.factor_x, self.factor_y))
		self.top_bar_defcon_level = pygame.transform.smoothscale_by(top_bar_defcon_level, (self.factor_x, self.factor_y))	


		self.game_speed = 1	
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
			self.current_minute = 0
			if self.current_hour >= 24:
				self.current_hour = self.current_hour - 24
				self.current_day += 1
				if self.current_day == self.days_in_each_mounth[str(self.current_month)] + 1:
					self.current_day = 1
					self.current_month += 1
					if self.current_month == 13:
						self.current_month = 1
						self.current_year += 1

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
class Earth_Map:
	def __init__(self, factor_x, factor_y, screen_width, screen_height, earth_daymap, earth_nightmap, Clock_UI):
		self.factor_x = factor_x
		self.factor_y = factor_y

		self.last_zoom_factor = 1
		self.zoom_factor = 1

		self.screen_width = screen_width
		self.screen_height = screen_height

		self.Clock_UI = Clock_UI

		self.source_earth_daymap = earth_daymap
		self.source_earth_nightmap = earth_nightmap

		self.earth_daymap = earth_daymap.copy()
		self.earth_nightmap = earth_nightmap.copy()

		self.night_strips = self.calculate_night_strips(interval_minutes = 1)

		self.screen_sized_map_surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
		self._8k_sized_map_surface = pygame.Surface((self.source_earth_daymap.get_width(), self.source_earth_nightmap.get_height()), pygame.SRCALPHA)	

		self.time_zone = 6.1 # 6.1 == Greenwich

		self.map_position = [0, 0]
		self.offset_y = 0

	def calculate_night_strips(self, interval_minutes):
		night_strips = {}

		for minute in range(0, 1440, interval_minutes):
			longitude_start, longitude_end = self.calculate_night_longitude_range(minute)
			night_strips[minute] = [(longitude_start, longitude_end)]

			# Check if the night strip crosses the right edge
			if longitude_end > 360:
				night_strips[minute].append((0, longitude_end - 360))

		return night_strips

	def calculate_night_longitude_range(self, minute):
		# Calculate longitude range based on the minute of the day
		longitude_start = (minute / 1440) * 360
		longitude_end = ((minute + 720) / 1440) * 360
		return longitude_start, longitude_end

	def scale_map(self, zoom_factor_change, fps_freezing_avoidance, zoom_type):
		if fps_freezing_avoidance > 10:
			self.zoom_factor += zoom_factor_change
			if self.zoom_factor < 0.25:
				self.zoom_factor = 0.25
			if self.zoom_factor > 1:
				self.zoom_factor = 1

			if self.last_zoom_factor != self.zoom_factor:


				self.earth_daymap = pygame.transform.scale_by(self.source_earth_daymap, (self.zoom_factor))
				self.earth_nightmap = pygame.transform.scale_by(self.source_earth_nightmap, (self.zoom_factor))
				
				# DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER
				# DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER DO LATER

				if zoom_type == 'zoom_out':
					pass
				if zoom_type == 'zoom_in':
					pass

			self.last_zoom_factor = self.zoom_factor	

	def draw(self, screen):
		self.screen_sized_map_surface.fill((0, 0, 0, 0), (0, 0, self.screen_width, self.screen_height))
		self._8k_sized_map_surface.fill((0, 0, 0, 0), (0, 0, self.screen_width, self.screen_height))

		# HEIGHT
		self.offset_y = abs(self.map_position[1]) if abs(self.map_position[1]) <  self.earth_daymap.get_height() else self.earth_daymap.get_height() - 1
		#--------------#
				

		# DAYMAP		
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
		#--------------#
		
		self._8k_sized_map_surface.blit(self.screen_sized_map_surface, (0, 0))


		current_minute = (1440 - (self.Clock_UI.current_hour * 60 + self.Clock_UI.current_minute)) + self.time_zone * 60
		if current_minute >= 1440:
			current_minute -= 1440

		closest_key = min(self.night_strips.keys(), key=lambda x: abs(x - current_minute))
		current_night_strips = self.night_strips[closest_key]

		for start, end in current_night_strips:
			x_start = int((start / 360) * self.earth_nightmap.get_width())
			x_end = int((end / 360) * self.earth_nightmap.get_width())

			# Blit night map for the current night strips
			columns_to_copy = min(x_end - x_start, self.earth_nightmap.get_width() - x_start)
			if self.map_position[0] > 0:
				height = self.screen_height if self.screen_height + self.offset_y <= self.earth_nightmap.get_height() else self.earth_nightmap.get_height() - self.offset_y

				self._8k_sized_map_surface.blit(self.earth_nightmap.subsurface((x_start, self.offset_y, columns_to_copy, height)), (x_start + abs(self.map_position[0]), 0))
				if x_start + columns_to_copy + abs(self.map_position[0]) > self.earth_nightmap.get_width():
					difference = (x_start + columns_to_copy + abs(self.map_position[0])) - self.earth_nightmap.get_width()
					self._8k_sized_map_surface.blit(self.earth_nightmap.subsurface((x_start, self.offset_y, columns_to_copy, height)), (-columns_to_copy + difference, 0))
			else:
				height = self.screen_height if self.screen_height + self.offset_y <= self.earth_nightmap.get_height() else self.earth_nightmap.get_height() - self.offset_y

				self._8k_sized_map_surface.blit(self.earth_nightmap.subsurface((x_start, self.offset_y, columns_to_copy, height)), (x_start - abs(self.map_position[0]), 0))
				self._8k_sized_map_surface.blit(self.earth_nightmap.subsurface((x_start, self.offset_y, columns_to_copy, height)), (self.earth_nightmap.get_width() - abs(self.map_position[0]) + x_start, 0))
		
		screen.blit(self._8k_sized_map_surface, (0, 0))






