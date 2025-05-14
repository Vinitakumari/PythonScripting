# zip () - it is used to combine two or more iterables

servers = ['web1','web2','web3''db1','cache1']
ip_address = ['192.164.255.255','192.172.255.255']
for server,ip in zip(servers, ip_address):
    print(f"{server} has a ip-address{ip_address}")