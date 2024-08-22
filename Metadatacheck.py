import pandas as pd

# File paths
input_file_path = r'D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\Metadata\Clean_data.csv'
output_file_path = r'D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\tests\data_check.txt'

# Loading the data
df = pd.read_csv(input_file_path)

# Function to perform data checks
def check_data(df):
    report = []

    # Check for missing values
    if df.isnull().values.any():
        report.append("Missing values found.")

    # Check data types
    for column in df.columns:
        if df[column].dtype == 'object':
            report.append(f"Column '{column}' contains text data.")
        elif df[column].dtype in ['int64', 'float64']:
            report.append(f"Column '{column}' contains numeric data.")

    # Check for duplicates
    if df.duplicated().any():
        report.append("Duplicates found in the data.")

    # Add additional checks as needed
    return report

# Performing data checks
data_report = check_data(df)

# Saving the data check results to a file with UTF-8 encoding
with open(output_file_path, 'w', encoding='utf-8') as f:
    for line in data_report:
        f.write(line + '\n')

print(f"Data check results have been saved to {output_file_path}")
