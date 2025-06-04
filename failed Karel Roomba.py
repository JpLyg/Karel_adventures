# This tells PyCharm who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

def main():
    while front_is_clear():
        clear_row()
        change_floor()

def clear_row():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        safe_move()
    if beepers_present():
        pick_beeper()

def change_floor():
    if facing_east():
        turn_left()
        safe_move()
        turn_left()
    else:
        turn_right()
        safe_move()
        turn_right()


def safe_move():
    if front_is_clear():
        move()


def turn_right():
    for i in range (3):
        turn_left()
    


# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()



#Failed Karel Roomba - Karel get stuck in the top floor cleaning it indefinitely