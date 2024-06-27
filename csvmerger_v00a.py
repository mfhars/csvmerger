import pandas as pd
import os

# Source directory path
source_dir = r"C:\Users\Abdul\Downloads\SL_COUNTRY_LEVEL_based (1)\SL_COUNTRY_LEVEL_based\SLCL_MY"

# Function to remove file extension
def remove_extension(filename):
    return os.path.splitext(filename)[0]

# Initialize an empty dataframe for merging
merged_df = pd.DataFrame()

# Iterate over all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(source_dir, filename)
        
        # Read the CSV file without headers
        df = pd.read_csv(file_path, header=None)
        
        # Create new headers without the file extension
        new_headers = ["wavenumber", remove_extension(filename)]
        df.columns = new_headers
        
        # Merge dataframes on 'wavenumber'
        if merged_df.empty:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on="wavenumber", how="outer")

# Save the merged dataframe to a new CSV file
output_file_path = os.path.join(source_dir, "merged_data_no_extension.csv")
merged_df.to_csv(output_file_path, index=False)

print(f"Merged data saved to: {output_file_path}")

# Optionally display the first few rows of the merged dataframe
print(merged_df.head())
