from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        make_post()
        next_post()
    make_post()

def make_post():
    turn_left()
    while front_is_clear():
        put_beeper()
        safe_move()
    put_beeper()
    turn_around()
    while front_is_clear():
        safe_move()
    turn_left()

def next_post():
    for i in range (4):
        safe_move()




def safe_move():
    if front_is_clear():
        move()
def turn_right():
    for i in range (3):
        turn_left()
def turn_around():
    for i in range(2):
        turn_left() 

if __name__ == '__main__':
    main()