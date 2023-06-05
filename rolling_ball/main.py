#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port, Button
from pybricks.tools import StopWatch

REPEATS = 5
LENGTH = 0.325

timer = StopWatch()
timer.pause()
results = []
brick = EV3Brick()
motor = Motor(Port.C)
cage_button = TouchSensor(Port.S1)
bottom_button = TouchSensor(Port.S2)


def wait_until_pressed(button: Button) -> None:
    while not button.pressed():
        pass
    return

def wait_until_unpressed(button: Button) -> None:
    while button.pressed():
        pass
    return

def start_timer() -> None:
    timer.reset()
    timer.resume()

def get_timer() -> int:
    timer.pause()
    return timer.time() / 1000

def display_average() -> None:
    average_time = sum(results) / len(results)

    brick.screen.draw_text(
        0, 10,
        "avg = {0:.2f} s".format(average_time)
    )
    brick.screen.draw_text(
        0, 25,
        "accel = {0:.2f} m/s".format((2 * LENGTH) / (average_time ** 2))
    )

def display_results() -> None:
    for i in range(len(results)):
        brick.screen.draw_text(
            0, (45 + 15 * i),
            "{0}) {time:.2f} s".format(i+1, time=results[i])
        )

def update_screen() -> None:
    brick.screen.clear()
    display_average()
    display_results()

def main() -> None:
    wait_until_unpressed(cage_button)
    start_timer()
    wait_until_pressed(bottom_button)

    time = get_timer()
    results.append(time)
    update_screen()


if __name__ == "__main__":
    for _ in range(REPEATS):
        main()
        wait_until_pressed(cage_button)
    while True:
        pass
