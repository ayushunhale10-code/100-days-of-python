def turn_right():
    turn_left()
    turn_left()
    turn_left()

def up():
    turn_left()
    move()
def down():
    turn_right()
    move()
    turn_right()
    move()

while at_goal() != true:
    if wall_in_front():
        up()

        while wall_on_right():
            move()
        turn_right()
        move()

        turn_right()
        while front_is_clear():
            move()

        turn_left()
    else:
         move()







