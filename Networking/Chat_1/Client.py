import socket

s = socket.socket()
port = 9999

s.connect(('localhost',port))

msg = input("Enter your message : ")
while msg != 'q':
    s.send(msg.encode())
    data = s.recv(1024).decode()
    print("Server : ",data)
    msg = input("Enter your message : ")

s.close()