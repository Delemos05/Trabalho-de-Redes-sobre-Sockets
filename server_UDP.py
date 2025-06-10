import random
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('192.168.1.7', 12000))

while True:
    rand = random.randint(0, 10)
    message, address = server_socket.recvfrom(2048)
    message = message.upper()
    if rand >= 4:
        server_socket.sendto(message, address)