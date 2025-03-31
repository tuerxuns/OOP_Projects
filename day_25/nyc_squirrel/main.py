import pandas

data = pandas.read_csv("squirrel_data.csv")

gray_s = data[data["Primary Fur Color"] == "Gray"]
cinnamon_s = data[data["Primary Fur Color"] == "Cinnamon"]
black_s = data[data["Primary Fur Color"] == "Black"]

gray_s_count = len(gray_s)
cinnamon_s_count = len(cinnamon_s)
black_s_count = len(black_s)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_s_count, cinnamon_s_count, black_s_count],
}

squirrel_count = pandas.DataFrame(data_dict)
squirrel_count.to_csv("squirrel_count.csv")
