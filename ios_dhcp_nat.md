# DHCP y NAT para IOS

## DHCP

```
configure terminal
ip dhcp pool
network 192.168.20.0 255.255.255.0
default-router 192.168.20.1
exit
```


## NAT

```
interface gigabitethernet 0/2
ip nat inside

interface gigabitethernet 0/1
ip nat outside

access-list 1 permit 192.168.20.0 0.0.0.255
ip nat inside source list 1 interface GigabitEthernet0/1 overload
```
