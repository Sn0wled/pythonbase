import simple_draw as sd


def draw_branches(start_point, branches_length, angle_draw=90, start_width=10.0):
    branch_color = sd.COLOR_DARK_ORANGE
    if branches_length > 4:
        if branches_length < 10:
            branch_color = sd.COLOR_GREEN
        delta_angle = 30
        branch_vector = sd.get_vector(start_point=start_point, angle=angle_draw, length=branches_length)
        branch_vector.draw(width=int(start_width), color=branch_color)
        change_width = start_width * 0.8
        change_length = branches_length * 0.75
        new_branch_1_angle = angle_draw + delta_angle
        new_branch_2_angle = angle_draw - delta_angle
        draw_branches(start_point=branch_vector.end_point, branches_length=change_length, angle_draw=new_branch_1_angle,
                      start_width=change_width)
        draw_branches(start_point=branch_vector.end_point, branches_length=change_length, angle_draw=new_branch_2_angle,
                      start_width=change_width)


if __name__ == '__main__':
    point_0 = sd.get_point(300, 0)
    draw_branches(start_point=point_0, branches_length=100)
    sd.pause()
