import codey, rocky, time, event

def find_next_direction():
    rocky.turn_left_by_degree(90)
    if rocky.color_ir_sensor.is_obstacle_ahead():
        rocky.turn_right_by_degree(180)

@event.button_a_pressed
def on_button_a_pressed():
    while True:
        if rocky.color_ir_sensor.is_obstacle_ahead():
            find_next_direction()

        else:
            rocky.forward(50)

@event.button_b_pressed
def on_button_b_pressed():
    rocky.stop()
    codey.display.clear()
    codey.stop_all_scripts()
