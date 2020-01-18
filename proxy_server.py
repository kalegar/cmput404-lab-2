import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.google.com",80))
print('Connected to google')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("",8001))
server.listen()
print('server started...')
while True:
    conn, addr = server.accept()
    with conn:
        print('recieved connection')
        data = conn.recv(1024)
        sock.sendall(data)
        d = sock.recv(1024)
        while d:
            conn.sendall(d)
            d = sock.recv(1024)
    conn.close()
    print('closed connection')
    
print('shutting down...')
server.shutdown(socket.SHUT_RDWR)
server.close()

sock.shutdown(socket.SHUT_RDWR)
sock.close()
