def turn_right():
    turn_left()
    turn_left()
    turn_left()

def upside():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != true:
    if front_is_clear():
        move()
    else:
        upside()







