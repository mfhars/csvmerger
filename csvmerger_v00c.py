import pandas as pd
import os
from datetime import datetime

# Source directory path
source_dir = r"C:\Users\pingk\OneDrive - Chulalongkorn University\RandomDatas\FIKSASI\SPECTROCHEMPY\CSV_files\MiddleBox_file terkonversi ke CSV\RT_11\SPA and CSV\MIXED_DATE\RT_11"
# Output directory path
output_dir = r"C:\Users\pingk\Downloads\fadhli nitip\fadhli nitip"

# Function to remove file extension
def remove_extension(filename):
    return os.path.splitext(filename)[0]

# Function to convert country code to number
def country_code_to_number(country_code):
    mapping = {'TH': 0, 'ID': 1, 'MY': 2}
    return mapping.get(country_code, -1)  # Return -1 if country code is not in the mapping

# Initialize an empty dataframe for merging
merged_df = pd.DataFrame()

# Iterate over all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(source_dir, filename)
        
        # Read the CSV file without headers
        df = pd.read_csv(file_path, header=None)
        
        # Ensure the wavenumber column is of type float64
        df[0] = df[0].astype(float)
        
        # Create new headers without the file extension
        filename_without_extension = remove_extension(filename)
        new_headers = ["wavenumber"] + [filename_without_extension]
        df.columns = new_headers
        
        # Extract country code and convert to number
        country_code = filename_without_extension[:2]
        country_number = country_code_to_number(country_code)
        
        # Extract 4th-6th characters
        specific_chars = filename_without_extension[3:6]
        
        # Add rows for country origin and specific characters
        country_row = pd.DataFrame([[None, country_number]], columns=new_headers)
        specific_chars_row = pd.DataFrame([[None, specific_chars]], columns=new_headers)
        
        # Append the new rows to the dataframe
        df = pd.concat([country_row, specific_chars_row, df], ignore_index=True)
        
        # Merge dataframes on 'wavenumber'
        if merged_df.empty:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on="wavenumber", how="outer")

# Generate a timestamped output filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file_path = os.path.join(output_dir, f"merged_data_no_extension_{timestamp}.csv")
merged_df.to_csv(output_file_path, index=False)

print(f"Merged data saved to: {output_file_path}")

# Optionally display the first few rows of the merged dataframe
print(merged_df.head(10))
