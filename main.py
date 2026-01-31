from src.core.ingestor import BathymetryIngestor    
import os

def main():
    
    print("---- DeepGuard 3D Bathymetry Ingestion ----")
    
    #1.define the path to the raw data
    data_path = os.path.join("data","raw","mock_seabed.csv")
    
    
    
    #2. initialize the ingestor
    try:
        
        ingestor = BathymetryIngestor(data_path)
        
        #3. load the data
        df = ingestor.load_data()
        
        #4. display engineering statistics
        print("\n[i] Seabed Statistical Summary:")
        print("-"*30)
        stats = ingestor.get_statistics()
        print(stats)
        print("-"*30)
        
        #5. quick chet deepest point
        deepest_point = df['depth'].min()
        print(f"[i] Deepest Point: {deepest_point:.2f} meters")
        
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        print("Tip: Run 'python scripts/generate_mock_data.py' first!")
    except Exception as e:
        print(f"[FATAL ERROR] An unexpected error occurred: {e}")
    
if __name__ == "__main__":
    main()