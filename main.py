from src.core.ingestor import BathymetryIngestor
from src.visualization.visualizer import BathymetryVisualizer
from src.security.integrity import DataIntegrityManager
from src.security.logger import SecurityLogger
import os

def main():
    print("--- DeepGuard 3D: Mission Control ---")
    data_path = os.path.join("data", "raw", "output_SRTM15Plus.tif")
    
    # 1. SECURITY AUDIT START
    logger = SecurityLogger()
    integrity = DataIntegrityManager(data_path)
    current_hash = integrity.calculate_sha256()
    
    # 2. DATA PROCESSING
    ingestor = BathymetryIngestor(data_path)
    df = ingestor.load_data()
    
    # 3. THREAT ANALYSIS
    danger_points = df[df['depth'] > -7.0].shape[0]
    
    # 4. RECORD THE EVENT
    logger.log_event("output_SRTM15Plus.tif", current_hash, danger_points)
    
    # 5. VISUALIZATION
    visualizer = BathymetryVisualizer(df)
    visualizer.render_point_cloud()

if __name__ == "__main__":
    main()