"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Places beepers in a zig zag pattern.
    """
    
    while front_is_clear():
        pass_entry() # Delete this line and write your code here! :)


# There is no need to edit code beyond this point

def pass_entry():
    put_beeper()
    safe_move()
    turn_left()
    safe_move()
    put_beeper()
    turn_around()
    safe_move()
    turn_left()
    safe_move()


def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left() 

def safe_move():
    if front_is_clear():
        move()


if __name__ == '__main__':
    main()