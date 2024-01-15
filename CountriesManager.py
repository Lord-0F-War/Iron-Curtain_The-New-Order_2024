

class National_Spirit:
    def __init__(self, national_spirit_name, national_spirit_icon, national_spirit_description) -> None:
        self.national_spirit_name = national_spirit_name
        self.national_spirit_icon = national_spirit_icon
        self.national_spirit_description = national_spirit_description

        self.rect = None

        self.points_cost = 0


class Laws_Group:
    def __init__(self, group_name = str, laws = list, active_law_index = int) -> None:
        self.group_name = group_name
        self.laws = laws

        self.total_value = 0

        for index, law in enumerate(self.laws):
            law.value = index + 1
            self.total_value += index + 1

        self.active_law = self.laws[active_law_index]
        self.active_law_rating = self.calculate_rating()

    def calculate_rating(self):
        proportion = self.active_law.value / (self.total_value - len(self.laws))
        rating = int(proportion * 100)

        return max(1, min(100, rating))

class Law:
    def __init__(self, name = str) -> None:
        self.name = name
        self.value = 0



class Country:
    def __init__(self, country_leader_name, country_capital_image,  country_leader_image, country_flag_image, country_name, country_ruler_ideology, country_music_playlist) -> None:
        self.country_leader_name = country_leader_name
        self.country_capital_image = country_capital_image
        self.country_leader_image = country_leader_image
        self.country_flag_image = country_flag_image
        self.country_name = country_name

        self.capital_pos = None

        self.country_ruler_ideology = country_ruler_ideology

        self.country_music_playlist = country_music_playlist

        self.country_national_spirits = []
        self.country_culture = None
        self.country_religion = None

        self.politics_popularity = [4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16, 4.16]
        self.culture_popularity = [7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14, 7.14]
        self.religion_popularity = [11.11, 11.11, 11.11, 11.11, 11.11, 11.11, 11.11, 11.11, 11.11]        

        self.country_ruling_party = 'party demo'
        self.country_government = 'government demo'
        self.country_elections = 'Never'

        self.country_brief_history = 'history demo'

        self.country_national_spirits_total_points = 100
        self.country_national_spirits_points_left = self.country_national_spirits_total_points

        self.country_stability = 100
        self.country_war_support = 100
        self.country_party_popularity = 100

        # DIPLOMACY
        self.diplomacy_rating = 100 

        # ARMY  
        self.military_rating = 75

        self.country_land_manpower = 150_500
        self.country_air_manpower = 150_500        
        
        self.army_staff = self.country_land_manpower + self.country_air_manpower
        
        self.production_capacity_army = 0
        self.production_capacity_navy = 0
        self.production_capacity_air = 0
        self.production_capacity_special = 0
        self.production_capacity_total = f"{self.production_capacity_army} / {self.production_capacity_navy} / {self.production_capacity_air} / {self.production_capacity_special}" 
        
        # ECONOMY
        self.economy_rating = 50 
        
        self.treasury = 85_952_542_000_000
        self.debt = 5_365_215_000_000

        self.credit_rating = 52.5
        self.inflation = 2.1
        self.unemployment = 5.2

        self.country_GDP = 10_550_000_000_000

        self.income = 10_550_000_000_000
        self.expenses = 550_600_000         

        # DOMESTIC
        self.domestic_rating = 25

        self.country_population = 100_600_000

        self.country_immigration = 10000
        self.country_emigration = 2000
        self.country_births = 10400
        self.country_deaths = 25000
        self.country_literacy_rate = 94

        self.population_political_leaning = "MODERATE"


        self.military_approval_rating = 100
        self.domestic_approval_rating = 80
        self.midia_approval_rating = 60
        self.secret_service_approval_rating = 40
        self.politics_approval_rating = 20 

        self.internal_economy_rating = 100
        self.external_economy_rating = 50    


        # LAWS

        #   POLITICAL LAWS

        self.political_parties_1 = Law('test')
        self.political_parties_2 = Law('test')
        self.political_parties_3 = Law('test')

        self.political_parties  =    Laws_Group('political_parties', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)
        self.religious_rights   =    Laws_Group('religious_rights', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.trade_unions       =    Laws_Group('trade_unions', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 2)
        self.public_protest     =    Laws_Group('public_protest', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.gun_control        =    Laws_Group('gun_control', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.privacy_rights     =    Laws_Group('privacy_rights', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.speach_rights      =    Laws_Group('speach_rights', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.press_rights       =    Laws_Group('press_rights', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.voting_rights      =    Laws_Group('voting_rights', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)


        self.political_laws_groups = [self.political_parties, self.religious_rights, self.trade_unions, self.public_protest, self.gun_control, self.privacy_rights, self.speach_rights, self.press_rights, self.voting_rights]

        #   MILITARY LAWS

        self.conscription                =    Laws_Group('conscription', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)                  
        self.women_in_service            =    Laws_Group('women_in_service', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.training_level              =    Laws_Group('racial_admission', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 2)
        self.racial_admission            =    Laws_Group('racial_admission', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 2)
        self.national_security           =    Laws_Group('national_security', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)
        self.deployment                  =    Laws_Group('deployment', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)
        self.reserves                    =    Laws_Group('reserves', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)
        self.economical_militarization   =    Laws_Group('economical_militarization', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)


        self.military_laws_groups = [self.conscription, self.women_in_service, self.training_level, self.racial_admission, self.national_security, self.deployment, self.reserves, self.economical_militarization]


        #   ECONOMICAL LAWS

        self.economic_system        =    Laws_Group('economic_system', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)        
        self.trade_laws             =    Laws_Group('trade_laws', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.taxation_system        =    Laws_Group('taxation_system', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 2)
        self.regulations            =    Laws_Group('regulations', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)
        self.monetary_policy        =    Laws_Group('monetary_policy', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)
        self.property_rights        =    Laws_Group('property_rights', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)
        self.nationalization        =    Laws_Group('nationalization', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 2)
        self.brand_rights           =    Laws_Group('brand_rights', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.public_services        =    Laws_Group('public_services', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)


        self.economical_laws_groups = [self.economic_system, self.trade_laws, self.taxation_system, self.regulations, self.monetary_policy, self.property_rights, self.nationalization, self.brand_rights, self.public_services]


        #   SOCIAL LAWS

        self.emigration_immigration     =    Laws_Group('emigration_immigration', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 2)
        self.minorities_rights          =    Laws_Group('minorities_rights', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 2)
        self.welfare                    =    Laws_Group('welfare', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 2)
        self.reproduction               =    Laws_Group('reproduction', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.morality_laws              =    Laws_Group('morality_laws', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.drug_laws                  =    Laws_Group('drug_laws', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 1)
        self.work_laws                  =    Laws_Group('work_laws', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)
        self.justice_system             =    Laws_Group('justice_system', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)
        self.enviromental               =    Laws_Group('enviromental', [self.political_parties_1, self.political_parties_2, self.political_parties_3], 0)


        self.social_laws_groups = [self.emigration_immigration, self.minorities_rights, self.welfare, self.reproduction, self.morality_laws, self.drug_laws, self.work_laws, self.justice_system, self.enviromental]