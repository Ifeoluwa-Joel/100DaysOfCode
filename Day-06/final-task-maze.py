def wall_on_left():
    turn_left()
    if wall_in_front():
        turn_right()
        return True


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
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
    while front_is_clear() and not at_goal():
        move()
        if front_is_clear() and right_is_clear():
            turn_right()
        elif front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
        elif right_is_clear() == False:
            turn_left
    if right_is_clear():
        turn_right()
    else:
        turn_left()

#    if right_is_clear() and front_is_clear() and wall_on_left():
#        move()
#    elif right_is_clear():
#        turn_right()
#    elif right_is_clear() and front_is_clear():
#        move()
#    elif right_is_clear() == False and front_is_clear():
#        move()
#    elif right_is_clear() == False and front_is_clear() == False:
#        turn_left()
