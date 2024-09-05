# jun/28/2024 19:15:41 by RouterOS 7.6
# software id = 
#
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=dhcp_pool0 ranges=172.25.28.130-172.25.28.254
/ip dhcp-server
add address-pool=dhcp_pool0 interface=ether3 name=dhcp1
/port
set 0 name=serial0
set 1 name=serial1
/ip address
add address=172.25.28.129/25 interface=ether3 network=172.25.28.128
add address=172.25.28.1/25 interface=ether2 network=172.25.28.0
/ip dhcp-client
add interface=ether1
/ip dhcp-server network
add address=172.25.28.128/25 gateway=172.25.28.129
