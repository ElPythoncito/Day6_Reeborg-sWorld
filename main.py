def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()

while not wall_in_front():
    move()

while not at_goal():
    if right_is_clear():
        jump()
    elif front_is_clear():
        move()
    elif wall_on_right() and not front_is_clear():
        turn_left()
