Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Darren Hislop
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Darren Hislop

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. Yes. They used it on csic.umiacs.umd.edu

2. Their names are laz0r4hx and c0uchpot4doz

3. Their IPs are 206.189.113.189 which is located in London, United Kingdom. The other is 104.248.224.85, located in New York City.

4. They are using port 2749.

5. It is happening the next day from when the breach occurred at 1500.

6. https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing. It is possible to read that file using some parser that they sent to each other.

7. They expect to see each other tomorrow (after whenever the breach happened).

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. It was generated on October 25, 2018 at 12:40:07 AM.

2. laz0r4hx wrote the file.

3. It says that it has 9 sections but there are actually 11 sections.

4. 1) ASCII string -> Call this number to get your flag: (422) 537 - 7946 <br>
   2) Words -> 3 1 4 1 5 9 2 6 5 3 5 8 9 7 9  <br>
   3) Coordinates -> 38.991610,-77.027540  <br>
   4) Reference -> 1 <br>
   5) ASCII string -> The infamous security pr0s at CMSC389R will never find this!  <br>
   6) ASCII string -> The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}  <br>
   7) Coordinates -> 38.991094, -76.932802  <br>
   8) PNG -> A picture <br>
   9) ASCII string -> AF(saSAdf1AD)Snz**asd1  <br>
   10) ASCII string -> Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9  <br>
   11) Dwords -> 4, 8, 15, 16, 23, 42  <br>

5. The flags are CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}, CMS389R-{PlaIN_dIfF_FLAG}
