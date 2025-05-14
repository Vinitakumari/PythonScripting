logs = [
    '192.168.0.1 - GET /index.html',
    'INFO: Connected to DB',
    '172.16.0.5 - POST /upload',
    'No IP here'
]

import re
ips =[re.match(r'\d+\.\d+\.\d+\.\d+',line)for line in logs]
result =[','.join( ip.group()for ip in ips if ip)]
print (result)

