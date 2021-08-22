from . import draw_wall, draw_roof


def draw_house(start_point, house_wall_height, house_wall_length, wall_color=draw_wall.sd.COLOR_YELLOW,
               roof_color=draw_wall.sd.COLOR_RED):
    draw_wall.draw_wall(start_point=start_point, wall_height=house_wall_height, wall_width=house_wall_length,
                        wall_color=wall_color)
    draw_roof.draw_roof(start_point=start_point, house_wall_height=house_wall_height,
                        house_wall_length=house_wall_length, roof_color=roof_color)


if __name__ == '__main__':
    point_0 = draw_wall.sd.get_point(100, 100)
    draw_house(start_point=point_0, house_wall_height=300, house_wall_length=400)
    draw_wall.sd.pause()
