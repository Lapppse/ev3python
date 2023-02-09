#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Button, Color
from pybricks.tools import wait, StopWatch


REPEATS = 10
BIG_ZEROES = range(-12, 12)
SMALL_ZEROES = range(-8, 8)

timer = StopWatch()
timer.pause()
brick = EV3Brick()
eyes = ColorSensor(Port.S1)
#eyes.reset_angle(-90)

def update_screen(i: int):
    brick.screen.clear()
    brick.screen.draw_text(
        10, 10,
        "time: {time:.2f} seconds".format(time=timer.time() / 1000)
    )
    brick.screen.draw_text(
        10, 25,
        "strokes #{0}".format(i)# // 2)
    )
    #brick.screen.draw_text(10, 50, eyes.color())


def main() -> None:
    i = 0
    while i < REPEATS:
        update_screen(i)
        wait(150)
        
        if eyes.color() is not None:
            timer.resume()            
            i += 1
            update_screen(i)
            wait(50 + 25 * (i + 1))
    
    timer.pause()
    update_screen(10)
    """
    i = 0
    while eyes.angle() < -85:
        update_screen(0)
    timer.reset()
    timer.resume()
    while i < REPEATS:
        if i < 5 and eyes.angle() in BIG_ZEROES:
            i += 1
        elif i >= 5 and eyes.angle() in SMALL_ZEROES:
            i += 1
        update_screen(i)
    """


if __name__ == "__main__":
    main()
    while True:
        pass
