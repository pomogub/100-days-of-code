# with open('weather_data.csv', 'r') as x:
#     data = [entry.strip() for entry in x.readlines()]
# print(data)

# import csv
# import pandas
# from statistics import mean
# from numpy import max

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = [int(row[1]) for row in data if row[1] != 'temp']
#     print(int(mean(temperatures)))

# data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(int(data['temp'].mean()))

# get data in column
# print(data.temp.max())

# get data in row
# print(data[data.day == 'Monday'])

# print row of data which had highest temperature
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# mondays_temp = data.at[0, 'temp']
# print(((mondays_temp) * 9/5) + 32)

# alternate to above
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# print((monday_temp * 9/5) + 32)

# pull specific value from csv
# print(data.temp[3])

# create dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv('new_data.csv')

import csv
import pandas

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260205.csv')

# first draft
# squirrel_colors = squirrel_data['Primary Fur Color']
# greys = 0
# reds = 0
# blacks = 0
#
# for squirrel in squirrel_colors:
#     if squirrel == 'Gray':
#         greys += 1
#     if squirrel == 'Cinnamon':
#         reds += 1
#     if squirrel == 'Black':
#         blacks += 1

# revised
greys = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
reds = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
blacks = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

squirrel_dict = {
    'Fur Color': ['Grey', 'Red', 'Black'],
    'Count': [greys, reds, blacks]
}
squirrel_count = pandas.DataFrame(squirrel_dict)
squirrel_count.to_csv('squirrel_count.csv')
