# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
#

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# temp_average = data["temp"].mean()
# print(temp_average)
#
# temp_max = data["temp"].max()
# print(temp_max)
#
# print(data.condition)
#

print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# temp_f = monday_temp * (9 / 5) + 32
# print(temp_f)

# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
