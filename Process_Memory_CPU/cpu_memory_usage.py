import psutil 
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().total/(1024 ** 3)
# top memory consuming process
for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
    try:
        print(proc.info)
    except psutil.NoSuchProcess:
        pass

print(f"cpu usuage in percentage:{cpu_usage}")
print(f"memoryusage in percenatge:{memory_usage:.2f}")

