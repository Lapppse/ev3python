from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.tools import wait

brick = EV3Brick()

low = 30
high = 100
len_range = list(range(low, high + 1))

def get_length_update_screen(i, edge=None) -> None:
    brick.screen.clear()
    brick.screen.draw_text(
        10, 10,
        "Choose string"
    )
    brick.screen.draw_text(
        10, 25,
        "length"
    )
    if edge is None:
        brick.screen.draw_text(
            10, 50,
            "{num} cm".format(num=len_range[i + 1])
        )
        brick.screen.draw_text(
            10, 65,
            "> {num} cm".format(num=len_range[i])
        )
        brick.screen.draw_text(
            10, 80,
            "{num} cm".format(num=len_range[i - 1])
        )
    elif edge == "up":
        brick.screen.draw_text(
            10, 65,
            "> {num} cm".format(num=len_range[i])
        )
        brick.screen.draw_text(
            10, 80,
            "{num} cm".format(num=len_range[i - 1])
        )
    else:
        brick.screen.draw_text(
            10, 50,
            "{num} cm".format(num=len_range[i + 1])
        )
        brick.screen.draw_text(
            10, 65,
            "> {num} cm".format(num=len_range[i])
        )
    wait(50)

def get_length_buttons_wait(button, last_pressed, counter):
    if last_pressed == button:
        if counter > 3:
            wait(35)
        else:
            wait(200)
            counter += 1
    else:
        last_pressed = button
        counter = 1
        wait(200)
    
    return last_pressed, counter

def get_length() -> float:
    i = 50 - low
    last_pressed = None
    counter = 0
    get_length_update_screen(i)

    while True:
        buttons = brick.buttons.pressed()
        if Button.CENTER in buttons:
            return len_range[i]
        if Button.UP in buttons and i < high - low:
            edge = None if i < (high - low - 1) else "up"
            i += 1
            get_length_update_screen(i, edge)
            last_pressed, counter = get_length_buttons_wait(Button.UP, last_pressed, counter)
        if Button.DOWN in buttons and i > 0:
            edge = None if i > 1 else "down"
            i -= 1
            get_length_update_screen(i, edge)
            last_pressed, counter = get_length_buttons_wait(Button.DOWN, last_pressed, counter)

        if not buttons:
            counter = 0
