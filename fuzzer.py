#!/usr/bin/python3

import socket

dest = ''
dport = 
commands = ['', '']
buff = ['A']
counter = 50
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while len(buff) <= 80:
     buff.append('A' * counter)
     counter += 50

for command in commands:
     for chars in buff:
          print('Fuzzing ' + command + ' ' + str(len(chars)))
          s.connect((dest, dport))
          s.recv(100)
          s.sendall((command + chars).encode())
          s.close()
