import hashlib 
import os

class DataIntegrityManager:
    """
    Acts as the 'Security Gateway' for DeepGuard 3D.
    Responsible for signing and verifying the integrity of bathymetric files.
    """
    
    def __init__(self,file_path: str):
        self.file_path = file_path
        
    
    def calculate_sha256(self) -> str:
        """
        Generates a SHA-256 digital fingerprint of the data.
        We read in chunks (4096 bytes) to handle massive NOAA files without 
        crashing your RAM.
        """
        sha256_hash = hashlib.sha256()
        
        try:
            with open(self.file_path,"rb") as f:
                
                for byte_block in iter(lambda: f.read(4096),b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except FileNotFoundError:
            return "ERROR: File not found. "
    
    def verify_integrity(self,expected_hash: str) -> bool:
        """
        Compares the current file against a 'Known Good' hash.
        This is how we detect 'Data Spoofing' attacks.
        """
        
        current_hash = self.calculate_sha256()
        is_valid = current_hash == expected_hash
        
        if is_valid:
            print(f"[✓] Integrity Verified: Data is authentic.")
        else:
            print(f"[X] SECURITY ALERT: Data has been tampered with!")
        
        return is_valid      