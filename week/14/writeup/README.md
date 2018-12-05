Writeup 10 - Crypto II
=====

Name: Darren Hislop
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Darren Hislop

## Assignment 10 Writeup

### Part 1 (70 Pts)
<p>
I understood from the prompt that this part would involve a SQL injection. Initially, I thought that you had to do it via cookie forging, so I tried to do that for a while. Once I realized that nothing was working, I noticed that the webpage's url had a query string in it. From there I tried using multiple different SQL commands such as admin or 1 = 1, or 1=1 (with no apostrophes), 'admin' or '1=1', etc. I would try interchanging where I placed the apostrophes in the input as well as the words that I used but many of these commands would do nothing or cause an internal server error. After some more trial and error with changing around the commands, I was able to determine the input that would cause the website to dump the table. The input that end up up working for me was ' or' 1=1. The flag was CMSC38R-{y0U-are_the_5ql_n1nja} (I'm not sure if there was a typo in the formatting of the flag).
</p>

### Part 2 (30 Pts)

<p>
***Level 1:***
I was familiar with the first level because I remembered doing this in the discussion section of my CMSC330 class. This level involved creating a simple alert popup box. The code I used was:
 </p>

`<script>alert("Hello");</script>`

<p>
***Level 2:***
I initially tried to use the same technique from the last level but that did not work. Eventually I realized that I needed to find another way to create a popup alert. I figured that inserting a fake image tag with along with an onerror event could probably work and it did.The code I ended up using was:
</p>

`<img src=hi.txt onerror=alert("hello")>`

<p>
***Level 3:***
I clicked between the different image tabs and noticed how the only thing that changes was the frame number in the url. Considering how there was no other place to insert code, I knew that I probably could just modify the url. The fact that the page used images I knew that onerror could probably work again. The code I used was:
</p>

`https://xss-game.appspot.com/level3/frame#1' onerror=alert("Hi")>`

<p>
***Level 4:***
I had to look at the hints for this level to understand what was happening. After looking at the code for the level I noticed how the timer was processing user input. I realized that if you created some sort of input that would close the parenthesis in for the timer's onload that whatever code you put in between the parenthesis would be executed by the onload. The code I inserted into the timer was
</p>

`')alert("Hi")('x`

<p>
***Level 5:***
After looking at the code for this level I noticed how on the signup.html file, next was used as a target. Knowing this I decided to edit the url so that when you clicked next it would end up running the code assigned to the next parameter in the url. The url I used for this level was:
</p>

`https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert("Hi")`

<p>
***Level 6:***
After looking at the code, I noticed that there was a regular expression match that tried to prevent an attacker from using a malicious url. The regular expression will only do an exact match of https:// and it isnt case sensitve. I wasnt really sure how to carry out the attack so I had to look at the hints. There, I learned that you could use google to access the javascript api along with callback to call whatever function you use as a variable. Know that, I used it with alert. The url I used for this level was:
</p>

`https://xss-game.appspot.com/level6/frame#Https://google.com/jsapi?callback=alert`
