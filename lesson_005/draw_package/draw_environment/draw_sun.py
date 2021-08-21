import simple_draw as sd


def draw_sun(sun_point):
    sun_radius = 50
    sd.circle(center_position=sun_point, radius=sun_radius, width=0)
    ray_length = sun_radius * 2
    for ray_angle in range(0, 360, 36):
        ray_vector = sd.get_vector(start_point=sun_point, angle=ray_angle, length=ray_length)
        ray_vector.draw(width=4)


if __name__ == '__main__':
    draw_sun(sd.get_point(300, 300))
    sd.pause()
