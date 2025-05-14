#log cleanup script
"""logs = ['2025-04-22 10:22:31', 'Error: File not found', '404', 'Disk full', '100% usage']
logs_cleaned = '\n'.join([log for log in logs if any(ch.isalpha() or ch.isdigit() for ch in log) ])
print(logs_cleaned)"""

# extract and join only 
logs = ['INFO: System started', 'error: connection timeout', 'WARNING: Low disk', 'ERROR: Disk failure']
result = '|'.join([log for log in logs if 'error' in log.lower()])
print (result)