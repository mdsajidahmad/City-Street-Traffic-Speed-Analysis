import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'Street': ['MG Road', 'MG Road', 'MG Road', 'Ring Road', 'Ring Road', 'Ring Road',
               'Station Road', 'Station Road', 'Station Road'],
    'Hour': [8, 14, 18, 8, 14, 18, 8, 14, 18],
    'Average_Speed': [18, 35, 20, 22, 45, 25, 15, 30, 18]
}

df = pd.DataFrame(data)
df
df.info()
df.describe()
plt.figure(figsize=(8,5))

for street in df['Street'].unique():
    street_data = df[df['Street'] == street]
    plt.plot(street_data['Hour'], street_data['Average_Speed'], marker='o', label=street)

plt.xlabel("Hour of Day")
plt.ylabel("Average Speed (km/h)")
plt.title("Traffic Speed Variation Over Time")
plt.legend()
plt.grid(True)
plt.show()
pivot_table = df.pivot(index='Street', columns='Hour', values='Average_Speed')

plt.figure(figsize=(7,4))
sns.heatmap(pivot_table, annot=True, cmap='Reds')
plt.title("Traffic Congestion Heatmap")
plt.xlabel("Hour")
plt.ylabel("Street")
plt.show()
def congestion_level(speed):
    if speed < 20:
        return 'High Congestion'
    elif speed <= 40:
        return 'Moderate Traffic'
    else:
        return 'Free Flow'

df['Congestion_Level'] = df['Average_Speed'].apply(congestion_level)
df
