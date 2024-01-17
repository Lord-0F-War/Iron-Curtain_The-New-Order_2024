

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
        self.active_law_index = active_law_index

        self.total_value = 0

        for index, law in enumerate(self.laws):
            law.value = index + 1
            self.total_value += index + 1

        self.active_law:Law = self.laws[active_law_index]
        self.active_law_rating = self.calculate_rating()

    def calculate_rating(self):
        proportion = self.active_law.value / len(self.laws)
        rating = int(proportion * 100)

        return max(1, min(100, rating))

class Law:
    def __init__(self, name = str, description = str) -> None:
        self.name = name
        self.description = description

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

        self._1 = Law('LAW NAME 1', description = 'desc') 
        self._2 = Law('LAW NAME 1', description = 'desc')  
        self._3 = Law('LAW NAME 1', description = 'desc')  
        self._4 = Law('LAW NAME 1', description = 'desc')  
        self._5 = Law('LAW NAME 1', description = 'desc')  
        self._6 = Law('LAW NAME 1', description = 'desc')  
        self._7 = Law('LAW NAME 1', description = 'desc')  
        self._8 = Law('LAW NAME 1', description = 'desc')  
            
        self.political_parties_1 = Law('Total Ban on Political Parties',                description = 'The formation and existence of political\nparties are completely prohibited.\n\nAny attempt to organize or support a\npolitical party is met with severe\npenalties.')
        self.political_parties_2 = Law('Single-Party System',                           description = 'Only one political party is allowed to\nexist, and it monopolizes political\npower.\n\nOpposition parties are banned, and\ndissent is not tolerated.')
        self.political_parties_3 = Law('State Approval Required\nMulti-Party System',   description = 'Multiple political parties are allowed,\nbut strict government approval is\nrequired.\n\nThe state has significant control over\nthe formation and activities of\npolitical parties.')
        self.political_parties_4 = Law('Limited Opposition',                            description = 'While multiple parties are allowed, the\ngovernment closely monitors the acts\nof opposition parties.\n\nThere are restrictions on political\ndissent, and opposition voices are\nconstrained.')
        self.political_parties_5 = Law('Free and Fair Elections',                       description = 'Political parties operate freely, and\nelections are conducted in a free and\nfair manner.\n\nThe democratic process ensures that\ncitizens can choose their representatives\nwithout undue influence.')
        self.political_parties_6 = Law('Inclusive Representation\nDiversity Enforced',  description = 'Political parties are required by law to\nensure inclusive representation that\nreflects the government diversity quota.\n\nMeasures, such as quotas or\naffirmative action, are mandatory and\nthe removal of already elected\npoliticians may happen if needed.')
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