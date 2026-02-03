import pyvista as pv
import pandas as pd
import numpy as np

class BathymetryVisualizer:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def render_point_cloud(self):
        print("[*] Applying Security Overlay...")
        
        # 1. Processing 
        sea_data = self.df[self.df['depth'] < 0].copy()
        x = (sea_data['longitude'].values - sea_data['longitude'].min()) * 111000
        y = (sea_data['latitude'].values - sea_data['latitude'].min()) * 111000
        z = sea_data['depth'].values

        points = np.column_stack((x, y, z))
        surf = pv.PolyData(points).delaunay_2d()

        # 2. THE SECURITY LOGIC: Create an Alert Mask
        # Anything between 0 and -7 meters is "Danger"
        danger_threshold = -7.0
        is_danger = z > danger_threshold 

        # 3. Setup Plotter
        plotter = pv.Plotter(title="DeepGuard 3D - Security Dashboard")
        plotter.set_background("#050505")
        
        # Base Mesh
        plotter.add_mesh(surf, scalars=z, cmap="viridis", label="Standard Depth")

        
        danger_points = points[is_danger]
        if len(danger_points) > 0:
            plotter.add_mesh(
                pv.PolyData(danger_points), 
                color="red", 
                point_size=10, 
                render_points_as_spheres=True,
                label="!!! SHALLOW WATER ALERT !!!"
            )
        
        water_surface = pv.Plane(
            center=(np.mean(x), np.mean(y), 0),
            direction=(0, 0, 1),
            i_size=max(x)-min(x),
            j_size=max(y)-min(y)
        )
        
        plotter.add_mesh(
        water_surface, 
        color="#00b4d8", 
        opacity=0.2,    
        label="Mean Sea Level"
    )

        plotter.add_legend()
        plotter.add_axes()
        print(f"[!] Alert: {len(danger_points)} shallow points detected in the harbor.")
        plotter.show()