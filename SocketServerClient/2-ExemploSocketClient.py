import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem_envio = input('Digite a mensagem:')
    client.sendto(mensagem_envio.encode(),('127.0.0.1',12000))
    mensagem_bytes, endereco_ip_servidor = client.recvfrom(2048)
    print(mensagem_bytes.decode())