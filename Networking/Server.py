import socket

s = socket.socket()

port = 9999
s.bind(('localhost', port))
print("Socket binded to",port)

s.listen(5)
print("Socket is listening...")
msg = "Thankyou for Connecting"

while True:
    conn, address = s.accept()
    print("Got connection from",address)
    conn.send(msg.encode())
    conn.close()