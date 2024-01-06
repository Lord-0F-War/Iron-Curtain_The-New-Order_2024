from PIL import Image
from numpy import array as numpy_array
import GenericUtilitys
from PygameManager import pygame

from pyvidplayer import Video



class ESC_Menu:
	def __init__(self, screen_width, screen_height, ESC_menu_background, generic_hover_over_button_menu_sound, generic_click_menu_sound, 
			  hovered_green_button_menu_image, hovered_red_button_menu_image, Options_Menu) -> None:
		
		self.Options_Menu = Options_Menu 

		self.hovered_green_button_menu_image, self.hovered_red_button_menu_image =  hovered_green_button_menu_image, hovered_red_button_menu_image
		self.hover_over_button_sound, self.click_menu_sound = generic_hover_over_button_menu_sound, generic_click_menu_sound
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
	def __init__(self, screen_width, screen_height, options_menu_background, generic_hover_over_button_menu_sound, generic_click_menu_sound, 
			  hovered_green_button_menu_image, hovered_red_button_menu_image, Sounds_Manager, Main_Menu) -> None:
		
		self.Sounds_Manager = Sounds_Manager
		self.Main_Menu = Main_Menu

		self.hover_over_button_sound, self.click_menu_sound = generic_hover_over_button_menu_sound, generic_click_menu_sound
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

		self.Main_Menu.vid.set_volume(self.sound_slider.value/100)		


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

		self.Main_Menu.vid.set_volume(self.sound_slider.value/100)

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
		self.new_game_menu_background_middle_y = (screen_height/2 - new_game_menu_background_height/2)		
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
		
		self.menu_gui_middle_x = (screen_width/1.35 - menu_gui_width/2)
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
		new_game_button_y_offset = 101 * self.factor_y
		self.new_game_button = GenericUtilitys.Button(self.new_game_menu_background_middle_x + new_game_button_x_offset, self.new_game_menu_background_middle_y + new_game_button_y_offset, new_game_button_width, new_game_button_height)

		load_save_button_width = 371 * self.factor_x
		load_save_button_height = 34 * self.factor_y
		load_save_button_x_offset = 59 * self.factor_x
		load_save_button_y_offset = 152 * self.factor_y
		self.load_save_button = GenericUtilitys.Button(self.new_game_menu_background_middle_x + load_save_button_x_offset, self.new_game_menu_background_middle_y + load_save_button_y_offset, load_save_button_width, load_save_button_height)

		back_button_width = 371 * self.factor_x
		back_button_height = 34 * self.factor_y
		back_button_x_offset = 59 * self.factor_x
		back_button_y_offset = 465 * self.factor_y
		self.back_button = GenericUtilitys.Button(self.new_game_menu_background_middle_x + back_button_x_offset, self.new_game_menu_background_middle_y + back_button_y_offset, back_button_width, back_button_height)

		self.vid = Video("Know Your History.mp4", size=(936* self.factor_x, 374* self.factor_y))
		self.vid.set_volume(0)


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

		screen.blit(self.game_logo, (70 * self.factor_x, 0))	
		
		if self.is_in_new_game_menu == False:
			self.vid.draw(screen, (self.menu_gui_middle_x + 2 * self.factor_x, self.menu_gui_middle_y + 2 * self.factor_y))

			if self.vid.frames >= 1674:
				self.vid.restart()	

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
					screen.blit(self.hovered_green_button_menu_image, self.back_button.rect)										
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

		self.hovered = False
		self.hover_over_button_sound = hover_over_button_sound

		self.click_menu_sound = generic_click_menu_sound


	def get_button_by_interaction(self, mouse_rect):
		if self.start_button.rect.colliderect(mouse_rect):
			return 'start'
		elif self.back_button.rect.colliderect(mouse_rect):
			return 'back'
		else:
			return 'none'


	def get_clicked_button(self, mouse_rect):
		clicked_button = self.get_button_by_interaction(mouse_rect)
		if clicked_button != 'none':
			self.hover_over_button_sound.fadeout(150)
			self.click_menu_sound.play()
		return clicked_button


	def get_hovered_button(self, mouse_rect):
		hovered_button = self.get_button_by_interaction(mouse_rect)
		if self.hovered == False and self.hovered_button != 'none' or (self.hovered_button != self.last_hovered_button and self.hovered_button != 'none'):
			self.hover_over_button_sound.play()
			self.hovered = True	
			self.last_hovered_button = self.hovered_button		
		return hovered_button


	def draw(self, screen):
		screen.blit(self.menu_gui, (self.menu_gui_middle_x, self.menu_gui_middle_y))

		screen.blit(self.python_logo, (0, self.screen_height - self.python_logo.get_height()))		

		screen.blit(self.game_logo, (70 * self.factor_x, 0))

		if self.hovered_button != 'none':
			if self.hovered_button == 'start':
				screen.blit(self.hovered_select_scenario_button_menu_image, self.start_button.rect)
			if self.hovered_button == 'back':
				screen.blit(self.hovered_back_button_menu_image, self.back_button.rect)
		else:
			self.hover_over_button_sound.fadeout(200)	

			self.hovered = False		


