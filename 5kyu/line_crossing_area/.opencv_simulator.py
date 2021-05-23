import cv2 as cv
import numpy as np

drawing = False  # true if mouse is pressed
pt0_x, pt0_y = 0, 0
pt1_x, pt1_y = 0, 0
point_number = 0


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

        else:
            return False

    # Check if line is horizontal
    elif p1_y - p0_y == 0:

        # Check if horizontal line is crossing rectangle
        if (
            r_height[0] <= p0_y <= r_height[1]
            and min(p0_x, p1_x) <= r_width[0]
            and max(p0_x, p1_x) >= r_width[1]
        ):
            return True

        else:
            return False

    # Line is not vertical nor horizontal
    else:
        # Extract line equations parameters
        # y = mx + b
        # x = (y-b)/m
        m = (p1_y - p0_y) / (p1_x - p0_x)
        b = p1_y - (m * p1_x)

        results = []

        # Check if line is crossing each boundary
        if min(p0_y, p1_y) < r_height[0] < max(p0_y, p1_y):
            if r_width[0] <= (r_height[0] - b) / m <= r_width[1]:
                results.append("Upper")
                return True

        if min(p0_y, p1_y) < r_height[1] < max(p0_y, p1_y):
            if r_width[0] <= (r_height[1] - b) / m <= r_width[1]:
                results.append("Lower")
                return True

        if min(p0_x, p1_x) < r_width[0] < max(p0_x, p1_x):
            if r_height[0] <= (m * r_width[0]) + b <= r_height[1]:
                results.append("Left")
                return True

        if min(p0_x, p1_x) < r_width[1] < max(p0_x, p1_x):
            if r_height[0] <= (m * r_width[1]) + b <= r_height[1]:
                results.append("Right")
                return True

        # If no boundaries were crossed, return False
        if results == []:
            # return "Not crossing"
            return False
        else:
            # return results, line
            pass


def line_drawing(event, x, y, flags, param):
    global pt0_x, pt0_y, pt1_x, pt1_y, point_number, drawing

    if event == cv.EVENT_LBUTTONDOWN:

        if point_number == 0:
            pt0_x, pt0_y = x, y
            point_number = 1

        else:
            pt1_x, pt1_y = x, y
            point_number = 0

        result = line_crossing_area(
            (300, 300, 100, 100), ((pt0_x, pt0_y), (pt1_x, pt1_y))
        )

        print(
            f"test.assert_equals(line_crossing_area((300, 300, 100, 100), (({pt0_x}, {pt0_y}), ({pt1_x}, {pt1_y}))), {result})"
        )


cv.namedWindow("canvas")
cv.setMouseCallback("canvas", line_drawing)

while True:
    img = np.zeros((600, 600, 3), np.uint8)

    cv.rectangle(img, (250, 250), (350, 350), (0, 0, 255), 1)
    cv.line(img, (pt0_x, pt0_y), (pt1_x, pt1_y), color=(255, 255, 255), thickness=1)

    cv.imshow("canvas", img)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()
