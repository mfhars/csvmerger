import pandas as pd
import os
from datetime import datetime

# Source directory path
source_dir = r"C:\Users\pingk\OneDrive - Chulalongkorn University\RandomDatas\FIKSASI\SPECTROCHEMPY\CSV_files\MiddleBox_file terkonversi ke CSV\RT_6\SPA and CSV\MIXED_DATE\rt6mix"
# Output directory path
output_dir = r"C:\Users\pingk\Downloads\fadhli nitip\fadhli nitip"

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
        
        # Ensure the wavenumber column is of type float64
        df[0] = df[0].astype(float)
        
        # Create new headers without the file extension
        new_headers = ["wavenumber"] + [remove_extension(filename)]
        df.columns = new_headers
        
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
print(merged_df.head())
