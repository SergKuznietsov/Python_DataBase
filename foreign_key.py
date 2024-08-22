import pandas as pd

# File path
file_path = r'D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\Metadata\Clean_data.csv'
output_file_path = r'D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\Metadata\Clean_data_modified.csv'

# Load the CSV file
df = pd.read_csv(file_path)

# Convert necessary columns to strings
df['VIN'] = df['VIN'].astype(str)
df['County'] = df['County'].astype(str)
df['City'] = df['City'].astype(str)
df['Postal_Code'] = df['Postal_Code'].astype(str)
df['DOL_Vehicle_ID'] = df['DOL_Vehicle_ID'].astype(str)

# Create Foreign Key for each row, using all characters from 'DOL Vehicle ID'
df['Foreign Key'] = (
    df['VIN'].str[:3] +
    df['County'].str[:1] +
    df['City'].str[:1] +
    df['Postal_Code'].str[-3:] +
    df['DOL_Vehicle_ID']
)

# Add the generated Foreign Key to column R starting from the 2nd row
df['R'] = ""  # Clear column R
df.loc[1:, 'R'] = df['Foreign_Key'].iloc[1:]

# Drop the Foreign Key column R
df.drop(columns=['R'], inplace=True)

# Save the modified file with a new name
df.to_csv(output_file_path, index=False)

print(f"Column R has been successfully removed. The file has been saved as {output_file_path}.")
