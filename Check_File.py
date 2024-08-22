import pandas as pd
import os

# Path to the metadata file
metadata_file_path = r'D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\Metadata\Electric_Vehicle_Population_Data.csv'

# Load data from the CSV file
df = pd.read_csv(metadata_file_path)

# Display all column names to verify them
print(df.columns)
