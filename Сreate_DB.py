import sqlite3
import pandas as pd
import os

# Path to the database and its name
db_path = r"D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\Electric_cars.db"

# Connecting to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Clearing the tables before importing new data
cursor.execute('DELETE FROM vehicles')
cursor.execute('DELETE FROM locations')
cursor.execute('DELETE FROM utilities')
cursor.execute('DELETE FROM foreign_keys')

# Creating tables according to the schema
cursor.execute('''
CREATE TABLE IF NOT EXISTS vehicles (
    DOL_Vehicle_ID INTEGER PRIMARY KEY,
    VIN TEXT,
    Model_Year INTEGER,
    Make TEXT,
    Model TEXT,
    Electric_Vehicle_Type TEXT,
    CAFV_Eligibility TEXT,
    Electric_Range INTEGER,
    Base_MSRP INTEGER,
    Legislative_District TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS locations (
    DOL_Vehicle_ID INTEGER PRIMARY KEY,
    County TEXT,
    City TEXT,
    State TEXT,
    Postal_Code TEXT,
    Vehicle_Location TEXT,
    FOREIGN KEY (DOL_Vehicle_ID) REFERENCES vehicles(DOL_Vehicle_ID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS utilities (
    DOL_Vehicle_ID INTEGER PRIMARY KEY,
    Electric_Utility TEXT,
    Census_Tract TEXT,
    FOREIGN KEY (DOL_Vehicle_ID) REFERENCES vehicles(DOL_Vehicle_ID)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS foreign_keys (
    Foreign_Key INTEGER PRIMARY KEY UNIQUE,
    DOL_Vehicle_ID INTEGER,
    FOREIGN KEY (DOL_Vehicle_ID) REFERENCES vehicles(DOL_Vehicle_ID)
)
''')

# Path to CSV files
csv_dir = r"D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\csvfiles"

# Function to import CSV into tables with data type handling
def import_csv_to_table(csv_file, table_name, dtype_mapping):
    # Reading the CSV without enforcing types
    df = pd.read_csv(os.path.join(csv_dir, csv_file))
    
    # Outputting data types for verification
    print(f"Data types in {table_name}:")
    print(df.dtypes)
    
    # Convert only numeric columns where necessary
    for column, dtype in dtype_mapping.items():
        if dtype == 'int64':
            df[column] = pd.to_numeric(df[column], errors='coerce')
    
    # Insert data into the table
    df.to_sql(table_name, conn, if_exists='append', index=False)

# Setting data types for each table
dtype_mapping_vehicles = {
    'DOL_Vehicle_ID': 'int64',
    'VIN': 'object',
    'Model_Year': 'int64',
    'Make': 'object',
    'Model': 'object',
    'Electric_Vehicle_Type': 'object',
    'CAFV_Eligibility': 'object',
    'Electric_Range': 'int64',
    'Base_MSRP': 'int64',
    'Legislative_District': 'object'
}

dtype_mapping_locations = {
    'DOL_Vehicle_ID': 'int64',
    'County': 'object',
    'City': 'object',
    'State': 'object',
    'Postal_Code': 'object',
    'Vehicle_Location': 'object'
}

dtype_mapping_utilities = {
    'DOL_Vehicle_ID': 'int64',
    'Electric_Utility': 'object',
    'Census_Tract': 'object'
}

dtype_mapping_foreign_keys = {
    'Foreign_Key': 'int64',
    'DOL_Vehicle_ID': 'int64'
}

# Importing data for each table with the correct data types
import_csv_to_table('vehicles.csv', 'vehicles', dtype_mapping_vehicles)
import_csv_to_table('locations.csv', 'locations', dtype_mapping_locations)
import_csv_to_table('utilities.csv', 'utilities', dtype_mapping_utilities)
import_csv_to_table('foreign_keys.csv', 'foreign_keys', dtype_mapping_foreign_keys)

# Closing the connection
conn.commit()
conn.close()
