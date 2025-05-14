#Automating server health checks using psutil:
import psutil
cpu_usage =psutil.cpu_percent(interval = 1)

free_memory=psutil.virtual_memory().free /(1024 ** 3)
used_memory= psutil.virtual_memory().used/ (1024 ** 3)

disk_usage = psutil.disk_usage('/')

print(f"cpuusage :{cpu_usage}%,freememoru:{free_memory}GB,used memory{used_memory}GB")