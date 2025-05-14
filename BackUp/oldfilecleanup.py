#How to clean up old files from a directory?
import time
import os
def deleted_log_files(directory,days):

    now= time.time()
    cutoff = now -(days *86400)
    for file in os.listdir(directory):
        file_path = os.path.join(directory,file)
        if os.path.isfile(file_path) and os.stat(file_path).st_mtime <cutoff:
         os.remove(file_path)
         print(f"deleted file :{file_path}")


#directory = os.path.abspath(os.path.dirname(__file__))
deleted_log_files('/tmp/test-logs',7)