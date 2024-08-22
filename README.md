# Python_DataBase
**Python Scripts for Metadata Processing and Database Creation**

This repository contains Python scripts used for metadata processing, relational database creation, and data integrity validation. The work was carried out in several stages:

**1. Metadata Validation:**

Replacing empty values with "other."
Removing empty rows.
Ensuring data integrity.

_Example code for data cleaning_

def clean_data(data):

    data = data.dropna(how='all')
    
    data = data.fillna('other')
    
    return data
    
**2. Creating Foreign Key** for External Identification in the Database:
Generating a foreign key to ensure relationships between tables.

_Creating foreign key_

def create_foreign_key(table, key_column):

    table['foreign_key'] = table[key_column].apply(lambda x: generate_key(x))
    
    return table
    

**3. Performing Metadata Check:**
Verifying metadata quality after changes were applied.

_Example of metadata validation_
def check_metadata(metadata):
    # Check for any null values
    assert not metadata.isnull().values.any(), "Metadata contains null values!"
    return True

**4. Designing** the Relational Database Schema:
Structuring the database.
_Tables:_
- vehicles
- locations
- utilities
- foreign_keys

**5. Creating CSV Files Based on the Schema:**
Exporting data to CSV format for each table.

_Creating CSV file_

def export_to_csv(table, filename):

    table.to_csv(filename, index=False)
    

**6. Validating Transferred Files Against Primary Key:**
Checking data integrity after transferring to the database.

_Data transfer validation_

def validate_data_transfer(table, primary_key):

    assert table[primary_key].is_unique, "Primary key constraint violated!"
    
    return True
    

**7. Creating SQLite Database:**

_Importing data into a SQLite database._

import sqlite3

def create_database(db_name):

    conn = sqlite3.connect(db_name)
    
    # Creating tables and importing data
    
    return conn
    

**8. Final Database Validation:**
Ensuring the integrity of the final database.

_Final validation_

def final_check(database):

    # Checking the record counts in each table
    
    pass
    

**Test Conducted After Database Creation**
After completing all the steps, we conducted a test to validate the integrity of the database by comparing the unique DOL_Vehicle_ID values in different tables, such as vehicles.csv, locations.csv, utilities.csv, and foreign_keys.csv, against the Clean_data.csv file.

**Test Results:**
Number of unique DOL_Vehicle_ID values in all files: 200048
Difference from Clean_data.csv: 0 values
These results confirm that all data was successfully transferred, and the database structure is as expected.


