# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd

import draw_package

sd.resolution = (1280, 800)
sd.background_color = sd.COLOR_BLUE

ground_lvl = 100
draw_package.draw_environment.draw_rainbow.draw_rainbow()
draw_package.draw_environment.draw_sun.draw_sun(sd.get_point(1000, 650))
draw_package.draw_environment.draw_float.draw_float(ground_lvl, sd.COLOR_DARK_GREEN)
house_x = 400
house_point = sd.get_point(house_x, ground_lvl)
draw_package.draw_house.draw_house(house_point, house_wall_height=200, house_wall_length=400,
                                   roof_color=sd.COLOR_DARK_ORANGE)
draw_package.draw_environment.draw_snawfall.create_snowfall(start_x=0, end_x=house_x-30, ground_y=ground_lvl)
draw_package.draw_environment.draw_rainbow.draw_rainbow()
draw_package.draw_environment.draw_float.draw_float(ground_lvl, sd.COLOR_DARK_GREEN)
draw_package.draw_environment.draw_tree.draw_branches(sd.get_point(1000, ground_lvl), branches_length=70)
draw_package.draw_environment.draw_tree.draw_branches(sd.get_point(1200, ground_lvl), branches_length=40)
human_point = sd.get_point(900, ground_lvl)
draw_package.draw_human.draw_human(human_point, sd.COLOR_BLACK)

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
sd.pause()
