class stat():
  def __init__(self):
    self.nation = 'None'
    self.infantry = 0

  def german_empire(self, menu):
    self.provinces = ['Berlin', 'East Prussia', 'Alsace Lorraine', 'Rhine', 'Lower Prussia']
    self.nation = 'German Empire'
    self.infantry = self.infantry + 10

  
  def france(self, menu):
    self.provinces = ['Paris', 'South France', 'East France', 'Brest']
    self.nation = 'France'

  def USA(self, menu):
    self.provinces = ['California', 'East Coast', 'Texas', 'North USA']
    self.nation = 'USA'
    
  def japan(self, menu):
    self.provinces = ['Tokyo', 'Korea', 'North Island', 'Nagasaki Island', 'Kanto Island']
    self.nation = 'Japan'
  
  def uk(self, menu):
    self.provinces = ['London', 'Scotland', 'Wales', 'England', 'Northern Ireland']
    self.nation = 'British Empire'
  
  def serbia(self, menu):
    self.provinces = ['Serbia']
    self.nation = 'Serbia'
  
  def montenegro(self, menu):
    self.provinces = ['Montenegro']
    self.nation = 'Montenegro'

  def A_H(self, menu):
    self.provinces = ['Czech', 'Slovakia', 'South Poland', 'Hungary', 'Austria', 'Bosnia', 'Croatia', 'Slovenia']
    self.nation = 'A-H'
  
  def otto(self, menu):
    self.provinces = ['Iraq', 'Syria', 'Ankara', 'Istanbul', 'West Turkey', 'Armenia']
    self.nation = 'Ottoman Empire'
  
  def italy(self, menu):
    self.provinces = ['Northern Italy', 'Rome', 'Two Peninsulas', 'Sicily', 'Sardinia']
    self.nation = 'Italy'
  
  def russia(self, menu):
    self.provinces = ['Moscow', 'Saint Petersburg', 'Poland', 'Baltic', 'Finland', 'Siberia', 'Ukraine', 'Belarus', 'Caucasus']
    self.nation = 'Russian Empire'

  def bel(self, menu):
    self.provinces = ['Flanders', 'Wallonia', 'Brussels']
    self.nation = 'Belgium'

  def lux(self, menu):
    self.provinces = ['Luxembourg']
    self.nation = 'Luxembourg'