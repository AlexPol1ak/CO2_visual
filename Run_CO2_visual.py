
from graph import show_graph, show_chart
from co2_f import csv_object_converter, show_contries

file = 'co2_emissions_for_person.csv'

# Получаем словарь обектов- стран на основе csv.
dict_country = csv_object_converter(file)

# Просматриваем список дотупных стран
show_contries(dict_country)

# Функция отображает график выброса CO2(тонна на человека в год) по указаной стране ,если она есть. 
#По умолчнию диапазон 1980-2018.
show_graph(dict_country, 'Belarus') 
show_graph(dict_country, 'Belarus', 2005,2010)









# # Отображение  и вывод списка доступных стран.
# c = show_contries(file) 

# # Отображение информации.Метод класса Сountry
# c['Latvia'].show_data(1990)



 #Так же принимает аргументы для отображения определнного периода по стране.

# # Отображает графики CO2 по нескольким странам за указанный период.Пустой список- весь дипазон(1980-2018).
# show_chart(file, [1990, 2015],'Belarus', 'Latvia', 'Poland', 'Latvia') 
