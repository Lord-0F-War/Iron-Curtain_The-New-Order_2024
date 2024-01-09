

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

        self.country_land_manpower = 150_500
        self.country_air_manpower = 150_500

        self.country_GDP = 10_550_000_000_000

        self.income = 10_550_000_000_000
        self.expenses = 550_600_000        


