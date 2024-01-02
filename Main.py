import sys
import os
from json import load as json_load, dump as json_dump


exe_folder = os.path.dirname(sys.argv[0])

screen_width = 1920
screen_height = 1080


import PygameManager
Pygame_Manager = PygameManager.Pygame(screen_width, screen_height)
pygame = Pygame_Manager.start_pygame()
clock, QUIT, ActionTick, FPS_update, key_delay, screen_update, display, screen, surface_alfa, territory_ownership_surface = Pygame_Manager.config_pygame()

import ScreenManager
import SoundsManager
import GenericUtilitys
import MenuManager
import CountriesManager


class Main:
	def __init__(self, screen_width, screen_height, Pygame_Manager, pygame, clock, QUIT, ActionTick, FPS_update, key_delay, screen_update, display, screen, surface_alfa) -> None:
		
		self.screen_width, self.screen_height = screen_width, screen_height
		self.Pygame_Manager = Pygame_Manager
		self.pygame = pygame
		self.clock, self.QUIT, self.ActionTick, self.FPS_update, self.key_delay, self.screen_update, self.display, self.screen, self.surface_alfa = clock, QUIT, ActionTick, FPS_update, key_delay, screen_update, display, screen, surface_alfa

		self.player_country = CountriesManager.Player_Country(None, None, None, None, None, [])

		self.countries = []

		self.exe_folder = os.path.dirname(sys.argv[0])
		self.leaders_image_dic = {}		
		self.flags_image_dic = {}
		self.national_spirits_image_dic = {}
		self.music_files_dic = {}
		self.load_assets()
		self.create_countries_default_frame()
		self.create_national_spirits()
		self.create_classes()
		self.setup_variables()
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
	def load_flags_images(self, flags_folder):	
		if os.path.isdir(flags_folder):
			for filename in os.listdir(flags_folder):
				if filename.endswith(".png") or filename.endswith(".jpg"):
					image_path = os.path.join(flags_folder, filename)
					image_name = os.path.splitext(filename)[0]
					self.flags_image_dic[image_name] = self.pygame.image.load(image_path).convert()
					self.flags_image_dic[image_name] = self.pygame.transform.smoothscale_by(self.flags_image_dic[image_name], (self.factor_x, self.factor_y))	
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
	def load_music_files(self, musics_folder):	
		for folder_name in os.listdir(musics_folder):
			folder_path = os.path.join(musics_folder, folder_name)
			if os.path.isdir(folder_path):
				for filename in os.listdir(folder_path):
					if filename.endswith(".wav") or filename.endswith(".ogg"):
						music_path = os.path.join(folder_path, filename)
						image_name = os.path.splitext(filename)[0]
						self.music_files_dic[image_name] = music_path						
	def load_assets(self):
		self.reference_screen_size_x = 1920
		self.reference_screen_size_y = 1080
		self.factor_x = screen_width / self.reference_screen_size_x
		self.factor_y = screen_height / self.reference_screen_size_y
		self.factor = self.factor_x * self.factor_y

		## ###
		self.gfx_folder = os.path.join(self.exe_folder, 'gfx')

		self.flags_folder = os.path.join(self.gfx_folder, 'flags')
		self.load_flags_images(self.flags_folder)

		##
		self.leaders_folder = os.path.join(self.gfx_folder, 'leaders')
		self.load_leaders_images(self.leaders_folder)
		self.generic_leader = self.leaders_image_dic['Portrait_NULL_Generic_Leader']

		##

		##
		self.interface_folder = os.path.join(self.gfx_folder, 'Interface')

		self.main_menu_backgound = self.pygame.image.load(os.path.join(self.interface_folder, 'main_menu.png')).convert_alpha()
		self.main_menu_backgound = self.pygame.transform.smoothscale(self.main_menu_backgound, (screen_width, screen_height))

		self.game_logo = self.pygame.image.load(os.path.join(self.interface_folder, 'game_logo.png')).convert_alpha()

		self.main_menu_menu_gui = self.pygame.image.load(os.path.join(self.interface_folder, 'menu_gui.png')).convert_alpha()
		self.main_menu_options_gui = self.pygame.image.load(os.path.join(self.interface_folder, 'options_gui.png')).convert_alpha()
		self.hovered_green_button_menu_image = self.pygame.image.load(os.path.join(self.interface_folder, 'hovered_green_button_menu_image.png')).convert_alpha()
		self.hovered_red_button_menu_image = self.pygame.image.load(os.path.join(self.interface_folder, 'hovered_red_button_menu_image.png')).convert_alpha()

		self.python_logo = self.pygame.image.load(os.path.join(self.interface_folder, 'python_logo.png')).convert_alpha()
		self.python_logo = self.pygame.transform.smoothscale_by(self.python_logo, (self.factor_x, self.factor_y))

		self.ESC_menu_background = self.pygame.image.load(os.path.join(self.interface_folder, 'ESC_menu_background.png')).convert_alpha()
		self.ESC_menu_background = self.pygame.transform.smoothscale_by(self.ESC_menu_background, (self.factor_x, self.factor_y))

		self.scenario_selection_folder = os.path.join(self.interface_folder, 'scenario_selection')

		self.scenario_selection_menu_gui = self.pygame.image.load(os.path.join(self.scenario_selection_folder, 'select_date_background.png')).convert_alpha()
		self.hovered_select_scenario_button_menu_image = self.pygame.image.load(os.path.join(self.scenario_selection_folder, 'hovered_select_scenario_button_menu.png')).convert_alpha()
		self.hovered_back_to_main_menu_button_menu_image = self.pygame.image.load(os.path.join(self.scenario_selection_folder, 'hovered_back_button_menu.png')).convert_alpha()

		
		self.country_selection_folder = os.path.join(self.interface_folder, 'country_selection')


		self.country_selection_background = self.pygame.image.load(os.path.join(self.country_selection_folder, 'country_selection_background.png')).convert_alpha()
		self.political_compass_image = self.pygame.image.load(os.path.join(self.country_selection_folder, 'political_compass.png')).convert_alpha()
		self.ideologies_CRT_overlay_effect = self.pygame.image.load(os.path.join(self.country_selection_folder, 'ideologies_CRT_overlay_effect.png')).convert_alpha()
		self.CRT_flag_overlay_effect = self.pygame.image.load(os.path.join(self.country_selection_folder, 'flag_overlay.png')).convert_alpha()

		self.country_info_display_background = self.pygame.image.load(os.path.join(self.country_selection_folder, 'country_info_display_background.png')).convert_alpha()
		self.national_spirits_background = self.pygame.image.load(os.path.join(self.country_selection_folder, 'national_spirits_background.png')).convert_alpha()
		self.national_spirits_background = pygame.transform.smoothscale_by(self.national_spirits_background, (self.factor_x, self.factor_y))

		self.hovered_create_map_button = self.pygame.image.load(os.path.join(self.country_selection_folder, 'hovered_create_map_button.png')).convert_alpha()
		self.hovered_select_flag_style_button_image = self.pygame.image.load(os.path.join(self.country_selection_folder, 'hovered_select_flag_style_button.png')).convert_alpha()
		self.hovered_select_national_spirit_button_image = self.pygame.image.load(os.path.join(self.country_selection_folder, 'hovered_select_national_spirit_button.png')).convert_alpha()
		
		self.hovered_laws_button_image = self.pygame.image.load(os.path.join(self.country_selection_folder, 'hovered_laws_button.png')).convert_alpha()

		self.blocked_full_right_side = self.pygame.image.load(os.path.join(self.country_selection_folder, 'blocked_full_right_side.png')).convert_alpha()
		self.blocked_all_laws = self.pygame.image.load(os.path.join(self.country_selection_folder, 'blocked_all_laws.png')).convert_alpha()
		self.blocked_select_national_spirit_button = self.pygame.image.load(os.path.join(self.country_selection_folder, 'blocked_select_national_spirit_button.png')).convert_alpha()
		self.blocked_select_flag_style_button = self.pygame.image.load(os.path.join(self.country_selection_folder, 'blocked_select_flag_style_button.png')).convert_alpha()
		self.blocked_create_map_button = self.pygame.image.load(os.path.join(self.country_selection_folder, 'blocked_create_map_button.png')).convert_alpha()


		self.ideas_folder = os.path.join(self.interface_folder, 'ideas')
		
		self.national_spirits_folder = os.path.join(self.ideas_folder, 'national_spirits')
		self.load_national_spirits(self.national_spirits_folder)
		
		##
		## ###


		##
		self.sounds_folder = os.path.join(self.exe_folder, 'Sounds')
		self.sounds_menu_folder = os.path.join(self.sounds_folder, 'menu')

		self.generic_hover_over_button_menu_sound = self.pygame.mixer.Sound(os.path.join(self.sounds_menu_folder, 'generic_hover_over_button_menu.ogg'))

		self.click_main_menu_sound = self.pygame.mixer.Sound(os.path.join(self.sounds_menu_folder, 'click_main_menu.ogg'))
		self.generic_click_menu_sound = self.pygame.mixer.Sound(os.path.join(self.sounds_menu_folder, 'generic_click_menu.ogg'))

		##

		##
		self.music_folder = os.path.join(self.exe_folder, 'Music')
		self.load_music_files(self.music_folder)

		##
	
	def create_countries_default_frame(self):
		self.USSR = CountriesManager.Country(
					'Leonid Ilyich Brezhnev',
				    self.leaders_image_dic['Portrait_USSR_Leonid_Ilyich_Brezhnev'], 
				    self.flags_image_dic['USSR'],
					'Union of Soviet Socialist Republics',
					'Marxist_Leninism',
					[self.music_files_dic['those_were_the_days']])
		self.USSR.country_ruling_party = 'Communist Party of the Soviet Union'
		self.USSR.country_government = 'Single-Party Socialist State'
		self.USSR.country_elections = 'Never'
		self.USSR.country_brief_history = """
As you  step  into  a  world  forever  altered  by  the
relentless efforts of  the  KGB,  the  very  fabric  of
society   quivers   beneath   the   sinister   art   of
manipulation and deception.

The KGB, ever vigilant,  works  tirelessly  to  maintain
the  illusion  of  stability, even  as  the  foundations
of the Soviet Union crumble beneath the surface.

The cracks in  the  facade  of  the  once-mighty  empire
have  grown  into  chasms, carefully  concealed  by  the
KGB's  propaganda,  threatening  to   engulf   not  only
the  Eastern   Bloc   but   the   entire   world   in  a
catastrophic maelstrom."""		
		
		self.CHI = CountriesManager.Country(
				    'Mao Zedong',
					self.leaders_image_dic['Portrait_CHI_Mao_Zedong'], 
				    self.flags_image_dic['CHI'],
					"People's Republic of China",
					'Command_Socialism',
					[self.music_files_dic['red_sun_in_the_sky']])

		self.CHI2 = CountriesManager.Country(
			'Mao Zedong',
			self.leaders_image_dic['Portrait_CHI_Mao_Zedong'], 
			self.flags_image_dic['CHI'],
			"People's Republic of China",
			'Command_Socialism',
			[self.music_files_dic['red_sun_in_the_sky']])	
		
		self.GNW = CountriesManager.Country(
					'Ernst Thalmann',
				    self.leaders_image_dic['Portrait_GNW_Ernst_Thalmann'], 
				    self.flags_image_dic['GNW'],
					'German National Worker State',
					'National_Syndicalism',
					[self.music_files_dic['roter_morgen_theme']])
		
		self.POR = CountriesManager.Country(
					'Antonio de Oliveira Salazar',
					self.leaders_image_dic['Portrait_POR_Antonio_de_Oliveira_Salazar'], 
				    self.flags_image_dic['POR'],
					'Estado Novo',
					'Corporautocracy',
					[self.music_files_dic['ressurreicao']])	
		
		self.KSA = CountriesManager.Country(
					'Faisal Bin Abdulaziz Al Saud',
					self.leaders_image_dic['Portrait_KSA_Faisal_Bin_Abdulaziz_Al_Saud'], 
				    self.flags_image_dic['KSA'],
					'Kingdom of Saudi Arabia',
					'Absolute_Monarchism',
					[self.music_files_dic['saudi_arabia_national_anthem']])
		
		self.GDR = CountriesManager.Country(
					'Erich Ernst Paul Honecker',
					self.leaders_image_dic['Portrait_GDR_Erich_Ernst_Paul_Honecker'], 
				    self.flags_image_dic['GDR'],
					'German Democratic Republic',
					'Consumer_Socialism',
					[self.music_files_dic['auferstanden_aus_ruinen']])	
		
		self.YUG = CountriesManager.Country(
					'Josip Broz Tito',
					self.leaders_image_dic['Portrait_YUG_Josip_Broz_Tito'], 
				    self.flags_image_dic['YUG'],
					'Socialist Federal Republic of Yugoslavia',
					'Authoritarian_Market_Socialism', 
					[self.music_files_dic['yugoslav_patriotic_song']])
		
		self.BRA = CountriesManager.Country(
					'Emilio Garrastazu Medici',
					self.leaders_image_dic['Portrait_BRA_Emilio_Garrastazu_Medici'], 
				    self.flags_image_dic['BRA'],
					'United States of Brazil',
					'Social_Statism',
					[self.music_files_dic['hino_da_independencia']])	
		
		self.CHL = CountriesManager.Country(
					'Augusto Pinochet',
					self.leaders_image_dic['Portrait_CHL_Augusto_Pinochet'], 
				    self.flags_image_dic['CHL'],
					'Chile',
					'Pinochetism',
					[self.music_files_dic['mi_general_augusto_pinochet']])	
		
		self.SWE = CountriesManager.Country(
					'Sven Olof Joachim Palme',
					self.leaders_image_dic['Portrait_SWE_Sven_Olof_Joachim_Palme'], 
				    self.flags_image_dic['SWE'],
					'Sweden',
					'Democratic_Socialism',
					[self.music_files_dic['national_anthem_of_sweden']])	
		
		self.WGR = CountriesManager.Country(
					'Willy Brandt',
					self.leaders_image_dic['Portrait_WGR_Willy_Brandt'], 
				    self.flags_image_dic['WGR'],
					'Federal Republic of Germany',
					'Social_Democracy', 
					[self.music_files_dic['national_anthem_of_west_germany']])
		
		self.USA = CountriesManager.Country(
					'Richard Nixon',
					self.leaders_image_dic['Portrait_USA_Richard_Nixon'], 
				    self.flags_image_dic['USA'],
					'United States of America',
					'Keynesianism',
					[self.music_files_dic['house_of_the_black_sun']])
		self.USA.country_ruling_party = 'Republican'
		self.USA.country_government = 'Federal Republic'
		self.USA.country_elections = '4 years'
		self.USA.country_brief_history = '''	
The land of the brave and the home of the free has been
usurped by a sinister force, an unseen hand that tugs at
the threads of democracy, trust, and truth.

The American dream, once a beacon of hope, now flickers
in the encroaching darkness, the stars and stripes that
once fluttered with pride now seem like mere illusions.

The fate of a nation hangs in the balance, as the clock
ticks relentlessly toward an uncertain future.

The relentless countdown of the cataclysm adds urgency
to the fate of the nation, perhaps the world, rests on
your shoulders.
'''
		
		self.SWI = CountriesManager.Country(
					'Federal Council',
					self.leaders_image_dic['Portrait_SWI_Federal_Council'], 
				    self.flags_image_dic['SWI'],
					'Switzerland',
					'Social_Liberalism',
					[self.music_files_dic['national_anthem_of_switzerland']])		
		
		self.TEX = CountriesManager.Country(
					'John Connally',
					self.leaders_image_dic['Portrait_TEX_John_Connally'], 
				    self.flags_image_dic['TEX'],
					'Texas',
					'Libertarian_Capitalism',
					[self.music_files_dic['come_and_take_it']])	
		
		self.PCO = CountriesManager.Country(
					'Hans Hermann Hoppe',
					self.leaders_image_dic['Portrait_PCO_Hans_Hermann_Hoppe'], 
				    self.flags_image_dic['PCO'],
					'Propertarian Commonwealth',
					'Anarcho_Capitalism',
					[self.music_files_dic['main_theme']])													
		
		self.countries.extend([self.USSR, self.CHI, self.GNW, self.POR, self.KSA, self.GDR, self.YUG, self.BRA, self.CHL, self.SWE, self.WGR, self.USA, self.SWI, self.TEX, self.PCO])
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

		#### COUNTRIES
		
		# USSR

		self.USSR_ideas_localization_folder = os.path.join(self.ideas_localization_folder, 'USSR')
		
		with open(os.path.join(self.USSR_ideas_localization_folder, 'KGB.txt'), 'r') as file:
			KGB_description = file.read()			
		self.kgb = CountriesManager.National_Spirit('KGB', self.national_spirits_image_dic['KGB'], KGB_description)

		with open(os.path.join(self.USSR_ideas_localization_folder, 'army_race_cost.txt'), 'r') as file:
			arms_race_cost_description = file.read()			
		self.arms_race_cost = CountriesManager.National_Spirit('Arms Race Cost', self.national_spirits_image_dic['arms_race_cost'], arms_race_cost_description)
		
		with open(os.path.join(self.USSR_ideas_localization_folder, 'ussr_economical_stagnation.txt'), 'r') as file:
			ussr_economical_stagnation_description = file.read()		
		self.ussr_economical_stagnation = CountriesManager.National_Spirit('Economical Stagnation', self.national_spirits_image_dic['ussr_economical_stagnation'], ussr_economical_stagnation_description)

		with open(os.path.join(self.USSR_ideas_localization_folder, 'ussr_huge_oil_reserves.txt'), 'r') as file:
			ussr_huge_oil_reserves_description = file.read()			
		self.ussr_huge_oil_reserves = CountriesManager.National_Spirit('Huge Oil Reserves', self.national_spirits_image_dic['ussr_huge_oil_reserves'], ussr_huge_oil_reserves_description)

		with open(os.path.join(self.USSR_ideas_localization_folder, 'limitless_science.txt'), 'r') as file:
			limitless_science_description = file.read()		
		self.limitless_science = CountriesManager.National_Spirit('Limitless Science', self.national_spirits_image_dic['limitless_science'], limitless_science_description)

		self.USSR.country_national_spirits.extend([self.kgb, self.arms_race_cost, self.ussr_economical_stagnation, self.ussr_huge_oil_reserves, self.limitless_science])
		self.USSR.country_culture = self.Ultraprogressive
		self.USSR.country_religion = self.Atheism


		# China

		self.CHI.country_national_spirits.extend([self.GENERIC])

		self.CHI.country_culture = self.Ultraprogressive
		self.CHI.country_religion = self.Ultraprogressive

		# German National Worker State

		self.GNW.country_national_spirits.extend([self.GENERIC])

		self.GNW.country_culture = self.Reactionary
		self.GNW.country_religion = self.Atheism


		# Estado Novo Portugal

		self.POR_ideas_localization_folder = os.path.join(self.ideas_localization_folder, 'POR')

		with open(os.path.join(self.POR_ideas_localization_folder, 'lusitanian_haven.txt'), 'r') as file:
			lusitanian_haven_description = file.read()
		self.lusitanian_haven = CountriesManager.National_Spirit('Lusitanian Haven', self.national_spirits_image_dic['lusitanian_haven'], lusitanian_haven_description)
		
		self.POR.country_national_spirits.extend([self.lusitanian_haven])
		self.POR.country_culture = self.Traditionalist
		self.POR.country_religion = self.Christianity			


		# Kingdom of Saudi Arabia

		self.KSA.country_national_spirits.extend([self.GENERIC])

		self.KSA.country_culture = self.Traditionalist
		self.KSA.country_religion = self.Islam		


		# German Democratic Republic

		self.GDR.country_national_spirits.extend([self.GENERIC])

		self.GDR.country_culture = self.Ultraprogressive
		self.GDR.country_religion = self.Atheism		


		# Socialist Federal Republic of Yugoslavia

		self.YUG.country_national_spirits.extend([self.GENERIC])

		self.YUG.country_culture = self.Centrist
		self.YUG.country_religion = self.Atheism			

		# United States of Brazil

		self.BRA.country_national_spirits.extend([self.GENERIC])

		self.BRA.country_culture = self.Conservative
		self.BRA.country_religion = self.Christianity		


		# Chile

		self.CHL.country_national_spirits.extend([self.GENERIC])

		self.CHL.country_culture = self.Reactionary
		self.CHL.country_religion = self.Christianity			


		# Sweden 

		self.SWE.country_national_spirits.extend([self.GENERIC])

		self.SWE.country_culture = self.Progressive
		self.SWE.country_religion = self.Christianity			


		# Federal Republic of Germany

		self.WGR.country_national_spirits.extend([self.GENERIC])

		self.WGR.country_culture = self.Progressive
		self.WGR.country_religion = self.Christianity			


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

		# Switzerland 

		self.SWI.country_national_spirits.extend([self.GENERIC])

		self.SWI.country_culture = self.Centrist
		self.SWI.country_religion = self.Christianity		


		# Texas

		self.TEX.country_national_spirits.extend([self.GENERIC])

		self.TEX.country_culture = self.Neoconservatism
		self.TEX.country_religion = self.Christianity		


		# Ancap

		self.PCO.country_national_spirits.extend([self.GENERIC])

		self.PCO.country_culture = self.Reactionary
		self.PCO.country_religion = self.Christianity			

	def create_classes(self):
		self.Sounds_Manager = SoundsManager.Sounds_Manager(self.generic_hover_over_button_menu_sound, self.click_main_menu_sound, self.generic_click_menu_sound)

		self.Options_Menu = MenuManager.Options_Menu(self.screen_width, self.screen_height, self.main_menu_options_gui, 
											   self.Sounds_Manager.generic_hover_over_button_menu_sound, self.Sounds_Manager.click_main_menu_sound, 
									   self.hovered_green_button_menu_image, self.hovered_red_button_menu_image, self.Sounds_Manager)
		self.ESC_Menu = MenuManager.ESC_Menu(self.screen_width, self.screen_height, self.ESC_menu_background, 
									   self.Sounds_Manager.generic_hover_over_button_menu_sound, self.Sounds_Manager.click_main_menu_sound, 
									   self.hovered_green_button_menu_image, self.hovered_red_button_menu_image, self.Options_Menu)

		self.Main_Menu = MenuManager.Main_Menu(self.screen_width, self.screen_height, self.pygame, self.game_logo, self.python_logo, self.main_menu_menu_gui, self.main_menu_options_gui, 
										 self.hovered_green_button_menu_image, self.hovered_red_button_menu_image, self.Sounds_Manager.generic_hover_over_button_menu_sound, 
										 self.Sounds_Manager.click_main_menu_sound)
	
		
		self.Scenario_Selection_Menu = MenuManager.Scenario_Selection_Menu(self.screen_width, self.screen_height, self.pygame, self.game_logo, self.python_logo,
									self.scenario_selection_menu_gui, self.hovered_select_scenario_button_menu_image, self.hovered_back_to_main_menu_button_menu_image,
									self.Sounds_Manager.generic_hover_over_button_menu_sound, self.Sounds_Manager.click_main_menu_sound)


		self.Country_Selection_Flag_Selection_Menu = MenuManager.Country_Selection_Flag_Selection_Menu(screen_width, screen_height, self.countries, 
											       self.Sounds_Manager.generic_hover_over_button_menu_sound, self.Sounds_Manager.generic_click_menu_sound)
		self.Country_Selection_National_Spirits_Selection_Menu = MenuManager.Country_Selection_National_Spirits_Selection_Menu(self.screen_width, self.screen_height, 
														       self.national_spirits_background, self.generic_national_spirits, self.Sounds_Manager.generic_hover_over_button_menu_sound,
															   self.Sounds_Manager.click_main_menu_sound)
		self.Country_Selection_Menu = MenuManager.Country_Selection_Menu(self.Country_Selection_Flag_Selection_Menu, self.Country_Selection_National_Spirits_Selection_Menu, 
								 	self.screen_width, self.screen_height, self.pygame, self.Sounds_Manager.generic_hover_over_button_menu_sound, self.Sounds_Manager.generic_click_menu_sound, 
									self.country_selection_background, self.country_info_display_background, self.political_compass_image, self.ideologies_CRT_overlay_effect,
									self.hovered_create_map_button, self.hovered_select_national_spirit_button_image, self.hovered_select_flag_style_button_image, 
									self.hovered_laws_button_image, self.generic_leader, self.CRT_flag_overlay_effect, self.blocked_select_national_spirit_button, 
									self.blocked_select_flag_style_button, self.blocked_create_map_button, self.blocked_full_right_side, self.blocked_all_laws)
		
		self.Screen_Manager = ScreenManager.Screen(self.pygame, self.display, self.screen, self.surface_alfa, self.player_country, self.Main_Menu, self.Country_Selection_Menu,
											self.Scenario_Selection_Menu, self.ESC_Menu, self.main_menu_backgound, 
											self.python_logo)
	def setup_variables(self):
		self.screen_center = (self.screen_width/2, self.screen_height/2)

		self.mouse_pos = self.pygame.mouse.get_pos()
		self.mouse_rect = self.pygame.Rect(self.mouse_pos, (2, 2))

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


	def main_loop(self):
		while self.starting_the_game:
			self.rects_of_active_UI = []


			if self.is_in_main_menu_screen == True:
				if self.main_menu_music_started == False or self.pygame.mixer.music.get_busy() == False:
					self.main_menu_music_started = True
					self.pygame.mixer.music.load(self.music_files_dic['main_theme'])
					self.pygame.mixer.music.play()

				for event in self.pygame.event.get():
					keys = self.pygame.key.get_pressed()	
					if event.type == QUIT:
						self.starting_the_game = False		
					if event.type == FPS_update:
						self.pygame.display.set_caption(str(round(clock.get_fps(), 2)))							
					if event.type == screen_update:
						self.Screen_Manager.render_main_menu(self.Options_Menu.brightness_slider.value, self.is_options_menu_open)

					if self.is_options_menu_open == True:
						self.Options_Menu.interacting_with_UI_slides(event)							

					self.mouse_pos = self.pygame.mouse.get_pos()	
					
					if event.type == self.pygame.MOUSEBUTTONUP:	
						pass
					
					elif event.type == self.pygame.MOUSEBUTTONDOWN:
						self.mouse_rect = self.pygame.Rect(self.mouse_pos, (2, 2))
						
						if self.is_options_menu_open == False:
							self.clicked_button = self.Main_Menu.get_clicked_button(self.mouse_rect)
							if self.clicked_button != 'none':
								if self.clicked_button == 'start':
									self.pygame.time.delay(100)
									self.is_in_scenario_selection_screen = True
									self.is_in_main_menu_screen = False
								elif self.clicked_button == 'quit':
									self.pygame.time.delay(200)
									self.starting_the_game = False
								elif self.clicked_button == 'options':
									self.pygame.time.delay(200)
									self.is_options_menu_open = True									
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


				self.mouse_rect = self.pygame.Rect(self.mouse_pos, (2, 2))

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
					self.pygame.mixer.music.load(self.music_files_dic['main_theme'])
					self.pygame.mixer.music.play()

				for event in self.pygame.event.get():
					keys = self.pygame.key.get_pressed()	
					if event.type == QUIT:
						self.starting_the_game = False		
					if event.type == FPS_update:
						self.pygame.display.set_caption(str(round(clock.get_fps(), 2)))							
					if event.type == screen_update:
						self.Screen_Manager.render_select_scenario_menu(self.Options_Menu.brightness_slider.value, self.is_in_esc_menu, self.is_options_menu_open)	

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
						self.mouse_rect = self.pygame.Rect(self.mouse_pos, (2, 2))

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

									elif self.clicked_button == 'quit':
										self.starting_the_game = False
										self.is_in_game_screen = False
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

				self.mouse_rect = self.pygame.Rect(self.mouse_pos, (2, 2))
				
				if self.is_in_esc_menu == False:
					self.hovered_button = self.Scenario_Selection_Menu.get_hovered_button(self.mouse_rect)
					self.Scenario_Selection_Menu.hovered_button = self.hovered_button
				else:
					self.hovered_button = self.ESC_Menu.get_hovered_button(self.mouse_rect, self.is_options_menu_open)
					self.ESC_Menu.hovered_button = self.hovered_button
					self.Options_Menu.hovered_button = self.hovered_button


			if self.is_in_country_selection_screen == True:
				for event in self.pygame.event.get():
					keys = self.pygame.key.get_pressed()	
					if event.type == QUIT:
						self.starting_the_game = False
						self.is_in_country_selection_screen = False		
					if event.type == FPS_update:
						self.pygame.display.set_caption(str(round(clock.get_fps(), 2)))							
					if event.type == screen_update:
						self.Screen_Manager.render_country_selection_menu(self.Options_Menu.brightness_slider.value, self.is_in_esc_menu, self.is_options_menu_open)	

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
						self.mouse_rect = self.pygame.Rect(self.mouse_pos, (2, 2))

						if self.is_in_esc_menu == False:
							if self.Country_Selection_Menu.is_flag_selection_menu_open == False:
								self.clicked_button = self.Country_Selection_Menu.get_clicked_button(self.mouse_rect)
								if self.clicked_button != 'none' and self.clicked_button != None:
									if self.clicked_button == 'create_map':
										self.is_in_country_selection_screen = False
										self.is_in_map_creation_screen = True
										self.is_in_esc_menu = False

										self.player_country = self.Country_Selection_Flag_Selection_Menu.selected_country
										self.countries.remove(self.Country_Selection_Flag_Selection_Menu.selected_country)

								elif self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == False:
									clicked_ideology = self.Country_Selection_Menu.get_clicked_ideology(self.mouse_rect)

								else:
									clicked_national_spirit = self.Country_Selection_National_Spirits_Selection_Menu.get_clicked_national_spirit(self.mouse_rect)
									self.Country_Selection_Menu.selected_selectable_national_spirits = self.Country_Selection_National_Spirits_Selection_Menu.selected_national_spirits

							else:
								self.clicked_flag = self.Country_Selection_Flag_Selection_Menu.get_clicked_flag(self.mouse_rect)
								if self.clicked_flag != None:
									self.pygame.mixer.music.fadeout(200)
									self.Country_Selection_Flag_Selection_Menu.flag_rects = []
									self.Country_Selection_Menu.flag_size = None
									self.Country_Selection_Menu.is_flag_selection_menu_open = False
									self.Country_Selection_Menu.selected_flag_image = self.clicked_flag
									self.Country_Selection_Menu.selected_selectable_national_spirits = []
									self.Country_Selection_National_Spirits_Selection_Menu.selected_national_spirits = []
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

									elif self.clicked_button == 'quit':
										self.starting_the_game = False
										self.is_in_game_screen = False
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

				self.mouse_rect = self.pygame.Rect(self.mouse_pos, (2, 2))
				

				if self.is_in_esc_menu == False:
					self.Country_Selection_Menu.mouse_pos = self.mouse_pos
					self.Country_Selection_Flag_Selection_Menu.mouse_rect = self.mouse_rect
					
					self.hovered_button = self.Country_Selection_Menu.get_hovered_button(self.mouse_rect)
					self.Country_Selection_Menu.hovered_button = self.hovered_button

					if self.Country_Selection_Menu.is_flag_national_spirits_selection_menu_open == True:
						self.hovered_selectable_national_spirit = self.Country_Selection_National_Spirits_Selection_Menu.get_hovered_national_spirit(self.mouse_rect)
						self.Country_Selection_National_Spirits_Selection_Menu.hovered_national_spirit = self.hovered_selectable_national_spirit
					else:
						self.hovered_ideology_rect = self.Country_Selection_Menu.get_hovered_ideology_rect(self.mouse_rect)
						self.Country_Selection_Menu.hovered_ideology_rect = self.hovered_ideology_rect

					self.hovered_national_spirit = self.Country_Selection_Menu.get_hovered_national_spirit(self.mouse_rect)
					self.Country_Selection_Menu.hovered_national_spirit = self.hovered_national_spirit
				else:
					self.hovered_button = self.ESC_Menu.get_hovered_button(self.mouse_rect, self.is_options_menu_open)
					self.ESC_Menu.hovered_button = self.hovered_button
					self.Options_Menu.hovered_button = self.hovered_button

				self.Country_Selection_Menu.music_player()

				if self.main_menu_music_started == False or self.pygame.mixer.music.get_busy() == False:
					self.main_menu_music_started = True
					self.pygame.mixer.music.play()				


			clock.tick()

		self.pygame.quit()



Main(screen_width, screen_height, Pygame_Manager, pygame, clock, QUIT, ActionTick, FPS_update, key_delay, screen_update, display, screen, surface_alfa)

