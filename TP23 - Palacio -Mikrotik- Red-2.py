from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.0.0.37',
    'username': 'admin',
    'password': '1234',
    'port': 22,            # optional, defaults to 22
    'secret': '',           # optional, defaults to ''
}

conexion = ConnectHandler(**router_mikrotik)

# Definir comandos a ejecutar
configurar = [
    '/ip pool add name=dhcp_pool0 ranges=172.26.28.130-172.26.28.254',
    '/ip dhcp-server add address-pool=dhcp_pool0 interface=ether2 name=dhcp1',
    '/ip address add address=172.26.28.129/25 interface=ether2 network=172.26.28.128',
    '/ip address add address=192.168.28.2/30 interface=ether3 network=192.168.28.0',
    '/ip dhcp-client add interface=ether1',
    '/ip dhcp-server network add address=172.26.28.128/25 gateway=172.26.28.129',
    '/ip firewall nat add action=masquerade chain=srcnat out-interface=ether1',
    '/ip route add disabled=no dst-address=172.26.28.0/25 gateway=192.168.28.1 routing-table=main suppress-hw-offload=no',
]

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar)
print(accion1)

# Visualizar comandos (send_command - para enviar comandos de visualización)
accion2 = conexion.send_command('/ip address print')
print(accion2)

# Cerrar la conexión
conexion.disconnect()