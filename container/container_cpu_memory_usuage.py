import subprocess
import time
import shlex

THRESHOLD = 80

def container_cpu_memory_usuage():
    #docker stats cmd -> docker stats --no-stream --format {{.Name}} {{.CPUPerc}}
   
    try:
        # Correctly formatted string with escaped inner double quotes
        cmd = "docker stats --no-stream --format \"{{.Name}} {{.CPUPerc}}\""
        stats_output = subprocess.check_output(shlex.split(cmd)).decode().strip()
        return stats_output.split('\n')
    except subprocess.CalledProcessError as e:
        print("Error occurred while fetching docker stats:")
        print(e.output.decode())
        return []

"""while True:
    stats = container_cpu_memory_usuage()
    name,cpu = """

stats =container_cpu_memory_usuage()
print (stats)
