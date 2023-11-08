import rocky, time, codey, event

POWER = 50
NAME = 'Matt'

def say_hi():
    codey.display.show('hello, your name is')
    codey.display.show(NAME)

def move_forward():
    rocky.forward(POWER, 1)

def turn_left():
    rocky.turn_left_by_degree(90)

def turn_right():
    rocky.turn_right_by_degree(90)

def turn_around():
    rocky.turn_right_by_degree(180)

def out_and_back():
    move_forward()
    turn_right()
    move_forward()
    turn_right()
    move_forward()

@event.button_a_pressed
def on_button_a_pressed():
    out_and_back()
    say_hi()

