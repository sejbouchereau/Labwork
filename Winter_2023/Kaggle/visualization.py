import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Modifier le chemin pour votre emplacement des fichiers combinés du Dataset
data_file = r"C:\Users\sejbo\.kaggle\420-318-ah-a24\full_dataset.csv"
sample_file = r"C:\Users\sejbo\.kaggle\420-318-ah-a24\sample_dataset.csv"   # 200 000 premières données

# Importer (changer data_file -> sample_file pour visualiser l'échantillon seulement)
data = pd.read_csv(data_file)

# Convertir en format Timestamp
data['Timestamp [ms]'] = pd.to_datetime(data['Timestamp [ms]'])

# Trier et interpoler les données en ordre chronologique
data = data.sort_values(by='Timestamp [ms]').interpolate(method='linear')

# Filtrer les données aberrantes du CPU usage [%]
# data = data[(data['CPU usage [%]'] >= 0) & (data['CPU usage [%]'] <= 100)]

# Filtrer les données aberrantes du Memory usage [KB] pour ne conserver que les pics importants
# data = data[(data['Memory usage [KB]'] >= 12500000) & (data['Memory usage [KB]'] <= 22500000)]

# Création du template des graphiques
fig, axs = plt.subplots(2, 2, figsize=(15, 8))

# 1. Tracer le CPU usage et le memory usage
ax1 = axs[0, 0]
ax1.plot(data['Timestamp [ms]'], data['CPU usage [%]'], color='tab:blue', label='CPU usage [%]', linewidth=0.1)
ax1.set_xlabel('Time')
ax1.set_ylabel('CPU usage [%]', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.plot(data['Timestamp [ms]'], data['Memory usage [KB]'], color='tab:red', label='Memory usage [KB]', linewidth=0.4)
ax2.set_ylabel('Memory usage [KB]', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

ax1.set_title('CPU usage [%] & Memory usage [KB]')

# 2. Boxplot du CPU usage [%]
ax2_1 = axs[0, 1]
sns.boxplot(data=data, x='CPU usage [%]', color='tab:blue', ax=ax2_1)
ax2_1.set_title('CPU usage [%] Boxplot')
ax2_1.set_xlabel('CPU usage [%]')

# 3. Histogramme du CPU usage [%]
ax3_1 = axs[1, 0]
sns.histplot(data['CPU usage [%]'], bins=200, color='tab:blue', kde=True, ax=ax3_1)
ax3_1.set_xlabel('CPU usage [%]')
ax3_1.set_ylabel('Frequency')
ax3_1.set_title('CPU usage [%]')

# 4. Heatmap des corrélations
ax4_1 = axs[1, 1]
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True, ax=ax4_1)
ax4_1.set_title('Dataset Heatmap')

# Afficher
plt.tight_layout()
plt.show()

# Afficher les informations du Dataset
# print(data.info())
