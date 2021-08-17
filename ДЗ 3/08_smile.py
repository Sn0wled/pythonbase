# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: координата X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x_position, y_position, color):
    start_point = sd.get_point(x_position, y_position)
    sd.circle(start_point, radius=40, color=color, width=2)
    sd.circle(start_point, radius=40, color=sd.COLOR_YELLOW, width=0)

    eye_distance = 15
    left_eye_pos = sd.get_point(x_position + eye_distance, y_position + 10)
    right_eye_pos = sd.get_point(x_position - eye_distance, y_position + 10)
    sd.circle(left_eye_pos, 5, color, 2)
    sd.circle(right_eye_pos, 5, color, 2)

    mouth_width = 20
    y_mouth_pos = y_position - 12
    mouth_height = 10
    mouth_left_pos = sd.get_point(x_position - mouth_width, y_mouth_pos)
    mouth_right_pos = sd.get_point(x_position + mouth_width, y_mouth_pos)
    mouth_bottom_left_pos = sd.get_point(x_position - mouth_width / 2, y_mouth_pos - mouth_height)
    mouth_bottom_right_pos = sd.get_point(x_position + mouth_width / 2, y_mouth_pos - mouth_height)
    mouth_points = [mouth_left_pos, mouth_right_pos, mouth_bottom_right_pos, mouth_bottom_left_pos]
    sd.polygon(mouth_points, color=color, width=2)

    horn_height = 30

    horn1_pos_start = sd.get_point(x_position + 20, y_position + 3 ** .5 * 20)
    horn1_pos_end = sd.get_point(x_position + 3 ** .5 * 20, y_position + 20)
    horn1_tip_pos = sd.get_point(x_position + 3 ** .5 * 20, y_position + 20 + horn_height)

    horn2_pos_start = sd.get_point(x_position - 20, y_position + 3 ** .5 * 20)
    horn2_pos_end = sd.get_point(x_position - 3 ** .5 * 20, y_position + 20)
    horn2_tip_pos = sd.get_point(x_position - 3 ** .5 * 20, y_position + 20 + horn_height)

    horn1_points = [horn1_pos_start, horn1_tip_pos, horn1_pos_end]
    horn2_points = [horn2_pos_start, horn2_tip_pos, horn2_pos_end]
    sd.lines(horn1_points, color, width=2)
    sd.lines(horn2_points, color, width=2)


sd.background_color = sd.COLOR_WHITE

for _ in range(10):
    x_pos, y_pos = sd.randint(40, 560), sd.randint(40, 560)
    # x_pos, y_pos = 300, 300
    smile_color = sd.COLOR_BLACK
    smile(x_pos, y_pos, smile_color)

sd.pause()
