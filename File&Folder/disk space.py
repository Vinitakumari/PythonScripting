import os
import shutil
"""def disk_usage(path = "/"):
   stat= os.statvfs(path)
   total = (stat.f_blocks * stat.f_frsize)/(1024 ** 3)
   
   available = (stat.f_bavail *stat.f_frsize) /(1024 ** 3)

   used = total - available
   print(f"total: {total:2f}GB")

disk_usage("/") """
def check_disk_usage(path="C:/"):
    total, used, free = shutil.disk_usage(path)

    # Convert bytes to GB
    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)

    print(f"Total: {total_gb:.2f} GB")
    print(f"Used: {used_gb:.2f} GB")
    print(f"Available: {free_gb:.2f} GB")

check_disk_usage("C:/")
   
