import time
import socket

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(1.0)
    message = b'test'
    addr = ('192.168.1.5', 12000)

    try:
        client_socket.connect(addr)
        start = time.time()
        client_socket.send(message)
        data = client_socket.recv(2048)
        end = time.time()
        elapsed = end - start
        print(f'{data} {pings} {elapsed}')
    except socket.timeout:
        print('REQUEST TIMED OUT')
    except ConnectionRefusedError:
        print('CONNECTION REFUSED')
    finally:
        client_socket.close()