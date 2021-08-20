# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 50

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

snowflake_arrow = list()

for i in range(N):
    random_length = sd.randint(10, 100)
    snowflake_arrow.append({"length": random_length, "point": sd.random_point()})

while True:
    test = True
    for snowflake_data in snowflake_arrow:
        sd.start_drawing()
        sd.snowflake(snowflake_data['point'], snowflake_data['length'], color=sd.background_color)
        if snowflake_data['point'].y > snowflake_data['length']:
            snowflake_data['point'].y -= 10
            test = False
        sd.snowflake(snowflake_data['point'], snowflake_data['length'])
        sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit() or test:
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
