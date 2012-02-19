#!/usr/bin/env python

quit_confirm = """Are you sure you want to quit? y, [n]
"""

while 1:
    cmd = raw_input("Enter a command: ")
    if cmd == "exit" or cmd == "quit" or cmd == "q":
        confirm = raw_input(quit_confirm)
        if confirm == "yes" or confirm == "y":
            print "Game over!"
            break
        else:
            continue

    print "Command:", cmd
