#!/usr/bin/python3
from netmiko import ConnectHandler
import time


hosts = ["10.2.3.107","10.2.3.105","10.2.3.103","10.2.3.108"]
user = "netsim"
password = "netsim1234"
port = 22
commands = ["show ip interface brief","show interface description"]

for host in hosts:
    ssh_client = ConnectHandler(host, device_type='autodetect', username=user, port=port, password=password)
    print(host + ":")
    for command in commands:
        # Aux Vars:
        print(command)
        # Execute command:
        output = ssh_client.send_command_timing(command,last_read=1)
        print(output)
    print("************************************************************************"+"\n")
    ssh_client.disconnect()



