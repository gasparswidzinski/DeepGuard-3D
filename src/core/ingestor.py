import pandas as pd
import numpy as np
import os   

class BathymetryIngestor:
    """
    Clase encargada de la ingesta segura de datos batimétricos.
    """
    def __init__(self,file_path: str):
        self.file_path = file_path
        self.data = None
        
    def load_data(self) -> pd.DataFrame:
        """Carga datos desde un archivo .csv o .xyz"""
        
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No se encontro el archivo {self.file_path}")
        
        print(f"[*] Cargando datos desde: {self.file_path}")
        
        # Leo el archivo asumiendo formato: Longitud, Latitud, Profundidad
        self.data = pd.read_csv(self.file_path, names=['longitude', 'latitude', 'depth'])
        
        print(f"[+] Exito al cargar {len(self.data)} registros.")
        
        return self.data
    
    def get_statistics(self) -> dict:
        """Devuelve estadísticas básicas del relieve submarino"""
        if self.data is not None:
            return self.data['depth'].describe()
    