class Country_Selection_Menu:
	def __init__(self, Country_Selection_Flag_Selection_Menu, Country_Selection_National_Spirits_Selection_Menu, screen_width, screen_height, pygame, 
	      
		  generic_hover_over_button_menu_sound, generic_click_menu_sound, country_selection_background, country_info_display_background, political_compass_image, 
		  
		  ideologies_CRT_overlay_effect, hovered_start_game_button, hovered_select_national_spirit_button_image, hovered_select_country_button_image, 
		  
		  hovered_laws_button_image, generic_leader, CRT_flag_overlay_effect, blocked_select_national_spirit_button, blocked_select_country_button, blocked_start_game_button, 
		  
		  blocked_full_right_side, blocked_all_laws):
		
		self.national_spirits_display_rects = []
		self.hovered_national_spirit = None
		self.last_hovered_national_spirit = None

		self.selected_selectable_national_spirits = []

		self.mouse_pos = [0, 0]
		
		self.hovered_ideology_rect = None
		self.last_overed_ideology = 'none'
		
		self.hovered_button = 'none'
		self.last_hovered_button ='none'
		
		self.Country_Selection_Flag_Selection_Menu = Country_Selection_Flag_Selection_Menu
		self.is_flag_selection_menu_open = False
		self.selected_flag_image = None
		self.flag_size = None

		self.Country_Selection_National_Spirits_Selection_Menu = Country_Selection_National_Spirits_Selection_Menu
		self.is_flag_national_spirits_selection_menu_open = False
		
		self.screen_width = screen_width 
		self.screen_height = screen_height
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y
		self.factor = self.factor_x * self.factor_y

		self.pygame = pygame

		self.country_selection_background = pygame.transform.smoothscale_by(country_selection_background, (self.factor_x, self.factor_y))
		self.political_compass_image = pygame.transform.smoothscale_by(political_compass_image, (self.factor_x, self.factor_y))
		self.ideologies_CRT_overlay_effect = pygame.transform.smoothscale_by(ideologies_CRT_overlay_effect, (self.factor_x, self.factor_y))
		self.CRT_flag_overlay_effect = pygame.transform.smoothscale_by(CRT_flag_overlay_effect, (self.factor_x, self.factor_y))

		self.country_info_display_background = pygame.transform.smoothscale_by(country_info_display_background, (self.factor_x, self.factor_y))
		self.Country_Selection_Flag_Selection_Menu.country_info_display_background = self.country_info_display_background

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
		self.Country_Selection_National_Spirits_Selection_Menu.background_position = [political_compass_image_rect[0]*0.65, political_compass_image_rect[1]*0.95]

		self.leader_portrait_position = (1053 * self.factor_x, 25 * self.factor_y)
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
		law_button_width = 210 * self.factor_x
		law_button_height = 29 * self.factor_y		


		### FIRST ROW
		self.first_row_law_button_y_offset_1 = 430 * self.factor_y
		self.first_row_law_button_y_offset_2 = 463 * self.factor_y		
		self.first_row_law_button_y_offset_3 = 495 * self.factor_y	
		self.first_row_law_button_y_offset_4 = 528 * self.factor_y	
		self.first_row_law_button_y_offset_5 = 560 * self.factor_y
		self.first_row_law_button_y_offset_6 = 592 * self.factor_y
		self.first_row_law_button_y_offset_7 = 623 * self.factor_y	
		self.first_row_law_button_y_offset_8 = 656 * self.factor_y
		self.first_row_law_button_y_offset_9 = 690 * self.factor_y	
		
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
		self.military_law_button_x_offset = 1700 * self.factor_x

		self.military_law_button_1 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.military_law_button_2 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.military_law_button_3 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.military_law_button_4 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.military_law_button_5 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.military_law_button_6 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.military_law_button_7 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.military_law_button_8 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_8, law_button_width, law_button_height)
		self.military_law_button_9 = GenericUtilitys.Button(self.military_law_button_x_offset, self.first_row_law_button_y_offset_9, law_button_width, law_button_height)			
		##
		###

		### SECOND ROW
		self.second_row_law_button_y_offset_1 = 781 * self.factor_y
		self.second_row_law_button_y_offset_2 = 813 * self.factor_y		
		self.second_row_law_button_y_offset_3 = 846 * self.factor_y	
		self.second_row_law_button_y_offset_4 = 878 * self.factor_y	
		self.second_row_law_button_y_offset_5 = 911 * self.factor_y
		self.second_row_law_button_y_offset_6 = 943 * self.factor_y
		self.second_row_law_button_y_offset_7 = 976 * self.factor_y	
		self.second_row_law_button_y_offset_8 = 1008 * self.factor_y
		self.second_row_law_button_y_offset_9 = 1041 * self.factor_y	
		
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
		self.social_law_button_x_offset = 1700 * self.factor_x

		self.social_law_button_1 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_1, law_button_width, law_button_height)
		self.social_law_button_2 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_2, law_button_width, law_button_height)
		self.social_law_button_3 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_3, law_button_width, law_button_height)
		self.social_law_button_4 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_4, law_button_width, law_button_height)
		self.social_law_button_5 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_5, law_button_width, law_button_height)
		self.social_law_button_6 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_6, law_button_width, law_button_height)
		self.social_law_button_7 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_7, law_button_width, law_button_height)
		self.social_law_button_8 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_8, law_button_width, law_button_height)
		self.social_law_button_9 = GenericUtilitys.Button(self.social_law_button_x_offset, self.second_row_law_button_y_offset_9, law_button_width, law_button_height)			
		##		
		####

		self.hovered = False
		self.hover_over_button_sound = generic_hover_over_button_menu_sound

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


	def get_button_by_interaction(self, mouse_rect):
		if self.start_game_button.rect.colliderect(mouse_rect) and self.selected_flag_image != None:
			return 'start_game'
		elif self.select_national_spirit_button.rect.colliderect(mouse_rect) and self.selected_flag_image != None:
			return 'select_national_spirit'
		elif self.select_flag_style_button.rect.colliderect(mouse_rect) and self.clicked_ideology != None:
			return 'select_flag/style'				
		elif self.selected_flag_image != None:
			
			for number in range(9):
				button = getattr(self, f'political_law_button_{str(number+1)}', None)
				if button.rect.colliderect(mouse_rect):
					return f'political_law_button_{str(number+1)}'
			
			for number in range(9):
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
			

			return 'none'


	def get_clicked_button(self, mouse_rect):
		if self.is_flag_selection_menu_open == False:
			clicked_button = self.get_button_by_interaction(mouse_rect)
			if clicked_button != 'none' and clicked_button != None:
				self.hover_over_button_sound.fadeout(50)
				self.click_menu_sound.play()

				if clicked_button == 'select_flag/style' and self.is_flag_national_spirits_selection_menu_open == False:
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
					self.selected_flag_image = None
					self.Country_Selection_Flag_Selection_Menu.selected_leader_image = self.generic_leader_image
					self.Country_Selection_Flag_Selection_Menu.selected_country_name = None

					self.hover_over_button_sound.fadeout(50)
					self.click_menu_sound.play()					
					return self.clicked_ideology

	
	def get_hovered_button(self, mouse_rect):
		if self.is_flag_selection_menu_open == False:
			hovered_button = self.get_button_by_interaction(mouse_rect)
			if self.hovered == False and self.hovered_button != 'none' or (self.hovered_button != self.last_hovered_button and self.hovered_button != 'none'):
				self.hover_over_button_sound.play()
				self.hovered = True	
				self.last_hovered_button = self.hovered_button
			return hovered_button
	def get_hovered_ideology_rect(self, mouse_rect):
		if self.is_flag_selection_menu_open == False:
			for ideology, rect in self.ideology_rects.items():
				rect = pygame.Rect(rect[0]*self.factor_x + 15 * self.factor_x, rect[1]*self.factor_y + 31 * self.factor_y, rect[2]*self.factor_x, rect[3]*self.factor_y)
				if rect.colliderect(mouse_rect) and ideology != self.last_overed_ideology:
					self.last_overed_ideology = ideology
					self.hover_over_button_sound.play()
					return rect
				elif rect.colliderect(mouse_rect):
					return rect

			self.hovered_ideology_rect = None
	def get_hovered_national_spirit(self, mouse_rect):
		if self.is_flag_selection_menu_open == False:
			for rect, national_spirit in self.national_spirits_display_rects:
				if rect.colliderect(mouse_rect) and national_spirit != self.last_hovered_national_spirit:
					self.last_hovered_national_spirit = national_spirit
					self.hover_over_button_sound.play()
					return national_spirit
				elif rect.colliderect(mouse_rect):
					return national_spirit
			self.last_hovered_national_spirit = None


	def music_player(self):
		if pygame.mixer.music.get_busy() == False and self.selected_flag_image != None:
			self.main_menu_music_started = True
			pygame.mixer.music.load(self.Country_Selection_Flag_Selection_Menu.selected_country.country_music_playlist[0])
			pygame.mixer.music.play()
		

	def draw(self, screen):
		self.Country_Selection_National_Spirits_Selection_Menu.selected_country = self.Country_Selection_Flag_Selection_Menu.selected_country

		screen.blit(self.political_compass_image, (15 * self.factor_x, 31 * self.factor_y))
		
		# Leader Portrait
		if self.Country_Selection_Flag_Selection_Menu.selected_country != None and self.is_flag_selection_menu_open == False and self.selected_flag_image != None:
			self.selected_leader_image = self.Country_Selection_Flag_Selection_Menu.selected_country.country_leader_image
			screen.blit(self.selected_leader_image, self.leader_portrait_position)
		else:
			screen.blit(self.generic_leader_image, self.leader_portrait_position)
		
		# Flag
		if self.selected_flag_image != None:
			if self.flag_size == None:
				self.selected_flag_image = pygame.transform.scale(self.selected_flag_image, (208, 126))
				self.selected_flag_image = pygame.transform.smoothscale_by(self.selected_flag_image, (self.factor_x, self.factor_y))
				self.flag_size = self.selected_flag_image.get_size()
			screen.blit(self.selected_flag_image, self.country_flag_position)	
			screen.blit(self.CRT_flag_overlay_effect, self.country_flag_position)	
		
		# BEHIND BACKGROUND
		screen.blit(self.country_selection_background, (0, 0))
		# IN FRONT OF BACKGROUND

		# Country Name | Leader Name | National Spirits
		if self.is_flag_selection_menu_open == False and self.selected_flag_image != None:
			if  self.Country_Selection_Flag_Selection_Menu.selected_country != None:
				country_name_text = self.medium_scalable_font.render(self.Country_Selection_Flag_Selection_Menu.selected_country.country_name, True, (255, 255, 255))
				screen.blit(country_name_text, self.country_name_position)	

				leader_name = self.Country_Selection_Flag_Selection_Menu.selected_country.country_leader_name
				leader_name_text = self.big_scalable_font.render(leader_name, True, (255, 255, 255))

				if leader_name_text.get_width() > 350 * self.factor_x:
					leader_name_text = self.medium_scalable_font.render(leader_name, True, (255, 255, 255))
				
				screen.blit(leader_name_text, self.leader_name_position)

				self.national_spirits_display_rects = []
				x_index = 0
				y_index = 0
	
				if len(self.Country_Selection_Flag_Selection_Menu.selected_country.country_national_spirits) > 10:
					for national_spirit in self.Country_Selection_Flag_Selection_Menu.selected_country.country_national_spirits:
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
					for national_spirit in self.Country_Selection_Flag_Selection_Menu.selected_country.country_national_spirits:	
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
				culture_national_spirit = self.Country_Selection_Flag_Selection_Menu.selected_country.country_culture
				screen.blit(culture_national_spirit.national_spirit_icon, (1840 * self.factor_x, 104 * self.factor_y))
				
				culture_national_spirit.rect = self.pygame.Rect(1840 * self.factor_x, 104 * self.factor_y,
						culture_national_spirit.national_spirit_icon.get_width(), culture_national_spirit.national_spirit_icon.get_height())					
				
				self.national_spirits_display_rects.append([culture_national_spirit.rect, culture_national_spirit])						
				
				# RELIGION	
				religion_national_spirit = self.Country_Selection_Flag_Selection_Menu.selected_country.country_religion
				screen.blit(religion_national_spirit.national_spirit_icon, (1840 * self.factor_x, 105 * self.factor_y + religion_national_spirit.national_spirit_icon.get_height()))
				
				religion_national_spirit.rect = self.pygame.Rect(1840 * self.factor_x, 105 * self.factor_y + religion_national_spirit.national_spirit_icon.get_height(),
						religion_national_spirit.national_spirit_icon.get_width(), religion_national_spirit.national_spirit_icon.get_height())					
				
				self.national_spirits_display_rects.append([religion_national_spirit.rect, religion_national_spirit])						
										

			if self.hovered_national_spirit != None:
				pygame.draw.rect(screen, (255,255,255), self.hovered_national_spirit.rect, 2)

				national_spirit_description_text = self.small_scalable_font.render(self.hovered_national_spirit.national_spirit_description, True, (255, 255, 255))
				text_position = (1435 * self.factor_x, 280 * self.factor_y)

				pygame.draw.rect(screen, (6,15,20), (1430 * self.factor_x, 275 * self.factor_y, 485 * self.factor_x, national_spirit_description_text.get_height() + 10 * self.factor_y))
				pygame.draw.rect(screen, (43,219,211), (1430 * self.factor_x, 275 * self.factor_y, 485 * self.factor_x, national_spirit_description_text.get_height() + 10 * self.factor_y), 2)

				screen.blit(national_spirit_description_text, text_position)							

		if self.clicked_ideology == None: # Blocked Buttons
			screen.blit(self.blocked_select_country_button, (self.select_flag_style_button_x_offset, self.select_flag_style_button_y_offset))
			screen.blit(self.blocked_select_national_spirit_button, (self.select_national_spirit_button_x_offset, self.select_national_spirit_button_y_offset))
			screen.blit(self.blocked_start_game_button, (self.start_game_button_x_offset, self.start_game_button_y_offset))				
			screen.blit(self.blocked_full_right_side, (self.screen_width - self.blocked_full_right_side.get_width(), 0))		
		elif self.selected_flag_image == None:
			screen.blit(self.blocked_select_national_spirit_button, (self.select_national_spirit_button_x_offset, self.select_national_spirit_button_y_offset))
			screen.blit(self.blocked_start_game_button, (self.start_game_button_x_offset, self.start_game_button_y_offset))
			screen.blit(self.blocked_all_laws, (self.screen_width - self.blocked_all_laws.get_width(), self.screen_height - self.blocked_all_laws.get_height()))
			self.national_spirits_display_rects = []
				
		if self.clicked_ideology_rect != None:
			pygame.draw.rect(screen, (255,255,255), self.clicked_ideology_rect, 5)

		if self.hovered_ideology_rect != None:
			pygame.draw.rect(screen, (255,255,255), self.hovered_ideology_rect, 2)
			self.Country_Selection_Flag_Selection_Menu.draw_flag_selection_preview(screen, self.last_overed_ideology, self.mouse_pos)	

		screen.blit(self.ideologies_CRT_overlay_effect, (15 * self.factor_x, 31 * self.factor_y))			
			
		if self.is_flag_selection_menu_open == True: # Draw Flag Selection Menu
			self.Country_Selection_Flag_Selection_Menu.draw(screen, self.clicked_ideology)	

		if self.hovered_button != 'none': # Buttons Selection 
			
			if self.hovered_button == 'start_game':
				screen.blit(self.hovered_start_game_button, (self.start_game_button_x_offset, self.start_game_button_y_offset))
			
			elif self.hovered_button == 'select_national_spirit':
				screen.blit(self.hovered_select_national_spirit_button_image, (self.select_national_spirit_button_x_offset, self.select_national_spirit_button_y_offset))
			
			elif self.hovered_button == 'select_flag/style':
				screen.blit(self.hovered_select_country_button_image, (self.select_flag_style_button_x_offset, self.select_flag_style_button_y_offset))				

			else:
				for number in range(9):
					if self.hovered_button == f'political_law_button_{str(number+1)}':
						button = getattr(self, f'political_law_button_{str(number+1)}', None)
						screen.blit(self.hovered_laws_button_image, (button.rect[:2]))
				
				for number in range(9):
					if self.hovered_button == f'military_law_button_{str(number+1)}':
						button = getattr(self, f'military_law_button_{str(number+1)}', None)
						screen.blit(self.hovered_laws_button_image, (button.rect[:2]))	
				
				for number in range(9):
					if self.hovered_button == f'economic_law_button_{str(number+1)}':
						button = getattr(self, f'economic_law_button_{str(number+1)}', None)
						screen.blit(self.hovered_laws_button_image, (button.rect[:2]))
				
				for number in range(9):
					if self.hovered_button == f'social_law_button_{str(number+1)}':
						button = getattr(self, f'social_law_button_{str(number+1)}', None)
						screen.blit(self.hovered_laws_button_image, (button.rect[:2]))															
		else: # Fade Audio
			self.hover_over_button_sound.fadeout(200)	
			self.hovered = False	

		if self.is_flag_national_spirits_selection_menu_open == True:
			self.Country_Selection_National_Spirits_Selection_Menu.draw(screen)


