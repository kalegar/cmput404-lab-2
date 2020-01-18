import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("",8001))
server.listen()

conn, addr = server.accept()
with conn:
    print('Peer name: {0}'.format(conn.getpeername()))
    print('Sock name: {0}'.format(conn.getsockname()))
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
