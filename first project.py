import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import datetime

# 1. SETUP: Generate Synthetic Traffic Data (Simulating a City)
np.random.seed(42)
rows = 1000
data = {
    'timestamp': pd.date_range(start='2023-01-01', periods=rows, freq='H'),
    'street_id': np.random.choice(['Main St', 'Broadway', '5th Ave', 'Park Ave'], rows),
    'latitude': np.random.uniform(40.70, 40.80, rows),
    'longitude': np.random.uniform(-74.00, -73.90, rows)
}

df = pd.DataFrame(data)

# Create a "Speed" column with logic (Lower speed during Rush Hours)
def calculate_speed(row):
    hour = row['timestamp'].hour
    # Typical Rush Hours: 8-10 AM and 5-7 PM
    if 8 <= hour <= 10 or 17 <= hour <= 19:
        return np.random.uniform(5, 25) # Congested
    else:
        return np.random.uniform(30, 60) # Free Flow

df['speed_kmh'] = df.apply(calculate_speed, axis=1)
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.day_name()

# --- ANALYSIS & VISUALIZATION ---

# 2. LINE PLOT: Speed Variations by Hour
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='hour', y='speed_kmh', hue='street_id', marker='o')
plt.title('Average Traffic Speed Variation by Hour', fontsize=15)
plt.xlabel('Hour of Day (24h Format)')
plt.ylabel('Average Speed (km/h)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 3. HEATMAP: Day vs. Hour Congestion
# Pivot data for the heatmap
pivot_df = df.groupby(['day_of_week', 'hour'])['speed_kmh'].mean().unstack()
# Reorder days for better visualization
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pivot_df = pivot_df.reindex(days)

plt.figure(figsize=(14, 7))
sns.heatmap(pivot_df, cmap='RdYlGn', annot=True, fmt=".0f")
plt.title('City-Wide Speed Heatmap (Red = Congested, Green = Fast)', fontsize=15)
plt.xlabel('Hour of Day')
plt.ylabel('Day of Week')
plt.show()

# 4. SPATIAL MAP: Congestion Zones (Using Plotly)
fig = px.density_mapbox(df, lat='latitude', lon='longitude', z='speed_kmh', radius=20,
                        center=dict(lat=40.75, lon=-73.95), zoom=11,
                        mapbox_style="carto-positron",
                        title='Spatial Congestion Hotspots (Inverse Speed)')
fig.show()