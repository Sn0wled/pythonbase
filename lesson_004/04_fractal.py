# -*- coding: utf-8 -*-

import simple_draw as sd

point_0 = sd.get_point(300, 0)

sd.resolution = (1000, 900)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# def draw_branches(start_point, angle_draw, branches_length):
#     delta_angle = 30
#     vector_1 = sd.get_vector(start_point, angle_draw + delta_angle, branches_length)
#     vector_2 = sd.get_vector(start_point, angle_draw - delta_angle, branches_length)
#     vector_1.draw(width=2)
#     vector_2.draw(width=2)


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# def draw_branches(start_point, angle_draw, branches_length):
#     if branches_length > 3:
#         delta_angle = 30
#         angle_vector_1 = angle_draw + delta_angle
#         angle_vector_2 = angle_draw - delta_angle
#         vector = sd.get_vector(start_point,angle_draw, branches_length)
#         vector.draw(width=2)
#         draw_branches(vector.end_point, angle_vector_1, branches_length*.75)
#         draw_branches(vector.end_point, angle_vector_2, branches_length*.75)
#
#
# # 3) первоначальный вызов:
root_point = sd.get_point(500, 30)


# draw_branches(start_point=root_point, angle_draw=90, branches_length=150)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

def draw_branches(start_point, angle_draw, branches_length):
    if branches_length > 3:
        delta_angle = 30
        angle_vector_1 = angle_draw + delta_angle * sd.randint(60, 140) / 100
        angle_vector_2 = angle_draw - delta_angle * sd.randint(60, 140) / 100
        vector = sd.get_vector(start_point, angle_draw, branches_length)
        vector.draw(width=2)
        draw_branches(vector.end_point, angle_vector_1, branches_length * .70 * sd.randint(80, 120) / 100)
        draw_branches(vector.end_point, angle_vector_2, branches_length * .70 * sd.randint(80, 120) / 100)
    else:
        delta_angle = 30
        angle_vector_1 = angle_draw + delta_angle * sd.randint(60, 140) / 100
        angle_vector_2 = angle_draw - delta_angle * sd.randint(60, 140) / 100
        vector = sd.get_vector(start_point, angle_draw, branches_length)
        vector.draw(width=5, color=sd.COLOR_DARK_GREEN)


draw_branches(root_point, 90, 100)

# Пригодятся функции
# sd.random_number()

sd.pause()
