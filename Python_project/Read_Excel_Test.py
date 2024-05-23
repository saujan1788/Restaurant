import pandas as pd

file_path = '/Users/saujanya.bohara/Desktop/Python_project/DataLake/Bhojan_Sample.xlsx'

df = pd.read_excel(file_path)

data = {}
for index, row in df.iterrows():
    branch = row["Branch"]
    manager = row["Manager"]
    most_sold = row["Most Sold"]
    investment = row["Investment"]

    data[branch] = {
        "Manager": manager,
        "MostSold": most_sold,
        "Investment": investment
    }

print(data)
