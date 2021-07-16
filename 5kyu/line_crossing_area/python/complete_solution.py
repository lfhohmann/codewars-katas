def line_crossing_area(rectangle, line):

    # Calculate rectangle width and height boundary lines
    r_width = rectangle[0] - (rectangle[2] / 2), rectangle[0] + (rectangle[2] / 2)
    r_height = rectangle[1] - (rectangle[3] / 2), rectangle[1] + (rectangle[3] / 2)

    # Check if any of the points are inside the area
    for point in line:
        if (
            r_width[0] <= point[0] <= r_width[1]
            and r_height[0] <= point[1] <= r_height[1]
        ):
            return True

    # Create points variables
    p0_x, p0_y = line[0]
    p1_x, p1_y = line[1]

    # Check if line is vertical
    if p1_x - p0_x == 0:

        # Check if vertical line is crossing rectangle
        if (
            r_width[0] <= p0_x <= r_width[1]
            and min(p0_y, p1_y) <= r_height[0]
            and max(p0_y, p1_y) >= r_height[1]
        ):
            return True

    # Check if line is horizontal
    elif p1_y - p0_y == 0:

        # Check if horizontal line is crossing rectangle
        if (
            r_height[0] <= p0_y <= r_height[1]
            and min(p0_x, p1_x) <= r_width[0]
            and max(p0_x, p1_x) >= r_width[1]
        ):
            return True

    # Line is not vertical nor horizontal
    else:
        # Extract line equations parameters
        # y = mx + b
        # x = (y-b)/m
        m = (p1_y - p0_y) / (p1_x - p0_x)
        b = p1_y - (m * p1_x)

        # Check if line is crossing each boundary
        if min(p0_y, p1_y) < r_height[0] < max(p0_y, p1_y):
            if r_width[0] <= (r_height[0] - b) / m <= r_width[1]:
                return True

        if min(p0_y, p1_y) < r_height[1] < max(p0_y, p1_y):
            if r_width[0] <= (r_height[1] - b) / m <= r_width[1]:
                return True

        if min(p0_x, p1_x) < r_width[0] < max(p0_x, p1_x):
            if r_height[0] <= (m * r_width[0]) + b <= r_height[1]:
                return True

        if min(p0_x, p1_x) < r_width[1] < max(p0_x, p1_x):
            if r_height[0] <= (m * r_width[1]) + b <= r_height[1]:
                return True

    return False
