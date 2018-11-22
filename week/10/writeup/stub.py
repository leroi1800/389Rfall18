#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import struct
import time

#####################################
### STEP 1: Calculate forged hash ###
#####################################

host = '142.93.118.186'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

s.recv(1024)
s.send("1" + '\n')
s.recv(1024)

message = 'hi'    # original message here
s.send(message + '\n')

data = s.recv(1024).split( )

pos = data.index('hash:')

legit = data[pos + 1].strip() # a legit hash of secret + message goes here, obtained from signing a message
print("Legit was: " + legit)

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'badhi'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print("Fake was: " + fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash


# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!


found = False
sec_len = 6
while sec_len < 16 and not found:
    one = '\x80'
    zeros = ('\x00' * (55 - len(message) - sec_len))
    padding = one + zeros
    temp = struct.pack('<Q', (sec_len + len(message)) * 8 )

    payload = message + padding + temp + malicious

    s.send("2" + '\n')
    s.recv(1024)

    print("sending hash: " + fake_hash)
    s.send(fake_hash + '\n')
    s.recv(1024)
    time.sleep(1)

    print("sending payload: " + repr(payload))
    s.send(payload + '\n')
    time.sleep(1)

    flag = s.recv(1024)

    if 'Hmm...' in flag:
        print("Not Found")
    else:
        print flag
        found = True
        print repr(payload)

    sec_len +=1
    print("------------------------------------")
s.close()
