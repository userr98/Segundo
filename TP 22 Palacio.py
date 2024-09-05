from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.0.0.80',
    'username': 'admin',
    'password': '1234',
    'port': 22,            # optional, defaults to 22
    'secret': '',           # optional, defaults to ''
}

conexion = ConnectHandler(**router_mikrotik)

# Definir comandos a ejecutar
configurar = [
    '/interface wireless security-profiles set [ find default=yes ] supplicant-identity=MikroTik',
    '/ip pool add name=dhcp_pool0 ranges=172.25.20.130-172.25.20.254',
    '/ip dhcp-server add address-pool=dhcp_pool0 interface=ether3 name=dhcp1',
    '/port set 0 name=serial0',
    '/port set 1 name=serial1',
    '/ip address add address=172.25.20.1/25 interface=ether2 network=172.25.20.0',
    '/ip address add address=172.25.20.129/25 interface=ether3 network=172.25.20.128',
    '/ip dhcp-client add interface=ether1',
    '/ip dhcp-server network add address=172.25.20.128/25 gateway=172.25.20.129',
    '/ip firewall nat add action=masquerade chain=srcnat out-interface=ether1',
    '/ipv6 firewall nat add action=accept chain=srcnat out-interface=ether1'
]

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar)
print(accion1)

# Visualizar comandos (send_command - para enviar comandos de visualización)
accion2 = conexion.send_command('/ip address print')
print(accion2)

# Cerrar la conexión
conexion.disconnect()