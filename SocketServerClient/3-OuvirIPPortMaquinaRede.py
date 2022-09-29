import socket
import subprocess
import threading

#SERV_IP = socket.gethostname()
SERV_IP = "10.57.76.10" #Altere o IP da máquina que quer ficar ouvindo na rede
SERV_PORT = 8500 #Altere a porta da máquina que quer ficar ouvindo na rede

back = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
back.connect((SERV_IP, SERV_PORT))


def receber():
    global back
    while True:
        msg = back.recv(1024)
        msg = msg.decode()  # encoding = 'UTF-8',errors = 'ignore'
        print("\nOutput: ", msg)


def enviar():
    global back
    while True:
        msg2 = input("MSG>>> ")
        msg2 = msg2.encode()
        back.send(msg2)
        print("Mensagem enviada!")


threading.Thread(target=receber).start()
threading.Thread(target=enviar).start()