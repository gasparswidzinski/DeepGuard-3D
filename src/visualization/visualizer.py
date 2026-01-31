import pyvista as pv
import numpy as np
import pandas as pd

class BathymetryVisualizer:
    
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe
    
    def render_point_cloud(self):
        """Renders the data as a 3D Point Cloud with a Bathymetric colormap."""
        print("[*] Initializing 3D Engine...")
        
        # Convert DataFrame to a NumPy array for PyVista
        # use Longitude (X), Latitude (Y), and Depth (Z)
        points = self.dataframe[['longitude', 'latitude', 'depth']].values
        
        # Create the PyVista point cloud object
        point_cloud = pv.PolyData(points)
        
        # Add the 'depth' as a scalar field for the colormap
        point_cloud["Depth (m)"] = points[:, 2]
        
        #initialize the plotter
        plotter = pv.Plotter(title= "DeepGuard 3D ")
        plotter.set_background("black") 
        
        plotter.add_mesh(
            point_cloud, 
            scalars="Depth (m)", 
            cmap="viridis", 
            point_size=5.0, 
            render_points_as_spheres=True
        )
        
        plotter.add_scalar_bar(title= "Depth (m)")
        plotter.add_axes()
        print("[+] Rendering window opened. Explore the seabed!")
        plotter.show()
    