import simple_draw as sd

N = 30
snowflake_arrow = list()


def create_snowfall(start_x, end_x, ground_y=100):
    def create_snowflake():
        random_length = sd.randint(5, 30)
        random_x = sd.randint(start_x, end_x)
        random_y = sd.randint(random_length + 100 + ground_y, sd.resolution[1])
        snowflake_arrow.append({"length": random_length, "point": sd.get_point(random_x, random_y)})

    for i in range(N):
        create_snowflake()
    test = True
    while test:
        test = False
        sd.start_drawing()
        for flake in snowflake_arrow:
            sd.snowflake(flake['point'], flake['length'], color=sd.background_color)
            if flake['point'].y > flake['length'] + ground_y:
                test = True
                flake['point'].y -= 5
            sd.snowflake(flake['point'], flake['length'])
            sd.finish_drawing()


if __name__ == '__main__':
    create_snowfall(start_x=10, end_x=200)
    sd.pause()
