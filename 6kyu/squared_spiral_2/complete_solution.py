def squared_spiral(x, y):
    x_dist, y_dist = 1, 1
    x_min, y_min = -1, -1
    x_max, y_max = 1, 1
    direction = "east"
    counter = 0
    x_pos, y_pos = 0, 0

    while x != x_pos or y != y_pos:
        if direction == "east":
            x_pos += 1

            if x_pos == x_max:
                direction = "north"
                y_max = y_pos + y_dist
                x_dist += 1

        elif direction == "north":
            y_pos += 1

            if y_pos == y_max:
                direction = "west"
                x_min = x_pos - x_dist
                y_dist += 1

        elif direction == "west":
            x_pos -= 1

            if x_pos == x_min:
                direction = "south"
                y_min = y_pos - y_dist
                x_dist += 1

        elif direction == "south":
            y_pos -= 1

            if y_pos == y_min:
                direction = "east"
                x_max = x_pos + x_dist
                y_dist += 1

        counter += 1

    return counter
