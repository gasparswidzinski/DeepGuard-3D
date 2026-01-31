import pandas as pd
import numpy as np
import os

def generate_bathymetry_csv(filename: str, num_points: int = 10000):
    """
    Generates a dummy CSV file with longitude, latitude and depth data
    """
    # Coordinates roughly around the Argentine Continental Shelf
    lon = np.random.uniform(-60.0, -55.0,num_points)
    lat = np.random.uniform(-40.0, -35.0,num_points)
    
    # Depth in meters (negative values for underwater)
    depth = -1 * (np.random.uniform(50, 500,num_points) + np.sin(lon)*10)
    
    df = pd.DataFrame({
        'longitude': lon,
        'latitude': lat,
        'depth': depth
    })
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    df.to_csv(filename, index=False, header=False)
    print(f"[+] Successfully generates {num_points} bathymetry points at {filename}")

if __name__ == "__main__":
    output_path = "data/raw/mock_seabed.csv"
    generate_bathymetry_csv(output_path)