# Содержит функции для обработки файлов csv, словарей , отображений стран.

import os
import csv
import json
from country import CountryCO2


def dict_json_convertor(dic_t):
	"""Получает словарь  и сохраняет его json формате в папке data."""
	try:
		os.mkdir('data')
	except FileExistsError:
		pass
	with open('data/dict_date.json', 'w', encoding='utf-8') as djc:
		json.dump(dic_t, djc, indent=4)


def csv_object_converter(file):
	"""Возвращает словарь объектов {странa: экземпляр}."""

	odject_dicts = {}
	#Cписок стран для мониторинга.
	cntry = ['Austria', 'Belgium', 'Bulgaria', 'Hungary', 'Greece', 'Denmark', 'Germany', 'Ireland', 'Spain', 'Italy',
        'Cyprus', 'Latvia', 'Lithuania', 'Luxembourg', 'Poland', 'Netherlands', 'Malta', 'Portugal', 'Romania',
        'Slovak Republic', 'Slovenia', 'Czech Republic', 'Finland', 'France', 'Sweden', 'Estonia', 'Belarus', 'Russia']

    # Извлечение данных из файла.
	with open(file, encoding='utf-8') as f:
		data = csv.reader(f)
		header = next(data)

		# Извлекаем года с 1980 по 2018 из заголовков файла.
		years = []
		for y in header:
		 	if y.isdigit():
		 		if int(y) >=1980 and int(y) <2019:
		 			years.append(int(y))

		# Извлекаем данные ( выброс углекислого газа (тонна на человека)) из файла по каждой стране, строим словарь{страна: экземпляр}.
		i = 0 
		for d in data:
			if d[0] in cntry: #проверяем вхождение страны из файла в список нужных стран
				d1 = [float(c) for c in d[181:220]]
				build =  CountryCO2(d[0], years, d1) # Построение экземпляра на основе данных из 'co2_emissions_for_person.csv'.
				odject_dicts[build.country] = build # Построение словаря {страна: экземпляр}.
				i += 1

	return odject_dicts


def show_contries(objects):
	"""Возвращает и выводит список доступных стран из словаря объектов.""" 
	print('Список доступных стран')
	print(list(objects.keys()))

	
