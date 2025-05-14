logs = ["error.log","access.log","debug.log"]
Important_logs = [ log for log in logs if log.startswith(("a","e"))]
print(Important_logs)