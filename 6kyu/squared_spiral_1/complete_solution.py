def squared_spiral(n):
    x_dist, y_dist = 1, 1
    x_min, y_min = -1, -1
    x_max, y_max = 1, 1
    direction = "east"
    counter = 0
    x, y = 0, 0

    while counter < n:
        if direction == "east":
            x += 1

            if x == x_max:
                direction = "north"
                y_max = y + y_dist
                x_dist += 1

        elif direction == "north":
            y += 1

            if y == y_max:
                direction = "west"
                x_min = x - x_dist
                y_dist += 1

        elif direction == "west":
            x -= 1

            if x == x_min:
                direction = "south"
                y_min = y - y_dist
                x_dist += 1

        elif direction == "south":
            y -= 1

            if y == y_min:
                direction = "east"
                x_max = x + x_dist
                y_dist += 1

        counter += 1

    return (x, y)
