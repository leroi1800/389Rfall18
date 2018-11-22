Writeup 10 - Crypto II
=====

Name: Darren Hislop
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Darren Hislop

## Assignment 10 Writeup

### Part 1 (70 Pts)
<p>
I begun by connecting to the server and messing around a bit to determine how it received and processed my input. After doing so I constructed my script using ```hi``` as my message and ```badhi``` as the malicious message. I used sockets to help automate the process. I extracted the hash by getting the string that appeared on the output after the word ```hash:``` by using split with space as the token. When it came to determining the right amount of padding in order to get the flag I used a loop to go between 6 and 15, which were the bounds established by the assignment. Since md5 uses 64 bytes with 9 for the length field and the 1 byte in the padding field, I set up my string so that it would add as many zeros as the difference of 55 minus the length of my string minus what ever value the loop was at for the length of the secret. Then for each iteration of the loop, my script would send the payload to the server and would not stop until it saw something other than ```hmm...``` in the output the server gives after it gets the payload. At the end I found the flag was CMSC389R-{i_still_put_the_M_between_the_DV}. The original hash I used was 46c8b80c930046c68a50f3380c0ed782. The fake hash used was eba7d31dbcd73dcc58085479122ef6da. The final payload was: hi\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00badhi.
</p>

### Part 2 (30 Pts)
<p>
The command to create a pgp key was:
```
gpg --gen-key
```
</p>

<p>
The command to import the provided key was:
```
gpg --import pgpassignment.key
```
</p>

<p>
The command I used to encrypt the message was:
```
gpg -e -u "Darren Hislop" -r "UMD Cybersecurity Club" msg.txt
```
</p>
