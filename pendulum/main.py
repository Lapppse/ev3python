#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

from update_screen import update_screen
from get_length import get_length

REPEATS = 10
HALF_REPEATS = REPEATS * 2

pi = 3.141593
timer = StopWatch()
timer.pause()
brick = EV3Brick()

def main() -> None:
    i = 0
    length = get_length() / 100
    eyes = ColorSensor(Port.S4)

    queue_len = 2
    queue = [None, None]
    
    brick.screen.clear()
    brick.screen.draw_text(
        10, 10,
        "{length:.2} m".format(length=length)
    )
    wait(1000)

    while i < HALF_REPEATS + 1:
        time = timer.time()
        color = eyes.color()
        update_screen(i, time)
        queue.insert(0, color)
        if len(queue) > queue_len:
            queue = queue[:-1]
        if color is not None and queue[1] is None:
            timer.resume()
            i += 1

    time = timer.time()
    timer.pause()
    update_screen(i, time)

    result = (4 * (pi ** 2)) * ((length * (REPEATS ** 2)) / ((time / 1000) ** 2))

    brick.screen.draw_text(
        0, 50,
        "accel = {0:.2f}".format(result)
    )


if __name__ == "__main__":
    main()
    while True:
        pass
