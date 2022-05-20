import csv
import pandas

# with open("weather_data.csv") as data_file:
#     temperatures = []
#     reader = csv.reader(data_file)
#     for row in reader:
#         temperatures.append(row[1])
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(data)
# temp_list = data["temp"].to_list()
# maximum = data["temp"].max()
# print(temp_list)
# print(data[data.day == "Monday"].temp)

squirrel_data = pandas.read_csv("squirrel_count.csv")
colors = squirrel_data["Primary Fur Color"].unique().tolist()
colors = colors[1:]
color_count_list = []
for color in colors:
    color_count = squirrel_data[squirrel_data["Primary Fur Color"] == color]["Primary Fur Color"].count()
    color_count_list.append(color_count)
print(color_count_list)

data_dict = {
    "colors": colors,
    "count": color_count_list
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")















