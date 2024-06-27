import pandas as pd
import os

# Specify the source directory
source_dir = r"C:\Users\pingk\OneDrive - Chulalongkorn University\RandomDatas\FIKSASI\SPECTROCHEMPY\CSV_files\MiddleBox_file terkonversi ke CSV\RT_3\SAMPLE_LOCATION_based\SL_COUNTRY_LEVEL_based\SLCL_ID"

# Get a list of all CSV files in the directory
csv_files = [os.path.join(source_dir, file) for file in os.listdir(source_dir) if file.lower().endswith(".csv")]

# Read each CSV file into a DataFrame
dfs = [pd.read_csv(file, header=None) for file in csv_files]  # Specify header=None

# Extract filenames without extensions
file_names = [os.path.splitext(os.path.basename(file))[0] for file in csv_files]

# Add headers to each DataFrame
for i, df in enumerate(dfs):
    df.columns = [f"wavenumber_{file_names[i]}", f"absorbance_{file_names[i]}"]

# Merge DataFrames
merged_df = pd.concat(dfs, axis=1)

# Remove duplicated columns (keep the first occurrence)
merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]

# Save merged DataFrame to a new CSV file
output_file = os.path.join(source_dir, "merged_output.csv")  # Include the file extension
merged_df.to_csv(output_file, index=False)

print(f"Merged DataFrame exported to: {output_file}")
