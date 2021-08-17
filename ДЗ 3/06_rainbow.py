# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# start_point = sd.get_point(50, 50)
# end_point = sd.get_point(350, 450)
#
# step = 5
# width = step-1
#
# for i in range(7):
#     start_point = sd.get_point(50 + step * i, 50)
#     end_point = sd.get_point(350 + step * i, 450)
#     color = rainbow_colors[i]
#     sd.line(start_point, end_point, color, width)


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

start_point = sd.get_point(500, -100)
start_radius = 300
step = 40
circle_width = step-1
for i in range(7):
    radius = start_radius+i*step
    color = rainbow_colors[i]
    sd.circle(start_point, radius, color, circle_width)
sd.pause()
