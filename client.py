import socket

sock = socket.create_connection(("www.google.com", 80))

def recieve_data(sock, size):
    dat = sock.recv(size)
    while dat:
        print(dat)
        dat = sock.recv(size)
msg = 'GET / HTTP/1.0 \r\n\r\n'

sock.sendall(msg.encode())
recieve_data(sock,1024)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
