# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 10
sd.resolution = (1000, 900)

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

snowflake_arrow = list()


def create_snowflake():
    random_length = sd.randint(10, 100)
    random_x = sd.randint(0, sd.resolution[0])
    random_y = sd.randint(random_length + 100, sd.resolution[1])
    snowflake_arrow.append({"length": random_length, "point": sd.get_point(random_x, random_y)})


for i in range(N):
    create_snowflake()

fallen_snowflakes = list()

while True:
    sd.start_drawing()
    for flake in snowflake_arrow:
        sd.snowflake(flake['point'], flake['length'], color=sd.background_color)
        if flake['point'].y > flake['length']:
            flake['point'].y -= 20
            flake['point'].x -= sd.randint(-10, 10)
            if flake['point'].y <= flake['length']:
                create_snowflake()
        sd.snowflake(flake['point'], flake['length'])
        sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
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
