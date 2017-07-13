import socket

from time import sleep

import TODO as TODO

#create a ring buffer for user input
#scan that user input for the right combination of bytes
#if they do have valid http provide a response based on their parsed data

print socket.gethostname()
print socket.gethostbyname('jproffitt')

HOST =''
PORT = 50069
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

buffer = bytearray(64)
# while 1:
#     conn.recvfrom_into(buffer,64)
#     print buffer
#     if 'EOL' in buffer:
#         conn.send(buffer)
#         buffer = bytearray()
#
conn.close()
#
# print 'hello world'