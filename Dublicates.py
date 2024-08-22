import pandas as pd
import os

# Paths to files
clean_data_path = r"D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\Metadata\Clean_data.csv"
output_dir = r"D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\csvfiles"

# Check if the directory exists, if not - create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the data
df = pd.read_csv(clean_data_path)

# Function to check the uniqueness of primary keys
def check_primary_key_uniqueness(df, primary_key_column):
    duplicates = df[df.duplicated(subset=primary_key_column, keep=False)]
    if not duplicates.empty:
        print(f"Duplicates found in the column {primary_key_column}:")
        print(duplicates)
    else:
        print(f"The column {primary_key_column} is unique.")

# Check the uniqueness of Foreign_Key
check_primary_key_uniqueness(df, 'Foreign_Key')

# You can review the duplicates and decide how to handle them further
