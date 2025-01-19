import pandas as pd
import os

# Path to the folder containing the Dataset (change it according to the location of your local files)
path = r"C:\Users\sejbo\.kaggle\420-318-ah-a24\Bitbrains-fastStorage\2013-8"
output_data_file = r"C:\Users\sejbo\.kaggle\420-318-ah-a24\dataset.csv"
output_sample_file = r"C:\Users\sejbo\.kaggle\420-318-ah-a24\sample.csv"

# List all .csv files
csv_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]

# Load the .csv files
dfs = []
for file in csv_files:
    df = pd.read_csv(file, sep=';')
    dfs.append(df)

# Combine all DataFrames
combined_data = pd.concat(dfs, ignore_index=True)

# Format the columns
combined_data.columns = [col.strip().replace('\t', '') for col in combined_data.columns]

# Save all data locally
combined_data.to_csv(output_data_file, index=False)

# Use only the first 200,000 rows of the Dataset
data_sample = combined_data.head(200000)

# Save the sample locally
data_sample.to_csv(output_sample_file, index=False)

print(f"Files saved at: {output_data_file, output_sample_file}")
