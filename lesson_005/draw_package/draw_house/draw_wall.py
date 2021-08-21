import simple_draw as sd


def draw_wall(start_point, wall_height, wall_width, wall_color=sd.COLOR_YELLOW):
    line_width = 2
    v1 = sd.get_vector(start_point, angle=0, length=wall_width)
    v2 = sd.get_vector(v1.end_point, angle=90, length=wall_height)
    v3 = sd.get_vector(v2.end_point, angle=180, length=wall_width)
    v4 = sd.get_vector(v3.end_point, angle=270, length=wall_height)

    v1.draw(color=wall_color, width=line_width)
    v2.draw(color=wall_color, width=line_width)
    v3.draw(color=wall_color, width=line_width)
    v4.draw(color=wall_color, width=line_width)

    break_height = 20
    break_length = 2 * break_height

    for i, y in enumerate(range(0, wall_height, break_height)):
        wall_y = start_point.y + y
        v1 = sd.get_vector(sd.get_point(start_point.x, wall_y), length=wall_width, angle=0)
        v1.draw(color=wall_color, width=line_width)
        for x in range(break_length // 2 * (i % 2), wall_width, break_length):
            wall_x = start_point.x + x
            v1 = sd.get_vector(sd.get_point(wall_x, wall_y), length=break_height, angle=90)
            v1.draw(color=wall_color, width=line_width)


if __name__ == '__main__':
    point_0 = sd.get_point(100, 100)
    draw_wall(start_point=point_0, wall_height=200, wall_width=400)
    sd.pause()
