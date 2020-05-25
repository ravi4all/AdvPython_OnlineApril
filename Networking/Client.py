import socket

s = socket.socket()
port = 9999

s.connect(('localhost',port))
data = s.recv(1024)
print(data)
s.close()