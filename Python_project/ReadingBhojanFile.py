import pandas as pd

file_path = "/Users/saujanya.bohara/Desktop/Python_project/DataLake/Bhojan_Kapan_Clean.xlsx"
df = pd.read_excel(file_path)

# Ensure the TIME column is treated as string
df['TIME'] = df['TIME'].astype(str)

# Strip any extra spaces from column names
df.columns = df.columns.str.strip()
print(df.columns)  # To verify column names

data = {}
line = 1

#function to filter time

def filter_time(time_value):
    formatted_time = time_value.strip()
    return formatted_time

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    time = filter_time(row["TIME"])


    name = row.get("NAME","")
    pax = row.get("PAX", "")
    thali = row.get("THALI", "")
    number = row.get("NUMBER", "")
    table = row.get("TABLE", "")
    details = row.get("DETAILS", "")

    # Print the time for debugging purposes
    print(time)
    print(name)
    print(thali)



print(data)
