Writeup 3 - Pentesting I
======

Name: Darren Hislop
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Darren Hislop

## Assignment 4 Writeup

### Part 1 (45 pts)
<p>
Initially I was unsure about how to approach finding the flag. I realized that you needed to enter an IP address which was then inserted into a ping command that would be printed to the command line but I was unsure how to move on from there. Then I remembered from the end of CMSC330 that you can insert extra commands into the command line by using `|`. I tested the pipe out by using a random IP address and `|ls`. This ended up working as it brought the directories. I assumed that the flag would probably be in the home directory just like the assignment from week 2 so I tried to use the pipe operator again but with a random IP address and `|cd home`, however this did nothing. I tried many different combinations commands for listing the files in the directory such as `|cd home | ls` and `|cd home | pwd` , but none of them worked. Then I tried listing  the files in the directory with `|ls home`, which revealed a file called flag.txt. Finally I used the command `|cat home/flag.txt` which revealed the flag, `CMSC389-{p1ng_as_a_$erv1c3}`.
</p>
<p>
After poking around on the server, I was able to locate the shell script that is running on the server in a file called `container_startup.sh` in the opt directory. The main thing that Fred could do to improve his security is to sanitize his input from the command line. Currently the shell takes whatever comes in to the command line and inserts that into a ping command. By sanitizing (escaping special characters) his input he would be able to prevent any commands that use `|` or `;` to insert any commands. Other options for preventing command injection commands are whitelisting and blacklisting inputs. Whitelisting involves only accepting a specific set of commands for the command line while blacklisting involves rejecting any commands that could be potentially harmful.
</p>


### Part 2 (55 pts)
<p>
The approach I had for my shell script was to have the `main` method handle the help, pull and quit commands and then the `execute_cmd` method would handle the shell for the server. At a basic level both methods use a `while` loop to keep taking input from from the command line. The while loop in the main method continues to loop until it sees `quit` from the command line. `help` just prints out the menu of available commands. `pull` creates a socket to the server and stores the data through `cat` and the remote path. It then stores the data in a variable which is then written into a file on the user's system. In the `execute_cmd` method, the loop stops if it sees `exit` from the command line. Inside of the loop it establishes a socket to the server and checks the input from the command line. If the command contains `cd` then it saves the directory name to an array. This is to account for the fact that the server closes the connection after each command that you enter so whenever there is a new command that is supposed to take place in a directory, the shell converts the array into a path that can then be used to exploit the command injection vulnerability the next time the shell establishes a connection to the server.
</p>
