# First step: Find a way to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Use while loop to keep the robot working
# until it reaches the goal
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()