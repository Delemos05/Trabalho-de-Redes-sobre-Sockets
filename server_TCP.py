import random
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.7', 12000))
server_socket.listen(1)

while True:
    connection_socket, addr = server_socket.accept()
    try:
        rand = random.randint(0, 10)
        message = connection_socket.recv(2048)
        message = message.upper()
        if rand >= 4:
            connection_socket.send(message)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection_socket.close()