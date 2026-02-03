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
        
        
        
    def get_statistics(self) -> dict:
        """Devuelve estadísticas básicas del relieve submarino"""
        if self.data is not None:
            return self.data['depth'].describe()
    