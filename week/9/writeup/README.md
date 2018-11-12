Writeup 9 - Crypto I
=====

Name: Darren Hislop
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Darren Hislop

## Assignment 9 Writeup

### Part 1 (60 Pts)
<p>
The solutions for this part are k with neptune, m with jordan, p with pizza, and u with loveyou. First, I copied over all of the target hashes into an array. Then I copied all of the passwords in the password file into another array. Since I was reading from a file, I made sure to strip the newline character off of each line that got copied into the arrays. I then looped through each character in the list of salts. For each character in salts, I then looped through each password in the list of passwords. After doing that I added the character from salts to beginning of the current password, got the hash of that and then checked to see if that hash was in the list of hashes. If that was the case I printed the result to the console.
</p>

### Part 2 (40 Pts)
<p>
The flag was CMSC389R-{H4sh-5l!ngInG-h@sH3r}. The first thing I did when I started to solve the problem was connect to the server using nc, ip address and the port. Once I saw what came up, I entered a random sequence of characters to see what happen. The result of that was that the server responds by saying it expected a hash. I tried that again to see if was a pattern between what the initial response from the server was. From there I noticed that every time you connect to the server, the server's response is essentially the same except that the hashing algorithm and the string that it wants to be hashed changes. Knowing this, I opened up a separate terminal, connected to the server on my initial terminal and computed what the server was asking for. I then copied that into the terminal connected to the server to see what happens, which was the server responds with another string it wants to be hashed.
</p>

<p>
Next, I began to construct my script. I used a while loop that would continuously send and receive data to the server  until the data received contains the beginning of the standard flag format, CMSC389R. At the beginning of the loop, my script splits the data received by spaces so that it can be processed by an array. I then accessed the hashing function that the server wants by getting the next string in the array after the word "the" and the required string by accessing the word after "of" in the list of strings. I then created a string containing the command to find the hash which was "hashlib.hashing_function(string).hexdigest()", since the hashing function and string from the data array would be in the form of strings. I then passed the command string into the eval function in order to evaluate the command in the form of a string. The result of eval is the answer to the question being asked by the server so I then sent that to the socket. Again this loop would continue until it sees the beginning of the standard flag format.
</p>
