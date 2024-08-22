import os
import pandas as pd

# Directory containing the CSV files
directory_path = r"D:\Finance_success\DataAnalytics\Portfolio\Python\1.txtcsv_Pandas\DataBase"

# Function to clean the data
def clean_data(file_path):
    try:
        df = pd.read_csv(file_path)

        # Iterate over columns and replace blank cells
        for col in df.columns:
            if df[col].dtype == 'object':  # TEXT columns
                df[col].fillna('OTHER', inplace=True)
            elif df[col].dtype in ['int64', 'float64']:  # INTEGER columns
                df[col].fillna(0, inplace=True)

        # Save the cleaned file back
        df.to_csv(file_path, index=False)
        return True
    except Exception as e:
        print(f"Failed to clean {file_path}: {e}")
        return False

def main():
    success = True
    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory_path, filename)
            result = clean_data(file_path)
            if not result:
                success = False

    if success:
        print("Success")
    else:
        print("Not Success")

if __name__ == "__main__":
    main()
