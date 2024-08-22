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

# Function to check the presence of columns
def validate_columns(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {', '.join(missing_columns)}")

# Function to check for null values in critical columns
def validate_not_null(df, critical_columns):
    for col in critical_columns:
        if df[col].isnull().any():
            raise ValueError(f"Column {col} contains null values.")

# Function to check the uniqueness of primary keys
def validate_unique_primary_key(df, primary_key_columns):
    duplicates = df[df.duplicated(subset=primary_key_columns, keep=False)]
    if not duplicates.empty:
        raise ValueError(f"Duplicates found in primary key columns {primary_key_columns}: {duplicates}")

# Function to check the integrity of foreign keys
def validate_foreign_keys(df, referenced_df, foreign_key_column, referenced_column):
    missing_keys = df[~df[foreign_key_column].isin(referenced_df[referenced_column])]
    if not missing_keys.empty:
        raise ValueError(f"Column {foreign_key_column} contains invalid foreign keys.")

# Validation and saving the vehicles table
vehicles_columns = [
    'DOL_Vehicle_ID', 'VIN', 'Model_Year', 'Make', 'Model',
    'Electric_Vehicle_Type', 'CAFV_Eligibility', 'Electric_Range',
    'Base_MSRP', 'Legislative_District'
]
validate_columns(df, vehicles_columns)
validate_not_null(df, ['DOL_Vehicle_ID'])
validate_unique_primary_key(df, ['DOL_Vehicle_ID'])
vehicles_df = df[vehicles_columns]
vehicles_df.to_csv(os.path.join(output_dir, 'vehicles.csv'), index=False)

# Validation and saving the locations table
locations_columns = [
    'DOL_Vehicle_ID', 'County', 'City', 'State', 'Postal_Code', 'Vehicle_Location'
]
validate_columns(df, locations_columns)
validate_not_null(df, ['DOL_Vehicle_ID'])
validate_foreign_keys(df[locations_columns], vehicles_df, 'DOL_Vehicle_ID', 'DOL_Vehicle_ID')
locations_df = df[locations_columns]
locations_df.to_csv(os.path.join(output_dir, 'locations.csv'), index=False)

# Validation and saving the utilities table
utilities_columns = [
    'DOL_Vehicle_ID', 'Electric_Utility', 'Census_Tract'
]
validate_columns(df, utilities_columns)
validate_not_null(df, ['DOL_Vehicle_ID'])
validate_foreign_keys(df[utilities_columns], vehicles_df, 'DOL_Vehicle_ID', 'DOL_Vehicle_ID')
utilities_df = df[utilities_columns]
utilities_df.to_csv(os.path.join(output_dir, 'utilities.csv'), index=False)

# Validation and saving the foreign_keys table
foreign_keys_columns = [
    'Foreign_Key', 'DOL_Vehicle_ID'
]
validate_columns(df, foreign_keys_columns)
validate_not_null(df, ['Foreign_Key', 'DOL_Vehicle_ID'])
validate_unique_primary_key(df, ['Foreign_Key'])
validate_foreign_keys(df[foreign_keys_columns], vehicles_df, 'DOL_Vehicle_ID', 'DOL_Vehicle_ID')
foreign_keys_df = df[foreign_keys_columns]
foreign_keys_df.to_csv(os.path.join(output_dir, 'foreign_keys.csv'), index=False)

print("Files successfully saved in CSV format after validation.")
