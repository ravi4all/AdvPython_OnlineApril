import socket

s = socket.socket()

port = 9999
s.bind(('localhost', port))
print("Socket binded to",port)

s.listen(1)
print("Socket is listening...")

conn, address = s.accept()
print("Got connection from",address)

while True:
    data = conn.recv(1024).decode()
    if not data:
        print("Not data received")
        break
    print("Client : ",data)

    msg = input("Enter your message : ")
    conn.send(msg.encode())
conn.close()
