import socket
import sys

# Stream - flow of data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created Successfully")

port = 80
try:
    host_ip = socket.gethostbyname('www.google.com')
    s.connect((host_ip,port))
    print("Successfully connected to google on",host_ip)
except socket.gaierror:
    print("Error")
    sys.exit()

