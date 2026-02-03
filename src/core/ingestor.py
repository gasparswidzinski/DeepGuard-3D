import pandas as pd
import numpy as np
import os   
import rasterio

class BathymetryIngestor:
    """
    Clase encargada de la ingesta segura de datos batimétricos.
    """
    def __init__(self,file_path: str):
        self.file_path = file_path
        self.data = None
        
    def load_data(self) -> pd.DataFrame:
        """Carga datos desde un archivo .csv o .xyz"""
        print(f"[*] Extracting real bathymetry from: {self.file_path}")
        with rasterio.open(self.file_path) as dataset:
            data = dataset.read(1)
            # Filter out 'No Data' and land values if necessary
            mask = (data != dataset.nodata ) & (~np.isnan(data))
            rows,col = np.where(mask)
            lons,lats = dataset.xy(rows,col)
            depths = data[rows,col]
            
            return pd.DataFrame({'longitude': lons, 'latitude': lats, 'depth': depths})
        
        
    def get_statistics(self) -> dict:
        """Devuelve estadísticas básicas del relieve submarino"""
        if self.data is not None:
            return self.data['depth'].describe()
    