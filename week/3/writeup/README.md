Writeup 3 - OSINT II, OpSec and RE
======

Name: Darren Hislop
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Darren Hislop

## Assignment 3 Writeup

### Part 1 (100 pts)
>In my opinion, the three most dangerous vulnerability in the Cornerstone web and admin servers were the weak admin server login information, the exposed server ports, and the admin IP address being the URL for the admin page of the website.

>The main issue with the login information was that both the username and the password were relatively easy to discover after conducting OSINT against the target. You shouldn't  reuse the username(or a variation of the username) to your social media accounts for the admin credentials for your company. The password (pokemon) would have been a solid choice for an attacker to use without discovering it from using a brute force attack, due to the fact that pokemon seemed to be an interest of Fred's on his Instagram. In order to fix this you should start off by using passwords that aren't entirely plain text (made up of alphanumeric characters as well as certain other special characters). You could also improve by using password managers such a LastPass, 1Password, or any form of offline password manager. These applications store your password in encrypted databases and even have the option to generate passwords for you.

>The next major issue with the web site and admin server's security was the exposed server ports. It is a common security practice to close unused web ports. According to [title](https://www.acunetix.com/blog/articles/close-unused-open-ports/), open ports allow attackers to exploit old versions of unused software running on those ports and gain better information about your network. Open unused ports also can serve as attack vectors against your servers, as was seen in the attacks by the 389R Ethical Hackers. In order to prevent this you should close unused open ports as well as use firewalls and IDS/IPS like Snort to filter out suspicious traffic before it enters the network.

>The last issue with the web site and admin server's security was using the IP address of the admin server as the URL for the admin page of the website. This vulnerability gives the attackers direct access to your server for them to craft attacks. You could solve this problem by registering a domain for that part of the website and then locking it behind a login page that needs admin credentials or by not listing that section of the site on the public webpage.
