#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait, StopWatch


REPEATS = 10 * 2
BIG_ZEROES = range(-12, 12)
SMALL_ZEROES = range(-8, 8)

pi = 3.141593
timer = StopWatch()
timer.pause()
brick = EV3Brick()
lengths = (0.5, 1.0)


def display_length(length: float) -> None:
    brick.screen.clear()
    brick.screen.draw_text(
        0, 25,
        "length = {0}cm".format(length)
    )
    brick.screen.draw_text(
        0, 50,
        "press RIGHT button"
    )
    brick.screen.draw_text(
        0, 65,
        "to select length"
    )

def get_length() -> float:
    i = 0
    pressed = False
    display_length(lengths[i])
    while Button.CENTER not in brick.buttons.pressed():
        if Button.RIGHT in brick.buttons.pressed():
            if not pressed:
                pressed = True
                i  = (i + 1) % len(lengths)
                display_length(lengths[i])
        else:
            pressed = False

    return lengths[i]

def update_screen(i: int):
    brick.screen.clear()
    brick.screen.draw_text(
        0, 10,
        "time: {time:.2f} seconds".format(time=timer.time() / 1000)
    )
    brick.screen.draw_text(
        0, 25,
        "strokes #{0}".format(i)# // 2)
    )
    wait(100)

def main() -> None:
    length = get_length()
    eyes = ColorSensor(Port.S3) if length == 0.5 else ColorSensor(Port.S4)
    i = 0
    seen = False
    while i < REPEATS:
        update_screen(i)
        if eyes.color() is None:
            seen = False
        elif not seen:
            seen = True
            timer.resume()
            i += 1
    timer.pause()
    update_screen(i)

    result = (4 * (pi ** 2)) * ((length * (REPEATS ** 2)) / ((timer.time() / 1000) ** 2))
    print(result)

    brick.screen.draw_text(
        0, 50,
        "accel = {0:.2f}".format(result)
    )


if __name__ == "__main__":
    main()
    while True:
        pass