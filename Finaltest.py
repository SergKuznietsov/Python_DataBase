import pandas as pd
import sqlite3
import os

# Define file paths
metadata_file_path = r"D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\Metadata\Clean_data.csv"
db_file_path = r"D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\Electric_cars.Db"
output_file_path = r"D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\tests\Final_check.txt"

# Read the Metadata CSV file and count unique DOL_Vehicle_IDs
metadata_df = pd.read_csv(metadata_file_path, encoding='utf-8')
metadata_dol_count = metadata_df['DOL_Vehicle_ID'].nunique()

# Connect to the SQLite database
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# Find all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Initialize results dictionary
results = {}

# Check each table for DOL_Vehicle_ID column and count unique values if it exists
for table_name in tables:
    table_name = table_name[0]
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]
    
    if 'DOL_Vehicle_ID' in column_names:
        cursor.execute(f"SELECT COUNT(DISTINCT DOL_Vehicle_ID) FROM {table_name};")
        count = cursor.fetchone()[0]
        results[table_name] = count

# Close the connection
conn.close()

# Write results to output file
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(f"Count of unique DOL_Vehicle_IDs in Clean_data.csv: {metadata_dol_count}\n\n")
    f.write("Count of unique DOL_Vehicle_IDs in each table:\n")
    
    for table, count in results.items():
        f.write(f"{table}: {count}\n")
    
    f.write("\nComparison Results:\n")
    for table, count in results.items():
        comparison = "MATCH" if count == metadata_dol_count else "DOES NOT MATCH"
        f.write(f"{table}: {comparison}\n")
