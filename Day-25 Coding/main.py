# with open("weather_data_.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)
#
# import csv
#
# with open("weather_data_.csv") as data_files:
#     data = csv.reader(data_files)
#     tempreture = []
#     for row in data:
#         if row[1] != "temp":
#             tempreture.append(int(row[1]))
#     print(tempreture)

import pandas

data = pandas.read_csv("weather_data_.csv")
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()w
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get data in column
#
# print(data.condition)

#get data in row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # create a dataframe from skratch
#
# data_dic = {
#     "names":["yashwanth","sonali", "lavanya", "govtham"],
#     "pincode" : [23,33,42,55,]
# }
#
# data = pandas.DataFrame(data_dic)
# data.to_csv("new_list_item")

data = pandas.read_csv("centra_park.csv")
grey_squrrials_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squrrials_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squrrials_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squrrials_count)
print(red_squrrials_count)
print(black_squrrials_count)

data_dirt = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squrrials_count, red_squrrials_count, black_squrrials_count]
}

df = pandas.DataFrame(data_dirt)
print(df)
df.to_csv("Squrrials_count.csv")