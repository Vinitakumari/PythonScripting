import subprocess

def restart_multiple_server( service_name,hosts):
   
    for host in hosts:
        cmd = f"ssh  {host} 'sudo systemctl restart {service_name}' "
        try:
           subprocess.run(cmd, shell =True, check= True)
           print(f"{service_name} started in {host}")
        except subprocess.CalledProcessError:
            print(f"error")
