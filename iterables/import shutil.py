import shutil
import os
def backup_files(src,dest):
    try:
       shutil.copytree(src,dest)

       print("backup")
    except Exception as e:
       print(f"backup: {e}")

 



if __name__=='__main__':
 backup_files("", "/backup/data")