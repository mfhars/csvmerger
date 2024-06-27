import pandas as pd

# Load the merged CSV file
merged_file_path = r"C:\Users\pingk\Downloads\coba\hasil\Spectrochempy\merged_output.csv"  # Replace with the actual path to your merged CSV file
merged_df = pd.read_csv(merged_file_path)

# Identify columns that start with 'wavenumber_'
wavenumber_columns = [col for col in merged_df.columns if col.startswith('wavenumber_')]

# Ignore the first three rows for duplicate checking
data_to_check = merged_df.iloc[3:]

# Identify duplicate 'wavenumber' columns based on the data starting from the 4th row
duplicate_columns = data_to_check[wavenumber_columns].T.duplicated(keep='first')

# List of columns to keep (non-duplicate 'wavenumber' columns)
columns_to_keep = [col for col, is_duplicate in zip(wavenumber_columns, duplicate_columns) if not is_duplicate]

# Add the corresponding 'absorbance' columns to the list of columns to keep
for col in columns_to_keep:
    absorbance_col = col.replace('wavenumber_', 'absorbance_')
    columns_to_keep.append(absorbance_col)

# Filter the DataFrame to keep only the relevant columns
final_df = merged_df[columns_to_keep]

# Save the final DataFrame to a new CSV file
cleaned_output_file = 'cleaned_final_merged_output.csv'  # Replace with desired output path
final_df.to_csv(cleaned_output_file, index=False)

print("Cleaned final merged CSV file created successfully:", cleaned_output_file)
