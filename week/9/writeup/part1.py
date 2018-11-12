#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hashes = open("../hashes", 'r')
# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

#load in the hashes
hash_list = hashes.readlines()
hash_list = [x.strip('\n') for x in hash_list]

passes = wordlist.readlines()
passes = [x.strip('\n') for x in passes]

#for x in range(len(hash_list)):
#    print hash_list[x]

for salt in salts:
    #try each letter with each password
    for pas in passes:
        temp = hashlib.sha512(salt + pas).hexdigest()
        if temp in hash_list:
            print salt + " " + pas
