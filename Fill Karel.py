from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while left_is_clear():
        fill_row()
        return_to_first()
        climb_up()
    fill_row()



def fill_row():
    while front_is_clear():
        put_beeper()
        safe_move()
    put_beeper()

def return_to_first():
    turn_around()
    while front_is_clear():
        safe_move()

def climb_up():
    turn_right()
    safe_move()
    turn_right()


def safe_move():
    if front_is_clear():
        move()
def turn_right():
    for i in range (3):
        turn_left()
def turn_around():
    for i in range(2):
        turn_left() 
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()