import psutil

# Keyword to look for in process names or command lines

keyword = "docker"

print(f"Searching for processes containing '{keyword}'...\n")

found = False
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        name = proc.info['name'] or ""
        cmdline = proc.info['cmdline'] or []

        if keyword in name.lower() or any(keyword in arg.lower() for arg in cmdline):
            print(f"PID: {proc.info['pid']}, Name: {name}, Cmdline: {cmdline}")
            found = True

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue

if not found:
    print("No docker-related processes found.")


"""for proc in psutil.process_iter(['name','pid']):
    if proc.info['Name']=='ansible.exe':
        proc.kill()
    print(f"process killed:{proc.info['pid']}")"""