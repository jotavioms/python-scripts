# Executar na máquina atacante no diretorio dos scripts
# scp client.py {login da vítima}@{IP da vítima}:{pasta de destino}

scp client.py msfadmin@10.0.2.5:/tmp

# Após o erro
scp -o HostKeyAlgorithms=+ssh-rsa client.py msfadmin@10.0.2.5:/tmp