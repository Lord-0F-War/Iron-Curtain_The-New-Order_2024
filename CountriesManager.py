

class National_Spirit:
    def __init__(self, national_spirit_name, national_spirit_icon, national_spirit_description) -> None:
        self.national_spirit_name = national_spirit_name
        self.national_spirit_icon = national_spirit_icon
        self.national_spirit_description = national_spirit_description

        self.rect = None

        self.points_cost = 0


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


