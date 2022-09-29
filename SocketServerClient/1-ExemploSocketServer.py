import socket
import subprocess
import threading

# IP = "localhost"
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', PORT))  # server.bind((IP, PORT))

server.listen(1)
print("[+] Serv startado")

client, client_addr = server.accept()
print(f" {client_addr} O cliente abriu o chat")


def enviar():
    global client, client_addr

    while True:
        msg = input("MSG>>> ")
        msg = msg.encode()
        client.send(msg)
        print("Mensagem enviada!")


def receber():
    global client, server

    while True:
        msg2 = client.recv(1024)
        msg2 = msg2.decode(encoding='UTF-8', errors='ignore')
        print("\nOutput: ", msg2)


threading.Thread(target=enviar).start()
threading.Thread(target=receber).start()