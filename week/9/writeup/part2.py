#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)

found = False
while not found:
    temp = data.split(' ')
    for i in range(len(temp)):
        if (temp[i] == 'the'):
            hash = temp[i+1]
        if (temp[i] == 'of'):
            next2 = temp[i+1]
            str = next2[0:10]
            #print next2[0:10]
    temp1 = "hashlib."
    temp2 = "('"
    temp3 = "').hexdigest()"
    transport = temp1 + hash + temp2 + str + temp3
    print transport
    s.send(eval(transport) + "\n")
    data = s.recv(1024)
    if 'CMSC389R' in data:
        found = True
    print(data)

s.close()
