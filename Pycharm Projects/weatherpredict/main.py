import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
data_dic = {
    "Fur color": ["Gray", "black", "Cinnamon"],
    "Count": [gray_count, black_count, red_count]
}
df = pandas.DataFrame(data_dic)
df.to_csv("count.csv")
