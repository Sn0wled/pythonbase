import simple_draw as sd


def draw_float(float_y, float_color):
    left_bottom = sd.get_point(0, 0)
    right_top = sd.get_point(*sd.resolution)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=float_color, width=0)
