import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8001))

msg = 'GET / HTTP/1.0 \r\n\r\n'
print('connected')
sock.sendall(msg.encode())
print('sent message')
data = sock.recv(1024)
while data:
    print(data)
    data = sock.recv(1024)

sock.shutdown(socket.SHUT_RDWR)
sock.close()
