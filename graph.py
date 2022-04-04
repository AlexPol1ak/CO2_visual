# Содержит функции для отрисовки графиков, диаграмм 

import matplotlib.pyplot as plt
from plotly.graph_objs import Bar, Layout
import co2_f as co2
from random import random as r

def show_graph(objects, name_country, *years):
	"""Строит график выброса СО2 по стране за указаный период лет.По умолчанию с 1980 по 2018"""

	if name_country.title() in objects.keys():
		country = objects[name_country.title()]
		if years:
			x = country.r_years([years[0],years[1]])
			y = country.r_co2s([years[0],years[1]])
		else:
			x = country.r_years()
			y = country.r_co2s()

		name = country.r_name()
		plt.style.use('seaborn')
		fig, ax = plt.subplots(figsize=(12,9))
		ax.scatter(x, y, c = y, cmap=plt.cm.jet, s = 40)
		plt.plot(x, y, c = 'blue', linewidth = 2,alpha=0.8)
		plt.axis([min(x)+1, max(x), min(y), max(y)+1])
		plt.title(name, fontsize=20)
		plt.xlabel('Год', fontsize=14)
		plt.ylabel("Выбросы СО2 \n(тонна на человека в год)", fontsize=14)
		plt.tick_params(axis = 'both', which = 'major', labelsize = 12)
		plt.show()
	else:
		print('Данных по этой стране нет')
		print('Cписок доступных стран:', list(objects.keys()))

	

def show_chart(file_csv, yearslist, *name_country): 
	"""Отображает на графике выброс углекислого газа указанных стран ,за указанный промежуток лет."""

	objects = co2.csv_object_converter(file_csv)

	plt.style.use('dark_background') 
	fig, ax = plt.subplots(figsize=(12,9)) 
	leg= {} # Словарь для построения {имя: линия отрисовки} для отображения легенды.

	if len(name_country)>0:
		for nc in name_country: # Перебор списка стран и получения данных: период лет, СО2
			nc = nc.title()
			if type(yearslist) == list and len(yearslist) == 2:
				x = objects[nc].r_years([yearslist[0],yearslist[1]]) # года
				y = objects[nc].r_co2s([yearslist[0],yearslist[1]])  # СО2
			else:
				x = objects[nc].r_years()
				y = objects[nc].r_co2s()
			color = (r(),r(),r())
			ax.scatter(x, y, color = color, s = 40) 
			l = plt.plot(x, y, color = color, linewidth = 2,alpha=0.8)
			leg[nc] = l 

	leg_n = [str(n) for n in leg.keys()] # Получения имен стран для легенды
	leg_l = [l[0] for l in leg.values()] # Получение цвета
	name = ', '.join(leg_n)

	ax.legend(leg_l, leg_n)
	ax.axis([min(x)+1, max(x), min(y), max(y)])
	plt.title(name, fontsize=20)
	plt.xlabel('Год', fontsize=14)
	plt.ylabel("Выбросы СО2 \n(тонна на человека в год)", fontsize=14)
	ax.margins(0.1, 0.1)
	plt.tick_params(axis = 'both', which = 'major', labelsize = 10)
	
	plt.show()
