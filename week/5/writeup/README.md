Writeup 5 - Binaries I
======

Name: Darren Hislop
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Darren Hislop

## Assignment 5 Writeup

<p>
Initially, I was having issues with the invalid operand size operator. Eventually realized that I was trying to use the 64 bit size registers with characters which are only 1 byte. Another issue that I faced initially is that my loops would never terminate. After using the enhanced debugger, I was able to determine that the issue was caused by the fact that I wasn't actually using third parameter. I was able to fix that by moving the value in the rdx register into rcx register.
</p>
<p>
Using the facts the fact that the parameters are pushed into the rdi, rsi, and rdx as well as what I learned and observed in the first paragraph I begun both functions by using the rax register to represent the i variable from the C code. After the loop label in the first function, I used the byte size version of the rsi register to copy the character parameter into the position accessed by adding the value of rax to the location rdi was pointing to. I then incremented the value in the rax register and then continued the loop. After the loop ends, I move modified string into rax so that it can be safely returned once the function is popped off the stack.
</p>
<p>
The second function basically follows the same idea I had for the first one. The main differences are that I use the dl register to store the current character from the source string before I copy it into the destination string. I then increment rax and use that to access the next positions in both strings.
</p>
