import re
import os


def extract_instance_from_logs(log_file):
    instance_pattern = r"i-[0-9a-fA-F]{17}"
    with open( log_file,"r") as f:
        for line in f:
            instances = []
            matches = re.findall(instance_pattern,line)
            instances.extend(matches)
        return list(set(instances))

        
base_path = os.path.dirname(__file__)
log_file_path= os.path.join(base_path,"log_file.log")  
instances =extract_instance_from_logs(log_file_path)
for instance in instances:
    print(f"instance:{instance}")