import simple_draw as sd


def draw_body(start_point, color):
    point_1 = sd.get_point(start_point.x, start_point.y - 40)
    point_2 = sd.get_point(start_point.x, start_point.y - 120)
    point_hand_start = sd.get_point(start_point.x, start_point.y - 60)
    point_hand_end_1 = sd.get_point(start_point.x - 40, start_point.y - 120)
    point_hand_end_2 = sd.get_point(start_point.x + 40, start_point.y - 120)
    point_leg_end_1 = sd.get_point(start_point.x + 40, start_point.y - 190)
    point_leg_end_2 = sd.get_point(start_point.x - 40, start_point.y - 190)
    body_points = [point_2, point_1]
    hands_points = [point_hand_end_1, point_hand_start, point_hand_end_2]
    legs_points = [point_leg_end_1, point_2, point_leg_end_2]
    sd.lines(body_points, width=4, color=color)
    sd.lines(hands_points, width=4, color=color)
    sd.lines(legs_points, width=4, color=color)
