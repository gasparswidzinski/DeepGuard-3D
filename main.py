from src.core.ingestor import BathymetryIngestor
from src.visualization.visualizer import BathymetryVisualizer    
import os

def main():
    
    print("---- DeepGuard 3D Bathymetry Ingestion ----")
    
    #1.define the path to the raw data
    data_path = os.path.join("data","raw","mock_seabed.csv")
    
    
    
    #2. initialize the ingestor
    try:
        # Ingestion
        ingestor = BathymetryIngestor(data_path)
        df = ingestor.load_data()
        
        # Statistics
        print("\n[i] Seabed Statistical Summary:")
        print(ingestor.get_statistics())
        
        # Visualization
        visualizer = BathymetryVisualizer(df)
        visualizer.render_point_cloud()

    except Exception as e:
        print(f"[FATAL ERROR] {e}") 
    
if __name__ == "__main__":
    main()