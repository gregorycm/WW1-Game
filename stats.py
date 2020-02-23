class stat():
    def __init__(self):
        self.nation = 'None'
        self.infantry = 0
        self.provinces = []

    def german_empire(self):
        self.provinces = ['Berlin', 'East Prussia', 'Alsace Lorraine', 'Rhine', 'Lower Prussia']
        self.nation = 'German Empire'
        self.infantry = self.infantry + 10

    def france(self):
        self.provinces = ['Paris', 'South France', 'East France', 'Brest']
        self.nation = 'France'

    def usa(self):
        self.provinces = ['California', 'East Coast', 'Texas', 'North USA']
        self.nation = 'usa'

    def japan(self):
        self.provinces = ['Tokyo', 'Korea', 'North Island', 'Nagasaki Island', 'Kanto Island']
        self.nation = 'Japan'

    def uk(self):
        self.provinces = ['London', 'Scotland', 'Wales', 'England', 'Northern Ireland']
        self.nation = 'British Empire'

    def serbia(self):
        self.provinces = ['Serbia']
        self.nation = 'Serbia'

    def montenegro(self):
        self.provinces = ['Montenegro']
        self.nation = 'Montenegro'

    def austria_hungary(self):
        self.provinces = ['Czech', 'Slovakia', 'South Poland', 'Hungary', 'Austria', 'Bosnia', 'Croatia', 'Slovenia']
        self.nation = 'A-H'

    def otto(self):
        self.provinces = ['Iraq', 'Syria', 'Ankara', 'Istanbul', 'West Turkey', 'Armenia']
        self.nation = 'Ottoman Empire'

    def italy(self):
        self.provinces = ['Northern Italy', 'Rome', 'Two Peninsulas', 'Sicily', 'Sardinia']
        self.nation = 'Italy'

    def russia(self):
        self.provinces = ['Moscow', 'Saint Petersburg', 'Poland', 'Baltic', 'Finland', 'Siberia', 'Ukraine', 'Belarus',
                          'Caucasus']
        self.nation = 'Russian Empire'

    def bel(self):
        self.provinces = ['Flanders', 'Wallonia', 'Brussels']
        self.nation = 'Belgium'

    def lux(self):
        self.provinces = ['Luxembourg']
        self.nation = 'Luxembourg'
