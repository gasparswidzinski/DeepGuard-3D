import datetime
import os


class SecurityLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_file = os.path.join(log_dir, "security_audit.log")
    
    def log_event(self, filename, file_hash, alerts_count):
        """Generates a permanent audit record of the scan."""
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        status = "CRITICAL" if alerts_count > 0 else "SECURE"
        
        entry = (
            f"[{timestamp}] SOURCE: {filename} | "
            f"INTEGRITY: {file_hash[:16]}... | "
            f"ALERTS: {alerts_count} | STATUS: {status}\n"
        )
        
        with open(self.log_file, "a") as f:
            f.write(entry)
        print(f"[i] Security audit saved to {self.log_file}")
            