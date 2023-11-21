import rocky, time, codey, event

POWER = 50
NAME = 'Matt'

def move_forward( seconds ):
    rocky.forward(POWER, seconds)

def turn( direction ):
    if (direction == 'l'):
        rocky.turn_left_by_degree(90)
    elif (direction == 'r'):
        rocky.turn_right_by_degree(90)

def square_dance():
    move_forward(1)
    turn('r')
    move_forward(1)
    turn('r')
    move_forward(1)
    turn('r')
    move_forward(1)
    turn('r')

@event.button_a_pressed
def on_button_a_pressed():
    while True:
        square_dance()

@event.button_b_pressed
def on_button_b_pressed():
    rocky.stop()
    codey.display.clear()
    codey.stop_all_scripts()
