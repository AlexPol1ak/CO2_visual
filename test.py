import unittest 
from co2_f import csv_object_converter
from country import CountryCO2

file = 'co2_emissions_for_person.csv'

class TestCountry(unittest.TestCase):
	"""Тесты для класса CountryCO2 из country.py и функции построения экземпляров 'csv_object_converter' из co2_f.py. """

	def setUp(self):
		"""Создаем экземпляр класса CountryCO2 через функцию 'csv_object_converter'."""
		self.objects = csv_object_converter(file)

	def test_csv_object_converter1(self):
		"""Возвращает ли функция словарь ?"""
		type_dict = isinstance(self.objects, dict)
		self.assertTrue(type_dict)

	def test_csv_object_converter2(self):
		"""Возвращает ли функция словарь типа {страна(str): экземпляр (<class 'country.CountryCO2'>)}?"""

		for key, item in self.objects.items():
			self.assertTrue(isinstance(key, str))
			self.assertEqual(str(type(item)), "<class 'country.CountryCO2'>" )

	def test_keyName_instanceName(self):
		"""Соотвествует ли ключ словаря(название страны)  имени экземпляру страны?"""
		
		for key, item in self.objects.items():
			self.assertEqual(key, item.country)

	def test_len_values(self):
		"""Соотвествует ли количество значений(лет,years) количеству значений(СО2) в экземплярах?"""

		for obj in self.objects.values():
			self.assertEqual(len(obj.years), len(obj.co2_per_person))

	def test_type_value_country(self):
		"""Соотвествуют ли тип данных экземпляров: .country-str ?"""

		for obj in self.objects.values():
			self.assertTrue(isinstance(obj.country, str))

	def test_type_years(self):
		"""Соотвествуют ли тип данных экземпляров:  .years-int ? co2_per_person- float?"""

		for obj in self.objects.values():
			for year in obj.years:
				self.assertTrue(isinstance(year, int))

	def test_type_co2_per_person(self):
		"""Соотвествуют ли тип данных экземпляров: .co2_per_person- float?"""

		for obj in self.objects.values():
			for co2 in obj.co2_per_person:
				self.assertTrue(isinstance(co2, float))

	def test_r_year(self):
		"""Возвращает ли указаный год?"""

		year = self.objects['Belarus'].r_year(2005)
		self.assertEqual(year, 2005)



	def test_r_years(self):
		"""Возвращает ли указаный промежуток лет?"""

		years = self.objects['Belarus'].r_years([1995,1997])
		flag1 = False
		if type(years)== list and years[0] == 1995 and years[1] == 1996 and years[2] == 1997 :
			flag1 = True

		self.assertTrue(flag1)



	def test_r_co2(self):
		"""Возвращает значение выброса углекислого газа за указанный год?"""

		c1 = self.objects['Belarus'].r_co2(2017)
		self.assertEqual(c1, 6.64)

	def test_r_co2s(self):
		"""Возвращает значения выброса углекислого газа за указанный период лет?"""
		c2 = self.objects['Belarus'].r_co2s([1980,1985])
		flag2 = False
		if type(c2) == list and c2[0] == 11.4 and c2[1] == 11.1 and c2[2] == 11.2 and c2[3] == 11.3 and c2[4] == 11.3:
			flag2= True

		self.assertTrue(flag2)

	def test_r_name(self):
		"""Правильно ли возвращает имя?."""

		name = self.objects['Belarus'].r_name()
		self.assertEqual(name, 'Belarus')




		



if __name__ == '__main__':
	unittest.main()











