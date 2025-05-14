import os
import time
from datetime import datetime, timedelta
from pathlib import Path

log_dir = Path("/tmp/test-logs")
log_dir.mkdir(parents=True, exist_ok=True)

# Create log files with timestamps from 8 to 17 days ago
for i in range(8, 18):
    log_file = log_dir / f"app-log-{i}.log"
    log_file.touch()
    
    # Set file's modification time to `i` days ago
    backdate = datetime.now() - timedelta(days=i)
    mod_time = backdate.timestamp()
    os.utime(log_file, (mod_time, mod_time))

print("Old log files created.")