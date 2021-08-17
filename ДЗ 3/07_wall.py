# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
simple_draw.resolution = (600, 600)
window_width, window_height = simple_draw.resolution
color_red = simple_draw.COLOR_RED
brick_width = 2
brick_color = color_red
for x in range(0, window_width, 100):
    for y in range(0, window_height, 100):
        start_point = simple_draw.get_point(x, y)
        end_point = simple_draw.get_point(x + 100, y + 50)
        simple_draw.rectangle(start_point, end_point, width=brick_width, color=brick_color)
        start_point = simple_draw.get_point(x + 50, y + 50)
        end_point = simple_draw.get_point(x + 150, y + 100)
        simple_draw.rectangle(start_point, end_point, width=brick_width, color=brick_color)

simple_draw.pause()
