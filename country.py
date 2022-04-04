class CountryCO2():
	"""Предстовляет страну и данные выброса СO2 (в год тонну на челоека.)."""
	source = 'https://pythonru.com/baza-znanij/gde-brat-dannye-dlja-analiza'

	def __init__(self, country, years, co2):
		"""Инициализирует страну, период лет, выбросы CO2."""

		self.country = country
		self.years = years
		self.co2_per_person = co2

	def show_data(self,*year):
		"""Отображает страну, период лет и выбросы углекислого газа(тонна на человека в год)."""
		
		if year:
			year = year[0]
			ind = self.years.index(year)
			print(f"\tСтрана: {self.country}")
			print(f"Год:{self.years[ind]}")
			print(f"Выбросы СО2 (тонна на человека в год):{self.co2_per_person[ind]}")
		else:
			print(f"\tСтрана: {self.country}")
			print(f"Годa:{self.years}")
			print(f"Выбросы СО2 (тонна на человека в год):{self.co2_per_person}")

	def r_year(self, value):
		"""Вовзращает год."""
		if type(value) == int and value in self.years:
			return value
		else:
			print("Нет такого значения.")
			return None
			

	def r_years(self, values = 'all'):
		"""Возвращает требуемый промежуток лет. 'All' - 1980 по 2018."""

		if values =='all':
			return self.years
		if type(values) == list and len(values) ==2 and values[0] != values[1]:
			self.r_y_ears = list(self.years[self.years.index(values[0]):self.years.index(values[1])+1])
			return self.r_y_ears
		else:
			print("Нет такого значения")
			return None
			
	def r_co2(self, value):
		"""Возвращает значение выброса углекислого газа за указанный год."""

		if value in self.years:
			self.r_co_2 = self.co2_per_person[self.years.index(value)]
			return self.r_co_2

		else:
			print("Нет такого значения.")
			return None

	def r_co2s(self, values = 'all'):
		"""Возращает значения выброса углекислого газа за указаный промежуток лет."""

		if values =='all':
			return self.co2_per_person
		if type(values) == list and len(values) ==2 and values[0] != values[1]:
			ind1 = self.years.index(values[0])
			ind2 = self.years.index(values[1])
			self.r_co_2s = list(self.co2_per_person[ind1: ind2+1])
			return self.r_co_2s
		else:
			print("Нет такого значения")
			return None

	def r_name(self):
		"""Вовзращает имя."""

		return self.country.title()
