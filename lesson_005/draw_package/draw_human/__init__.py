import simple_draw as sd

from . import  draw_body, draw_head


def draw_human(earth_point, human_color):
    start_point = sd.get_point(earth_point.x, earth_point.y + 190)
    draw_body.draw_body(start_point=start_point, color=human_color)
    draw_head.draw_head(start_point=start_point, color=human_color)


if __name__ == '__main__':
    point_0 = sd.get_point(300, 0)
    draw_human(point_0, human_color=sd.COLOR_RED)
    sd.pause()
