from datetime import datetime,timedelta
import os
import time

# directory containing log files
log_dir = r"C:/Users/HP/Desktop/log"

def remove_log_files(directory_path,days):
    now = time.time() #current time in seconds
    cutoff_time = now-days *86400

    # iterate through the files
   
    for file in os.listdir(directory_path):
        #try:
        file_path = os.path.join(directory_path,file)
       # except Exception as e:
        #  raise e
      
        
        if os.path.isfile(file_path):
            file_modified_time = os.path.getmtime(file_path)

            if file_modified_time <cutoff_time:
                os.remove(file_path)
                print("fDeleted:{file_path}")
remove_log_files(log_dir,7)

