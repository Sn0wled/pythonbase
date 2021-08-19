# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def draw_rectangle(start_point, edge_length, start_angle=0, apex_number=3):
    end_point = start_point
    for angle in range(start_angle, start_angle + 360 - int(360 / apex_number), int(360 / apex_number)):
        v1 = sd.get_vector(start_point=end_point, angle=angle, length=edge_length)
        v1.draw(width=3, color=color)
        end_point = v1.end_point
    sd.line(start_point, end_point, width=3, color=color)


def draw_triangle(start_point, edge_length, start_angle=0):
    draw_rectangle(start_point, edge_length, start_angle=0, apex_number=3)


def draw_square(start_point, edge_length, start_angle=0):
    draw_rectangle(start_point, edge_length, start_angle=0, apex_number=4)


def draw_pentagon(start_point, edge_length, start_angle=0):
    draw_rectangle(start_point, edge_length, start_angle=0, apex_number=5)


def draw_hexagon(start_point, edge_length, start_angle=0):
    draw_rectangle(start_point, edge_length, start_angle=0, apex_number=6)


colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

print('Выберите цвет фигур:')
print('1) Красный; 2) Оранжевый; 3) желтый; 4) Зелёный; 5) Циан; 6) Синий; 7) Фиолетовый')
number_input = int(input())
color = colors[number_input - 1] if 0 < number_input < 8 else None

if color:
    x = list(range(50, 600, 150))
    point_0 = sd.get_point(x[0], 200)
    draw_triangle(point_0, 100, 30)
    point_0 = sd.get_point(x[1], 200)
    draw_square(point_0, 80, 60)
    point_0 = sd.get_point(x[2], 200)
    draw_pentagon(point_0, 60, 90)
    point_0 = sd.get_point(x[3], 200)
    draw_hexagon(point_0, 60, 120)
else:
    print('Ошибка выбора цвета')

sd.pause()
