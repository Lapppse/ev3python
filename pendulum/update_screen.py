from pybricks.hubs import EV3Brick
from pybricks.tools import wait

brick = EV3Brick()

def update_screen(i, time):
    brick.screen.clear()
    brick.screen.draw_text(
        0, 10,
        "time: {time:.2f} s".format(time=time / 1000)
    )
    brick.screen.draw_text(
        0, 25,
        "strokes #{0}".format(i // 2)
    )
    wait(50)
