from src.core.ingestor import BathymetryIngestor
from src.visualization.visualizer import BathymetryVisualizer
from src.security.integrity import DataIntegrityManager
import os

def main():
    print("--- DeepGuard 3D: Mission Control ---")
    data_path = os.path.join("data", "raw", "output_SRTM15Plus.tif")
    
    # 1. SECURITY LAYER
    integrity = DataIntegrityManager(data_path)
    current_hash = integrity.calculate_sha256()
    print(f"[SEC] SHA-256 Fingerprint: {current_hash}")
    
    # 2. INGESTION LAYER
    ingestor = BathymetryIngestor(data_path)
    df = ingestor.load_data()
    
    # 3. VISUALIZATION LAYER
    visualizer = BathymetryVisualizer(df)
    visualizer.render_point_cloud()

if __name__ == "__main__":
    main()