import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Update the path to your location of the combined Dataset files
data_file = r"C:\Users\sejbo\.kaggle\420-318-ah-a24\full_dataset.csv"
sample_file = r"C:\Users\sejbo\.kaggle\420-318-ah-a24\sample_dataset.csv"   # First 200,000 records

# Import data (change data_file -> sample_file to visualize only the sample)
data = pd.read_csv(data_file)

# Convert to Timestamp format
data['Timestamp [ms]'] = pd.to_datetime(data['Timestamp [ms]'])

# Sort and interpolate the data in chronological order
data = data.sort_values(by='Timestamp [ms]').interpolate(method='linear')

# Filter outliers in CPU usage [%]
# data = data[(data['CPU usage [%]'] >= 0) & (data['CPU usage [%]'] <= 100)]

# Filter outliers in Memory usage [KB] to keep only significant peaks
# data = data[(data['Memory usage [KB]'] >= 12500000) & (data['Memory usage [KB]'] <= 22500000)]

# Create the graph template
fig, axs = plt.subplots(2, 2, figsize=(15, 8))

# 1. Plot CPU usage and memory usage
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

# 2. Boxplot of CPU usage [%]
ax2_1 = axs[0, 1]
sns.boxplot(data=data, x='CPU usage [%]', color='tab:blue', ax=ax2_1)
ax2_1.set_title('CPU usage [%] Boxplot')
ax2_1.set_xlabel('CPU usage [%]')

# 3. Histogram of CPU usage [%]
ax3_1 = axs[1, 0]
sns.histplot(data['CPU usage [%]'], bins=200, color='tab:blue', kde=True, ax=ax3_1)
ax3_1.set_xlabel('CPU usage [%]')
ax3_1.set_ylabel('Frequency')
ax3_1.set_title('CPU usage [%]')

# 4. Heatmap of correlations
ax4_1 = axs[1, 1]
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True, ax=ax4_1)
ax4_1.set_title('Dataset Heatmap')

# Display the graphs
plt.tight_layout()
plt.show()

# Display information about the Dataset
# print(data.info())
