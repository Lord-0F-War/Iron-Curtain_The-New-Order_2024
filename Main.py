import sys
import os
from json import load as json_load, dump as json_dump
import pandas as pd


exe_folder = os.path.dirname(sys.argv[0])

with open(f'{exe_folder}\settings.txt', 'r') as file:
	configs = json_load(file)
	screen_width = configs["screen_width"]
	screen_height = configs["screen_height"]

import PygameManager
Pygame_Manager = PygameManager.Pygame(screen_width, screen_height)
pygame = Pygame_Manager.start_pygame()
clock, QUIT, date_tick, FPS_update, key_delay, display, screen, surface_alfa = Pygame_Manager.config_pygame()

import ScreenManager
import SoundsManager
import GenericUtilitys
import MenuManager
import CountriesManager


class Main:
	def __init__(self, screen_width, screen_height, Pygame_Manager, pygame, clock, QUIT, date_tick, FPS_update, key_delay, display, screen, surface_alfa) -> None:
		
		self.screen_width, self.screen_height = screen_width, screen_height
		self.Pygame_Manager = Pygame_Manager
		self.pygame = pygame
		self.clock, self.QUIT, self.date_tick, self.FPS_update, self.key_delay, self.display, self.screen, self.surface_alfa = clock, QUIT, date_tick, FPS_update, key_delay, display, screen, surface_alfa

		self.countries = []

		self.mouse_start_pos = (0,0)
		self.mouse_end_pos = (0,0)
		self.last_difference_x = 0
		self.last_difference_y = 0

		self.exe_folder = os.path.dirname(sys.argv[0])
		
		self.leaders_image_dic = {}
		self.capitals_images_dic = {}		
		self.flags_image_dic = {}
		
		self.national_spirits_image_dic = {}
		self.national_focus_image_dic = {}

		self.researche_icons_image_dic = {}
		self.researche_institute_icons_image_dic = {}

		self.intelligency_agencies_icons_image_dic = {}
		
		self.decision_icons_image_dic = {}
		self.decision_on_tree_menu_icons_dic = {}
		
		self.music_files_dic = {}
		self.load_assets()
		self.create_countries_default_frame()
		self.create_national_spirits()
		self.create_classes()
		self.setup_variables()

		self.counties_data = pd.DataFrame(self.read_counties_data_from_file(location = os.path.join(os.path.join(self.map_folder, 'counties'), 'USA_counties')))

		self.pygame.event.clear()
		self.main_loop()

	def load_leaders_images(self, leaders_folder):
		for folder_name in os.listdir(leaders_folder):
			folder_path = os.path.join(leaders_folder, folder_name)
			if os.path.isdir(folder_path):
				for filename in os.listdir(folder_path):
					if filename.endswith(".png") or filename.endswith(".jpg"):
						image_path = os.path.join(folder_path, filename)
						image_name = os.path.splitext(filename)[0]
						self.leaders_image_dic[image_name] = self.pygame.image.load(image_path).convert()
						self.leaders_image_dic[image_name] = self.pygame.transform.smoothscale_by(self.leaders_image_dic[image_name], (self.factor_x, self.factor_y))
	def load_capitals_images(self, flags_folder):	
		if os.path.isdir(flags_folder):
			for filename in os.listdir(flags_folder):
				if filename.endswith(".png") or filename.endswith(".jpg"):
					image_path = os.path.join(flags_folder, filename)
					image_name = os.path.splitext(filename)[0]
					self.capitals_images_dic[image_name] = self.pygame.image.load(image_path).convert()
					self.capitals_images_dic[image_name] = self.pygame.transform.smoothscale_by(self.capitals_images_dic[image_name], (self.factor_x, self.factor_y))		
	def load_flags_images(self, flags_folder):	
		if os.path.isdir(flags_folder):
			for filename in os.listdir(flags_folder):
				if filename.endswith(".png") or filename.endswith(".jpg"):
					image_path = os.path.join(flags_folder, filename)
					image_name = os.path.splitext(filename)[0]
					self.flags_image_dic[image_name] = self.pygame.image.load(image_path).convert()
					self.flags_image_dic[image_name] = self.pygame.transform.smoothscale_by(self.flags_image_dic[image_name], (self.factor_x, self.factor_y))	
	
	def load_decision_icons(self, decision_icons_folder):
		for folder_name in os.listdir(decision_icons_folder):
			folder_path = os.path.join(decision_icons_folder, folder_name)		
			if os.path.isdir(folder_path):
				for filename in os.listdir(folder_path):
					if filename.endswith(".png") or filename.endswith(".jpg"):
						image_path = os.path.join(folder_path, filename)
						image_name = os.path.splitext(filename)[0]
						self.decision_icons_image_dic[image_name] = self.pygame.image.load(image_path).convert_alpha()
						self.decision_icons_image_dic[image_name] = self.pygame.transform.smoothscale_by(self.decision_icons_image_dic[image_name], (self.factor_x, self.factor_y))		
	def load_decision_on_tree_menu_icon(self, decision_on_tree_menu_icon_folder):
		for folder_name in os.listdir(decision_on_tree_menu_icon_folder):
			folder_path = os.path.join(decision_on_tree_menu_icon_folder, folder_name)		
			if os.path.isdir(folder_path):
				for filename in os.listdir(folder_path):
					if filename.endswith(".png") or filename.endswith(".jpg"):
						image_path = os.path.join(folder_path, filename)
						image_name = os.path.splitext(filename)[0]
						self.decision_on_tree_menu_icons_dic[image_name] = self.pygame.image.load(image_path).convert_alpha()
						self.decision_on_tree_menu_icons_dic[image_name] = self.pygame.transform.smoothscale_by(self.decision_on_tree_menu_icons_dic[image_name], (self.factor_x, self.factor_y))	
	
	def load_national_spirits(self, national_spirits_folder):
		for folder_name in os.listdir(national_spirits_folder):
			folder_path = os.path.join(national_spirits_folder, folder_name)		
			if os.path.isdir(folder_path):
				for filename in os.listdir(folder_path):
					if filename.endswith(".png") or filename.endswith(".jpg"):
						image_path = os.path.join(folder_path, filename)
						image_name = os.path.splitext(filename)[0]
						self.national_spirits_image_dic[image_name] = self.pygame.image.load(image_path).convert_alpha()
						self.national_spirits_image_dic[image_name] = self.pygame.transform.smoothscale_by(self.national_spirits_image_dic[image_name], (self.factor_x, self.factor_y))		
	def load_national_focus(self, national_focus_folder):
		for folder_name in os.listdir(national_focus_folder):
			folder_path = os.path.join(national_focus_folder, folder_name)		
			if os.path.isdir(folder_path):
				for filename in os.listdir(folder_path):
					if filename.endswith(".png") or filename.endswith(".jpg"):
						image_path = os.path.join(folder_path, filename)
						image_name = os.path.splitext(filename)[0]
						self.national_focus_image_dic[image_name] = self.pygame.image.load(image_path).convert_alpha()
						self.national_focus_image_dic[image_name] = self.pygame.transform.smoothscale_by(self.national_focus_image_dic[image_name], (self.factor_x, self.factor_y))			
	
	def load_researche_icons(self, researche_icons_folder):
		for folder_name in os.listdir(researche_icons_folder):
			folder_path = os.path.join(researche_icons_folder, folder_name)		
			if os.path.isdir(folder_path):
				for filename in os.listdir(folder_path):
					if filename.endswith(".png") or filename.endswith(".jpg"):
						image_path = os.path.join(folder_path, filename)
						image_name = os.path.splitext(filename)[0]
						self.researche_icons_image_dic[image_name] = self.pygame.image.load(image_path).convert_alpha()
						self.researche_icons_image_dic[image_name] = self.pygame.transform.smoothscale_by(self.researche_icons_image_dic[image_name], (self.factor_x, self.factor_y))
	def load_researche_institute_icons(self, researche_institute_icons_folder):
		for folder_name in os.listdir(researche_institute_icons_folder):
			folder_path = os.path.join(researche_institute_icons_folder, folder_name)		
			if os.path.isdir(folder_path):
				for filename in os.listdir(folder_path):
					if filename.endswith(".png") or filename.endswith(".jpg"):
						image_path = os.path.join(folder_path, filename)
						image_name = os.path.splitext(filename)[0]
						self.researche_institute_icons_image_dic[image_name] = self.pygame.image.load(image_path).convert_alpha()
						self.researche_institute_icons_image_dic[image_name] = self.pygame.transform.smoothscale_by(self.researche_institute_icons_image_dic[image_name], (self.factor_x, self.factor_y))						

	def load_intelligency_agencies_icons(self, intelligency_agencies_icons_folder):
		for folder_name in os.listdir(intelligency_agencies_icons_folder):
			folder_path = os.path.join(intelligency_agencies_icons_folder, folder_name)		
			if os.path.isdir(folder_path):
				for filename in os.listdir(folder_path):
					if filename.endswith(".png") or filename.endswith(".jpg"):
						image_path = os.path.join(folder_path, filename)
						image_name = os.path.splitext(filename)[0]
						self.intelligency_agencies_icons_image_dic[image_name] = self.pygame.image.load(image_path).convert_alpha()
						self.intelligency_agencies_icons_image_dic[image_name] = self.pygame.transform.smoothscale_by(self.intelligency_agencies_icons_image_dic[image_name], (self.factor_x, self.factor_y))

	def load_music_files(self, musics_folder):	
		for folder_name in os.listdir(musics_folder):
			folder_path = os.path.join(musics_folder, folder_name)
			if os.path.isdir(folder_path):
				for filename in os.listdir(folder_path):
					if filename.endswith(".wav") or filename.endswith(".ogg") or filename.endswith(".mp3"):
						music_path = os.path.join(folder_path, filename)
						image_name = os.path.splitext(filename)[0]
						self.music_files_dic[image_name] = music_path						
	
	def load_assets(self):
		self.reference_screen_size_x = 1920
		self.reference_screen_size_y = 1080
		self.factor_x = screen_width / self.reference_screen_size_x
		self.factor_y = screen_height / self.reference_screen_size_y
		self.factor = self.factor_x * self.factor_y

		self.map_folder = os.path.join(self.exe_folder, 'map')

		self.map_counties_color 					= self.pygame.image.load(os.path.join(self.map_folder, 'counties_color.png')).convert_alpha()

		self.earth_daymap 						= self.pygame.image.load(os.path.join(self.map_folder, 'earth_daymap.jpg')).convert_alpha()	
		self.earth_political_map 				= self.pygame.image.load(os.path.join(self.map_folder, 'earth_political_map.png')).convert_alpha()
		self.earth_political_map_filled 		= self.pygame.image.load(os.path.join(self.map_folder, 'earth_political_map_filled.png')).convert_alpha()


		self.gfx_folder = os.path.join(self.exe_folder, 'gfx')

		self.capitals_folder = os.path.join(self.gfx_folder, 'capitals')
		self.load_capitals_images(self.capitals_folder)

		self.flags_folder = os.path.join(self.gfx_folder, 'flags')
		self.load_flags_images(self.flags_folder)

		self.leaders_folder = os.path.join(self.gfx_folder, 'leaders')
		self.load_leaders_images(self.leaders_folder)
		self.generic_leader = self.leaders_image_dic['Portrait_NULL_Generic_Leader']

		self.interface_folder = os.path.join(self.gfx_folder, 'Interface')

		self.main_menu_backgound 				= self.pygame.image.load(os.path.join(self.interface_folder, 'main_menu.png')).convert_alpha()
		self.main_menu_backgound 				= self.pygame.transform.smoothscale(self.main_menu_backgound, (screen_width, screen_height))

		self.game_logo 							= self.pygame.image.load(os.path.join(self.interface_folder, 'game_logo.png')).convert_alpha()

		self.main_menu_UI 						= self.pygame.image.load(os.path.join(self.interface_folder, 'menu_UI.png')).convert_alpha()
		self.menu_options_UI 					= self.pygame.image.load(os.path.join(self.interface_folder, 'options_UI.png')).convert_alpha()
		self.hovered_green_button_menu_image 	= self.pygame.image.load(os.path.join(self.interface_folder, 'hovered_green_button_menu_image.png')).convert_alpha()
		self.hovered_red_button_menu_image 		= self.pygame.image.load(os.path.join(self.interface_folder, 'hovered_red_button_menu_image.png')).convert_alpha()

		self.python_logo 						= self.pygame.image.load(os.path.join(self.interface_folder, 'python_logo.png')).convert_alpha()
		self.python_logo 						= self.pygame.transform.smoothscale_by(self.python_logo, (self.factor_x, self.factor_y))

		self.ESC_menu_background 				= self.pygame.image.load(os.path.join(self.interface_folder, 'ESC_menu_background.png')).convert_alpha()
		self.ESC_menu_background 				= self.pygame.transform.smoothscale_by(self.ESC_menu_background, (self.factor_x, self.factor_y))

		self.new_game_menu_background 			= self.pygame.image.load(os.path.join(self.interface_folder, 'new_game_menu_background.png')).convert_alpha()
		self.new_game_menu_background 			= self.pygame.transform.smoothscale_by(self.new_game_menu_background, (self.factor_x, self.factor_y))		

		self.scenario_selection_folder = os.path.join(self.interface_folder, 'scenario_selection')

		self.scenario_selection_menu_gui 					= self.pygame.image.load(os.path.join(self.scenario_selection_folder, 'select_date_background.png')).convert_alpha()
		self.hovered_select_scenario_button_menu_image 		= self.pygame.image.load(os.path.join(self.scenario_selection_folder, 'hovered_select_scenario_button_menu.png')).convert_alpha()
		self.hovered_back_to_main_menu_button_menu_image 	= self.pygame.image.load(os.path.join(self.scenario_selection_folder, 'hovered_back_button_menu.png')).convert_alpha()

		
		self.country_selection_folder = os.path.join(self.interface_folder, 'country_selection')


		self.country_selection_background 					= self.pygame.image.load(os.path.join(self.country_selection_folder, 'country_selection_background.png')).convert_alpha()
		self.political_compass_image 						= self.pygame.image.load(os.path.join(self.country_selection_folder, 'political_compass.png')).convert_alpha()
		self.ideologies_CRT_overlay_effect 					= self.pygame.image.load(os.path.join(self.country_selection_folder, 'ideologies_CRT_overlay_effect.png')).convert_alpha()
		self.CRT_flag_overlay_effect 						= self.pygame.image.load(os.path.join(self.country_selection_folder, 'flag_overlay.png')).convert_alpha()

		self.country_info_display_background 				= self.pygame.image.load(os.path.join(self.country_selection_folder, 'country_info_display_background.png')).convert_alpha()
		self.national_spirits_background 					= self.pygame.image.load(os.path.join(self.country_selection_folder, 'national_spirits_background.png')).convert_alpha()
		self.national_spirits_background 					= pygame.transform.smoothscale_by(self.national_spirits_background, (self.factor_x, self.factor_y))

		self.hovered_start_game_button 						= self.pygame.image.load(os.path.join(self.country_selection_folder, 'hovered_start_game_button.png')).convert_alpha()
		self.hovered_select_country_button_image			= self.pygame.image.load(os.path.join(self.country_selection_folder, 'hovered_select_country_button.png')).convert_alpha()
		self.hovered_select_national_spirit_button_image 	= self.pygame.image.load(os.path.join(self.country_selection_folder, 'hovered_select_national_spirit_button.png')).convert_alpha()

		self.blocked_full_right_side 						= self.pygame.image.load(os.path.join(self.country_selection_folder, 'blocked_full_right_side.png')).convert_alpha()
		self.blocked_all_laws 								= self.pygame.image.load(os.path.join(self.country_selection_folder, 'blocked_all_laws.png')).convert_alpha()
		self.blocked_select_national_spirit_button 			= self.pygame.image.load(os.path.join(self.country_selection_folder, 'blocked_select_national_spirit_button.png')).convert_alpha()
		self.blocked_select_country_button 					= self.pygame.image.load(os.path.join(self.country_selection_folder, 'blocked_select_country_button.png')).convert_alpha()
		self.blocked_start_game_button 						= self.pygame.image.load(os.path.join(self.country_selection_folder, 'blocked_start_game_button.png')).convert_alpha()

		self.laws_description_image 						= self.pygame.image.load(os.path.join(self.country_selection_folder, 'laws_description_image.png')).convert_alpha()		


		self.selected_law_background = self.pygame.image.load(os.path.join(self.country_selection_folder, 'selected_law_background.png')).convert_alpha()


		self.game_HUD_folder = os.path.join(self.interface_folder, 'game_HUD')

		self.top_bar_right_background 				= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'top_bar_right_background.png')).convert_alpha()
		self.top_bar_game_speed_indicator 			= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'top_bar_game_speed_indicator.png')).convert_alpha()
		self.top_bar_defcon_levels 					= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'defcon_levels.png')).convert_alpha()		
		self.top_bar_left_background 				= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'top_bar_left_background.png')).convert_alpha()
		self.top_bar_flag_overlay 					= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'top_bar_flag_overlay.png')).convert_alpha()
		self.top_bar_flag_overlay_hovering_over 	= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'top_bar_flag_overlay_hovering_over.png')).convert_alpha()		
		self.country_overview 						= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'country_overview.png')).convert_alpha()	
		self.popularity_circle_overlay 				= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'popularity_circle_overlay.png')).convert_alpha()
		self.progressbar_huge 						= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'progressbar_huge.png')).convert_alpha()	
		self.progressbar 							= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'progressbar.png')).convert_alpha()	
		self.progressbar_vertical 					= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'progressbar_vertical.png')).convert_alpha()	
		self.progressbar_small 						= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'progressbar_small.png')).convert_alpha()	
		self.bottom_HUD 							= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'bottom_HUD.png')).convert_alpha()	
		
		self.country_laws_background 				= self.pygame.image.load(os.path.join(self.game_HUD_folder, 'country_laws_background.png')).convert_alpha()
		

		self.ideas_folder = os.path.join(self.interface_folder, 'ideas')
		
		self.national_spirits_folder = os.path.join(self.ideas_folder, 'national_spirits')
		self.load_national_spirits(self.national_spirits_folder)



		self.decisions_folder = os.path.join(self.interface_folder, 'decisions')

		self.decision_icons_folder = os.path.join(self.decisions_folder, 'decision_icons')
		self.load_decision_icons(self.decision_icons_folder)
		
		self.decision_on_tree_menu_icons_folder = os.path.join(self.decisions_folder, 'decision_on_tree_menu_icons')
		self.load_decision_on_tree_menu_icon(self.decision_on_tree_menu_icons_folder)



		self.national_focus_folder = os.path.join(self.interface_folder, 'national_focus')
		self.load_national_focus(self.national_focus_folder)


		self.top_bar_interface_folder = os.path.join(self.game_HUD_folder, 'top_bar_interface')


		self.economic_overview_folder = os.path.join(self.top_bar_interface_folder, 'economic_overview')
		self.economic_overview_background			= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'economic_overview_background.png')).convert_alpha()
		
		self.poverty_rate_0				= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'poverty_rate_0.png')).convert_alpha()
		self.poverty_rate_5				= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'poverty_rate_5.png')).convert_alpha()
		self.poverty_rate_10			= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'poverty_rate_10.png')).convert_alpha()
		self.poverty_rate_15			= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'poverty_rate_15.png')).convert_alpha()
		self.poverty_rate_25			= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'poverty_rate_25.png')).convert_alpha()
		self.poverty_rate_50			= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'poverty_rate_50.png')).convert_alpha()
		self.poverty_rate_80			= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'poverty_rate_80.png')).convert_alpha()

		self.credit_ratings				= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'credit_ratings.png')).convert_alpha()
		self.economic_warning			= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'economic_warning.png')).convert_alpha()

		self.economic_freedom_index_green			= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'economic_freedom_index_green.png')).convert_alpha()
		self.economic_freedom_index_red				= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'economic_freedom_index_red.png')).convert_alpha()
		self.economic_freedom_score_green			= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'economic_freedom_score_green.png')).convert_alpha()
		self.economic_freedom_score_red				= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'economic_freedom_score_red.png')).convert_alpha()
		self.small_rating_green						= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'small_rating_green.png')).convert_alpha()		
		self.small_rating_red						= self.pygame.image.load(os.path.join(self.economic_overview_folder, 'small_rating_red.png')).convert_alpha()

		self.intelligence_overview_folder = os.path.join(self.top_bar_interface_folder, 'intelligence_overview')
		self.intelligence_overview_background			= self.pygame.image.load(os.path.join(self.intelligence_overview_folder, 'intelligence_overview_background.png')).convert_alpha()
		self.load_intelligency_agencies_icons(os.path.join(self.intelligence_overview_folder, 'intelligence_agencies'))	

		self.research_overview_folder = os.path.join(self.top_bar_interface_folder, 'research_overview')
		self.research_overview_background			= self.pygame.image.load(os.path.join(self.research_overview_folder, 'research_overview_background.png')).convert_alpha()
		self.active_research_background				= self.pygame.image.load(os.path.join(self.research_overview_folder, 'active_research_background.png')).convert_alpha()
		self.load_researche_icons(os.path.join(self.research_overview_folder, 'tech_tree_icon'))
		self.load_researche_institute_icons(os.path.join(self.research_overview_folder, 'research_institutes_icon'))

		self.construction_overview_folder = os.path.join(self.top_bar_interface_folder, 'construction_overview')
		self.construction_overview_background			= self.pygame.image.load(os.path.join(self.construction_overview_folder, 'construction_overview_background.png')).convert_alpha()

		self.production_overview_folder = os.path.join(self.top_bar_interface_folder, 'production_overview')
		self.production_overview_background			= self.pygame.image.load(os.path.join(self.production_overview_folder, 'production_overview_background.png')).convert_alpha()	


		self.bottom_bar_interface_folder = os.path.join(self.game_HUD_folder, 'bottom_bar_interface')	

		self.law_opinion_survey_icon			= self.pygame.image.load(os.path.join(self.bottom_bar_interface_folder, 'law_opinion_survey_icon.png')).convert_alpha()
		self.law_opinion_survey_menu			= self.pygame.image.load(os.path.join(self.bottom_bar_interface_folder, 'law_opinion_survey_menu.png')).convert_alpha()


		self.finances_menu_folder = os.path.join(self.bottom_bar_interface_folder, 'finances_menu')	

		self.finances_menu_background			= self.pygame.image.load(os.path.join(self.finances_menu_folder, 'finances_menu_background.png')).convert_alpha()
		self.budget_menu						= self.pygame.image.load(os.path.join(self.finances_menu_folder, 'budget_menu.png')).convert_alpha()
		self.debt_menu							= self.pygame.image.load(os.path.join(self.finances_menu_folder, 'debt_menu.png')).convert_alpha()		
		self.taxation_menu						= self.pygame.image.load(os.path.join(self.finances_menu_folder, 'taxation_menu.png')).convert_alpha()	
		self.currency_menu						= self.pygame.image.load(os.path.join(self.finances_menu_folder, 'currency_menu.png')).convert_alpha()	
		self.finance_menu						= self.pygame.image.load(os.path.join(self.finances_menu_folder, 'finance_menu.png')).convert_alpha()	

		self.government_menu_folder = os.path.join(self.bottom_bar_interface_folder, 'government_menu')	

		self.government_menu_background			= self.pygame.image.load(os.path.join(self.government_menu_folder, 'government_menu_background.png')).convert_alpha()
		self.head_of_state_menu					= self.pygame.image.load(os.path.join(self.government_menu_folder, 'head_of_state_menu.png')).convert_alpha()
		self.cabinet_menu						= self.pygame.image.load(os.path.join(self.government_menu_folder, 'cabinet_menu.png')).convert_alpha()		
		self.parliament_menu					= self.pygame.image.load(os.path.join(self.government_menu_folder, 'parliament_menu.png')).convert_alpha()	
		self.elections_menu						= self.pygame.image.load(os.path.join(self.government_menu_folder, 'elections_menu.png')).convert_alpha()	
		self.political_parties_menu				= self.pygame.image.load(os.path.join(self.government_menu_folder, 'political_parties_menu.png')).convert_alpha()		


		
		self.sounds_folder = os.path.join(self.exe_folder, 'Sounds')
		self.sounds_menu_folder = os.path.join(self.sounds_folder, 'menu')

		self.generic_hover_over_button_sound 	= self.pygame.mixer.Sound(os.path.join(self.sounds_menu_folder, 'generic_hover_over_button_sound.wav'))
		self.generic_click_button_sound 		= self.pygame.mixer.Sound(os.path.join(self.sounds_menu_folder, 'generic_click_button_sound.wav'))


		self.music_folder = os.path.join(self.exe_folder, 'Music')
		self.load_music_files(self.music_folder)

	def read_counties_data_from_file(self, location):
		file_path = f'{location}.json'

		try:
			with open(file_path, 'r') as file:
				counties_data = json_load(file)

			return counties_data

		except FileNotFoundError:
			print(f'Error: File {file_path} not found.')
			return []

	def read_focus_from_file(self, location):
		file_path = f'{location}.json'

		try:
			with open(file_path, 'r') as file:
				focus_data = json_load(file)

			focus_id = 0
			focus_dict = {}
			for focus_data_entry in focus_data:
				focus = CountriesManager.National_Focus(
					focus_data_entry['name'],
					self.national_focus_image_dic[focus_data_entry['icon']],
					focus_data_entry['description'],
					focus_data_entry['x_offset'],
					focus_data_entry['completion_time'],
					focus_data_entry['next_focus'],
					focus_data_entry.get('decision_time', None),
					focus_data_entry.get('path_selection_description', None)
				)
				focus.focus_id = focus_id
				focus_dict[focus_id] = focus
				focus_id += 1

			return focus_dict

		except FileNotFoundError:
			print(f'Error: File {file_path} not found.')
			return []
	def read_decision_tree_from_file(self, location):
		file_path = f'{location}.json'

		try:
			with open(file_path, 'r') as file:
				decision_data = json_load(file)

			decisions_tree_dict = {}
			for decision_data_entry in decision_data:
				decision_data_entry:dict

				button_list = []
				for button in decision_data_entry['buttons']:
					button_list.append(GenericUtilitys.Button(button[0], button[1], button[2], button[3]))

				button_icon_list = []
				for button_icon_name in decision_data_entry['button_icon_image_names']:
					button_icon_list.append(self.decision_icons_image_dic[button_icon_name])
				
				decision = CountriesManager.Decision(
					button_list,
					decision_data_entry['button_descriptions'],
					button_icon_list,
					self.decision_icons_image_dic[decision_data_entry['decision_image_name']],
					decision_data_entry['decision_description'],
					decision_data_entry['x_pos'],
					decision_data_entry['y_pos'],
					decision_data_entry.get('requirements', None)
				)
				decision_on_tree_menu_icon = decision_data_entry.get('decision_on_tree_menu_icon', None)
				if decision_on_tree_menu_icon:
					decision.decision_on_tree_menu_icon = self.decision_on_tree_menu_icons_dic[decision_on_tree_menu_icon]
				
				decisions_tree_dict[decision_data_entry['decision_name']] = decision

			return decisions_tree_dict

		except FileNotFoundError:
			print(f'Error: File {file_path} not found.')
			return []		
	def create_countries_default_frame(self):
		self.countries = []
		self.common_folder = os.path.join(self.exe_folder, 'common')
		self.national_focus_folder = os.path.join(self.common_folder, 'national_focus')	

		self.national_decisions_folder = os.path.join(self.common_folder, 'national_decisions')	
		self.national_active_decisions_folder = os.path.join(self.national_decisions_folder, 'national_active_decisions')	
		self.national_decisions_tree_folder = os.path.join(self.national_decisions_folder, 'national_decisions_tree')	
		##---------------------------------------------------------------------------------------------------------------------##
		##---------------------------------------------------------------------------------------------------------------------##

		self.USA = CountriesManager.Country()
		
		self.USA.country_name = 'United States of America'

		self.USA.country_leader_name = 'Richard Nixon'
		self.USA.country_leader_image = self.leaders_image_dic['Portrait_USA_Richard_Nixon']
		self.USA.country_leader_title = 'President'
		self.USA.country_ruler_ideology = 'Keynesianism'

		close_people = CountriesManager.Person('carlos', self.leaders_image_dic['Portrait_TEX_John_Connally'])
		self.USA.head_of_state_close_people = [close_people,close_people,close_people,close_people,close_people,close_people,close_people,close_people,close_people]
		
		self.USA.country_capital_image = self.capitals_images_dic['USA']
		
		self.USA.country_flag_image = self.flags_image_dic['USA']
		
		self.USA.country_music_playlist = [self.music_files_dic['house_of_the_black_sun']]

		self.USA.country_ruling_party = 'Republican'
		self.USA.country_government = 'Federal Republic'
		
		self.USA.country_elections = '4 years'
		
		self.USA.country_brief_history = """	
The land of the brave and the home of the free has been
usurped by a sinister force, an unseen hand that tugs at
the threads of democracy, trust, and truth.

The American dream, once a beacon of hope, now flickers
in the encroaching darkness.
The stars and stripes thatonce fluttered with pride now
seem like mere illusions.

The fate the nation hangs in the balance, as the clock
ticks relentlessly toward an uncertain future.

The relentless countdown of the cataclysm adds urgency
to the fate of the nation, perhaps the world, rests on
your shoulders.
"""
		# Country Government
		cabinet_member = CountriesManager.Person('bob', self.leaders_image_dic['Portrait_TEX_John_Connally'])
		self.USA.country_government_gabinet = [cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member,cabinet_member]
		
		self.USA.total_parliament_seats = 100
		self.USA.total_senate_seats = 100

		self.USA.parliament_head = CountriesManager.Person('bob', self.leaders_image_dic['Portrait_TEX_John_Connally'])   
		self.USA.parliament_parties_head = CountriesManager.Person('bob', self.leaders_image_dic['Portrait_TEX_John_Connally']) 

		self.USA.senate_head = CountriesManager.Person('bob', self.leaders_image_dic['Portrait_TEX_John_Connally'])
		self.USA.senate_parties_head = CountriesManager.Person('bob', self.leaders_image_dic['Portrait_TEX_John_Connally']) 		

		# Country Focus
		usa_focus_dict = self.read_focus_from_file(location = os.path.join(self.national_focus_folder, 'USA'))
		self.USA.country_focus_tree = usa_focus_dict	

		# Country Decisions
		usa_decision_tree_dict = self.read_decision_tree_from_file(location = os.path.join(self.national_decisions_tree_folder, 'USA'))
		self.USA.country_decisions_tree = usa_decision_tree_dict

		usa_active_decisions_dict = self.read_decision_tree_from_file(location = os.path.join(self.national_active_decisions_folder, 'USA'))
		self.USA.country_active_decisions = usa_active_decisions_dict

		# Country Stats
		self.USA.country_national_spirits_total_points = 100
		self.USA.country_national_spirits_points_left = self.USA.country_national_spirits_total_points
		
		self.USA.country_stability = 100
		self.USA.country_war_support = 100
		self.USA.country_party_popularity = 100

		self.USA.weekly_head_of_state_popularity_data = [self.USA.country_party_popularity]

		# 		Country Diplomacy Stats
		self.USA.diplomacy_rating = 100
		
		# 		Country Military Stats
		self.USA.military_rating = 100
		self.USA.country_land_manpower = 150_000
		self.USA.country_air_manpower = 150_000
		self.USA.army_staff = self.USA.country_land_manpower + self.USA.country_air_manpower
		self.USA.production_capacity_army = 0
		self.USA.production_capacity_navy = 0
		self.USA.production_capacity_air = 0
		self.USA.production_capacity_special = 0
		self.USA.production_capacity_total = f"{self.USA.production_capacity_army} / {self.USA.production_capacity_navy} / {self.USA.production_capacity_air} / {self.USA.production_capacity_special}"
		
		# 		Country Economy Stats
		self.USA.economy_rating = 100
		self.USA.treasury = 85_952_542_000_000
		self.USA.debt = 5_365_215_000_000
		self.USA.credit_rating = 52.5
		self.USA.credit_stability = 0.89
		self.USA.inflation = 2.1
		self.USA.currency_interest_rate = 0
		self.USA.unemployment = 5.2
		self.USA.country_GDP = 10_550_000_000_000
		self.USA.income = 10_550_000_000_000
		
		self.USA.expenses = 5000  

		self.USA.agriculture_expense = 1000
		self.USA.culture_expense = 1000
		self.USA.debt_interest_expense = 500
		self.USA.defense_expense = 500
		self.USA.economy_expense = 500
		self.USA.education_expense = 500
		self.USA.employment_social_expense = 1000
		self.USA.energy_expense = 0
		self.USA.environment_expense = 0
		self.USA.family_expense = 0
		self.USA.foreign_affairs_expense = 0
		self.USA.health_expense = 0
		self.USA.homeland_security_expense = 0
		self.USA.housing_expense = 0
		self.USA.industry_expense = 0
		self.USA.information_expense = 0
		self.USA.justice_expense = 0
		self.USA.miscellaneous_expense = 0
		self.USA.religion_expense = 0
		self.USA.research_expense = 0
		self.USA.secret_services_expense = 0
		self.USA.social_security_expense = 0
		self.USA.sport_expense = 0
		self.USA.tourism_expense = 0
		self.USA.transport_expense = 0
		self.USA.treasury_expense = 0
		self.USA.unemployment_insurance_expense = 0	

		self.USA.weekly_debt_to_gdp_data = [round((self.USA.debt / self.USA.country_GDP) * 100, 2)]	
		self.USA.weekly_inflation_data = [self.USA.inflation]
		self.USA.weekly_currency_interest_rate_data = [self.USA.currency_interest_rate] 
		self.USA.weekly_country_GDP_data = [self.USA.country_GDP]
		
		# 		Country Domestic Stats
		self.USA.domestic_rating = 100
		self.USA.country_population = 100_600_000
		self.USA.country_immigration = 10000
		self.USA.country_emigration = 2000
		self.USA.country_births = 10400
		self.USA.country_deaths = 25000
		self.USA.country_literacy_rate = 94
		self.USA.country_poverty_rate = [0.50, 0.30, 0.20] # Poverty / Poor + Middle Class / Upper Class

		self.USA.population_political_leaning = 'Moderate'

		# 		Country Internal Approval Stats
		self.USA.military_approval_rating = 100
		self.USA.domestic_approval_rating = 80
		self.USA.midia_approval_rating = 60
		self.USA.secret_service_approval_rating = 40
		self.USA.politics_approval_rating = 20 

		self.USA.internal_economy_rating = 100
		self.USA.external_economy_rating = 50
		

		# Country Laws
		self.USA.country_immigration_policy = 'Not Implemented'
		self.USA.country_moral_code = 'Not Implemented'

		self.USA.political_parties.set_active_law(			0)
		self.USA.religious_rights.set_active_law(			0)
		self.USA.trade_unions.set_active_law(				0)
		self.USA.public_protest.set_active_law(				0)
		self.USA.gun_control.set_active_law(				0)
		self.USA.privacy_rights.set_active_law(				0)
		self.USA.speach_rights.set_active_law(				0)
		self.USA.press_rights.set_active_law(				0)
		self.USA.voting_rights.set_active_law(				0)
		self.USA.conscription.set_active_law(				0)
		self.USA.women_in_service.set_active_law(			0)
		self.USA.training_level.set_active_law(				0)
		self.USA.racial_admission.set_active_law(			0)
		self.USA.national_security.set_active_law(			0)
		self.USA.deployment.set_active_law(					0)
		self.USA.reserves.set_active_law(					0)
		self.USA.economical_militarization.set_active_law(	0)
		self.USA.economic_system.set_active_law(			0)
		self.USA.trade_laws.set_active_law(					0)
		self.USA.taxation_system.set_active_law(			0)
		self.USA.regulations.set_active_law(				0)
		self.USA.monetary_policy.set_active_law(			0)
		self.USA.property_rights.set_active_law(			0)
		self.USA.nationalization.set_active_law(			0)
		self.USA.brand_rights.set_active_law(				0)
		self.USA.public_services.set_active_law(			0)
		self.USA.emigration_immigration.set_active_law(		0)
		self.USA.minorities_rights.set_active_law(			0)
		self.USA.welfare.set_active_law(					0)
		self.USA.reproduction.set_active_law(				0)
		self.USA.morality_laws.set_active_law(				0)
		self.USA.drug_laws.set_active_law(					0)
		self.USA.work_laws.set_active_law(					0)
		self.USA.justice_system.set_active_law(				0)
		self.USA.environmental.set_active_law(				0)
		#----------------------------------------------------------------#
		#----------------------------------------------------------------#		
		self.countries.extend([self.USA])
	def create_national_spirits(self):
		self.localization_folder = os.path.join(self.exe_folder, 'localization')
		self.ideas_localization_folder = os.path.join(self.localization_folder, 'ideas')

		#### CULTURAL
		self.cultural_ideas_localization_folder = os.path.join(self.ideas_localization_folder, '_cultural')

		with open(os.path.join(self.cultural_ideas_localization_folder, 'Accelerationism.txt'), 'r') as file:
			Accelerationism_description = file.read()
		self.Accelerationism = CountriesManager.National_Spirit('Accelerationism', self.national_spirits_image_dic['Accelerationism'], Accelerationism_description)
		
		with open(os.path.join(self.cultural_ideas_localization_folder, 'Ultraprogressive.txt'), 'r') as file:
			Ultraprogressive_description = file.read()
		self.Ultraprogressive = CountriesManager.National_Spirit('Ultraprogressive', self.national_spirits_image_dic['Ultraprogressive'], Ultraprogressive_description)
		
		with open(os.path.join(self.cultural_ideas_localization_folder, 'Progressive.txt'), 'r') as file:
			Progressive_description = file.read()
		self.Progressive = CountriesManager.National_Spirit('Progressive', self.national_spirits_image_dic['Progressive'], Progressive_description)
		
		with open(os.path.join(self.cultural_ideas_localization_folder, 'Environmentalism.txt'), 'r') as file:
			Environmentalism_description = file.read()
		self.Environmentalism = CountriesManager.National_Spirit('Environmentalism', self.national_spirits_image_dic['Environmentalism'], Environmentalism_description)

		with open(os.path.join(self.cultural_ideas_localization_folder, 'Globalism.txt'), 'r') as file:
			Globalism_description = file.read()
		self.Globalism = CountriesManager.National_Spirit('Globalism', self.national_spirits_image_dic['Globalism'], Globalism_description)	

		with open(os.path.join(self.cultural_ideas_localization_folder, 'Multiculturalism.txt'), 'r') as file:
			Multiculturalism_description = file.read()
		self.Multiculturalism = CountriesManager.National_Spirit('Multiculturalism', self.national_spirits_image_dic['Multiculturalism'], Multiculturalism_description)	

		with open(os.path.join(self.cultural_ideas_localization_folder, 'Secularism.txt'), 'r') as file:
			Secularism_description = file.read()
		self.Secularism = CountriesManager.National_Spirit('Secularism', self.national_spirits_image_dic['Secularism'], Secularism_description)			

		with open(os.path.join(self.cultural_ideas_localization_folder, 'Centrist.txt'), 'r') as file:
			Centrist_description = file.read()
		self.Centrist = CountriesManager.National_Spirit('Centrist', self.national_spirits_image_dic['Centrist'], Centrist_description)

		with open(os.path.join(self.cultural_ideas_localization_folder, 'Liberal.txt'), 'r') as file:
			Liberal_description = file.read()
		self.Liberal = CountriesManager.National_Spirit('Liberal', self.national_spirits_image_dic['Liberal'], Liberal_description)

		with open(os.path.join(self.cultural_ideas_localization_folder, 'Neoconservatism.txt'), 'r') as file:
			Neoconservatism_description = file.read()
		self.Neoconservatism = CountriesManager.National_Spirit('Neoconservatism', self.national_spirits_image_dic['Neoconservatism'], Neoconservatism_description)		
		
		with open(os.path.join(self.cultural_ideas_localization_folder, 'Conservative.txt'), 'r') as file:
			Conservative_description = file.read()
		self.Conservative = CountriesManager.National_Spirit('Conservative', self.national_spirits_image_dic['Conservative'], Conservative_description)

		with open(os.path.join(self.cultural_ideas_localization_folder, 'Reactionary.txt'), 'r') as file:
			Reactionary_description = file.read()
		self.Reactionary = CountriesManager.National_Spirit('Reactionary', self.national_spirits_image_dic['Reactionary'], Reactionary_description)	
		
		with open(os.path.join(self.cultural_ideas_localization_folder, 'Traditionalist.txt'), 'r') as file:
			Traditionalist_description = file.read()
		self.Traditionalist = CountriesManager.National_Spirit('Traditionalist', self.national_spirits_image_dic['Traditionalist'], Traditionalist_description)
		
		with open(os.path.join(self.cultural_ideas_localization_folder, 'Nationalism.txt'), 'r') as file:
			Nationalism_description = file.read()
		self.Nationalism = CountriesManager.National_Spirit('Nationalism', self.national_spirits_image_dic['Nationalism'], Nationalism_description)
		
		# RELIGION
		self.religion_ideas_localization_folder = os.path.join(self.ideas_localization_folder, '_religion')

		with open(os.path.join(self.religion_ideas_localization_folder, 'Christianity.txt'), 'r') as file:
			Christianity_description = file.read()
		self.Christianity = CountriesManager.National_Spirit('Christianity', self.national_spirits_image_dic['Christianity'], Christianity_description)	

		with open(os.path.join(self.religion_ideas_localization_folder, 'Judaism.txt'), 'r') as file:
			Judaism_description = file.read()
		self.Judaism = CountriesManager.National_Spirit('Judaism', self.national_spirits_image_dic['Judaism'], Judaism_description)			

		with open(os.path.join(self.religion_ideas_localization_folder, 'Islam.txt'), 'r') as file:
			Islam_description = file.read()
		self.Islam = CountriesManager.National_Spirit('Islam', self.national_spirits_image_dic['Islam'], Islam_description)

		with open(os.path.join(self.religion_ideas_localization_folder, 'Hinduism.txt'), 'r') as file:
			Hinduism_description = file.read()
		self.Hinduism = CountriesManager.National_Spirit('Hinduism', self.national_spirits_image_dic['Hinduism'], Hinduism_description)

		with open(os.path.join(self.religion_ideas_localization_folder, 'Buddhism.txt'), 'r') as file:
			Buddhism_description = file.read()
		self.Buddhism = CountriesManager.National_Spirit('Buddhism', self.national_spirits_image_dic['Buddhism'], Buddhism_description)		
		
		with open(os.path.join(self.religion_ideas_localization_folder, 'Taoism.txt'), 'r') as file:
			Taoism_description = file.read()
		self.Taoism = CountriesManager.National_Spirit('Taoism', self.national_spirits_image_dic['Taoism'], Taoism_description)

		with open(os.path.join(self.religion_ideas_localization_folder, 'Shintoism.txt'), 'r') as file:
			Shintoism_description = file.read()
		self.Shintoism = CountriesManager.National_Spirit('Shintoism', self.national_spirits_image_dic['Shintoism'], Shintoism_description)	
		
		with open(os.path.join(self.religion_ideas_localization_folder, 'Indigenous.txt'), 'r') as file:
			Indigenous_description = file.read()
		self.Indigenous = CountriesManager.National_Spirit('Indigenous', self.national_spirits_image_dic['Indigenous'], Indigenous_description)
		
		with open(os.path.join(self.religion_ideas_localization_folder, 'Atheism.txt'), 'r') as file:
			Atheism_description = file.read()
		self.Atheism = CountriesManager.National_Spirit('Atheism', self.national_spirits_image_dic['Atheism'], Atheism_description)


		#### GENERIC
		self.GENERIC = CountriesManager.National_Spirit('GENERIC', self.national_spirits_image_dic['general_staff'], "NOTHING YET")

		self.selectable_ideas_localization_folder = os.path.join(self.ideas_localization_folder, '_selectable')

		with open(os.path.join(self.selectable_ideas_localization_folder, 'winter_resistance.txt'), 'r') as file:
			winter_resistance_description = file.read()
		self.winter_resistance = CountriesManager.National_Spirit('Winter Resistance', self.national_spirits_image_dic['winter_resistance'], winter_resistance_description)
		
		with open(os.path.join(self.selectable_ideas_localization_folder, 'local_business_traditional_support.txt'), 'r') as file:
			local_business_traditional_support_description = file.read()		
		self.local_business_traditional_support = CountriesManager.National_Spirit('Traditional Support Local Business', 
			self.national_spirits_image_dic['local_business_traditional_support'], local_business_traditional_support_description)
		
		with open(os.path.join(self.selectable_ideas_localization_folder, 'nuclear_capable.txt'), 'r') as file:
			nuclear_capable_description = file.read()			
		self.nuclear_capable = CountriesManager.National_Spirit('Nuclear Capable', self.national_spirits_image_dic['nuclear_capable'], nuclear_capable_description)
		
		with open(os.path.join(self.selectable_ideas_localization_folder, 'educational_culture.txt'), 'r') as file:
			educational_culture_description = file.read()			
		self.educational_culture = CountriesManager.National_Spirit('Educational Culture', self.national_spirits_image_dic['educational_culture'], educational_culture_description)
		
		with open(os.path.join(self.selectable_ideas_localization_folder, 'armor_industry.txt'), 'r') as file:
			armor_industry_description = file.read()			
		self.armor_industry = CountriesManager.National_Spirit('Armor Industry', self.national_spirits_image_dic['armor_industry'], armor_industry_description)
		
		with open(os.path.join(self.selectable_ideas_localization_folder, 'oil_abundance.txt'), 'r') as file:
			oil_abundance_description = file.read()			
		self.oil_abundance = CountriesManager.National_Spirit('Oil Abundance', self.national_spirits_image_dic['oil_abundance'], oil_abundance_description)
		
		with open(os.path.join(self.selectable_ideas_localization_folder, 'crops_abundance.txt'), 'r') as file:
			crops_abundance_description = file.read()				
		self.crops_abundance = CountriesManager.National_Spirit('Crops Abundance', self.national_spirits_image_dic['crops_abundance'], crops_abundance_description)
		
		with open(os.path.join(self.selectable_ideas_localization_folder, 'general_staff.txt'), 'r') as file:
			general_staff_description = file.read()			
		self.general_staff = CountriesManager.National_Spirit('General Staff', self.national_spirits_image_dic['general_staff'], general_staff_description)
	

		self.generic_national_spirits = [self.winter_resistance, self.local_business_traditional_support, self.nuclear_capable, 
			self.educational_culture, self.armor_industry, self.oil_abundance, self.crops_abundance, self.general_staff]
		
		for np in self.generic_national_spirits:
			np.points_cost = 5

		#### COUNTRIES

		# United States of America

		self.USA_ideas_localization_folder = os.path.join(self.ideas_localization_folder, 'USA')

		with open(os.path.join(self.USA_ideas_localization_folder, 'usa_pentagon.txt'), 'r') as file:
			usa_pentagon_description = file.read()
		with open(os.path.join(self.USA_ideas_localization_folder, 'usa_anti_war.txt'), 'r') as file:
			usa_anti_war_description = file.read()
		with open(os.path.join(self.USA_ideas_localization_folder, 'world_trade_center_half.txt'), 'r') as file:
			world_trade_center_half_description = file.read()
		with open(os.path.join(self.USA_ideas_localization_folder, 'CIA.txt'), 'r') as file:
			CIA_description = file.read()
		with open(os.path.join(self.USA_ideas_localization_folder, 'usa_race_riots.txt'), 'r') as file:
			usa_race_riots = file.read()						

		self.usa_pentagon = CountriesManager.National_Spirit('Usa Pentagon', self.national_spirits_image_dic['usa_pentagon'], usa_pentagon_description)
		self.usa_anti_war = CountriesManager.National_Spirit('Anti War Movement', self.national_spirits_image_dic['usa_anti_war'], usa_anti_war_description)
		self.world_trade_center_half = CountriesManager.National_Spirit('World Trade Center Half', self.national_spirits_image_dic['world_trade_center_half'], world_trade_center_half_description)
		self.CIA = CountriesManager.National_Spirit('C.I.A.', self.national_spirits_image_dic['CIA'], CIA_description)
		self.usa_race_riots = CountriesManager.National_Spirit('Race Riots', self.national_spirits_image_dic['usa_race_riots'], usa_race_riots)
		self.USA.country_national_spirits.extend([self.usa_pentagon, self.usa_anti_war, self.CIA, self.usa_race_riots, self.world_trade_center_half])

		self.USA.country_culture = self.Liberal
		self.USA.country_religion = self.Christianity		

	def create_classes(self):
		self.Sounds_Manager = SoundsManager.Sounds_Manager(self.generic_hover_over_button_sound, self.generic_click_button_sound)

		self.Main_Menu = MenuManager.Main_Menu(self.screen_width, self.screen_height, self.pygame, self.game_logo, self.python_logo, self.main_menu_UI, self.hovered_green_button_menu_image,
				self.hovered_red_button_menu_image, self.new_game_menu_background, self.Sounds_Manager.generic_hover_over_button_sound, self.Sounds_Manager.generic_click_button_sound)

		self.Scenario_Selection_Menu = MenuManager.Scenario_Selection_Menu(self.screen_width, self.screen_height, self.pygame, self.game_logo, self.python_logo,
				self.scenario_selection_menu_gui, self.hovered_select_scenario_button_menu_image, self.hovered_back_to_main_menu_button_menu_image,
				self.Sounds_Manager.generic_hover_over_button_sound, self.Sounds_Manager.generic_click_button_sound)


		self.Country_Selection_Screen = MenuManager.Country_Selection_Screen(
				self.screen_width, self.screen_height, self.pygame, self.countries, self.Sounds_Manager.generic_hover_over_button_sound, self.Sounds_Manager.generic_click_button_sound, 
				self.country_selection_background, self.country_info_display_background, self.political_compass_image, self.ideologies_CRT_overlay_effect,
				self.hovered_start_game_button, self.hovered_select_national_spirit_button_image, self.hovered_select_country_button_image, 
				self.generic_leader, self.CRT_flag_overlay_effect, self.blocked_select_national_spirit_button, self.blocked_select_country_button, self.blocked_start_game_button,
				self.blocked_full_right_side, self.blocked_all_laws, self.national_spirits_background, self.generic_national_spirits, self.progressbar, self.progressbar_vertical,
				self.progressbar_small, self.progressbar_huge, self.selected_law_background, self.laws_description_image)
		

		self.Options_Menu = MenuManager.Options_Menu(self.screen_width, self.screen_height, self.menu_options_UI, 
				self.Sounds_Manager.generic_hover_over_button_sound, self.Sounds_Manager.generic_click_button_sound, self.hovered_green_button_menu_image,
				self.hovered_red_button_menu_image, self.Sounds_Manager, self.Main_Menu)
		self.ESC_Menu = MenuManager.ESC_Menu(self.screen_width, self.screen_height, self.ESC_menu_background, 
				self.Sounds_Manager.generic_hover_over_button_sound, self.Sounds_Manager.generic_click_button_sound, self.hovered_green_button_menu_image,
				self.hovered_red_button_menu_image, self.Options_Menu)
		

		self.Game_Screen = MenuManager.Game_Screen(self.screen_width, self.screen_height, self.pygame, self.clock, self.Sounds_Manager.generic_hover_over_button_sound, self.Sounds_Manager.generic_click_button_sound, 
			self.top_bar_right_background, self.top_bar_game_speed_indicator, self.top_bar_defcon_levels, self.top_bar_left_background, self.top_bar_flag_overlay,
			self.top_bar_flag_overlay_hovering_over, self.country_overview, self.popularity_circle_overlay, self.earth_daymap, self.earth_political_map, self.earth_political_map_filled,
			self.progressbar_huge, self.progressbar, self.progressbar_vertical, self.progressbar_small, self.country_laws_background, self.laws_description_image, self.game_logo,
			self.economic_overview_background, self.poverty_rate_0, self.poverty_rate_5, self.poverty_rate_10, self.poverty_rate_15, self.poverty_rate_25, self.poverty_rate_50,
			self.poverty_rate_80, self.credit_ratings, self.economic_warning, self.economic_freedom_index_green, self.economic_freedom_index_red, self.economic_freedom_score_green, self.economic_freedom_score_red,
			self.small_rating_green, self.small_rating_red, self.intelligence_overview_background, self.intelligency_agencies_icons_image_dic, self.research_overview_background, self.active_research_background, self.researche_icons_image_dic,
			self.researche_institute_icons_image_dic, self.construction_overview_background, self.production_overview_background, self.bottom_HUD, self.law_opinion_survey_icon, self.law_opinion_survey_menu,
			self.finances_menu_background, self.budget_menu, self.debt_menu, self.taxation_menu, self.currency_menu, self.finance_menu, self.government_menu_background, self.head_of_state_menu,
			self.cabinet_menu, self.parliament_menu, self.elections_menu, self.political_parties_menu)


		self.Screen_Manager = ScreenManager.Screen(self.pygame, self.display, self.screen, self.surface_alfa, self.Main_Menu, self.Country_Selection_Screen,
				self.Scenario_Selection_Menu, self.ESC_Menu, self.Game_Screen, self.main_menu_backgound, self.python_logo)
		
	def setup_variables(self):
		self.screen_center = (self.screen_width/2, self.screen_height/2)

		self.mouse_pos = self.pygame.mouse.get_pos()
		self.mouse_rect = self.pygame.Rect(self.mouse_pos, (1, 1))

		self.clicked_button = 'none'
		self.hovered_button = 'none'


		self.main_menu_music_started = False

		self.starting_the_game = True 
		###
		self.is_options_menu_open = False

		self.is_in_esc_menu = False

		self.is_in_main_menu_screen = True

		self.is_in_scenario_selection_screen = False

		self.is_in_country_selection_screen = False

		self.is_in_game_screen = False

	def main_loop(self):
		to_draw = True
		while self.starting_the_game:
			if self.is_in_main_menu_screen == True:
				if self.main_menu_music_started == False or self.pygame.mixer.music.get_busy() == False:
					self.main_menu_music_started = True
					self.pygame.mixer.music.load(self.music_files_dic['clock-ticking'])
					self.pygame.mixer.music.play()

				self.Screen_Manager.render_main_menu(self.Options_Menu.brightness_slider.value, self.is_options_menu_open)					

				for event in self.pygame.event.get():
					keys = self.pygame.key.get_pressed()	
					if event.type == QUIT:
						self.starting_the_game = False		
					if event.type == FPS_update:
						self.pygame.display.set_caption(str(round(clock.get_fps(), 2)))							

					if self.is_options_menu_open == True:
						self.Options_Menu.interacting_with_UI_slides(event)							

					self.mouse_pos = self.pygame.mouse.get_pos()	
					
					if event.type == self.pygame.MOUSEBUTTONUP:	
						pass
					
					elif event.type == self.pygame.MOUSEBUTTONDOWN:
						self.mouse_rect = self.pygame.Rect(self.mouse_pos, (1, 1))
						
						if self.is_options_menu_open == False:
							self.clicked_button = self.Main_Menu.get_clicked_button(self.mouse_rect)
							if self.clicked_button != 'none':
								if self.Main_Menu.is_in_new_game_menu == False:
									if self.clicked_button == 'start':
										self.pygame.time.delay(50)
										self.Main_Menu.is_in_new_game_menu = True
										self.Main_Menu.main_menu_intro_video.toggle_pause()
										self.Options_Menu.music_slider.value = 60
										self.Options_Menu.music_slider.update()
										pygame.mixer.music.set_volume(self.Options_Menu.music_slider.value/100)
									elif self.clicked_button == 'quit':
										self.pygame.time.delay(50)
										self.starting_the_game = False
									elif self.clicked_button == 'options':
										self.pygame.time.delay(50)
										self.is_options_menu_open = True
								else:
									if self.clicked_button == 'new_game':
										self.is_in_scenario_selection_screen = True
										self.is_in_main_menu_screen = False
										self.Main_Menu.is_in_new_game_menu = False
									elif self.clicked_button == 'load_save':
										self.Main_Menu.is_in_new_game_menu = False
									elif self.clicked_button == 'back':		
										self.Main_Menu.is_in_new_game_menu = False
										self.Main_Menu.main_menu_intro_video.toggle_pause()
										self.Options_Menu.music_slider.value = 10
										self.Options_Menu.music_slider.update()
										pygame.mixer.music.set_volume(self.Options_Menu.music_slider.value/100)

						else:
							self.clicked_button = self.ESC_Menu.get_clicked_button(self.mouse_rect, self.is_options_menu_open)
							
							if self.clicked_button == 'back':
								self.is_options_menu_open = False

							resolution_to_save = None
							if self.clicked_button == 'resolution_2560x1440':
								resolution_to_save = (2560,1440)
							elif self.clicked_button == 'resolution_1920x1080':
								resolution_to_save = (1920,1080)
							elif self.clicked_button == 'resolution_1600x900':
								resolution_to_save = (1600,900)
							elif self.clicked_button == 'resolution_1440x900':
								resolution_to_save = (1440,900)
							elif self.clicked_button == 'resolution_1280x1024':
								resolution_to_save = (1280,1024)

							if resolution_to_save != None:
								with open(f'{self.exe_folder}\\settings.txt', 'r') as file:
									configs = json_load(file)

								configs["screen_width"], configs["screen_height"] = resolution_to_save

								with open(f'{self.exe_folder}\\settings.txt', 'w') as file:
									json_dump(configs, file)

				self.mouse_rect = self.pygame.Rect(self.mouse_pos, (1, 1))

				if self.is_options_menu_open == False:				
					self.hovered_button = self.Main_Menu.get_hovered_button(self.mouse_rect)
					self.Main_Menu.hovered_button = self.hovered_button
				else:
					self.hovered_button = self.ESC_Menu.get_hovered_button(self.mouse_rect, self.is_options_menu_open)
					self.ESC_Menu.hovered_button = self.hovered_button
					self.Options_Menu.hovered_button = self.hovered_button


			if self.is_in_scenario_selection_screen == True:
				if self.main_menu_music_started == False or self.pygame.mixer.music.get_busy() == False:
					self.main_menu_music_started = True
					self.pygame.mixer.music.load(self.music_files_dic['clock-ticking'])
					self.pygame.mixer.music.play()

				self.Screen_Manager.render_select_scenario_menu(self.Options_Menu.brightness_slider.value, self.is_in_esc_menu, self.is_options_menu_open)						

				for event in self.pygame.event.get():
					keys = self.pygame.key.get_pressed()	
					if event.type == QUIT:
						self.starting_the_game = False		
					if event.type == FPS_update:
						self.pygame.display.set_caption(str(round(clock.get_fps(), 2)))							

					if self.is_options_menu_open == True:
						self.Options_Menu.interacting_with_UI_slides(event)	

					if event.type == self.pygame.KEYDOWN:
						if keys[self.pygame.K_ESCAPE]:
							self.is_in_esc_menu = not self.is_in_esc_menu
							self.is_options_menu_open = False											

					self.mouse_pos = self.pygame.mouse.get_pos()	
					if event.type == self.pygame.MOUSEBUTTONUP:	
						pass
					
					elif event.type == self.pygame.MOUSEBUTTONDOWN:
						self.mouse_rect = self.pygame.Rect(self.mouse_pos, (1, 1))

						if self.is_in_esc_menu == False:						
							self.clicked_button = self.Scenario_Selection_Menu.get_clicked_button(self.mouse_rect)
							if self.clicked_button != 'none':
								if self.clicked_button == 'start':
									self.pygame.time.delay(100)
									self.is_in_country_selection_screen = True
									self.is_in_scenario_selection_screen = False
								if 	self.clicked_button == 'back':
									self.pygame.time.delay(50)
									self.is_in_scenario_selection_screen = False
									self.is_in_main_menu_screen = True
									self.Main_Menu.main_menu_intro_video.toggle_pause()
						else:
							self.clicked_button = self.ESC_Menu.get_clicked_button(self.mouse_rect, self.is_options_menu_open)
							if self.clicked_button != 'none' and self.clicked_button != None:
								if self.is_options_menu_open == False:
									if self.clicked_button == 'options':
										self.is_options_menu_open = True

									elif self.clicked_button == 'main_menu':
										self.is_in_scenario_selection_screen = False
										self.is_in_main_menu_screen = True
										self.is_in_esc_menu = False
										self.Main_Menu.main_menu_intro_video.toggle_pause()

									elif self.clicked_button == 'quit':
										self.starting_the_game = False
										self.is_in_scenario_selection_screen = False
										self.pygame.time.delay(200)	
								else:
									if self.clicked_button == 'back':
										self.is_options_menu_open = False

									resolution_to_save = None
									if self.clicked_button == 'resolution_2560x1440':
										resolution_to_save = (2560,1440)
									elif self.clicked_button == 'resolution_1920x1080':
										resolution_to_save = (1920,1080)
									elif self.clicked_button == 'resolution_1600x900':
										resolution_to_save = (1600,900)
									elif self.clicked_button == 'resolution_1440x900':
										resolution_to_save = (1440,900)
									elif self.clicked_button == 'resolution_1280x1024':
										resolution_to_save = (1280,1024)

									if resolution_to_save != None:
										with open(f'{self.exe_folder}\\settings.txt', 'r') as file:
											configs = json_load(file)

										configs["screen_width"], configs["screen_height"] = resolution_to_save

										with open(f'{self.exe_folder}\\settings.txt', 'w') as file:
											json_dump(configs, file)								

				self.mouse_rect = self.pygame.Rect(self.mouse_pos, (1, 1))
				
				if self.is_in_esc_menu == False:
					self.hovered_button = self.Scenario_Selection_Menu.get_hovered_button(self.mouse_rect)
					self.Scenario_Selection_Menu.hovered_button = self.hovered_button
				else:
					self.hovered_button = self.ESC_Menu.get_hovered_button(self.mouse_rect, self.is_options_menu_open)
					self.ESC_Menu.hovered_button = self.hovered_button
					self.Options_Menu.hovered_button = self.hovered_button


			if self.is_in_country_selection_screen == True:
				self.Screen_Manager.render_country_selection_menu(self.Options_Menu.brightness_slider.value, self.is_in_esc_menu, self.is_options_menu_open, self.mouse_pos, self.mouse_rect)	

				for event in self.pygame.event.get():
					keys = self.pygame.key.get_pressed()	
					if event.type == QUIT:
						self.starting_the_game = False
						self.is_in_country_selection_screen = False		
					if event.type == FPS_update:
						self.pygame.display.set_caption(str(round(clock.get_fps(), 2)))							

					if self.is_options_menu_open == True:
						self.Options_Menu.interacting_with_UI_slides(event)

					if event.type == self.pygame.KEYDOWN:
						if keys[self.pygame.K_ESCAPE]:
							self.is_in_esc_menu = not self.is_in_esc_menu
							self.is_options_menu_open = False

					self.mouse_pos = self.pygame.mouse.get_pos()

					if event.type == self.pygame.MOUSEBUTTONUP:	
						pass
					
					elif event.type == self.pygame.MOUSEBUTTONDOWN:
						self.mouse_rect = self.pygame.Rect(self.mouse_pos, (1, 1))

						if self.is_in_esc_menu == False:
							self.clicked_button = self.Country_Selection_Screen.get_clicked_button(self.mouse_rect)
							if self.clicked_button != None:
								if self.clicked_button == 'start_game':
									self.is_in_country_selection_screen = False
									self.is_in_esc_menu = False
									self.is_in_game_screen = True

									self.Game_Screen.PlayerCountry = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country

									self.Game_Screen.Country_Overview.PlayerCountry = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country
									self.Game_Screen.Country_Overview.politics_popularity = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country.politics_popularity
									self.Game_Screen.Country_Overview.culture_popularity = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country.culture_popularity
									self.Game_Screen.Country_Overview.religion_popularity = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country.religion_popularity

									self.Game_Screen.Country_Focus_Tree.PlayerCountry = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country

									self.Game_Screen.Laws_Menu.PlayerCountry = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country

									self.Game_Screen.Decisions_Menu.PlayerCountry = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country
									self.Game_Screen.Decisions_Menu.generate_decisions_tree()

									self.Game_Screen.Finances_Menu.PlayerCountry = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country

									self.Game_Screen.intelligence_Menu.PlayerCountry = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country

									self.Game_Screen.Research_Menu.PlayerCountry = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country
									self.Game_Screen.Research_Menu.Warfare_Tech_Tree.generate_researche_images(self.Game_Screen.Research_Menu.PlayerCountry)
									self.Game_Screen.Research_Menu.Transport_Tech_Tree.generate_researche_images(self.Game_Screen.Research_Menu.PlayerCountry)
									self.Game_Screen.Research_Menu.Science_Tech_Tree.generate_researche_images(self.Game_Screen.Research_Menu.PlayerCountry)
									self.Game_Screen.Research_Menu.Technology_Tech_Tree.generate_researche_images(self.Game_Screen.Research_Menu.PlayerCountry)
									self.Game_Screen.Research_Menu.Medical_Tech_Tree.generate_researche_images(self.Game_Screen.Research_Menu.PlayerCountry)
									self.Game_Screen.Research_Menu.Society_Tech_Tree.generate_researche_images(self.Game_Screen.Research_Menu.PlayerCountry)

									self.Game_Screen.Clock_UI.PlayerCountry = self.Country_Selection_Screen.Flag_Selection_Menu.selected_country

									#self.Game_Screen.Earth_Map.scale_map(zoom_factor_change = -0.70, fps_freezing_avoidance = round(clock.get_fps(), 2), zoom_type = 'zoom_out')

									self.Game_Screen.Earth_Map.map_position[0] -= 900

									self.Game_Screen.Bottom_HUD.start_menus(self.Country_Selection_Screen.Flag_Selection_Menu.selected_country)
						else:
							self.clicked_button = self.ESC_Menu.get_clicked_button(self.mouse_rect, self.is_options_menu_open)
							if self.clicked_button != 'none' and self.clicked_button != None:
								if self.is_options_menu_open == False:
									if self.clicked_button == 'options':
										self.is_options_menu_open = True

									elif self.clicked_button == 'main_menu':
										self.is_in_country_selection_screen = False
										self.is_in_main_menu_screen = True
										self.is_in_esc_menu = False
										self.Options_Menu.music_slider.value = 10
										self.Options_Menu.music_slider.update()
										pygame.mixer.music.set_volume(self.Options_Menu.music_slider.value/100)										
										self.Main_Menu.main_menu_intro_video.toggle_pause()

									elif self.clicked_button == 'quit':
										self.starting_the_game = False
										self.is_in_country_selection_screen = False
										self.pygame.time.delay(200)	
								else:
									if self.clicked_button == 'back':
										self.is_options_menu_open = False

									resolution_to_save = None
									if self.clicked_button == 'resolution_2560x1440':
										resolution_to_save = (2560,1440)
									elif self.clicked_button == 'resolution_1920x1080':
										resolution_to_save = (1920,1080)
									elif self.clicked_button == 'resolution_1600x900':
										resolution_to_save = (1600,900)
									elif self.clicked_button == 'resolution_1440x900':
										resolution_to_save = (1440,900)
									elif self.clicked_button == 'resolution_1280x1024':
										resolution_to_save = (1280,1024)

									if resolution_to_save != None:
										with open(f'{self.exe_folder}\\settings.txt', 'r') as file:
											configs = json_load(file)

										configs["screen_width"], configs["screen_height"] = resolution_to_save

										with open(f'{self.exe_folder}\\settings.txt', 'w') as file:
											json_dump(configs, file)									

				self.mouse_rect = self.pygame.Rect(self.mouse_pos, (1, 1))
				if self.is_in_esc_menu == False:
					self.Country_Selection_Screen.get_hovered_button(self.mouse_rect)
				else:
					self.hovered_button = self.ESC_Menu.get_hovered_button(self.mouse_rect, self.is_options_menu_open)
					self.ESC_Menu.hovered_button = self.hovered_button
					self.Options_Menu.hovered_button = self.hovered_button

				self.Country_Selection_Screen.music_player()

				if self.main_menu_music_started == False or self.pygame.mixer.music.get_busy() == False:
					self.main_menu_music_started = True
					self.pygame.mixer.music.play()				


			if self.is_in_game_screen == True:
				if to_draw == True:
					self.Screen_Manager.render_game_screen(self.Options_Menu.brightness_slider.value, self.is_in_esc_menu, self.is_options_menu_open, self.mouse_rect)
				
				to_draw = not to_draw

				if self.Game_Screen.Country_Focus_Tree.keep_game_paused == True:
					self.Game_Screen.Clock_UI.game_speed = 0
				
				for event in self.pygame.event.get():
					keys = self.pygame.key.get_pressed()	
					if event.type == QUIT:
						self.starting_the_game = False
						self.is_in_game_screen = False		
					if event.type == FPS_update:
						self.pygame.display.set_caption(str(round(clock.get_fps(), 2)))	
						continue						
					if event.type == date_tick:
						self.Game_Screen.Clock_UI.date_tick()
						self.Game_Screen.Country_Focus_Tree.current_day = self.Game_Screen.Clock_UI.current_day
						self.Game_Screen.Country_Focus_Tree.current_month = self.Game_Screen.Clock_UI.current_month
						self.Game_Screen.Country_Focus_Tree.current_year = self.Game_Screen.Clock_UI.current_year
						continue

					if self.is_options_menu_open == True:
						self.Options_Menu.interacting_with_UI_slides(event)

					if self.Game_Screen.Game_Introduction_Menu.is_menu_open == True:
						self.Game_Screen.Game_Introduction_Menu.text_scroll_bar.handle_event(event)
					elif self.Game_Screen.Decisions_Menu.is_menu_open == True:
						self.Game_Screen.Decisions_Menu.text_scroll_bar.handle_event(event)
					
					elif self.Game_Screen.Bottom_HUD.Legislative_Government_Menu.open_menu == 'head_of_state_menu_button':
						self.Game_Screen.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Head_Of_State_Menu.text_scroll_bar.handle_event(event)
					elif self.Game_Screen.Bottom_HUD.Legislative_Government_Menu.open_menu == 'parliament_menu_button':
						self.Game_Screen.Bottom_HUD.Legislative_Government_Menu.Legislative_Government_Parliament_Menu.text_scroll_bar.handle_event(event)

					if event.type == self.pygame.KEYDOWN:
						if keys[self.pygame.K_ESCAPE]:
							self.is_in_esc_menu = not self.is_in_esc_menu
							self.is_options_menu_open = False		
										
						elif self.Game_Screen.Research_Menu.receive_player_keybord_input == False:
							if keys[self.pygame.K_KP_PLUS]:
								if self.Game_Screen.Clock_UI.game_speed + 1 <= 5:
									self.Game_Screen.Clock_UI.game_speed += 1
							elif keys[self.pygame.K_KP_MINUS]:
								if self.Game_Screen.Clock_UI.game_speed - 1 >= 0:
									self.Game_Screen.Clock_UI.game_speed -= 1
							elif keys[self.pygame.K_1]:
								self.Game_Screen.Clock_UI.game_speed = 1
							elif keys[self.pygame.K_2]:
								self.Game_Screen.Clock_UI.game_speed = 2	
							elif keys[self.pygame.K_3]:
								self.Game_Screen.Clock_UI.game_speed = 3	
							elif keys[self.pygame.K_4]:
								self.Game_Screen.Clock_UI.game_speed = 4	
							elif keys[self.pygame.K_5]:
								self.Game_Screen.Clock_UI.game_speed = 5
							elif keys[self.pygame.K_SPACE]:
								self.Game_Screen.Clock_UI.game_speed = 0 if self.Game_Screen.Clock_UI.game_speed != 0 else 1

							if keys[self.pygame.K_9]:
								self.Game_Screen.Clock_UI.defcon_level += 1
							elif keys[self.pygame.K_0]:																													
								self.Game_Screen.Clock_UI.defcon_level -= 1
						
						else:
							if event.key == self.pygame.K_RETURN or event.key == self.pygame.K_KP_ENTER:
								self.Game_Screen.Research_Menu.apply_received_player_keybord_input = True
							elif event.key == self.pygame.K_BACKSPACE and len(self.Game_Screen.Research_Menu.received_player_keybord_input) > 0:
								self.Game_Screen.Research_Menu.received_player_keybord_input = self.Game_Screen.Research_Menu.received_player_keybord_input[:-1]
							elif str(event.unicode).isdecimal():
								self.Game_Screen.Research_Menu.received_player_keybord_input += event.unicode
					
					if event.type == self.pygame.MOUSEWHEEL:
						if event.y > 0:	
							self.Game_Screen.Earth_Map.scale_map(zoom_factor_change = 0.20, fps_freezing_avoidance = round(clock.get_fps(), 2), zoom_type = 'zoom_in')
						elif event.y < 0:
							self.Game_Screen.Earth_Map.scale_map(zoom_factor_change = -0.20, fps_freezing_avoidance = round(clock.get_fps(), 2), zoom_type = 'zoom_out')
					else:
						if keys[self.pygame.K_w]:																												
							self.Game_Screen.Earth_Map.map_position[1] += 10 if self.Game_Screen.Earth_Map.map_position[1] < 0 else 0
						if keys[self.pygame.K_a]:																													
							self.Game_Screen.Earth_Map.map_position[0] += 10
						if keys[self.pygame.K_s]:																													
							self.Game_Screen.Earth_Map.map_position[1] -= 10 if abs(self.Game_Screen.Earth_Map.map_position[1]) + self.screen_height < self.Game_Screen.Earth_Map.earth_daymap.get_height()*1.1 else 0
						if keys[self.pygame.K_d]:																													
							self.Game_Screen.Earth_Map.map_position[0] -= 10

					if self.Game_Screen.Earth_Map.map_position[0] > self.Game_Screen.Earth_Map.earth_daymap.get_width() or self.Game_Screen.Earth_Map.map_position[0] < -self.Game_Screen.Earth_Map.earth_daymap.get_width():
						self.Game_Screen.Earth_Map.map_position[0] = 0

					self.mouse_pos = self.pygame.mouse.get_pos()

					if event.type == self.pygame.MOUSEBUTTONUP:	
						pass
					
					elif event.type == self.pygame.MOUSEBUTTONDOWN:
						self.mouse_rect = self.pygame.Rect(self.mouse_pos, (1, 1))				

						if self.is_in_esc_menu == False:
							self.clicked_button = self.Game_Screen.get_clicked_button(self.mouse_rect)

							if self.clicked_button == None:
								clicked_map_location = (self.mouse_pos[0] - self.Game_Screen.Earth_Map.map_position[0], self.mouse_pos[1] - self.Game_Screen.Earth_Map.map_position[1])
								print(clicked_map_location)

						else:
							self.clicked_button = self.ESC_Menu.get_clicked_button(self.mouse_rect, self.is_options_menu_open)
							if self.clicked_button != 'none' and self.clicked_button != None:
								if self.is_options_menu_open == False:
									if self.clicked_button == 'options':
										self.is_options_menu_open = True

									elif self.clicked_button == 'main_menu':
										self.is_in_game_screen = False
										self.is_in_main_menu_screen = True
										self.is_in_esc_menu = False
										self.Options_Menu.music_slider.value = 10
										self.Options_Menu.music_slider.update()
										pygame.mixer.music.set_volume(self.Options_Menu.music_slider.value/100)										
										self.Main_Menu.main_menu_intro_video.toggle_pause()

									elif self.clicked_button == 'quit':
										self.starting_the_game = False
										self.is_in_game_screen = False
										self.pygame.time.delay(200)	
								else:
									if self.clicked_button == 'back':
										self.is_options_menu_open = False

									resolution_to_save = None
									if self.clicked_button == 'resolution_2560x1440':
										resolution_to_save = (2560,1440)
									elif self.clicked_button == 'resolution_1920x1080':
										resolution_to_save = (1920,1080)
									elif self.clicked_button == 'resolution_1600x900':
										resolution_to_save = (1600,900)
									elif self.clicked_button == 'resolution_1440x900':
										resolution_to_save = (1440,900)
									elif self.clicked_button == 'resolution_1280x1024':
										resolution_to_save = (1280,1024)

									if resolution_to_save != None:
										with open(f'{self.exe_folder}\\settings.txt', 'r') as file:
											configs = json_load(file)

										configs["screen_width"], configs["screen_height"] = resolution_to_save

										with open(f'{self.exe_folder}\\settings.txt', 'w') as file:
											json_dump(configs, file)									

				#--------------------------------------------------------------------------------------------------------#
				#--------------------------------------------------------------------------------------------------------#
				if self.Game_Screen.Game_Introduction_Menu.is_menu_open == False:
					mouse_buttons = pygame.mouse.get_pressed()
					# Check if the right mouse button is being held down
					if mouse_buttons[2]:	
						self.mouse_end_pos = self.mouse_pos
						
						difference_x = self.mouse_start_pos[0] - self.mouse_end_pos[0]
						difference_y = self.mouse_start_pos[1] - self.mouse_end_pos[1]

						original_difference_x = difference_x
						original_difference_y = difference_y

						difference_x -= self.last_difference_x
						difference_y -= self.last_difference_y

						self.last_difference_x = original_difference_x
						self.last_difference_y = original_difference_y	

						if self.Game_Screen.Country_Focus_Tree.is_menu_open == True:						
							self.Game_Screen.Country_Focus_Tree.focus_movement_x -= difference_x
							self.Game_Screen.Country_Focus_Tree.focus_movement_y -= difference_y
						elif self.Game_Screen.Decisions_Menu.is_menu_open == True:
							if self.mouse_pos[0] >= self.screen_width/2 and self.mouse_pos[1] >= 158 * self.factor_y and self.mouse_pos[1] <= self.screen_height - 110 * self.factor_y:
								self.Game_Screen.Decisions_Menu.tree_icons_offset_x = min(self.Game_Screen.Decisions_Menu.decisions_tree_surface.get_width() - self.screen_width/2, max(0, self.Game_Screen.Decisions_Menu.tree_icons_offset_x + difference_x))
								self.Game_Screen.Decisions_Menu.tree_icons_offset_y = min(self.Game_Screen.Decisions_Menu.decisions_tree_surface.get_height() - self.screen_height - (158 + 110) * self.factor_y, max(0, self.Game_Screen.Decisions_Menu.tree_icons_offset_y + difference_y))	
						elif self.Game_Screen.Research_Menu.is_menu_open == True:
							self.Game_Screen.Research_Menu.icons_offset_x = min(self.Game_Screen.Research_Menu.surface_size_x - 1217*self.factor_x, max(0, self.Game_Screen.Research_Menu.icons_offset_x + difference_x))
							self.Game_Screen.Research_Menu.icons_offset_y = min(self.Game_Screen.Research_Menu.surface_size_y - 796*self.factor_y, max(0, self.Game_Screen.Research_Menu.icons_offset_y + difference_y))							
						else:
							self.Game_Screen.Earth_Map.map_position[0] -= difference_x 
							self.Game_Screen.Earth_Map.map_position[1] -= difference_y 
							if self.Game_Screen.Earth_Map.map_position[1] >= 0:
								self.Game_Screen.Earth_Map.map_position[1] = 0	
					else:
						self.mouse_start_pos = self.mouse_pos
						self.last_difference_x = 0
						self.last_difference_y = 0

				#--------------------------------------------------------------------------------------------------------#
				#--------------------------------------------------------------------------------------------------------#

				self.mouse_rect = self.pygame.Rect(self.mouse_pos, (1, 1))

				if self.is_in_esc_menu == False:
					self.hovered_rect = self.Game_Screen.Country_Overview.get_hovered_rect(self.mouse_rect)

					self.hovered_top_bar_button = self.Game_Screen.get_hovered_button(self.mouse_rect)
				else:
					self.hovered_button = self.ESC_Menu.get_hovered_button(self.mouse_rect, self.is_options_menu_open)
					self.ESC_Menu.hovered_button = self.hovered_button
					self.Options_Menu.hovered_button = self.hovered_button

				self.Country_Selection_Screen.music_player()


			clock.tick()

		self.pygame.quit()



Main(screen_width, screen_height, Pygame_Manager, pygame, clock, QUIT, date_tick, FPS_update, key_delay, display, screen, surface_alfa)

#American Civil War v0.003