# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

point_0 = sd.get_point(200, 200)


def draw_rectangle(start_point, edge_length, start_angle=0, apex_number=3):
    end_point = start_point
    for angle in range(start_angle, start_angle + 360 - int(360 / apex_number), int(360 / apex_number)):
        v1 = sd.get_vector(start_point=end_point, angle=angle, length=edge_length)
        v1.draw(width=3)
        end_point = v1.end_point
    sd.line(start_point, end_point, width=3)


def draw_triangle(start_point, edge_length, start_angle=0):
    draw_rectangle(start_point, edge_length, start_angle=0, apex_number=3)


def draw_square(start_point, edge_length, start_angle=0):
    draw_rectangle(start_point, edge_length, start_angle=0, apex_number=4)


def draw_pentagon(start_point, edge_length, start_angle=0):
    draw_rectangle(start_point, edge_length, start_angle=0, apex_number=5)


def draw_hexagon(start_point, edge_length, start_angle=0):
    draw_rectangle(start_point, edge_length, start_angle=0, apex_number=6)


draw_pentagon(point_0, 200)
# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
