Writeup 7 - Forensics I
======

Name: Darren Hislop
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Darren Hislop

## Assignment 7 writeup

### Part 1 (40 pts)

1. This file is a JPEG image.

2. This picture was taken at the John Hancock Center in Chicago, IL

3. This picture was taken on Wednesday, August 22, 2018 at 11:33:24 AM.

4. It was taken with the back camera of an iPhone 8.

5. It was taken 539.5 meters above sea level.

6. The flags are CMSC389R-{look_I_f0und_a_string} and CMSC389R-{abr@cadabra}.

### Part 2 (55 pts)

<p>
I started off by trying to use strings in order to find the flag. Specifically I used it with the -n option with length 15. After doing that, I saw a string saying "Where is your flag", along with some other strings with random characters. This made me think that the flag was probably obscured somehow and that I was probably looking in the right direction. I then used radare2 to disassemble the binary file. After doing that I displayed all symbols with aa and used pdf @ sym.main to print the disassembled functions. After looking at the code, I realized that a lot of the first instructions in the file were mov; each associated with moving a character into a register. Putting the characters together creates the string /tmp/.stego. At first I was unsure what this was but then I realized that the string from earlier meant that I had to look in the /tmp directory for a hidden file name .stego. I then navigated to that directory and found the file.
</p>
<p>
I copied the file to the week 7 directory. Using binwalk I saw that the flag had JPEG image data so I recopied .stego into the week 7 directory as stego.jpg in order to try and see if I could open it regularly. However it failed to open in the image viewer so I used exiftool to see if there were any hints in the metadata. Exiftool returned that the flag had an unknown 1-byte header. I was unsure how to do this so Googled how to trim the picture's header. I used the tail command to do so. When I opened the trimmed image, I found that it was a picture of a stegosaurus. Considering all of the effort I went through to get this picture, I figured that the flag was probably hidden inside. I used steghide to extract anything that could have been hidden in the file with the  found the which was CMSC389R-{dropping_files_is_fun}.
</p>
