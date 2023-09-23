#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait, StopWatch

REPEATS: int = 10
HALF_REPEATS: int = REPEATS * 2
BIG_ZEROES = range(-12, 12)
SMALL_ZEROES = range(-8, 8)

pi = 3.141593
timer = StopWatch()
timer.pause()
brick = EV3Brick()
screen = brick.screen

low = 20
high = 100
len_range = list(range(low, high + 1))

queue = []
queue_len = 2

def add_to_queue(element):
    queue.insert(element)
    if len(queue) > queue_len:
        queue = queue[:-1]

def get_length_update_screen(i: int) -> None:
    screen.clear()
    screen.draw_text(
        10, 40,
        "{num} cm".format(num=len_range[i - 1])
    )
    screen.draw_text(
        10, 25,
        "> {num} cm".format(num=len_range[i])
    )
    screen.draw_text(
        10, 10,
        "{num} cm".format(num=len_range[i + 1])
    )
    wait(50)

def get_length_buttons_wait(button: Button, last_pressed: Button, counter: int):
    if last_pressed == button:
        if counter > 5:
            wait(100)
        else:
            wait(200)
            counter += 1
    else:
        last_pressed = button
        counter = 1
        wait(200)
    
    return last_pressed, counter

def get_length() -> float:
    i = (high - low) // 2
    last_pressed = None
    counter = 0
    get_length_update_screen(i)
    while True:
        buttons = brick.buttons.pressed()
        if Button.CENTER in buttons:
            return len_range[i]
        if Button.UP in buttons and i + 1 < high:
            i += 1
            get_length_update_screen(i)
            last_pressed, counter = get_length_buttons_wait(Button.UP, last_pressed, counter)
        if Button.DOWN in buttons and i - 1 > low:
            i -= 1
            get_length_update_screen(i)
            last_pressed, counter = get_length_buttons_wait(Button.DOWN, last_pressed, counter)

        if not buttons:
            counter = 0

def update_screen(i: int):
    brick.screen.clear()
    brick.screen.draw_text(
        0, 10,
        "time: {time:.2f} s".format(time=timer.time() / 1000)
    )
    brick.screen.draw_text(
        0, 25,
        "strokes #{0}".format(i // 2)
    )
    wait(100)

def main() -> None:
    i = 0
    length = get_length()
    eyes = ColorSensor(Port.S4)
    while i < HALF_REPEATS:
        update_screen(i)
        color = eyes.color()
        add_to_queue(color)
        if queue[1] is not None and queue[0] is None:
            timer.resume()
            i += 1

    timer.pause()
    update_screen(i)

    result = (4 * (pi ** 2)) * ((length * (REPEATS ** 2)) / ((timer.time() / 1000) ** 2))

    brick.screen.draw_text(
        0, 50,
        "accel = {0:.2f}".format(result)
    )


if __name__ == "__main__":
    main()
    while True:
        pass