class Country_Selection_Flag_Selection_Menu:
	def __init__(self, screen_width, screen_height, countries, generic_hover_over_button_menu_sound, generic_click_menu_sound) -> None:
		self.countries = countries

		self.selected_country = None

		
		self.screen_width = screen_width
		self.screen_height = screen_height
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y		

		self.mouse_rect = None

		self.flag_rects = []

		self.country_info_display_background = None

		self.last_selected_country_name = None
		self.selected_country_name = None

		self.normal_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(30 * self.factor_y))
		self.small_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(18 * self.factor_y))		
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(14 * self.factor_y))


		self.hover_over_button_sound, self.click_sound = generic_hover_over_button_menu_sound, generic_click_menu_sound


	def get_clicked_flag(self, mouse_rect):
		self.hover_over_button_sound.fadeout(50)
		self.click_sound.play()		
		for rect in self.flag_rects:
			if rect[0].colliderect(mouse_rect):
				self.selected_country = rect[3]
				return rect[1]
		else:
			return None			


	def draw(self, screen, selected_ideology):
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
				if rect[0].colliderect(self.mouse_rect) and self.country_info_display_background != None:
					pygame.draw.rect(screen, (255,40,30), rect[0], 4)
					
					self.selected_country_name = countries_with_selected_ideology[rect[2]].country_name
					country_name_text = self.normal_scalable_font.render(self.selected_country_name, True, (255, 255, 255))
					if country_name_text.get_width() > 300 * self.factor_x:
						country_name_text = self.small_scalable_font.render(self.selected_country_name, True, (255, 255, 255))
					if country_name_text.get_width() > 300 * self.factor_x:
						country_name_text = self.tiny_scalable_font.render(self.selected_country_name, True, (255, 255, 255))						

					text_position = (self.screen_width/2 - country_name_text.get_width()/1.95, self.screen_height - self.country_info_display_background.get_height() + self.country_info_display_background.get_height() * 0.079 - country_name_text.get_height() /2)
					screen.blit(country_name_text, text_position)

					country_info_display_background_position = [self.screen_width/2 - self.country_info_display_background.get_width()/2, self.screen_height - self.country_info_display_background.get_height() * 1.05]

					# LEADER
					leader_name = countries_with_selected_ideology[rect[2]].country_leader_name
					leader_name_text = self.small_scalable_font.render(leader_name, True, (255, 255, 255))
					if leader_name_text.get_width() > 265 * self.factor_x:
						leader_name_text = self.tiny_scalable_font.render(leader_name, True, (255, 255, 255))

					text_position = (66 * self.factor_x + country_info_display_background_position[0], 77 * self.factor_y + country_info_display_background_position[1])
					screen.blit(leader_name_text, text_position)

					# RUILING PARTY
					ruling_party_name = countries_with_selected_ideology[rect[2]].country_ruling_party
					ruling_party_name_text = self.small_scalable_font.render(ruling_party_name, True, (255, 255, 255))
					if ruling_party_name_text.get_width() > 265 * self.factor_x:
						ruling_party_name_text = self.tiny_scalable_font.render(ruling_party_name, True, (255, 255, 255))
					
					text_position = (66 * self.factor_x + country_info_display_background_position[0], 143 * self.factor_y + country_info_display_background_position[1])
					screen.blit(ruling_party_name_text, text_position)		

					# GOVERNMENT
					government_name_text = countries_with_selected_ideology[rect[2]].country_government
					government_name_text = self.small_scalable_font.render(government_name_text, True, (255, 255, 255))
					if government_name_text.get_width() > 265 * self.factor_x:
						government_name_text = self.tiny_scalable_font.render(government_name_text, True, (255, 255, 255))
					
					text_position = (66 * self.factor_x + country_info_display_background_position[0], 209 * self.factor_y + country_info_display_background_position[1])
					screen.blit(government_name_text, text_position)		

					# ELECTIONS
					elections_name = countries_with_selected_ideology[rect[2]].country_elections
					elections_name_text = self.small_scalable_font.render(elections_name, True, (255, 255, 255))
					if elections_name_text.get_width() > 265 * self.factor_x:
						elections_name_text = self.tiny_scalable_font.render(elections_name, True, (255, 255, 255))
					
					text_position = (165 * self.factor_x + country_info_display_background_position[0], 252 * self.factor_y + country_info_display_background_position[1])
					screen.blit(elections_name_text, text_position)															

					# BRIEF HISTORY
					brief_history_name = countries_with_selected_ideology[rect[2]].country_brief_history
					brief_history_name_text = self.tiny_scalable_font.render(brief_history_name, True, (255, 255, 255))
					
					text_position = (920 * self.factor_x + country_info_display_background_position[0], 65 * self.factor_y + country_info_display_background_position[1])
					screen.blit(brief_history_name_text, text_position)		


					screen.blit(countries_with_selected_ideology[rect[2]].country_leader_image, (self.country_info_display_background.get_width() * 0.2421 + self.screen_width/2 - self.country_info_display_background.get_width()/2, self.screen_height - self.country_info_display_background.get_height() * 1.05 + self.country_info_display_background.get_height() * 0.1516))					

					self.selected_leader_image = countries_with_selected_ideology[rect[2]].country_leader_image

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


class Country_Selection_National_Spirits_Selection_Menu:
	def __init__(self, screen_width, screen_height, national_spirits_background, selectable_national_spirits_list, hover_over_button_sound, click_sound) -> None:
		self.screen_width = screen_width
		self.screen_height = screen_height
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = screen_width / reference_screen_size_x
		self.factor_y = screen_height / reference_screen_size_y	

		self.background_position = None
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
		self.tiny_scalable_font = GenericUtilitys.ScalableFont('Aldrich.ttf', int(16 * self.factor_y))		

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
			national_spirit_description_text = self.tiny_scalable_font.render(self.hovered_national_spirit.national_spirit_description, True, (255, 255, 255))
			text_position = (534 * self.factor_x, 132 * self.factor_y)

			pygame.draw.rect(screen, (6,15,20), (525 * self.factor_x, 125 * self.factor_y, 495 * self.factor_x, national_spirit_description_text.get_height() + 10 * self.factor_y))
			pygame.draw.rect(screen, (43,219,211), (525 * self.factor_x, 125 * self.factor_y, 495 * self.factor_x, national_spirit_description_text.get_height() + 10 * self.factor_y), 2)

			screen.blit(national_spirit_description_text, text_position)

