import pandas as pd
import geopandas as gpd 
from shapely.geometry import Point
from pathlib import Path

#First we load the data (dataframe)

data_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "data.csv"

df = pd.read_csv(data_path)

# Second step is to clean the data. This includes handling missing values, standardizing formats, and filtering for relevant records.
# 2.1 Fill numeric gaps
# Fatalities should be 0 if unknown; population columns usually 0 or the median
df['fatalities'] = df['fatalities'].fillna(0)
pop_cols = ['population_1km', 'population_2km', 'population_5km']
for col in pop_cols:
    df[col] = df[col].fillna(0)

# 2.2 Fill categorical gaps
# If an actor or admin level is missing, "Unknown" is better than a blank cell
cat_cols = ['actor1', 'actor2', 'admin1', 'admin2', 'admin3', 'location']
df[cat_cols] = df[cat_cols].fillna('Unknown')

# 2.3 Data Type Standardization
# Convert event_date to actual datetime objects for time-series analysis
df['event_date'] = pd.to_datetime(df['event_date'])

# Ensure numeric columns are actually numbers (sometimes they import as strings)
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

# 2.4 Drop rows with NO coordinates
# You cannot map a point without Lat/Lon. Better to remove them than guess.
df = df.dropna(subset=['latitude', 'longitude'])

# 2.5 Filter relevant event types
# Only keep rows with specific event types of interest
relevant_event_types = ['Battles', 'Explosions/Remote violence', 'Violence against civilians']
df = df[df['event_type'].isin(relevant_event_types)]

# 2.6 Remove duplicate rows (if any)
df = df.drop_duplicates()

# 2.7 Validate coordinate ranges
# Remove rows with invalid latitude or longitude values
df = df[(df['latitude'] >= -90) & (df['latitude'] <= 90)]
df = df[(df['longitude'] >= -180) & (df['longitude'] <= 180)]

# 2.8 Strip whitespace from string columns
str_cols = ['actor1', 'actor2', 'admin1', 'admin2', 'admin3', 'location', 'event_type', 'sub_event_type', 'country', 'region']
for col in str_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()


# Third Convert to GeoDataFrame (Setting CRS to WGS84)
geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

# Fourth Save as GeoJSON (Better for Tableau/QGIS than CSV)
gdf.to_file("processed_incidents.json", driver='GeoJSON')

