import socket

def scan_ports(target_ip, start_port = 1, end_port = 1024):
    list_ports = []

    print(f'[+] Iniciando varredura as portas. Iniciando em: {start_port} ate {end_port}')

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            print(f'[+] A porta analisada {port} esta aberta.')
            list_ports.append(port)
        
        sock.close()

    return list_ports

if __name__ == "__main__":
    target_ip = '10.0.2.5'
    lista_portas = scan_ports(target_ip=target_ip)

    print(f'Portas abertas: {lista_portas}')