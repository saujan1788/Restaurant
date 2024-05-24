import pandas as pd
import numpy as np

# Loading the data
file_path = "/Users/saujanya.bohara/Desktop/SRE_Project/Restaurant/Python_project/DataLake/Bhojan_Kapan_Clean.xlsx"
df = pd.read_excel(file_path)

# Ensure the TIME and NUMBER columns are treated as strings
df['TIME'] = df['TIME'].astype(str)
df['NUMBER'] = df['NUMBER'].astype(str)

# Strip any extra spaces from column names
df.columns = df.columns.str.strip()
print(df.columns)  # To verify column names


# Function to clean and format time
def format_time(time_value):
    # Strip any leading or trailing whitespace
    formatted_time = time_value.strip()

    # Remove anything after a slash or backslash
    if '/' in formatted_time:
        formatted_time = formatted_time.split('/')[0]
    if '\\' in formatted_time:
        formatted_time = formatted_time.split('\\')[0]

    # Find the portion of the string with a colon
    if ':' in formatted_time:
        hour_minute = formatted_time.split(':')
        if len(hour_minute) >= 2:
            hour = hour_minute[0].zfill(2)
            minute = hour_minute[1].zfill(2)
            return f"{hour}:{minute}"
    # Handle cases with digits only
    elif formatted_time.isdigit():
        hour = formatted_time.zfill(2)
        return f"{hour}:00"

    # Return the original value if no colon is found and it's not a simple hour
    return formatted_time


# Apply the format_time function to the TIME column
df['TIME'] = df['TIME'].apply(format_time)


# Convert TIME to numerical values
def convert_time_to_numeric(time_str):
    try:
        time_value = pd.to_datetime(time_str).time()
        return time_value.hour + time_value.minute / 60.0
    except:
        return np.nan


df['TIME_NUMERIC'] = df['TIME'].apply(convert_time_to_numeric)


# Clean 'PAX' column
def clean_pax_value(pax):
    # Remove any leading or trailing whitespace
    pax = str(pax).strip()

    # Split by common delimiters and take the maximum value
    delimiters = ['/', '\\', '|']
    for delimiter in delimiters:
        if delimiter in pax:
            try:
                pax_values = [int(val) for val in pax.split(delimiter)]
                return max(pax_values)
            except ValueError:
                return np.nan

    # Ensure it's a valid numerical value
    try:
        pax_value = int(pax)
        if 0 <= pax_value <= 99:  # Assuming valid PAX values are between 0 and 99
            return pax_value
        else:
            return np.nan
    except ValueError:
        return np.nan


# Apply the clean_pax_value function to the PAX column
df['PAX_CLEANED'] = df['PAX'].apply(clean_pax_value)

# Drop rows with missing values in critical columns
df.dropna(subset=['TIME_NUMERIC', 'PAX_CLEANED'], inplace=True)

# Select the columns to be saved in the new file
columns_to_save = ['TIME_NUMERIC', 'NAME', 'PAX_CLEANED', 'NUMBER', 'TABLE', 'THALI']

# Create a new DataFrame with the selected columns
df_cleaned = df[['TIME_NUMERIC', 'NAME', 'PAX_CLEANED', 'NUMBER', 'TABLE', 'THALI']]

# Save the cleaned data to a new Excel file
output_file_path = "/Users/saujanya.bohara/Desktop/SRE_Project/Restaurant/Python_project/DataLake/CleanFileByScript.xlsx"
df_cleaned.to_excel(output_file_path, index=False)

# Print confirmation and the cleaned DataFrame
print("Cleaned data saved to:", output_file_path)
print(df_cleaned.head())
