# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1280, 960)
sd.background_color = sd.COLOR_WHITE

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
start_point = sd.get_point(600, 300)


# for i in range(50, 66, 5):
#     sd.circle(start_point, i, sd.COLOR_RED, 3)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def draw_bubble(point, step=5, start_radius=30, color=sd.COLOR_RED):
    for radius in range(start_radius, start_radius + step * 3 + 1, step):
        sd.circle(point, radius, color, 2)


# draw_bubble(start_point, 20)

# Нарисовать 10 пузырьков в ряд
# for i in range(100, 1001, 100):
#     start_point = sd.get_point(i, 100)
#     draw_bubble(start_point, 10)

# Нарисовать три ряда по 10 пузырьков
# for k in range(100, 301, 100):
#     for i in range(100, 1001, 100):
#         start_point = sd.get_point(i, k)
#         draw_bubble(start_point, 10)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    rand_point = sd.random_point()
    rand_color = (sd.randint(0, 255), sd.randint(0, 255), sd.randint(0, 255),)
    rand_step = sd.randint(4, 10)
    rand_radius = sd.randint(30, 70)
    draw_bubble(rand_point, start_radius=rand_radius, color=rand_color, step=rand_step)

sd.pause()
