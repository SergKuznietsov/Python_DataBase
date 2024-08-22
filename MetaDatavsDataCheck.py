import pandas as pd
import os

# File paths
metadata_file = r'D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\Metadata\Clean_data.csv'
csv_files_dir = r'D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\csvfiles'
report_file_path = r'D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\tests\MetadatavsData.txt'

# Load data from Clean_data.csv
clean_data_df = pd.read_csv(metadata_file)
clean_data_unique_ids = clean_data_df['DOL_Vehicle_ID'].nunique()

# List of files to check
csv_files = ['vehicles.csv', 'locations.csv', 'utilities.csv', 'foreign_keys.csv']

# Open the file for writing results with correct encoding
with open(report_file_path, 'w', encoding='utf-8') as report_file:
    report_file.write(f"Comparison of unique 'DOL_Vehicle_ID' values between Clean_data.csv and other files:\n\n")
    
    # Check unique values in each file
    for file_name in csv_files:
        file_path = os.path.join(csv_files_dir, file_name)
        df = pd.read_csv(file_path)
        unique_ids = df['DOL_Vehicle_ID'].nunique()
        
        # Compare the number of unique values
        report_file.write(f"{file_name}:\n")
        report_file.write(f"  Unique values in {file_name}: {unique_ids}\n")
        report_file.write(f"  Difference from Clean_data.csv: {clean_data_unique_ids - unique_ids} values\n\n")

print(f"Report successfully saved to file: {report_file_path}")
