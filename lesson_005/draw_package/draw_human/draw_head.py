import simple_draw as sd


def draw_head(start_point, color):
    horn_height = 30

    horn1_pos_start = sd.get_point(start_point.x + 20, start_point.y + 3 ** .5 * 20)
    horn1_pos_end = sd.get_point(start_point.x + 3 ** .5 * 20, start_point.y + 20)
    horn1_tip_pos = sd.get_point(start_point.x + 3 ** .5 * 20, start_point.y + 20 + horn_height)

    horn2_pos_start = sd.get_point(start_point.x - 20, start_point.y + 3 ** .5 * 20)
    horn2_pos_end = sd.get_point(start_point.x - 3 ** .5 * 20, start_point.y + 20)
    horn2_tip_pos = sd.get_point(start_point.x - 3 ** .5 * 20, start_point.y + 20 + horn_height)

    horn1_points = [horn1_pos_start, horn1_tip_pos, horn1_pos_end]
    horn2_points = [horn2_pos_start, horn2_tip_pos, horn2_pos_end]
    sd.polygon(horn1_points, color, width=0)
    sd.polygon(horn2_points, color, width=0)

    start_point = sd.get_point(start_point.x, start_point.y)
    sd.circle(start_point, radius=40, color=color, width=2)
    sd.circle(start_point, radius=40, color=sd.COLOR_YELLOW, width=0)

    eye_distance = 15
    left_eye_pos = sd.get_point(start_point.x + eye_distance, start_point.y + 10)
    right_eye_pos = sd.get_point(start_point.x - eye_distance, start_point.y + 10)
    sd.circle(left_eye_pos, 5, color, 2)
    sd.circle(right_eye_pos, 5, color, 2)

    mouth_width = 20
    y_mouth_pos = start_point.y - 12
    mouth_height = 10
    mouth_left_pos = sd.get_point(start_point.x - mouth_width, y_mouth_pos)
    mouth_right_pos = sd.get_point(start_point.x + mouth_width, y_mouth_pos)
    mouth_bottom_left_pos = sd.get_point(start_point.x - mouth_width / 2, y_mouth_pos - mouth_height)
    mouth_bottom_right_pos = sd.get_point(start_point.x + mouth_width / 2, y_mouth_pos - mouth_height)
    mouth_points = [mouth_left_pos, mouth_right_pos, mouth_bottom_right_pos, mouth_bottom_left_pos]
    sd.polygon(mouth_points, color=color, width=2)


if __name__ == '__main__':
    point_0 = sd.get_point(300, 300)
    draw_head(point_0, color=sd.COLOR_BLACK)
    sd.pause()
