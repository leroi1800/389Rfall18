Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Darren Hislop
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Darren Hislop

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. He has @kruegster1990 accounts on Twitter, Instagram, and Reddit. According to Twitter his location is Silver Spring, MD. He is the owner of Cornerstone Airlines. I found the social media accounts by using Custom Username Tools and Check Usernames. I also was able to find his company through his Twitter profile.  

3. The webserver's ip address is 142.93.118.186. I found this by using dnsdumpster. 

4. There was a hidden directory called /secret that was located on the robots.txt file. The flag was CMSC389R-{fly_th3_sk1es_w1th_u5} found by viewing source on the /secret site.  

5. The only other IP address that I found was 142.93.117.193. This IP was the url of the admin page of his website.  

6. 142.93.117.139 and 142.93.118.186 which are both located in North Bergen, New Jersey. I found this by using whois.domaintools.com.

7. Using nmap -O I found that the servers' OS were probably running Linux 2.4.37 or Linux 3.2. 

8. *(BONUS)*
CMSC389R-{dns-txt-rec0rd-ftw} found by using dnsdumpster.
CMSC389R-{h1dden_fl4g_in_s0urce} found on the home page's source code.



### Part 2 (55 pts)

I begun by nmaping the admin ip address (142.93.117.193) that I got in part 1. The only open ports were 80, 2222, and 100010. I tried nc with all of these ports but nothing happened. Once I realized that you could specify a range of ports to be scanned I used the nmap again with the -p option in order to scan up to port 5000. The only new port to appear was 1337. I then tried the nc with that port which brought up a login prompt. Once that happened I began to modify the provided python code. I first tried the username kruegster1990. When that began to take longer than 30 minutes, I tried the username kruegster which ended up working with the password pokemon. Once I gained access to the server I began to look around. I made my way to the home directory which had flight records as a subdirectory. I remembered that he had a ticket on his Instagram which had a flight number "AAC27670". I then read that file and got the flag CMSC389R-{c0rn3rstone-air-27670}. 