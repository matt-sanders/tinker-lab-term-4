# Remember these are imports, you can largely ignore this as long as you have it. It needs to come first
import rocky, time, codey, event

# Our variables are defined here.
# By convention these are uppercase, although they don't have to be.
# Remember, variables are like placeholders for other values that we can re-use over again.
POWER = 50
NAME = 'Matt'

def say_hi():
    # Here we are telling codey to display the words exactly as we've written them.
    # This is indicated by the words being surrounded by single quotes.
    codey.display.show('hello, your name is')
    # Notice here we are referencing the NAME variable we declared earlier.
    # It's not surrounded by single quotes, indicating that it is a reference to a variable.
    codey.display.show(NAME)

def move_forward():
    rocky.forward(POWER, 1)

def turn_right():
    rocky.turn_right_by_degree(90)

# Ignore the @event.button_a_pressed for now, just make sure to include it
@event.button_a_pressed
def on_button_a_pressed():
    # We have previously defined all our functions, but haven't actually called them!
    # We are calling them here, and this will run when you press the A button.
    say_hi()
    move_forward()
    turn_right()
    move_forward()
    turn_right()
    move_forward()
    

