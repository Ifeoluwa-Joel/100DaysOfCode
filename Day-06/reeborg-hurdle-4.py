# This program will never run outside Reeborg's
# environment.
# This code is not to be executed. It is merely saved here
# for future reference.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
    while front_is_clear:
        move()
        if wall_in_front():
            turn_left()
            break


while (at_goal() != True):
    if wall_in_front():
        jump()
    else:
        move()