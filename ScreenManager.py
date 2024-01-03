
import GenericUtilitys

class Screen:
	def __init__(self, pygame, display, screen, surface_alfa, Main_Menu, Country_Selection_Menu, Scenario_Selection_Menu, ESC_Menu, main_menu_backgound, python_logo):
		
		self.pygame = pygame
		
		self.display = display
		self.screen = screen
		self.surface_alfa = surface_alfa


		self.screen_width, self.screen_height = self.screen.get_size()	
		reference_screen_size_x = 1920
		reference_screen_size_y = 1080
		self.factor_x = self.screen_width / reference_screen_size_x
		self.factor_y = self.screen_height / reference_screen_size_y		
		self.screen_rect = pygame.Rect([0, 0, self.screen_width, self.screen_height])		

		self.UI_point_of_view_by_team_id = 2

		self.ESC_Menu = ESC_Menu
		##
		self.Main_Menu = Main_Menu
		self.main_menu_backgound = main_menu_backgound
		##

		
		self.Scenario_Selection_Menu = Scenario_Selection_Menu


		##
		self.Country_Selection_Menu = Country_Selection_Menu
		##

		self.loading_screen_index = 0

		##	

		self.python_logo = python_logo
		self.python_logo = pygame.transform.smoothscale_by(self.python_logo, (self.factor_x,self. factor_y))		

		self.loading_status_font = GenericUtilitys.ScalableFont('menu.ttf', 25)
		self.loading_screen_index = 0
		##


		self.brightness_surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
	

	def render_main_menu(self, brightness_value, is_options_menu_open):
		self.screen.fill((0, 0, 0))
		self.surface_alfa.fill((0, 0, 0, 0))
		self.brightness_surface.fill((0, 0, 0, 0))

		self.screen.blit(self.main_menu_backgound, (0, 0))

		self.Main_Menu.draw(self.screen)	

		if is_options_menu_open == True:
			self.ESC_Menu.Options_Menu.draw(self.surface_alfa)		

		self.screen.blit(self.surface_alfa, (0, 0))	

		self.pygame.draw.rect(self.brightness_surface, (255, 255, 255, brightness_value), ((0, 0), (self.screen_width, self.screen_height)))		
		self.screen.blit(self.brightness_surface, (0, 0))

		self.display.blit(self.screen, (0, 0))

		self.pygame.display.update(self.screen_rect)	

	
	def render_select_scenario_menu(self, brightness_value, is_in_esc_menu, is_options_menu_open):
		self.screen.fill((0, 0, 0))
		self.surface_alfa.fill((0, 0, 0, 0))

		self.screen.blit(self.main_menu_backgound, (0, 0))

		self.Scenario_Selection_Menu.draw(self.screen)

		if is_in_esc_menu == True:
			self.ESC_Menu.draw(self.surface_alfa, is_options_menu_open)	

		self.screen.blit(self.surface_alfa, (0, 0))	

		self.pygame.draw.rect(self.brightness_surface, (255, 255, 255, brightness_value), ((0, 0), (self.screen_width, self.screen_height)))		
		self.screen.blit(self.brightness_surface, (0, 0))			

		self.display.blit(self.screen, (0, 0))

		self.pygame.display.update(self.screen_rect)		


	def render_country_selection_menu(self, brightness_value, is_in_esc_menu, is_options_menu_open):
		self.screen.fill((0, 0, 0))
		self.surface_alfa.fill((0, 0, 0, 0))

		self.Country_Selection_Menu.draw(self.surface_alfa)

		if is_in_esc_menu == True:
			self.ESC_Menu.draw(self.surface_alfa, is_options_menu_open)

		self.screen.blit(self.surface_alfa, (0, 0))	

		self.pygame.draw.rect(self.brightness_surface, (255, 255, 255, brightness_value), ((0, 0), (self.screen_width, self.screen_height)))		
		self.screen.blit(self.brightness_surface, (0, 0))		

		self.display.blit(self.screen, (0, 0))

		self.pygame.display.update(self.screen_rect)

