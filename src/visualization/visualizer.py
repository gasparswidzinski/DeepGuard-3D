import pyvista as pv
import numpy as np
import pandas as pd

class BathymetryVisualizer:
    
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
    
    def render_point_cloud(self):
        print("[*] Initializing 3D Engine...")
        
        # 1. Extract coordinates
        x = self.df['longitude'].values
        y = self.df['latitude'].values
        z = self.df['depth'].values

        # 2. APPLY SCALING (The Fix)
        # We shrink the Z axis so it matches the 'scale' of degrees
        # Or we can think of it as Z_scaled = Z * 0.01
        z_visual = z * 0.01 

        points = np.column_stack((x, y, z_visual))
        
        point_cloud = pv.PolyData(points)
        point_cloud["Depth (m)"] = z # We keep the original values for the legend

        plotter = pv.Plotter(title="DeepGuard 3D - Scaled Terrain")
        plotter.set_background("black")
        
        plotter.add_mesh(
            point_cloud, 
            scalars="Depth (m)", 
            cmap="viridis", 
            point_size=5.0, 
            render_points_as_spheres=True
        )

        plotter.add_scalar_bar(title="True Depth (m)")
        # This makes the floor look like a square instead of a line
        plotter.set_scale(zscale=1.0) 
        
        plotter.show()
    