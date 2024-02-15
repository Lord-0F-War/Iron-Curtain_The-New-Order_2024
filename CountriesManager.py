class Research_Institute:
    def __init__(self, name, icon_image_name, total_workers_amount, workforce_quality):
        self.name = name
        self.icon_image_name = icon_image_name
        self.total_workers_amount = total_workers_amount

        self.workforce_quality = workforce_quality

        self.workers_assigned = {}


        self.hovered = False

class Political_Party:
    def __init__(self, party_name:str, popularity:float, ideology:list, parliament_seats:int, senate_seats:int, officialdom:bool, party_color:set):
        self.party_name = party_name

        self.popularity = popularity

        self.ideology = ideology

        self.parliament_seats = parliament_seats
        self.senate_seats = senate_seats

        self.officialdom = officialdom

        self.party_color = party_color

class Intelligency_Agency:
    def __init__(self, name, icon_image_name):
        self.name = name
        self.icon_image_name = icon_image_name

class Decision:
    def __init__(self, buttons, buttons_descriptions, buttons_icons, main_image, decision_description, x_pos, y_pos, requirements):
        self.buttons = buttons
        self.buttons_descriptions = buttons_descriptions
        self.buttons_icons = buttons_icons
        
        self.main_image = main_image
        self.decision_description = decision_description

        self.last_height = 0

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.requirements = requirements

        self.decision_on_tree_menu_icon = None

class National_Focus:
    def __init__(self, national_focus_name, national_focus_icon, national_focus_description, x_offset, completion_time, next_focus, decision_time = None, national_focus_path_selection_description = ''):
        
        self.focus_id = None
        self.national_focus_name = national_focus_name
        self.national_focus_icon = national_focus_icon
        self.national_focus_description = national_focus_description

        self.completion_time = completion_time
        self.decision_time = decision_time

        self.x_offset = x_offset
        self.y_offset = self.completion_time['day'] * 10 + self.completion_time['month'] * 300

        self.next_focus = next_focus

        self.selected_path = 0
        self.national_focus_path_selection_description = national_focus_path_selection_description

        self.is_active = True

class National_Spirit:
    def __init__(self, national_spirit_name, national_spirit_icon, national_spirit_description):
        self.national_spirit_name = national_spirit_name
        self.national_spirit_icon = national_spirit_icon
        self.national_spirit_description = national_spirit_description

        self.rect = None

        self.points_cost = 0


class Laws_Group:
    def __init__(self, group_name = str, laws = list, active_law_index = int):
        self.group_name = group_name
        self.laws = laws
        self.active_law_index = active_law_index

        self.total_value = 0

        for index, law in enumerate(self.laws):
            law.value = index + 1
            self.total_value += index + 1

        self.active_law:Law = self.laws[self.active_law_index]
        self.active_law_rating = self.calculate_rating()

    def calculate_rating(self):
        proportion = self.active_law.value / len(self.laws)
        rating = int(proportion * 100)

        return max(1, min(100, rating))
    
    def set_active_law(self, index):
        self.active_law_index = index
        self.active_law:Law = self.laws[self.active_law_index]
        self.active_law_rating = self.calculate_rating()

class Law:
    def __init__(self, name = str, description = str, description_complement = None) -> None:
        self.name = name
        self.description = description
        self.description_complement = description_complement

        self.value = 0


class Person:
    def __init__(self, name, portrait):
        self.name = name
        self.portrait = portrait


