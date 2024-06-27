import pandas as pd
import glob
import os

# Directory containing the CSV files
directory = r'C:\Users\pingk\Downloads\coba\hasil\Spectrochempy'

# Output directory and file name
output_file = r'C:\Users\pingk\Downloads\coba\hasil\Spectrochempy\merged_output.csv'

# Find all CSV files in the directory
csv_files = glob.glob(os.path.join(directory, '*.csv'))

# List to hold individual dataframes
dfs = []

# Process each CSV file
for file in csv_files:
    # Load the CSV file without header
    df = pd.read_csv(file, header=None)
    
    # Get the filename without extension
    filename = os.path.splitext(os.path.basename(file))[0]
    
    # Ensure that the CSV file has exactly 2 columns
    if df.shape[1] == 2:
        # Rename the columns
        df.columns = [f'wavenumber_{filename}', f'absorbance_{filename}']
        # Append the dataframe to the list
        dfs.append(df)
    else:
        print(f"File {file} skipped due to unexpected number of columns: {df.shape[1]}")

# Merge all dataframes
if dfs:
    merged_df = pd.concat(dfs, axis=1)
    
    # Remove exact duplicates
    merged_df = merged_df.loc[:,~merged_df.columns.duplicated()]
    
    # Extract parts of the filename for the rows to be added
    first_2_chars = [os.path.splitext(os.path.basename(file))[0][:2] for file in csv_files if pd.read_csv(file, header=None).shape[1] == 2]
    chars_4_to_6 = [os.path.splitext(os.path.basename(file))[0][3:6] for file in csv_files if pd.read_csv(file, header=None).shape[1] == 2]
    chars_12_to_15 = [os.path.splitext(os.path.basename(file))[0][11:15] for file in csv_files if pd.read_csv(file, header=None).shape[1] == 2]
    
    # Create new rows
    row_first_2_chars = [item for sublist in zip(first_2_chars, first_2_chars) for item in sublist]
    row_chars_4_to_6 = [item for sublist in zip(chars_4_to_6, chars_4_to_6) for item in sublist]
    row_chars_12_to_15 = [item for sublist in zip(chars_12_to_15, chars_12_to_15) for item in sublist]
    
    # Insert new rows at the top of the dataframe
    merged_df.loc[-1] = row_first_2_chars
    merged_df.index = merged_df.index + 1
    merged_df = merged_df.sort_index()
    
    merged_df.loc[-1] = row_chars_4_to_6
    merged_df.index = merged_df.index + 1
    merged_df = merged_df.sort_index()
    
    merged_df.loc[-1] = row_chars_12_to_15
    merged_df.index = merged_df.index + 1
    merged_df = merged_df.sort_index()
    
    # Save the final dataframe to a new CSV file
    merged_df.to_csv(output_file, index=False)
    print(f"Merged CSV file created successfully: {output_file}")
else:
    print("No valid CSV files found to merge.")
