import pandas as pd
import os

# Chemin vers le dossier contenant le Dataset (à changer selon l'emplacement de vos fichiers locaux)
path = r"C:\Users\sejbo\.kaggle\420-318-ah-a24\Bitbrains-fastStorage\2013-8"
output_data_file = r"C:\Users\sejbo\.kaggle\420-318-ah-a24\dataset.csv"
output_sample_file = r"C:\Users\sejbo\.kaggle\420-318-ah-a24\sample.csv"

# Lister tous les fichiers .csv
csv_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]

# Charger les fichiers .csv
dfs = []
for file in csv_files:
    df = pd.read_csv(file, sep=';')
    dfs.append(df)

# Combiner tous les DataFrames
combined_data = pd.concat(dfs, ignore_index=True)

# Formater les colonnes
combined_data.columns = [col.strip().replace('\t', '') for col in combined_data.columns]

# Sauvegarder localement l'intégralité des données
combined_data.to_csv(output_data_file, index=False)

# Utiliser uniquement les 200k premières lignes du Dataset
data_sample = combined_data.head(200000)

# Sauvegarder localement le sample
data_sample.to_csv(output_sample_file, index=False)

print(f"Fichiers sauvagardés à l'emplacement : {output_data_file, output_sample_file}")