class Country:
    def __init__(self):
        self.country_name = None

        self.country_leader_name = None
        self.country_leader_image = None
        self.country_leader_title = None
        self.country_ruler_ideology = None
        
        self.country_capital_image = None
        
        self.country_flag_image = None
        
        self.country_music_playlist = None

        self.country_national_spirits = []
        self.country_culture = None
        self.country_religion = None

        # RESEARCH
        self.known_warfare_researches = ['TECH NAME 1']
        self.known_transport_researches = []
        self.known_science_researches = ['TECH NAME 1']
        self.known_technology_researches = []
        self.known_medical_researches = ['TECH NAME 1']
        self.known_society_researches = []

        self.Massachusetts_Institute_of_Technology_MIT = Research_Institute('Massachusetts Institute of Technology (MIT)', 'MIT', 250, 0.9)
        self.research_institutes = [self.Massachusetts_Institute_of_Technology_MIT]

        # FOCUS TREE
        self.country_focus_tree = {}

        # DECISIONS
        self.country_decisions_tree  = {}

        self.country_active_decisions = {}        

        # POLITICS
        self.politics_popularity = [4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16]
        self.culture_popularity = [7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14]
        self.religion_popularity = [11.11, 11.11, 11.11, 11.11, 11.11, 11.11, 11.11, 11.11, 11.11]        

        self.country_ruling_party = 'None'
        self.country_government = 'None'
        self.country_elections = 'None'

        self.country_brief_history = 'None'

        self.country_national_spirits_total_points = 0
        self.country_national_spirits_points_left = 0

        self.country_stability = 0

        self.country_war_support = 0

        self.country_party_popularity = 0
        self.weekly_head_of_state_popularity_data = []

        self.country_next_presidential_election = '12/01/1970'
        self.country_next_congessional_election = '12/29/1970'

        self.head_of_state_close_people = []

        self.country_government_gabinet = []
        
        partie_1 = Political_Party('Test 1 party', 50, [], 50, 25, True, (255,0,0))
        partie_2 = Political_Party('Test 2 party', 25, [], 25, 50, True, (0,255,0))
        partie_3 = Political_Party('Test 3 party', 25, [], 25, 25, True, (0,0,255))

        self.country_official_parties = [partie_1, partie_2, partie_3] 
        self.country_clandestine_parties = [] 

        self.total_parliament_seats = 0
        self.total_senate_seats = 0   

        self.parliament_head = None   
        self.parliament_parties_head = None

        self.senate_head = None
        self.senate_parties_head = None

        self.population_political_leaning = "None"


        self.laws_to_be_voted = []

        # DIPLOMACY
        self.diplomacy_rating = 0 

        # ARMY  
        self.military_rating = 0

        self.country_land_manpower = 0
        self.country_air_manpower = 0        
        
        self.army_staff = 0
        
        self.production_capacity_army = 0
        self.production_capacity_navy = 0
        self.production_capacity_air = 0
        self.production_capacity_special = 0
        self.production_capacity_total = f"{self.production_capacity_army} / {self.production_capacity_navy} / {self.production_capacity_air} / {self.production_capacity_special}" 
        
        # ECONOMY
        self.economy_rating = 0 
        
        self.treasury = 0
        self.debt = 0
        
        self.weekly_debt_to_gdp_data = []

        self.credit_rating = 0
        self.credit_stability = 0

        self.inflation = 0
        self.weekly_inflation_data = []
        
        self.currency_interest_rate = 0
        self.weekly_currency_interest_rate_data = []

        self.unemployment = 0

        self.country_GDP = 1
        self.weekly_country_GDP_data = []

        self.income = 0
        self.expenses = 0  

        self.country_taxation_laws_values = {
            'Inheritance Tax':                          {'value': [15],            'value_type': 'porcentage',      'monthly_revenue': 100_000_000_000,        'description': 'none'},
            'Income Tax':                               {'value': [0, 0, 0],       'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Real Estate Tax':                          {'value': [2.15],          'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Value Added Tax':                          {'value': [1],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Audiovisual Tax':                          {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Gun Tax':                                  {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Employee Social Security Payments':        {'value': [99.99],         'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Employer Social Security Payments':        {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Company Tax':                              {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Tax On Company Turnover':                  {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Tax On Redudancies':                       {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Tax On Large Fortunes':                    {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Vehicle Registration Tax':                 {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Airline Ticket Tax':                       {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Tax On Internet Access':                   {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Pet Tax':                                  {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Tax On Financial Transactions':            {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Tobacco Tax':                              {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Liquor Tax':                               {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Wine Tax':                                 {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Pornography Industry Tax':                 {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Deforestation Tax':                        {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Industrial Pollution Tax':                 {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Tax On Petroleum Products':                {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Tax On Gambling':                          {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'},
            'Tourist Tax':                              {'value': [0],             'value_type': 'porcentage',      'monthly_revenue': 0,        'description': 'none'}                                               
        }


        #   EXPENSES
        self.agriculture_expense = 0
        self.culture_expense = 0
        self.debt_interest_expense = 0
        self.defense_expense = 0
        self.economy_expense = 0
        self.education_expense = 0
        self.employment_social_expense = 0
        self.energy_expense = 0
        self.environment_expense = 0
        self.family_expense = 0
        self.foreign_affairs_expense = 0
        self.health_expense = 0
        self.homeland_security_expense = 0
        self.housing_expense = 0
        self.industry_expense = 0
        self.information_expense = 0
        self.justice_expense = 0
        self.miscellaneous_expense = 0
        self.religion_expense = 0
        self.research_expense = 0
        self.secret_services_expense = 0
        self.social_security_expense = 0
        self.sport_expense = 0
        self.tourism_expense = 0
        self.transport_expense = 0
        self.treasury_expense = 0
        self.unemployment_insurance_expense = 0

        # DOMESTIC
        self.domestic_rating = 0

        self.country_population = 1

        self.country_immigration = 0
        self.country_emigration = 0
        self.country_births = 0
        self.country_deaths = 0
        self.country_literacy_rate = 0
        self.country_poverty_rate = [0, 0, 0]

        self.military_approval_rating = 0
        self.domestic_approval_rating = 0
        self.midia_approval_rating = 0
        self.secret_service_approval_rating = 0
        self.politics_approval_rating = 0 

        self.internal_economy_rating = 0
        self.external_economy_rating = 0   


        self.country_intelligency_agency = Intelligency_Agency('Central Intelligence Agency', 'CIA')

        # LAWS

        self.country_immigration_policy = 'None'
        self.country_moral_code = 'None'

        self.due_process_types = {
            'Mandatory_Sentences': '-Implementing mandatory sentences for\ncertain offenses, limiting judicial\ndiscretion.\n\n',
            'Legal_Uniformity': '-Embracing a legal system that\nprioritizes uniformity, where the same\nset of rules and penalties applies to\nall cases.\n\n',
            'Flexible_Sentencing': '-Allowing for flexible sentencing with\nincreased judicial discretion.\nThis model permits judges to consider\nindividual circumstances when\ndetermining penalties, providing a more\nnuanced approach to justice.\n\n',
            'Adversarial_System': '-Opposing parties present their cases\nbefore an impartial adjudicator or jury.\n\n',
            'Restorative_Justice': '-Shifting towards restorative justice\nprinciples, this model emphasizes\nrehabilitation over punitive measures.\n\n',
            'Community_Courts': '-Establishing community courts that\nfocus on localized justice, involving\ncommunity members in the resolution of\noffenses.\n\n'
            }
        self.country_due_process_characteristics = self.due_process_types['Mandatory_Sentences'] + self.due_process_types['Legal_Uniformity'] + self.due_process_types['Flexible_Sentencing'] + self.due_process_types['Adversarial_System'] + self.due_process_types['Restorative_Justice'] + self.due_process_types['Community_Courts']

        #   POLITICAL LAWS
        
        self.political_parties_1 = Law('Total Ban on Political Parties',                    description = 'The formation and existence of political\nparties are completely prohibited.\n\nAny attempt to organize or support a\npolitical party is met with severe\npenalties.')
        self.political_parties_2 = Law('Single-Party System',                               description = 'Only one political party is allowed to\nexist, and it monopolizes political\npower.\n\nOpposition parties are banned, and\ndissent is not tolerated.')
        self.political_parties_3 = Law('State Approval Required\nMulti-Party System',       description = 'Multiple political parties are allowed,\nbut strict government approval is\nrequired.\n\nThe state has significant control over\nthe formation and activities of\npolitical parties.')
        self.political_parties_4 = Law('Limited Opposition',                                description = 'While multiple parties are allowed, the\ngovernment closely monitors the acts\nof opposition parties.\n\nThere are restrictions on political\ndissent, and opposition voices are\nconstrained.')
        self.political_parties_5 = Law('Free and Fair Elections',                           description = 'Political parties operate freely, and\nelections are conducted in a free and\nfair manner.\n\nThe democratic process ensures that\ncitizens can choose their representatives\nwithout undue influence.')
        self.political_parties_6 = Law('Inclusive Representation\nDiversity Enforced',      description = 'Political parties are required by law to\nensure inclusive representation that\nreflects the government diversity quota.\n\nMeasures, such as quotas or\naffirmative action, are mandatory and\nthe removal of already elected\npoliticians may happen if needed.')
        self.political_parties  =    Laws_Group('political_parties', [self.political_parties_1, self.political_parties_2, self.political_parties_3, self.political_parties_4, self.political_parties_5, self.political_parties_6], 0)
        
        self.religious_rights_1 = Law('Total Religious Oppression',                             description = 'Any expression of religious beliefs is\nstrictly prohibited, and individuals face\nsevere consequences for practicing or\nprofessing any religion.') 
        self.religious_rights_2 = Law('Limited Religious Practices\nState Approval Required',   description = 'Citizens are allowed limited religious\npractices, but strict government\napproval is required.\n\nThe state has significant\ncontrol over religious activities.')  
        self.religious_rights_3 = Law('State-Endorsed Religion',                                description = 'The state endorses a particular religion\nas the official faith, and adherence to\nthis religion is mandated.\n\nOther religious practices may be\nrestricted or suppressed.')  
        self.religious_rights_4 = Law('Official Faith',                                         description = 'The state considers a particular religion\nas the official faith but respects\nother religious practices without\nimposing any restrictions.')  
        self.religious_rights_5 = Law('State Neutrality',                                       description = 'The state maintains neutrality regarding\nreligion, with no official endorsement\nof any faith.\n\nAll citizens have the right to practice\ntheir religion without interference from\nthe government.')  
        self.religious_rights_6 = Law('Inclusive Religious Rights',                             description = 'The law actively protects religious\nminorities by granting them special\nrights and privileges')          
        self.religious_rights   =    Laws_Group('religious_rights', [self.religious_rights_1, self.religious_rights_2, self.religious_rights_3, self.religious_rights_4, self.religious_rights_5, self.religious_rights_6], 0)
        
        self.trade_unions_1 = Law('Trade Union Ban',                                        description = 'The formation and existence of trade\nunions are completely prohibited.\n\nAny attempt to organize or support a\ntrade union is met with severe penalties.') 
        self.trade_unions_2 = Law('State-Controlled Union',                                 description = 'Only one trade union is permitted to\nexist, and it monopolizes representation.\n\nAlternative unions are banned, and\ndissent within the labor movement is not\ntolerated.')  
        self.trade_unions_3 = Law('Restricted Union Activities\nState Approval Required',   description = 'Trade unions are allowed, but their\nactivities are restricted, and government\napproval is required for major actions\nsuch as strikes.\n\nUnions may face limitations on collective\nbargaining.')  
        self.trade_unions_4 = Law('Limited Collective Bargaining\nNegotiation Constraints', description = 'While trade unions have the right to\nengage in collective bargaining, there\nare constraints on the scope and nature\nof negotiations.\n\nCertain issues may be off-limits for\ndiscussion.')  
        self.trade_unions_5 = Law('Union Autonomy\nLimited Interference',                   description = 'Trade unions operate with a significant\ndegree of autonomy, and the government\nrefrains from excessive interference in\ntheir internal affairs.\n\nUnions have the freedom to make\ndecisions independently.')  
        self.trade_unions_6 = Law('Free Collective Bargaining',                             description = 'Trade unions have the freedom to engage\nin collective bargaining with no\nrestrictions.')  
        self.trade_unions       =    Laws_Group('trade_unions', [self.trade_unions_1, self.trade_unions_2, self.trade_unions_3, self.trade_unions_4, self.trade_unions_5, self.trade_unions_6], 0)
        
        self.public_protest_1 = Law('Total Ban on Public Protests',                         description = 'Public protests are completely prohibited,\nand any attempt to gather for\ndemonstrations or express dissent is met\nwith severe penalties.') 
        self.public_protest_2 = Law('Permitted Protests with\nGovernment Approval',         description = 'Protests are allowed, but individuals or\ngroups must obtain government approval\nbeforehand.\n\nThe government has significant control\nover the types of protests permitted and\nmay deny permission for certain causes.')  
        self.public_protest_3 = Law('Designated Protest Zones\nLimited Expression',         description = 'Protests are permitted but are confined\nto specific designated zones.\n\nAny protest outside these areas is\nconsidered illegal, limiting the impact\nof public expression.')  
        self.public_protest_4 = Law('Limited Gathering Size\nSmall Groups Allowed',         description = 'Small groups are allowed to gather for\nprotests, but there are limitations on\nthe number of participants.\n\nLarger gatherings may require special\npermits.')  
        self.public_protest_5 = Law('Controlled Assemblies',                                description = 'Public protests are allowed, but strict\nregulations govern the assembly.\n\nOrganizers must adhere to specific rules\nset by the government, and any violation\nmay result in legal consequences.')  
        self.public_protest_6 = Law('Peaceful Assembly\nMinimal Interference',              description = 'Peaceful assembly for protest purposes\nis allowed with minimal interference.\n\nThe government respects the right to\nprotest peacefully, and organizers are\nnot subjected to excessive regulations.')  
        self.public_protest_7 = Law('Freedom of Assembly\nUnrestricted',                    description = 'Citizens have the unrestricted right to\npeacefully assemble for protests.')  
        self.public_protest_8 = Law('Peacefully Armed Protest',                             description = 'Citizens have the right to engage in\npeaceful protests while openly carrying\nlegal firearms.\n\nThe law allows for the expression of\ndissent with the understanding that\nindividuals participating in the protest\ndo so peacefully and responsibly, without\nposing a direct threat to public safety.')         
        self.public_protest     =    Laws_Group('public_protest', [self.public_protest_1, self.public_protest_2, self.public_protest_3, self.public_protest_4, self.public_protest_5, self.public_protest_6, self.public_protest_7, self.public_protest_8], 0)
        
        self.gun_control_1 = Law('Total Firearm Ban',                                       description = 'All citizens are prohibited from owning\nor possessing firearms.\n\nThe government strictly enforces a\ncomplete ban on civilian firearm\nownership.') 
        self.gun_control_2 = Law('Exceptional Firearm Ownership\nLimited Permits',          description = 'Firearms are strictly regulated, and\nonly individuals meeting specific\ncriteria are granted permits for\nownership.\n\nThe process is rigorous, and the number\nof permits issued is limited.')  
        self.gun_control_3 = Law('Restricted Firearm Ownership\nSpecific Types Allowed',    description = 'Citizens are allowed to own firearms,\nbut there are significant restrictions\non a lot of types of firearms permitted.\n\nCertain categories of firearms may be\nprohibited, and ownership requires\nlicenses.')  
        self.gun_control_4 = Law('Limited Allowance\nHeavily Regulated',                    description = 'Citizens are allowed to own firearms,\nbut there are significant restrictions:\n\n-Certain categories of firearms may be\nprohibited.\n\n-Citizens are allowed to carry concealed\nfirearms, but only under specific\ncircumstances and with the issuance of\na concealed carry permit.\n\n-It is mandatory for gun owners to\nregister their firearms with the\ngovernment, the registration system\nincludes detailed records of firearm\ntransactions.\n\n-All firearm transactions, including\nprivate sales, require a comprehensive\nbackground check.\n\n-A mandatory waiting period is imposed\non firearm purchases to provide a\n"cooling-off" period.\n\n-There are restrictions on the maximum\ncapacity of firearm magazines.\n\n-Red flag laws allow for the temporary\nremoval of firearms from individuals.')  
        self.gun_control_5 = Law('Firearm Ownership by Default\nMinimal Restrictions',      description = 'Citizens are allowed to own firearms by\ndefault, with minimal regulations on the\ntypes of firearms permitted.\n\nBackground checks may be conducted,\nbut the process is streamlined to\nfacilitate easy firearm ownership.')  
        self.gun_control_6 = Law('Swiss-style Firearm Ownership',                           description = 'Citizens have the right to own firearms,\nand gun ownership is widespread,\nreflecting a well-regulated militia system.\n\nThe emphasis is on responsible firearm\nownership and participation in community\ndefense.')  
        self.gun_control_7 = Law('Constitutional Right\nLimited Regulations',               description = 'Firearm ownership is protected\nas a constitutional right,\nand regulations are minimal:\n\n-There is no mandatory waiting period for\nfirearm purchases.\n\n-No restrictions on magazine capacity,\nallowing for greater flexibility in\nownership.\n\n-While firearm registration is available,\nit is voluntary, and gun owners are not\ncompelled to register their firearms.\n\n-Mininal ban on weapon types or automatic\nweapons.\n\n-Limited explosive devices ownership.')  
        self.gun_control_8 = Law('Libertarian: Community-Defined',                          description = "The firearm regulations within a\njurisdiction are determined by each\nlocal community.\n\nCommunities have the autonomy to\nestablish their own rules and\nrestrictions based on the preferences\nand values of their residents.\n\nCitizens are permitted to possess\nexplosives and WMD, but their use must\nbe conducted with the explicit consent\nof the community or individuals within\nthe weapon's range, violations may face\nletal force.")        
        self.gun_control        =    Laws_Group('gun_control', [self.gun_control_1, self.gun_control_2, self.gun_control_3, self.gun_control_4, self.gun_control_5, self.gun_control_6, self.gun_control_7, self.gun_control_8], 0)
        
        self.privacy_rights_1 = Law('No Privacy Protection',                                description = 'Citizens have no explicit privacy rights,\nand the government entities have\nunrestricted access to personal\ninformation without limitations.') 
        self.privacy_rights_2 = Law('Limited Privacy Rights\nGovernment Oversight',         description = 'Some privacy rights exist, but the\ngovernment has broad authority to access\nand monitor personal information under\ncertain circumstances, with limited\noversight.')  
        self.privacy_rights_3 = Law('Conditional Privacy\nCase-by-Case Basis',              description = 'Privacy rights are granted on a\ncase-by-case basis, subject to government\napproval.\n\nThe burden is on individuals to justify\nthe need for privacy in specific\nsituations.')  
        self.privacy_rights_4 = Law('Basic Privacy Protection\nLimited Scope',              description = 'Citizens have basic privacy protections,\nbut the scope is limited.\n\nGovernment entities may still access\npersonal information under specific\nconditions.')  
        self.privacy_rights_5 = Law('Data Protection Laws\nLimited Enforcement',            description = 'Comprehensive data protection laws exist,\nbut enforcement is limited.\n\nCitizens may have rights on paper, but\nviolations may occur without significant\nconsequences for the infringing parties.')  
        self.privacy_rights_6 = Law('Privacy as a Fundamental Right',                       description = 'Privacy is recognized as a fundamental\nright protected by law.\n\nCitizens have the right to control their\npersonal information, and any\ninfringement is subject to legal\nconsequences.')  
        self.privacy_rights_7 = Law('Autonomous Control',                                   description = 'Individuals have autonomous control over\ntheir identity.\n\nAdvanced technologies, such as\ndecentralized systems and blockchain,\nempower users to manage and protect\ntheir personal information without relying\non central authorities.')         
        self.privacy_rights     =    Laws_Group('privacy_rights', [self.privacy_rights_1, self.privacy_rights_2, self.privacy_rights_3, self.privacy_rights_4, self.privacy_rights_5, self.privacy_rights_6, self.privacy_rights_7], 0)
        
        self.speach_rights_1 = Law('Total Speech Suppression',                              description = 'All forms of speech are strictly\nprohibited, and individuals face severe\nconsequences for expressing dissenting\nopinions or challenging official\nnarratives.') 
        self.speach_rights_2 = Law('Single-Party Speech\nMonopoly of Expression',           description = "Speech is controlled by a single\npolitical party, leading to a monopoly\non information dissemination.\n\nAlternative viewpoints are suppressed,\nand individuals are coerced into\nconforming to the ruling party's agenda.")  
        self.speach_rights_3 = Law('State-Approved Speech\nLimited Expression',             description = 'Speech is allowed only if it aligns with\nstate-approved narratives.\n\nIndividuals are restricted from\nexpressing dissenting opinions, and\nthere are consequences for challenging\nofficial viewpoints.')  
        self.speach_rights_4 = Law('Censored Speech\nRestricted Expression',                description = 'Speech is allowed, but there are\nsignificant restrictions on the content.\n\nCertain topics are off-limits, and\nindividuals may face consequences for\ndiscussing sensitive issues.')  
        self.speach_rights_5 = Law('Limited Speech Freedom\nGovernment Oversight',          description = 'Speech freedom exists to a certain\nextent, but the government has the\nauthority to oversee and regulate speech\nactivities.\n\nIndividuals may face legal consequences\nfor expressing certain viewpoints.\n\nIndividuals may self-censor to avoid\nrepercussions, leading to constrained\nexpression.')  
        self.speach_rights_6 = Law('Free and Fair Expression\nIndependent Opinions',        description = 'Individuals have the freedom to express\nthemselves independently without undue\ninterference.\n\nSpeech operates in a free and fair\nenvironment, contributing to a\nwell-informed public.')  
        self.speach_rights_7 = Law('First Amendment Speech Rights\nBroad Protections',      description = 'Speech, including "hate speech", is\nprotected under the principles of the\nFirst Amendment(or something alike).\n\nIndividuals enjoy broad protections for\nfreedom of expression, and the\ngovernment cannot restrict or penalize\nspeech based on its content, no matter\nhow offensive or controversial it may be.\n\nThis legal framework emphasizes the\nimportance of an open marketplace of\nideas, allowing for the free exchange\nof diverse and sometimes dissenting\nopinions without fear of government\ninterference.')          
        self.speach_rights      =    Laws_Group('speach_rights', [self.speach_rights_1, self.speach_rights_2, self.speach_rights_3, self.speach_rights_4, self.speach_rights_5, self.speach_rights_6], 0)
        
        self.press_rights_1 = Law('Total Press Censorship',                                 description = 'The government exercises complete\ncontrol over all forms of press, with\nstrict censorship and suppression of\nany content deemed contrary to official\nnarratives.') 
        self.press_rights_2 = Law('Single-Party Press',                                     description = "The press is controlled by a single\npolitical party, leading to a monopoly\non information dissemination.\n\nAlternative viewpoints are suppressed,\nand journalists are aligned with the\nruling party's agenda.")          
        self.press_rights_3 = Law('State-Approved Journalism',                              description = 'Journalism is allowed, but only if it\naligns with state-approved narratives.\n\nIndependent reporting is restricted, and\njournalists face consequences for\nchallenging official viewpoints.') 
        self.press_rights_4 = Law('Censored News',                                          description = 'News reporting is allowed, but there are\nsignificant restrictions on the content.\n\nCertain topics are off-limits, and\njournalists may face consequences for\ncovering sensitive issues.')  
        self.press_rights_5 = Law('Limited Press Freedom\nGovernment Oversight',            description = 'Press freedom exists to a certain extent,\nbut the government has the authority to\noversee and regulate media activities.\n\nJournalists may face legal consequences\nfor reporting on certain issues.')  
        self.press_rights_6 = Law('Free and Fair Reporting\nIndependent Journalism',        description = 'Journalists have the freedom to report\nindependently without undue interference:\n\n-Journalistic sources are protected by\nlaw, and journalists are shielded from\ndisclosing their sources.\n\n-Journalists and media outlets operate\nwith complete independence and editorial\nautonomy, the law protects them from\nexternal interference, allowing for\nfearless reporting and holding those in\npower accountable.')       
        self.press_rights       =    Laws_Group('press_rights', [self.press_rights_1, self.press_rights_2, self.press_rights_3, self.press_rights_4, self.press_rights_5, self.press_rights_6], 0)
        
        self.voting_rights_1 = Law('Total Voting Ban',                                      description = 'Citizens are denied the right to vote,\nand any attempt to ask for elections is\nmet with severe consequences.') 
        self.voting_rights_2 = Law('Restricted Voting Rights\nLimited Eligibility',         description = 'Voting rights are restricted to a select\ngroup, with eligibility determined by\nstrict criteria.\n\nCertain individuals, such as specific\ndemographics or political affiliations,\nare excluded from the electoral process.')  
        self.voting_rights_3 = Law('Conditional Voting Rights\nApproval Required',          description = 'Citizens must seek government approval\nto exercise their voting rights.\n\nThe process is burdensome, and the\ngovernment has the authority to deny\nvoting privileges based on arbitrary\ncriteria.')  
        self.voting_rights_4 = Law('Selective Voting Access\nDiscriminatory Practices',     description = 'Voting access is selectively granted,\nwith discriminatory practices that\ndisproportionately impact certain groups.\n\nBarriers such as ethnicity, literacy\ntests or poll taxes restrict voting\nrights for specific demographics.')  
        self.voting_rights_5 = Law('Equal Voting Rights\nUniversal Suffrage',               description = 'Citizens have equal voting rights, but\ncertain barriers, such as registration\nrequirements, may still exist.\n\nEfforts are made to ensure universal\nsuffrage, but challenges remain.')  
        self.voting_rights_6 = Law('Easy Access to Voting',                                 description = 'Citizens have the option to vote by mail,\nproviding a convenient (un-safe...)\nalternative to in-person voting.\n\nEarly voting is allowed, providing\nextended opportunities for citizens\n(or others...) to cast their ballots.\n\nCitizens are automatically registered\nto vote upon reaching voting age, ensuring\na high level of participation\n(sometimes way too high...).')  
        self.voting_rights_7 = Law('Direct Participatory Democracy',                        description = 'Governance decisions are made directly\nby the people through participatory\nmechanisms, such as town hall meetings\nor citizen assemblies.')  
        self.voting_rights_8 = Law('Libertarian Governance',                                description = 'Citizens have the freedom to choose\ntheir preferred governance model.\n\nwhether it be through traditional\nelections, appointment-based systems,\nmeritocracy, consensus-based governance,\ndirect participatory democracy, or any\nother form outlined in the libertarian\nlegal framework.\n\n\nCURRENT GOVERNMENT TYPE:\n', description_complement = 'country_government')        
        self.voting_rights      =    Laws_Group('voting_rights', [self.voting_rights_1, self.voting_rights_2, self.voting_rights_3, self.voting_rights_4, self.voting_rights_5, self.voting_rights_6, self.voting_rights_7, self.voting_rights_8], 0)

        self.political_laws_groups = [self.political_parties, self.religious_rights, self.trade_unions, self.public_protest, self.gun_control, self.privacy_rights, self.speach_rights, self.press_rights, self.voting_rights]

        self.head_of_state_apointment_type_1 = Law('Election', description = '') 
        self.head_of_state_apointment_type_2 = Law('Dictatorship', description = '') 
        self.head_of_state_apointment      =    Laws_Group('voting_rights', [self.head_of_state_apointment_type_1, self.head_of_state_apointment_type_2], 0)

        #   MILITARY LAWS

        self.conscription_1 = Law('Mandatory Conscription\nUniversal Service',              description = 'All citizens, regardless of gender or\nbackground, are required to undergo\nmandatory military service for a\ndesignated period.') 
        self.conscription_2 = Law('Compulsory Military/Civil Service\nDual Options',        description = 'Citizens are required to serve but have\nthe option to choose between military\nservice and alternative civil service.\n\nThis approach allows individuals to\nfulfill their conscription obligation in\nnon-military capacities.')  
        self.conscription_3 = Law('Short-Term Conscription\nLimited Duration',              description = 'Conscription is implemented for a short,\nspecific duration, typically during\nperiods of heightened security concerns.\n\nCitizens serve for a brief period before\nreturning to civilian life.')  
        self.conscription_4 = Law('Skill-Based Conscription\nOccupation Matching',          description = "Conscription is based on individuals'\nskills and qualifications, with the aim\nof matching individuals to specific roles\nwithin the military that align with their\nexpertise.\n\nConscription is centered around\neducational and skill development.\n\nIndividuals undergo training and\neducation that contributes to their\npersonal and professional growth while\nfulfilling their conscription obligation.")  
        self.conscription_5 = Law('No Conscription\nVolunteer-Only Military',               description = 'The country relies entirely on a\nvolunteer-based military, and there is\nno conscription.\n\nCitizens choose to enlist voluntarily,\nand military service is not a mandatory\nobligation.')  
        self.conscription                =    Laws_Group('conscription', [self.conscription_1, self.conscription_2, self.conscription_3, self.conscription_4, self.conscription_5], 0)                  
        
        self.women_in_service_1 = Law('Full Exclusion\nNo Women in Military Service',       description = 'Women are entirely excluded from\nmilitary service, and the armed forces\nare exclusively composed of male\npersonnel.') 
        self.women_in_service_2 = Law('Limited Support Roles\nNon-Combat Positions Only',   description = 'Women are allowed to serve in the\nmilitary, but their roles are restricted\nto non-combat positions.\n\nCombat roles remain exclusive to male\npersonnel.')  
        self.women_in_service_3 = Law('Equal Opportunities\nAll Roles Open to Women',       description = 'Women have equal opportunities to serve\nin all military roles, including combat\npositions.\n\nThere are no gender-based restrictions\non entry into any branch or unit.\n\nWomen undergo the same training as their\nmale counterparts, ensuring equality in\npreparation for military service.')  
        self.women_in_service_4 = Law('Forced Representation Policy',                       description = "The military is mandated to meet strict\ndiversity quotas at all levels, including\ncombat units and leadership positions.\n\nThis policy aims to reflect a specific\ndemographic balance but doesn't prioritize\nindividual qualifications or combat\nreadiness.\n\nTraining standards have been adjusted to\naccommodate a broader range of physical\nabilities, heavily compromising the\noverall readiness and effectiveness of\ncombat units.\n\nPromotion criteria are heavily influenced\nby achieving demographic quotas rather\nthan merit or combat performance.\n\nThe forced representation policy has led\nto internal strife and dissent within\nthe military ranks.\n\nOperational decisions are sometimes\ninfluenced more by political correctness\nthan by practical military considerations.\n\nThe military faces challenges to its\nreputation, as critics argue that the\nforced representation policy prioritizes\nsocial agendas over national security\ninterests.")  
        self.women_in_service            =    Laws_Group('women_in_service', [self.women_in_service_1, self.women_in_service_2, self.women_in_service_3, self.women_in_service_4], 0)
        
        self.training_level_1 = Law('No Formal Training Requirement\nUnregulated Entry',    description = 'Individuals are allowed to join the military\nwithout undergoing any standardized\ntraining.\n\nThis approach prioritizes quick\nrecruitment but may lead to a lack of\nstandardized skills and preparedness.')
        self.training_level_2 = Law('Minimal Training Requirements\nBasic Proficiency',     description = 'The military requires only minimal\ntraining for personnel, focusing on\nbasic proficiency in essential skills.\n\nThis approach allows for quick\nrecruitment and deployment but may\nresult in limited capabilities.') 
        self.training_level_3 = Law('Standardized Training\nCore Competencies',             description = 'All military personnel undergo\nstandardized training programs to ensure\ncore competencies.\n\nThis approach establishes a baseline of\nskills and knowledge across the force.')  
        self.training_level_4 = Law('Advanced Specialized Training\nExpertise Development', description = "Personnel receive advanced and\nspecialized training in specific roles,\ndeveloping expertise beyond basic\nrequirements.\n\nThis approach enhances the military's\noverall capabilities by having highly\nskilled individuals in specialized areas.")  
        self.training_level_5 = Law('Continuous Training Programs',                         description = 'Training is an ongoing process, with\ncontinuous programs designed to keep\npersonnel updated on evolving tactics,\ntechnologies, and strategic\nconsiderations:\n\n-Training incorporates realistic\nsimulations to mimic various operational\nscenarios.\n\n-Personnel undergo cross-training to\nacquire skills outside their primary\nroles, promoting versatility and\nflexibility within the military force.\n\n-Military personnel engage in training\nprograms with international partners to\npromote collaboration, share best\npractices, and enhance interoperability.\n\n-Military personnel receive specialized\ntraining for crisis response, emphasizing\nrapid deployment and effective\ndecision-making in high-pressure\nsituations.')  
        self.training_level_6 = Law('Special Forces Training\nElite Units Development',     description = 'Elite units undergo rigorous and\nspecialized training to excel in\nunconventional and high-risk operations:\n\n-Specialized training focuses on\ncountering terrorism and conducting\nanti-terrorism operations.\n\n-Training programs address cyber warfare\ncapabilities, ensuring that military\npersonnel are proficient in defending\nagainst cyber threats.')  
        self.training_level_7 = Law('Massive Specialized Training\nElite Force Expansion',  description = 'Focuses on expanding elite forces\nthrough extensive and intensive training\nprograms.\n\nThe goal is to create a large\nexceptionally skilled and specialized\nsegment within the military, capable of\nhandling complex and advanced missions\nat massive scales.')             
        self.training_level              =    Laws_Group('racial_admission', [self.training_level_1, self.training_level_2, self.training_level_3, self.training_level_4, self.training_level_5, self.training_level_6, self.training_level_7], 0)
        
        self.racial_admission_1 = Law('Racial Exclusion\nDiscriminatory Entry',             description = 'Individuals from certain racial or\nethnic backgrounds are explicitly\nexcluded from military service based on\ndiscriminatory admission policies.') 
        self.racial_admission_2 = Law('Race-Blind Admission\nMerit-Based Only',             description = 'An admission policy that is entirely\nrace-blind, focusing solely on\nmerit-based criteria for recruitment.\n\nThis approach prioritizes individual\nqualifications, skills, and capabilities\nwithout considering racial or ethnic\nbackground.')          
        self.racial_admission            =    Laws_Group('racial_admission', [self.racial_admission_1, self.racial_admission_2], 0)
        
        self.national_security_1 = Law('Totalitarian Surveillance\nIntrusive Monitoring',               description = "A policy allowing for total surveillance,\ninvolving comprehensive monitoring of\ncitizens' activities through advanced\ntechnological systems.") 
        self.national_security_2 = Law('Secret Intelligence Directorate',                               description = 'Establishment of a highly secretive\nintelligence directorate with\nconsiderable or total autonomy from the\ngovernment.\n\nThis agency operates with extensive\npowers, conducting intelligence operations\nboth domestically and internationally.\n\nIts operations are shrouded in secrecy,\nand it possesses significant influence,\noften operating independently of oversight\nmechanisms and might kill if nescessary.')  
        self.national_security_3 = Law('Coordinated Intelligence Council\nLimited Autonomous Powers',   description = 'Creation of a Coordinated Intelligence\nCouncil that oversees intelligence\noperations but with limitations on\nautonomous power.\n\nThis council collaborates with government\nagencies, providing valuable intelligence,\nbut its authority is subject to checks\nand balances to prevent unchecked\ninfluence and ensure alignment with\ngovernmental policies.')  
        self.national_security_4 = Law('Critical Protection',                                           description = 'Development of comprehensive plans to\naddress crises that pose threats to\nnational security:\n\n-Policies focused on protecting critical\ninfrastructure, such as energy,\ntransportation, and communication\nsystems, to ensure resilience against\nattacks and disruptions.\n\n-Formation of specialized\ncounter-terrorism units equipped to\nrespond swiftly to potential threats.\n\n-Implementation of early warning\nsystems to identify potential threats\nbefore they escalate.\n\n-Conducting regular emergency\npreparedness drills at various levels,\nincluding communities, schools, and\nworkplaces.')         
        self.national_security           =    Laws_Group('national_security', [self.national_security_1, self.national_security_2, self.national_security_3, self.national_security_4], 0)
        
        self.deployment_1 = Law('Ad Hoc Deployment\nReactive Response',                     description = 'Ad hoc deployment characterized by a\nreactive response to emerging situations\nwithout a structured plan.\n\nThis approach lacks pre-established\nprotocols, coordination, and may lead to\ninefficiencies in resource allocation.') 
        self.deployment_2 = Law('Limited Deployment\nPartial Resource Allocation',          description = 'Limited deployment involves the partial\nallocation of resources to address\nspecific situations.\n\nWhile there may be some preparedness,\nthe response is not comprehensive, and\ncoordination may be limited.')  
        self.deployment_3 = Law('Strategic Deployment\nPlanned Response',                   description = 'Strategic deployment involves a planned\nand coordinated response to anticipated\nsituations.\n\nResources are strategically allocated\nbased on assessments, and there is a\nlevel of preparedness to address\npotential challenges.')  
        self.deployment_4 = Law('Crisis Management Centers\nCentralized Command',           description = 'Centralized crisis management centers\nequipped with real-time information and\ncommunication capabilities.\n\nThese centers serve as command hubs for\ncoordinated deployment efforts, ensuring\nefficient decision-making and resource\nallocation.')        
        self.deployment                  =    Laws_Group('deployment', [self.deployment_1, self.deployment_2, self.deployment_3, self.deployment_4], 0)
        
        self.reserves_1 = Law('Scraping the Barrel\nDesperate Measures',                    description = 'This extreme measure involves\nconscripting individuals without regard\nfor age or physical condition, including\nthose who may be deemed unfit or totally\nunfit for military service.') 
        self.reserves_2 = Law('Broad Age Range',                                            description = 'Mobilization involving a broader age\nrange, encompassing individuals in their\nlate teens to middle age.\n\nThis approach aims to tap into a larger\npool of potential reservists while still\nkeeping some physical fitness and combat\nreadiness.')  
        self.reserves_3 = Law('Limited Age Range\nYoung and Able-Bodied',                   description = 'A reserve mobilization strategy that\nfocuses on a limited age range, typically\ntargeting young and able-bodied\nindividuals.\n\nThis approach seeks to ensure a\nphysically capable and trainable pool of\nreservists who can be quickly integrated\ninto military service.')  
        self.reserves_4 = Law('Health Assessments\nPhysical Fitness Criteria',              description = 'A mobilization strategy prioritizing\nindividuals in optimal physical health\nand capability is implemented.\n\nThis approach ensures that the\nconscripted reservists are in prime\ncondition, ready to meet the rigorous\ndemands of military service.')          
        self.reserves                    =    Laws_Group('reserves', [self.reserves_1, self.reserves_2, self.reserves_3, self.reserves_4], 0)
        
        self.economical_militarization_1 = Law('Civilian Economy',                                          description = 'A civilian economy where military\ninfluence is limited.\n\nResources are primarily allocated to\ncivilian industries, and military\nexpenditures are minimal, reflecting a\npeacetime focus on economic development\nand civilian needs.') 
        self.economical_militarization_2 = Law('Partial Military Integration',                              description = 'Partial economic militarization with the\nintegration of dual-purpose industries.\n\nCertain sectors serve both civilian and\nmilitary needs, allowing for flexibility\nin resource allocation during times of\nheightened tension or regional\ninstability.')  
        self.economical_militarization_3 = Law('Military-Industrial Complex',                               description = 'The development of a military-industrial\ncomplex where the defense sector is\nintricately linked with the civilian\neconomy.\n\nThis integration involves extensive\ncollaboration between government,\nmilitary, and private industries,\ndriving economic growth through\ndefense-related projects:\n\n-Adopting military Keynesianism as an\neconomic strategy, where defense\nspending is seen as a stimulus for\neconomic growth.\n\n-Investments in defense projects\ncontribute to job creation, innovation,\nand overall economic stimulation.')  
        self.economical_militarization_4 = Law('War Economy\nResource Reallocation',                        description = 'Transitioning to a war economy, with a\nsubstantial reallocation of resources\nfrom civilian sectors to military\nefforts.\n\nThe focus shifts from routine economic\nactivities to wartime production,\nemphasizing the immediate needs of\nnational defense.')  
        self.economical_militarization_5 = Law('Total War Mobilization\nFull-Scale Economy Commitment',     description = 'Full-scale total war mobilization\ninvolving the complete commitment of the\neconomy to the war effort.\n\nIndustries, labor, and resources are\nfully dedicated to supporting the\nmilitary, with civilian priorities\nsecondary to the exigencies of wartime.')  
        self.economical_militarization_6 = Law('War Communism\nTotal Economic Control',                     description = 'Adopting a form of war communism where\nthe government assumes total control\nover economic activities.\n\nThe entire economy is subordinated to\nthe needs of the military, with civilian\nlife heavily regulated to support the\nwar effort.')        
        self.economical_militarization   =    Laws_Group('economical_militarization', [self.economical_militarization_1, self.economical_militarization_2, self.economical_militarization_3, self.economical_militarization_4, self.economical_militarization_5, self.economical_militarization_6], 0)

        self.military_laws_groups = [self.conscription, self.women_in_service, self.training_level, self.racial_admission, self.national_security, self.deployment, self.reserves, self.economical_militarization]


        #   ECONOMICAL LAWS
        
        self.economic_system_1 = Law('Total Central Planning\nCommunism',                   description = 'A command economy characterized by\ntotal central planning, where the\ngovernment owns and controls all means\nof production.\n\nEconomic decisions, resource allocation,\nand production targets are determined\ncentrally, with no individual or private\nenterprise.') 
        self.economic_system_2 = Law('State-Controlled Economy\nSocialism',                 description = 'A system where the state plays a\nsignificant role in controlling key\nindustries and directing economic\nactivities, while private ownership may\nexist to some extent.')  
        self.economic_system_3 = Law('Social Economy',                                      description = 'A mixed economy combining elements of\nsocialism and capitalism.\n\nWhile private enterprise is allowed, the\nstate intervenes in specific sectors to\nensure social welfare, wealth\nredistribution, and the provision of\nessential services like healthcare and\neducation.')  
        self.economic_system_4 = Law('Corporatist State Control',                           description = 'While private ownership exist, the state\nplays a crucial role in directing\neconomic activities to achieve political\nand social objectives.\n\nThe emphasis is on collective national\ninterests over individual liberties,\noften prioritize autarky\n(economic self-sufficiency),\nprotectionism, and centralized economic\nplanning to support nationalistic goals.')
        self.economic_system_5 = Law('Keynesian Economy',                                   description = 'An economic system where capitalism is\nthe dominant force, but the government\nintervenes to correct market failures,\nensure fair competition, and address\nsocial issues.\n\nRegulatory policies and social safety\nnets play a significant role in this\nmanaged capitalism approach.\n\nIn times of economic downturn, Keynesian\npolicies aim to stimulate demand and\nstabilize the economy.')   
        self.economic_system_6 = Law('Neoliberalism\nMarket-Led Development',               description = 'An economic philosophy emphasizing\nmarket-led development, deregulation,\nand reducing government intervention.\n\nNeoliberalism promotes free markets,\nglobalization, and reducing barriers to\ntrade as mechanisms for economic growth.')  
        self.economic_system_7 = Law('Classical Liberalism\nLimited Government',            description = 'A philosophy of classical liberalism\nwhere economic freedom and limited\ngovernment are central tenets.\n\nThe emphasis is on protecting individual\nrights, property rights, and promoting\nfree trade, with the belief that these\nprinciples lead to prosperity.')  
        self.economic_system_8 = Law('Austrian School',                                     description = 'The Austrian School of Economics is a\nframework that places a strong emphasis\non methodological individualism and the\ndecentralization of economic\ndecision-making:\n\n-At the core of the Austrian School is\nthe subjective theory of value, which\nposits that value is inherently\nsubjective and varies among individuals.\nPrices, therefore, emerge from the\ninterplay of subjective valuations by\nmarket participants.\n\n-Economic patterns and market dynamics\nare viewed as emergent outcomes of\ncountless individual decisions.\n\n-Austrian economics views competition as\na dynamic and evolutionary process rather\nthan a static equilibrium.\n\n-Methodologically, the Austrian School\nrelies on praxeology, the study of human\naction.\nIt explores the implications of purposeful\nhuman behavior, and the deductive\nreasoning from axioms to derive economic\nlaws.') 
        self.economic_system        =    Laws_Group('economic_system', [self.economic_system_1, self.economic_system_2, self.economic_system_3, self.economic_system_4, self.economic_system_5, self.economic_system_6, self.economic_system_7, self.economic_system_8], 0)        
        
        self.trade_laws_1 = Law('Closed Borders',                                           description = 'Adopting a fortress economy strategy\nthat involves complete economic\nisolation from the international\ncommunity.') 
        self.trade_laws_2 = Law('High Tariffs\nLimited International Trade',                description = 'Implementing high tariffs and import\nrestrictions, restricting the flow of\ngoods across borders.\n\nWhile not completely closed, this\napproach places significant barriers to\ninternational trade and may result in\nlimited economic engagement with other\nnations.')  
        self.trade_laws_3 = Law('Moderate Tariffs\nBalanced Protection',                    description = 'Maintaining moderate tariffs to strike\na balance between protecting domestic\nindustries and allowing for\ninternational trade.\n\nThis approach seeks to heavily protect\ncertain sectors without imposing\nexcessive barriers that could hinder\neconomic exchange.')  
        self.trade_laws_4 = Law('Low Tariffs\nOpen to International Trade',                 description = 'Adopting a policy of low tariffs,\nreducing barriers to international\ntrade.\n\nThis approach encourages economic\nopenness and allows for the free flow of\ngoods across borders, fostering economic\ncooperation with trading partners.')  
        self.trade_laws_5 = Law('Unrestricted Trade',                                       description = 'Adopting a policy of open borders with\nminimal to none trade barriers.\n\nThis approach allows for unrestricted\ninternational trade, fostering a high\ndegree of economic globalization and\nencouraging the free flow of goods and\nservices.')  
        self.trade_laws             =    Laws_Group('trade_laws', [self.trade_laws_1, self.trade_laws_2, self.trade_laws_3, self.trade_laws_4, self.trade_laws_5], 0)
        
        self.taxation_system_1 = Law('Confiscatory Taxation\nExtreme Progressive Tax Rates',description = 'Implementing confiscatory taxation with\nextremely high progressive tax rates.\n\nThis approach involves disproportionately\ntaxing higher income brackets, often to\nthe point of near-confiscation, as a\nmeans of wealth redistribution.') 
        self.taxation_system_2 = Law('Highly Progressive Tax System\nGraduated Tax Rates',  description = 'Utilizing a highly progressive tax\nsystem with graduated tax rates.\n\nIn this structure, higher income levels\nface higher tax rates, but the\nprogression is more moderate compared\nto confiscatory taxation.')  
        self.taxation_system_3 = Law('Progressive Tax System\nBalanced Taxation',  description = 'Employing a moderate progressive tax\nsystem where tax rates increase gradually\nwith income.\n\nThis approach seeks a balance between\naddressing income inequality and\nmaintaining incentives for economic\nproductivity.')  
        self.taxation_system_4 = Law('Flat Tax Rate\nUniform Taxation',                     description = 'Adopting a flat tax rate system where\nall income levels are taxed at the same\npercentage.\n\nThis simple and uniform approach aims to\nreduce complexity in tax codes and\nprovide a more equal tax burden across\nincome groups.')  
        self.taxation_system_5 = Law('Consumption-Based Taxation\nSales or Value-Added Tax',description = 'Shifting towards consumption-based\ntaxation, such as a sales tax or\nvalue-added tax (VAT).\n\nThese taxes focus on consumption rather\nthan income, aiming to encourage savings\nand investment while generating revenue\nfrom spending.')  
        self.taxation_system_6 = Law('No Taxation\nTax-Free Model',                         description = 'Implementing a tax-free model, where no\ndirect taxes are levied on income,\nwealth, or consumption.\n\nThis approach relies on alternative\nrevenue sources or fiscal policies to\nfund government operations without\ntraditional taxation.')           
        self.taxation_system        =    Laws_Group('taxation_system', [self.taxation_system_1, self.taxation_system_2, self.taxation_system_3, self.taxation_system_4, self.taxation_system_5, self.taxation_system_6], 0)
        
        self.regulations_1 = Law('Authoritarian Regulations\nStrict State Control',         description = 'Enforcing authoritarian regulations\ncharacterized by strict state control.\n\nIn this model, regulatory decisions are\ncentralized, and compliance is enforced\nthrough punitive measures, emphasizing\na top-down approach to governance.') 
        self.regulations_2 = Law('Centralized Regulation\nSingle Decision-Making Body',     description = 'Establishing a centralized regulatory\nauthority with a single decision-making\nbody responsible for formulating and\nenforcing regulations.\n\nThis model concentrates regulatory power\nin a specific entity or agency.')  
        self.regulations_3 = Law('Bureaucratic Regulation\nHierarchical Oversight',         description = 'Adopting a bureaucratic regulatory\nstructure characterized by hierarchical\noversight.\n\nRegulatory decisions flow through\ndistinct levels of authority, and\ncompliance is monitored through a\nformalized chain of command within\nregulatory agencies.')  
        self.regulations_4 = Law('Decentralized Decision-Making\nLocal Autonomy',           description = 'Decentralizing regulatory decision-making\nto grant local autonomy.\n\nIn this model, regulatory decisions are\nmade at lower levels of government or\nwithin specific regions, allowing for\ngreater responsiveness to local needs\nand conditions.')  
        self.regulations_5 = Law('Self-Regulation\nIndustry-Led Oversight',                 description = 'Encouraging self-regulation within\nindustries, where businesses voluntarily\nestablish and adhere to industry-specific\nstandards and best practices.\n\nThis model relies on the assumption\nthat industry members are best equipped\nto understand and address their unique\nregulatory needs.')  
        self.regulations_6 = Law('Deregulation',                                            description = 'Pursuing a policy of deregulation to\nminimize the overall regulatory burden\non businesses and individuals.')         
        self.regulations            =    Laws_Group('regulations', [self.regulations_1, self.regulations_2, self.regulations_3, self.regulations_4, self.regulations_5, self.regulations_6], 0)
        
        self.monetary_policy_1 = Law('National Currency Monopoly\nExclusive Use of\nNational Currency',     description = 'Maintaining a strict national currency\nmonopoly, where only the official\ncurrency issued by the national\ngovernment is recognized as legal tender.\n\nAll transactions and financial\nactivities must be conducted using the\nnational currency exclusively.') 
        self.monetary_policy_2 = Law('Strict Exchange Controls\nLimited Currency Convertibility',           description = 'Implementing strict exchange controls\nthat limit the convertibility of the\nnational currency.\n\nThis approach restricts the ability of\nindividuals and businesses to freely\nexchange the national currency for other\ncurrencies, often in an effort to manage\ncapital flows.')  
        self.monetary_policy_3 = Law('Fixed Exchange Rate System\nPegging Currency Value',                  description = 'Adhering to a fixed exchange rate system,\nwhere the national currency is pegged to\nanother major currency or a basket of\ncurrencies.\n\nThis approach aims to provide stability\nin international trade and financial\ntransactions but may limit the\nflexibility of monetary policy.')  
        self.monetary_policy_4 = Law('Currency Competition\nOpen to Multiple Currencies',                   description = 'Allowing for currency competition, where\nmultiple currencies, including foreign\ncurrencies or cryptocurrencies, are\naccepted for transactions.\n\nThis model introduces a degree of\nmonetary freedom, providing individuals\nand businesses with currency choices.')  
        self.monetary_policy_5 = Law('Free Banking\nDecentralized Banking System',                          description = 'Implementing a system of free banking\nwhere multiple private banks issue their\nown currencies.\n\nThis model allows for decentralized\nbanking and competitive issuance of\ncurrency, offering a high degree of\nmonetary freedom.')  
        self.monetary_policy_6 = Law('Total Currency Freedom\nCurrency Competition\nWithout Restrictions',  description = 'Embracing total currency freedom, where\nindividuals and businesses are free to\ntransact in any currency or form of\nmoney, including privately issued\ncryptocurrencies.\n\nThis model maximizes monetary freedom,\nallowing for a diverse array of\ncurrencies to coexist in the economy.')       
        self.monetary_policy        =    Laws_Group('monetary_policy', [self.monetary_policy_1, self.monetary_policy_2, self.monetary_policy_3, self.monetary_policy_4, self.monetary_policy_5, self.monetary_policy_6], 0)
        
        self.property_rights_1 = Law('No Recognized Property Rights\nAbsence of Legal Ownership',           description = 'Operating in a system where there is no\nformal recognition of property rights.') 
        self.property_rights_2 = Law('Weak Property Rights\nLimited Legal Protection',                      description = 'Weak property rights with limited legal\nprotection.\n\nWhile ownership is recognized to some\nextent, legal safeguards are insufficient.')  
        self.property_rights_3 = Law('Conditional Property Rights\nGovernment Control or\nRestrictions',    description = 'Operating under conditional property\nrights, where the government imposes\nrestrictions or controls on property use.\n\nOwnership is subject to specific\nconditions or limitations, potentially\naffecting the ability of owners to\nfully exercise their property rights.')  
        self.property_rights_4 = Law('Statutory Property Rights\nLegal Recognition',                        description = 'Having statutory property rights with\nlegal recognition and protection.\n\nOwnership is codified in law, providing\nindividuals with a legal framework for\nacquiring, using, and transferring\nproperty.\n\nHowever, potential limitations or\nregulations still exist.')  
        self.property_rights_5 = Law('Absolute Property Rights\nUnrestricted Ownership and\nControl',       description = 'Affirming absolute property rights,\nwhere individuals have unrestricted\nownership and control over their property.\n\nThis model provides the highest level\nof legal protection, allowing owners to\nuse, transfer, and exclude others from\ntheir property without undue interference.')        
        self.property_rights        =    Laws_Group('property_rights', [self.property_rights_1, self.property_rights_2, self.property_rights_3, self.property_rights_4, self.property_rights_5], 0)
        
        self.nationalization_1 = Law('Unrestricted Government\nArbitrary Nationalization',                  description = 'Allowing unrestricted government seizure,\nwhere the government can arbitrarily\nnationalize private assets without\nspecific legal constraints.\n\nThis approach grants authorities broad\npowers to take control of private\nentities or resources without predefined\nconditions.') 
        self.nationalization_2 = Law('Conditional Nationalization\nDefined Criteria for Seizures',          description = 'Establishing conditional nationalization,\nwhere the government can seize assets\nbased on predefined criteria.\n\nThis model outlines specific\ncircumstances, such as non-compliance\nwith regulations or financial\ninstability, under which nationalization\nmay occur.')  
        self.nationalization_3 = Law('Compulsory Purchase\nGovernment Purchase\nwith Compensation',         description = 'Allowing compulsory purchase by the\ngovernment, where private assets can be\nacquired, but owners are entitled to\ncompensation.\n\nThis approach provides a legal framework\nfor government acquisition with a focus\non fair compensation for affected parties.')  
        self.nationalization_4 = Law('Legal Framework\nfor Nationalization\nLegislative Approval',          description = 'Requiring a legal framework for\nnationalization that includes legislative\napproval.\n\nNationalization can only occur through\nestablished legal procedures, ensuring\nthat the decision is subject to\ndemocratic and institutional checks and\nbalances.')  
        self.nationalization_5 = Law('Public Referendum\nfor Nationalization\nDirect Approval by Citizens', description = 'Mandating a public referendum for\nnationalization, requiring direct\napproval by citizens.\n\nThis approach ensures that significant\ndecisions on nationalization are subject\nto the collective will of the population.')  
        self.nationalization_6 = Law('Shareholder Approval\nfor Nationalization\nCorporate Decision',       description = "Requiring shareholder approval for\nnationalization in the case of publicly\ntraded companies.\n\nThis model ensures that decisions on\nnationalization are subject to the will\nof the company's owners.")  
        self.nationalization_7 = Law('Prohibition of Nationalization\nLegal Protection Against\nSeizure',   description = 'Prohibiting nationalization altogether,\nproviding legal protection against the\nseizure of private assets by the\ngovernment.\n\nThis model emphasizes the sanctity of\nprivate property rights and limits\ngovernment intervention in the ownership\nand control of private entities.')        
        self.nationalization        =    Laws_Group('nationalization', [self.nationalization_1, self.nationalization_2, self.nationalization_3,  self.nationalization_4, self.nationalization_5, self.nationalization_6, self.nationalization_7], 0)
        
        self.brand_rights_1 = Law('Totalitarian Intellectual\nProperty (IP) System\nStrict Corporate Control',  description = 'Operating under a totalitarian IP regime\nwhere corporations have extensive control\nover intellectual property.\n\nThis model heavily favors corporate\ninterests, enabling monopolies on ideas,\nstifling competition, and contributing\nto an environment where innovation is\ntightly controlled, allowing them to\nexercise exclusive privileges over their\nbrands.') 
        self.brand_rights_2 = Law('Strong IP Protections\nCorporate-Led Legislation',                           description = 'Enforcing strong IP protections, often\ninfluenced by corporate lobbying.\n\nThis model sees corporations actively\nshaping legislation to enhance their\ncontrol over brands and ideas,\npotentially limiting competition and\nhindering broader societal benefits,\nallowing corporations to establish\nvirtual monopolies through restrictive\nIP enforcement.')  
        self.brand_rights_3 = Law('Extensive Copyright\nand Patent Terms\nProlonged Corporate Control',         description = 'Implementing extensive copyright and\npatent terms that grant corporations\nprolonged control over their intellectual\nproperty.\n\nThis model can result in extended\nperiods of exclusivity, potentially\nlimiting the public domain and impeding\nthe flow of ideas.')  
        self.brand_rights_4 = Law('Moderate IP Protections\nBalanced Regulation',                               description = 'Maintaining moderate IP protections that\nstrike a balance between fostering\ninnovation and preventing monopolistic\npractices.')  
        self.brand_rights_5 = Law('Reform of IP Laws\nCitizen-Centric Changes',                                 description = 'Advocating for the reform of IP laws to\nbe more citizen-centric.\n\nThis model seeks changes that prioritize\npublic interests, foster fair\ncompetition, and encourage innovation\nfor the benefit of society rather than\nconcentrating power in corporate hands.')  
        self.brand_rights_6 = Law('IP Abolition Advocacy',                                                      description = 'This model, yet still utilitarian,\naligns with the belief that ideas\ncannot be treated as property in the\ntraditional sense and that IP laws hinder\nfree markets, restrict innovation, and\ndisproportionately favor corporate\ninterests over individual rights and\nsocietal progress.')  
        self.brand_rights_7 = Law('Complete IP Abolition',                                                      description = 'Advocating for the complete abolition\nof intellectual property (IP) rights,\nrooted in the ethical foundations of\nlibertarian thought.\n\nThis model asserts that ideas lack the\nethical characteristics of scarcity and\nexclusivity inherent in physical property.\n\nIn the words of Rothbard:\n"It is in the nature of human thought to\ncreate new ideas...\nSince ideas are indeed non-scarce, it is\nclear that no physical property right\ncan be legitimately attached to them."\n\nHowever, to safeguard against foreign\nentities patenting ideas generated\nwithin the libertarian framework and\nrestricting their use, a multifaceted\napproach is necessary.')   
        self.brand_rights           =    Laws_Group('brand_rights', [self.brand_rights_1, self.brand_rights_2, self.brand_rights_3, self.brand_rights_4, self.brand_rights_5, self.brand_rights_6, self.brand_rights_7], 0)
        
        self.public_services_1 = Law('Government Monopoly\nExclusive Public Provision',                     description = 'Operating with a government monopoly\nwhere public services are exclusively\nprovided by state agencies.\n\nThis model involves direct government\nownership, operation, and funding of\nservices with limited or no involvement\nfrom private entities.') 
        self.public_services_2 = Law('Government Limited-Monopoly\nLimited Private Participation',          description = 'Allowing a government-regulated monopoly\nwith limited private participation.\n\nIn this model, the government retains\ncontrol over public services but permits\nsome private entities to operate under\nstrict regulations and oversight.')  
        self.public_services_3 = Law('Public-Private Partnerships\nJoint Collaboration',                    description = 'Introducing public-private partnerships\n(PPPs) to foster joint collaboration.\n\nUnder this model, the government\npartners with private entities to\ndeliver public services, sharing\nresponsibilities and risks.\n\nRegulations guide the partnership to\nensure public interests are safeguarded.')  
        self.public_services_4 = Law('Market-Oriented Reforms\nEncouraging Competition',                    description = 'Enacting market-oriented reforms to\nencourage competition in public services.\n\nThis model introduces elements of choice\nand competition, allowing private\nentities to compete with government\nservices within a regulated framework.\n\nConsumer preferences play a significant\nrole in shaping service provision.')  
        self.public_services_5 = Law('Voucher System\nGovernment-Funded Choices',                           description = 'Implementing a voucher system where the\ngovernment funds individuals directly,\nallowing them to choose private\nproviders for essential services like\neducation or healthcare.\n\nThis model introduces a degree of\ncompetition while maintaining government\nfinancial support.')  
        self.public_services_6 = Law('Municipalization\nLocalized Ownership and Control',                   description = 'Transitioning towards municipalization\nwith an emphasis on local ownership and\nregulatory autonomy.\n\nIn this model, local governments take\nownership and control over key public\nservices, empowering communities to\nshape service provision according to\ntheir unique priorities and values.\n\nImportantly, this approach grants\nmunicipalities the authority to remove\nor modify private regulations, allowing\nfor greater flexibility in tailoring\nservices to meet the specific needs of\nthe community.')  
        self.public_services_7 = Law('Total Free Market\nPrivate Sector Dominance',                         description = 'Embracing a total free-market approach,\nwhere public services are entirely\nprovided by private entities.\n\nThis model relies on competition and\nmarket forces to drive efficiency,\ninnovation, and responsiveness to\nconsumer demands.')      
        self.public_services        =    Laws_Group('public_services', [self.public_services_1, self.public_services_2, self.public_services_3, self.public_services_4, self.public_services_5, self.public_services_6, self.public_services_7], 0)

        self.economical_laws_groups = [self.economic_system, self.trade_laws, self.taxation_system, self.regulations, self.monetary_policy, self.property_rights, self.nationalization, self.brand_rights, self.public_services]


        #   SOCIAL LAWS        

        self.emigration_immigration_1 = Law('Total Closed Borders',                                 description = 'Implementing a system of total closed\nborders, where movement across national\nboundaries is highly restricted.\n\nThis model places stringent controls on\nemigration and immigration, limiting the\nflow of people in and out of the country.') 
        self.emigration_immigration_2 = Law('Controlled Immigration\nLimited Outflow',              description = 'Adhering to controlled immigration\npolicies with selective entry criteria.\n\nUnder this model, the government\nregulates immigration, allowing entry\nbased on specific criteria such as\nskills, family reunification, or\nhumanitarian reasons, while still\nmaintaining restrictions on emigration.')  
        self.emigration_immigration_3 = Law('Semi-Open Borders\nManaged Flow with Restrictions',    description = 'Embracing semi-open borders, where\nthere is a managed flow of both\nimmigrants and emigrants.\n\nWhile certain regulations and controls\nare in place, this model allows for a\ndegree of flexibility in both\nimmigration and emigration.')  
        self.emigration_immigration_4 = Law('Merit-Based Immigration',                              description = 'Implementing a points-based system for\nimmigration, where individuals are\nevaluated based on predetermined\ncriteria such as skills, education, or\ncontributions, while not maintaining\nrestrictions on emigration.')  
        self.emigration_immigration_5 = Law('Open Borders\nFreedom of Movement for All',            description = 'Embracing the concept of open borders,\nwhere there are minimal restrictions on\nboth immigration and emigration.')  
        self.emigration_immigration_6 = Law('Community-Driven\nImmigration Policies',                description = 'Introducing a community-driven approach\nto immigration policies, where local\ncommunities have the autonomy to decide\nthe level of openness or restrictiveness\nat their borders.\n\n\nCurrent Policy:\n', description_complement='country_immigration_policy') 
        self.emigration_immigration     =    Laws_Group('emigration_immigration', [self.emigration_immigration_1, self.emigration_immigration_2, self.emigration_immigration_3, self.emigration_immigration_4, self.emigration_immigration_5, self.emigration_immigration_6], 0)
        
        self.minorities_rights_1 = Law('Persecution and Atrocities',                        description = 'Minorities face humanity crimes,\nincluding persecution, discrimination,\nand atrocities.\n\nThis abhorrent state reflects a complete\nabsence of respect for the basic dignity\nor natural rights.') 
        self.minorities_rights_2 = Law('Affirmative Privileges\nor Apartheid',              description = 'Under this framework, certain minorities\nor designated groups receive preferential\ntreatment and enhanced rights beyond\nthose of the majority:\n\n-The law establishes group-based\npreferences, prioritizing certain\nminorities or designated groups in\nvarious aspects of life, including\neducation, employment, and public\nservices.\n\n-Companies and organizations are forced\nto implement special hiring quotas,\npotentially favoring individuals from\nspecific groups over others.\n\n-The law may include provisions that\nrestrict certain types of speech deemed\noffensive or contrary to the ideology\nbehind the affirmative privileges.\n\n-Educational curricula may be revised\nto incorporate identity-based\nrequirements, potentially altering the\nfocus of education and introducing\nideological considerations.\n\n-The law may introduce differential legal\nprotections, providing enhanced legal\nsafeguards for individuals from\ndesignated groups.') 
        self.minorities_rights_3 = Law('Legal Protections\nBasic Recognition',              description = 'Providing legal protections to\nminorities, offering basic recognition\nand safeguards against overt persecution.\n\nThis level signifies a recognition of\nthe need to prevent explicit violations\nof minority rights through legal\nframeworks.')  
        self.minorities_rights_4 = Law('Equal Treatment\nNon-Discrimination Principle',     description = 'Emphasizing equal treatment for\nminorities, guided by the non\ndiscrimination principle.\n\nThis stage acknowledges that minorities\nshould be treated fairly and justly, and\nlaws are in place to prevent\ndiscriminatory practices.')  
        self.minorities_rights_5 = Law('Legal Equality\nFull Legal Equality',               description = 'Ensuring full legal equality, where\nminorities enjoy the same rights and\nprotections as the majority.')  
        self.minorities_rights_6 = Law('Natural Rights',                                    description = 'Under this perspective, individuals,\nincluding minorities, are entitled to\nlive free from coercion or violence, and\nproperty owners maintain the right to\nexclude others based on voluntary\nassociation.')  
        self.minorities_rights          =    Laws_Group('minorities_rights', [self.minorities_rights_1, self.minorities_rights_2, self.minorities_rights_3, self.minorities_rights_4, self.minorities_rights_5, self.minorities_rights_6], 0)
        
        self.welfare_1 = Law('Minimal State Involvement\nLimited Welfare Services',         description = 'Reflecting a minimal state involvement,\nthis model provides limited welfare\nservices.\n\nThe focus is on individual responsibility\nand a reduced role for the government in\nproviding financial assistance or social\nsupport.') 
        self.welfare_2 = Law('Emergency Aid Only\nTargeted Assistance in Crisis',           description = 'Offering emergency aid only, this model\nprovides targeted assistance during\ncrises or extreme circumstances.\n\nWelfare services are limited to\naddressing immediate needs rather than\noffering comprehensive, long-term\nsupport.')  
        self.welfare_3 = Law('Conditional Assistance',                                      description = 'Assistance is conditional and subject to\nregular assessments of financial need,\nthis model offers support to individuals:\n\n-Facing job loss.\n\n-Poor families with children.\n\n-Affordable housing options to\nindividuals or families facing poverty.\n\n-Food assistance programs to addresses\nnutritional needs for individuals or\nfamilies facing food insecurity.\n\n-Disability support programs.')  
        self.welfare_4 = Law('Social Safety Nets\nComprehensive Welfare System',            description = 'This model involves an extensive social\nsafety net that includes a wide range of\nwelfare services.\n\nThe government plays a significant role\nin providing comprehensive support for\ncitizens in various aspects of life,\nincluding income, healthcare, education,\nand social services.')            
        self.welfare                    =    Laws_Group('welfare', [self.welfare_1, self.welfare_2, self.welfare_3, self.welfare_4], 0)
        
        self.reproduction_1 = Law('State-Controlled Reproduction',                                  description = 'Individuals have limited or no autonomy\nin family planning decisions, and the\nstate determines aspects such as the\nnumber of children allowed, spacing\nbetween births, and even the selection\nof partners.') 
        self.reproduction_2 = Law('Sterilization Programs',                                         description = 'Introducing sterilization programs as a\ncoercive means of family planning.\n\nThis model involves government\ninterventions to limit or control\nfertility, often leading to irreversible\nprocedures without any individual\nconsent.')  
        self.reproduction_3 = Law('Population Control Policies',                                    description = 'Implementing population control policies\nwhere the government sets limits on\nfamily size.\n\nIndividuals may face penalties or\nincentives based on compliance with\nstate-mandated reproductive quotas.')  
        self.reproduction_4 = Law('Government Approval\nfor Reproduction\nControlled Licensing',    description = 'Requiring government approval for\nreproduction through a controlled\nlicensing system.\n\nIndividuals or couples must obtain\npermission from the state to have\nchildren, often based on factors such\nas financial stability or perceived\nfitness as parents.')  
        self.reproduction_5 = Law('Reproductive Rights\nFundamental Autonomy',                      description = 'Recognizing basic reproductive rights\nthat grant individuals fundamental\nautonomy in family planning decisions.\n\nThis model acknowledges the importance\nof personal choice and the right to\ndecide on matters related to reproduction.')  
        self.reproduction_6 = Law('Abortion as Medical Necessity\nStrict Legal Consequences',       description = 'Permitting abortion only when deemed\nmedically necessary.\n\nThis model restricts abortion only to\ncases where the health of the pregnant\nindividual is at significant risk, with\na narrow interpretation of medical\nnecessity.')  
        self.reproduction_7 = Law('Abortion as Reproductive Choice',                                description = 'Unrestricted autonomy in abortion\ndecisions, individuals have the right\nto make their choices without legal or\nsocietal barriers.')  
        self.reproduction_8 = Law('Libertarian Abortion Model\nNon-Aggression Principle',           description = "Grounded in the Non-Aggression\nPrinciple (NAP), the act of abortion\nmust be conceptually separated into the\nacts of (a) eviction of the fetus from\nthe womb; and (b) killing the fetus.\n\nTherefore, a woman may legally abort if\nit is the first act, but not in certain\ncircumstances that causes the second act\nsince its nature is a initiation of force.")        
        self.reproduction               =    Laws_Group('reproduction', [self.reproduction_1, self.reproduction_2, self.reproduction_3, self.reproduction_4, self.reproduction_5, self.reproduction_6, self.reproduction_7, self.reproduction_8], 0)
        
        self.morality_laws_1 = Law('Authoritarian Moral Code\nStrict Enforcement',          description = 'At the most authoritarian end, this\nmodel features a comprehensive moral\ncode enforced by the state.\n\nCitizens are obligated to adhere to\nspecific moral standards, and legal\nconsequences are imposed for violations.') 
        self.morality_laws_2 = Law('State-Endorsed Morality\nPrescribed Values',            description = 'Enforcing a set of state-endorsed moral\nvalues without strict regulation.\n\nWhile not as intrusive as strict\nenforcement, the state actively promotes\nspecific moral principles through\neducation, public discourse, and\ncultural initiatives.')  
        self.morality_laws_3 = Law('Moral Licensing\nLimited State Intervention',           description = 'Embracing moral licensing, the\ngovernment subtly nudges citizens toward\ncertain moral behaviors.\n\nPolicies may include incentives,\ndisincentives, and public awareness\ncampaigns designed to guide individuals\ntoward socially accepted moral norms.')  
        self.morality_laws_4 = Law('Legal Minimalism\nMorality as a Private Matter',        description = 'Adopting a legal minimalist approach,\nthis model views morality as a private\nmatter.\n\nThe state refrains from intervening in\npersonal moral choices as long as they\ndo not violate the rights of others.')  
        self.morality_laws_5 = Law('Libertarian System',                                    description = 'This model envisions a system where\nindividuals voluntarily associate within\ncommunities based on shared values,\nnorms, and agreements.\n\n\nCurrent Moral Code:\n', description_complement = 'country_moral_code')          
        self.morality_laws              =    Laws_Group('morality_laws', [self.morality_laws_1, self.morality_laws_2, self.morality_laws_3, self.morality_laws_4, self.morality_laws_5], 0)
        
        self.drug_laws_1 = Law('Zero-Tolerance Policy\nStrict Prohibition',                 description = 'At the most restrictive end, this model\nimplements a zero-tolerance policy,\nstrictly prohibiting the production,\nsale, possession, and use of all drugs.\n\nLegal consequences, including severe\npenalties and incarceration, are\nenforced for any involvement with\ncontrolled substances.') 
        self.drug_laws_2 = Law('Decriminalization of\nPersonal Use\nReduced Penalties',     description = 'Decriminalizing the personal use of\ndrugs, shifting the focus from criminal\npenalties to civil fines or treatment\nprograms for individuals found in\npossession of small quantities for\npersonal use.\n\nThe legal system treats drug use as a\npublic health issue rather than a\ncriminal offense.')  
        self.drug_laws_3 = Law('Limited Legal Access\nfor Medical Purposes',                description = 'Allowing limited legal access to certain\ndrugs for medical purposes under strict\nregulations.\n\nThis model permits medical professionals\nto prescribe and administer drugs to\npatients for specific therapeutic\npurposes while maintaining strict\ncontrols.')  
        self.drug_laws_4 = Law('Regulated Medical and\nRecreational Use',                   description = 'Implementing a dual-access system where\ncertain drugs are available both for\nmedical and recreational use, subject to\nstringent regulations.\n\nThe legal framework allows for the\nregulated production, sale, and\nconsumption of drugs for both purposes.')  
        self.drug_laws_5 = Law('Decriminalization of\nLow-Risk Substances',                 description = 'Decriminalizing the possession and use\nof low-risk substances, emphasizing harm\nreduction strategies.\n\nThis model aims to redirect resources\nfrom criminalization to public health\ninitiatives, treating drug use as a\nsocial and health issue.')  
        self.drug_laws_6 = Law('Regulated Market for All Drugs\nStrict Controls',           description = 'A regulated market where all drugs are\navailable for purchase but subject to\nstrict controls, similar to the\nregulatory framework for alcohol and\ntobacco.\n\nThis model acknowledges individual\nautonomy while emphasizing harm\nreduction measures.')  
        self.drug_laws_7 = Law('Full Drug Legalization\nPersonal Autonomy',                 description = "Embracing full drug legalization,\nallowing individuals the autonomy to make\nchoices regarding drug use without fear\nof legal consequences.\n\nThis model views drug use as a personal\nchoice, and the legal system refrains\nfrom intervening in individuals' private\ndecisions.")          
        self.drug_laws                  =    Laws_Group('drug_laws', [self.drug_laws_1, self.drug_laws_2, self.drug_laws_3, self.drug_laws_4, self.drug_laws_5, self.drug_laws_6, self.drug_laws_7], 0)
        
        self.work_laws_1 = Law('Authoritarian Labor Control\nState-Driven Employment',              description = 'This model features state-driven\nemployment where the government\ndictates job assignments, wages, and\nworking conditions.\n\nIndividuals have limited autonomy in\nchoosing their professions, and the\nstate plays a dominant role in workforce\nmanagement.') 
        self.work_laws_2 = Law('Centralized Collective Bargaining\nState-Backed Union Regulation',  description = 'This model involves centralized\nnegotiations between labor unions and\nthe state or large corporations to\nestablish industry-wide standards for\nwages, working hours, and benefits.')  
        self.work_laws_3 = Law('Mandatory Minimum Wage\nand Working Hours\nRegulatory Safeguards',  description = 'Introducing mandatory minimum wage and\nworking hour regulations to safeguard\nworkers against exploitation.\n\nGovernment intervention sets baseline\nstandards for compensation and working\nconditions to ensure a level playing\nfield.')  
        self.work_laws_4 = Law('Worker Protections\nand Regulations\nBalanced Employment Laws',     description = 'Establishing comprehensive worker\nprotections and regulations to ensure\nfair treatment and safe working\nconditions.\n\nThis model seeks a balance between\nsafeguarding workers rights and allowing\nflexibility for employers to manage\ntheir businesses within a regulatory\nframework.')  
        self.work_laws_5 = Law('Employment Contracts\nIndividual Agreements',                       description = 'Employment terms, including wages and\nworking conditions, are determined\nthrough negotiations between employers\nand employees, fostering flexibility in\nthe job market.')  
        self.work_laws_6 = Law('Free Market\nNo Government Intervention',                           description = 'In this model, employers and employees\nengage in voluntary agreements without\nregulatory oversight, relying on market\nforces to shape employment relationships.')        
        self.work_laws                  =    Laws_Group('work_laws', [self.work_laws_1, self.work_laws_2, self.work_laws_3, self.work_laws_4, self.work_laws_5, self.work_laws_6], 0)
        
        self.justice_system_1 = Law('Totalitarian Justice\nState Dominance',                description = 'The state has absolute control over\nlegal proceedings, it determines guilt,\nimposes sentences without due process,\nand tightly controls every aspect of\nthe justice system.') 
        self.justice_system_2 = Law('Authoritarian Legal Oversight\nLimited Due Process',   description = 'Moving towards limited due process, the\nstate holds significant power in legal\nproceedings, and individual rights may\nbe curtailed in the interest of\nmaintaining order.')  
        self.justice_system_3 = Law('Balanced Legal Proceedings',                           description = 'Moving towards due process, the system\ncharacteristics are:\n\n', description_complement = 'country_due_process_characteristics')  
        self.justice_system_4 = Law('Polycentric Legal Systems\nCompetitive Legal Orders',  description = "Advocating for polycentric legal systems\nwhere multiple legal orders coexist and\ncompete for adherence.\n\nIn this model, individuals choose legal\nsystems based on their preferences,\nfostering competition among legal\nproviders.\n\nThe country's system characteristics are:\n\n", description_complement = 'country_due_process_characteristics')  
        self.justice_system_5 = Law('Libertarian Polycentric\nLegal System',                description = "Individuals have the freedom to choose\nfrom competing private arbitration and\nmediation services, all courts must\nadhere to a common ethical foundation,\nguided by the Non-Aggression Principle,\nhowever communities may define\nadditional crimes and change sentences.\n\nThe country's system characteristics are:\n\n", description_complement = 'country_due_process_characteristics')          
        self.justice_system             =    Laws_Group('justice_system', [self.justice_system_1, self.justice_system_2, self.justice_system_3, self.justice_system_4, self.justice_system_5], 0)
        
        self.environmental_1 = Law('Ecologist Totalitarianism',                                 description = 'The government dictates conservation\nmeasures, land use, and resource\nallocation without individual or\ncommunity input.') 
        self.environmental_2 = Law('Authoritarian Resource\nManagement',                        description = 'This model focuses on strict regulations\nand controls to address environmental\nconcerns, often with limited\nconsideration for individual property\nrights.')  
        self.environmental_3 = Law('Regulated Sustainable Practices\nTop-Down Oversight',       description = 'Shifting towards regulated sustainable\npractices, this model emphasizes\ntop-down oversight to ensure\nenvironmentally responsible actions.\n\nThe state establishes regulations\ngoverning resource use and environmental\npractices with an aim for sustainability.')  
        self.environmental_4 = Law('Mixed Environmental\nManagement\nLimited Decentralization', description = 'Incorporating limited decentralization,\nthis model features a mix of centralized\nand decentralized environmentals\nmanagement.\n\nWhile the state sets overarching\npolicies, some decision-making authority\nis delegated to local or regional\nentities.')  
        self.environmental_5 = Law('Property Rights-Centric\nApproach',                         description = 'Advocating for a property rights-centric\napproach where individuals are stewards\nof their own land.\n\nThis model encourages individuals,\ncommunities, and businesses to work\ntogether voluntarily to address\nenvironmental challenges without\ncoercive measures but the state might\ninterfere if necessary.')  
        self.environmental_6 = Law('Externalities-Driven\nConservation',                        description = 'At the libertarian end of the spectrum,\nthis model emphasizes individual\nresponsibility and accountability for\nexternalities.\n\nThe idea is that individuals or entities\nshould be held accountable for the\nnegative externalities they impose on\nothers such as pollution.')       
        self.environmental              =    Laws_Group('environmental', [self.environmental_1, self.environmental_2, self.environmental_3, self.environmental_4, self.environmental_5, self.environmental_6], 0)

        self.social_laws_groups = [self.emigration_immigration, self.minorities_rights, self.welfare, self.reproduction, self.morality_laws, self.drug_laws, self.work_laws, self.justice_system, self.environmental]
