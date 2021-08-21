import simple_draw as sd


def draw_roof(start_point, house_wall_height, house_wall_length, roof_color):
    roof_height = 100 # Регулировать высоту крыши
    roof_ledge = 50 # Регулировать выступ крыши
    line_width = 0
    point_1_x = start_point.x - roof_ledge
    point_1_y = start_point.y + house_wall_height
    point_1 = sd.get_point(point_1_x, point_1_y)
    point_2_x = start_point.x + house_wall_length + roof_ledge
    point_2_y = start_point.y + house_wall_height
    point_2 = sd.get_point(point_2_x, point_2_y)
    point_3_x = start_point.x + house_wall_length//2
    point_3_y = start_point.y + house_wall_height + roof_height
    point_3 = sd.get_point(point_3_x, point_3_y)
    roof_points = [point_1, point_2, point_3]
    sd.polygon(point_list=roof_points, color=roof_color, width=line_width)
