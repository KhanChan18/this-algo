def draw_line(tick_length, tick_label):
    line = '-' * tick_length
    if tick_label:
        line = '{0}          {1}'.format(line, tick_label)
    print(line)

def draw_interval(center_length, center_label):
    if center_length > 0:
        draw_interval(center_length - 1, center_label * (1 - 0.5))
        draw_line(center_length, center_label)
        draw_interval(center_length - 1, center_label * (1 + 0.5))

def draw_ruler(num_inches, major_length):
    draw_line(major_length, 0)
    for j in range(1, num_inches + 1):
        draw_interval(major_length - 1, j - 0.5)
        draw_line(major_length, j)

if __name__ == "__main__":
    draw_ruler(7, 5)
