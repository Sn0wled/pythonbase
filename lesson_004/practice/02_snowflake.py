# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()

# sd.snowflake(center=point_0, length=200, factor_a=0.5)

# реализовать падение одной снежинки
# y = 500
# x = 100
#
# y2 = 450
# x2 = 150
# while True:
#     sd.clear_screen()
#     point = sd.get_point(x, y)
#     sd.snowflake(center=point, length=50)
#     y -= 1
#     if y < 50:
#        break
#     x = x + 1
#
#     point2 = sd.get_point(x2, y2)
#     sd.snowflake(center=point2, length=30)
#     y2 -= 1
#     if y2 < 50:
#        break
#     x2 = x2 + 2
#
#     sd.sleep(0.01)
#     if sd.user_want_exit():
#         break

# реализовать падение одной снежинки из произвольного места экрана

random_x = sd.randint(0, sd.resolution[0]//2)
random_y = sd.randint(300, sd.resolution[1])
random_point = sd.get_point(random_x, random_y)

# while random_point.y > 50:
#     sd.clear_screen()
#     random_point.y -= 1
#     sd.snowflake(random_point, length=50)
#     sd.sleep(0.01)
# реализовать падение одной снежинки с ветром - смещение в сторону

while random_point.y > 50:
    sd.clear_screen()
    random_point.y -= 10
    random_point.x += 13
    sd.snowflake(random_point, length=50)
    sd.sleep(0.1)


sd.pause()
