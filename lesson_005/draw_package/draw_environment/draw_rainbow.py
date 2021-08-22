import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

sd.resolution = (1200, 700)


def draw_rainbow():
    start_point = sd.get_point(400, -200)
    start_radius = 800
    step = 10
    circle_width = step - 1
    for i in range(7):
        radius = start_radius + i * step
        color = rainbow_colors[i]
        sd.circle(start_point, radius, color, circle_width)
    sd.take_background()


if __name__ == '__main__':
    draw_rainbow()
    sd.pause()
