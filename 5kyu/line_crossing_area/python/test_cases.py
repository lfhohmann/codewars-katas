import codewars_test as test
import random


MAX_COORDINATES = 1000


def line_crossing_area_solution(rectangle, line):

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


def gen_tests():
    def gen_test():
        def gen_rectangle():
            r_x = random.randint(-MAX_COORDINATES, MAX_COORDINATES)
            r_y = random.randint(-MAX_COORDINATES, MAX_COORDINATES)

            r_w = random.randint(
                0, min(MAX_COORDINATES - abs(r_x), MAX_COORDINATES - r_x)
            )
            r_h = random.randint(
                0, min(MAX_COORDINATES - abs(r_y), MAX_COORDINATES - r_y)
            )

            return r_x, r_y, r_w, r_h

        def gen_line():
            def gen_point():
                x = random.randint(-MAX_COORDINATES, MAX_COORDINATES)
                y = random.randint(-MAX_COORDINATES, MAX_COORDINATES)

                return x, y

            while True:
                p0 = gen_point()
                p1 = gen_point()

                if p0[0] != p1[0] and p0[1] != p1[1]:
                    return p0, p1

        return gen_rectangle(), gen_line()

    t, f = 0, 0
    challenges = []

    while t < 50 or f < 50:
        rectangle, line = gen_test()

        result = line_crossing_area_solution(rectangle, line)

        if result:
            if t < 50:
                challenges.append(((rectangle, line), result))
                t += 1
        else:
            if f < 50:
                challenges.append(((rectangle, line), result))
                f += 1

    random.shuffle(challenges)

    return challenges


@test.describe("Tests")
def tests():
    @test.it("Fixed Tests")
    def fixed_tests():
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((302, 169), (0, 0))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((302, 169), (304, 212))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((410, 299), (304, 212))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((410, 299), (396, 327))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((336, 397), (396, 327))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((336, 397), (277, 384))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((195, 329), (277, 384))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((195, 329), (231, 296))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((251, 249), (231, 296))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((251, 249), (351, 250))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((280, 366), (351, 250))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((280, 366), (294, 220))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((296, 367), (294, 220))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((296, 367), (296, 224))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((321, 315), (296, 224))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((321, 315), (252, 409))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((177, 286), (252, 409))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((177, 286), (309, 296))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((401, 299), (309, 296))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((401, 299), (538, 163))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((458, 104), (538, 163))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((458, 104), (480, 445))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((421, 540), (480, 445))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((421, 540), (150, 501))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((64, 437), (150, 501))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((64, 437), (83, 187))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((180, 116), (83, 187))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((180, 116), (453, 467))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((145, 457), (453, 467))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((145, 457), (473, 137))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((446, 307), (473, 137))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((446, 307), (454, 480))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((285, 484), (454, 480))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((285, 484), (134, 471))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((116, 302), (134, 471))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((116, 302), (125, 161))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((306, 141), (125, 161))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((306, 141), (149, 321))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((323, 462), (149, 321))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((323, 462), (443, 310))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((299, 171), (443, 310))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((299, 171), (403, 479))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((177, 277), (403, 479))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((177, 277), (471, 173))), True
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((507, 517), (471, 173))), False
        )
        test.assert_equals(
            line_crossing_area((300, 300, 100, 100), ((507, 517), (53, 58))), True
        )
        test.assert_equals(
            line_crossing_area((-229, 383, 209, 361), ((-82, 826), (-290, 637))), False
        )
        test.assert_equals(
            line_crossing_area((290, -560, 448, 304), ((633, -2), (-373, -811))), True
        )
        test.assert_equals(
            line_crossing_area((196, 357, 713, 327), ((932, -82), (-910, 844))), True
        )
        test.assert_equals(
            line_crossing_area((-213, -583, 581, 371), ((536, 290), (840, 37))), False
        )
        test.assert_equals(
            line_crossing_area((948, 890, 35, 76), ((-718, -81), (-116, 910))), False
        )
        test.assert_equals(
            line_crossing_area((-158, 356, 70, 600), ((-6, 731), (833, -406))), False
        )
        test.assert_equals(
            line_crossing_area((-266, 330, 90, 143), ((-668, 589), (-454, 578))), False
        )
        test.assert_equals(
            line_crossing_area((-321, -55, 291, 773), ((71, -73), (-645, 671))), True
        )
        test.assert_equals(
            line_crossing_area((-19, -324, 499, 658), ((-214, -706), (-246, 939))), True
        )
        test.assert_equals(
            line_crossing_area((-241, -242, 584, 529), ((109, 219), (625, 284))), False
        )
        test.assert_equals(
            line_crossing_area((-521, -518, 130, 67), ((301, -998), (369, 152))), False
        )
        test.assert_equals(
            line_crossing_area((-287, -15, 298, 297), ((-367, 14), (567, -445))), True
        )
        test.assert_equals(
            line_crossing_area((61, -399, 131, 475), ((-416, -584), (340, -177))), True
        )
        test.assert_equals(
            line_crossing_area((571, 180, 179, 549), ((-45, 995), (981, -260))), True
        )
        test.assert_equals(
            line_crossing_area((-885, -39, 43, 543), ((-944, 678), (935, 221))), False
        )
        test.assert_equals(
            line_crossing_area((-477, 886, 244, 74), ((679, 984), (-437, 158))), False
        )
        test.assert_equals(
            line_crossing_area((282, 903, 530, 72), ((-231, -311), (-322, -931))), False
        )
        test.assert_equals(
            line_crossing_area((-257, 657, 5, 272), ((885, -621), (-620, -495))), False
        )
        test.assert_equals(
            line_crossing_area((339, 307, 573, 473), ((827, 875), (-137, -363))), True
        )
        test.assert_equals(
            line_crossing_area((-169, 23, 176, 959), ((-181, 412), (801, -161))), True
        )
        test.assert_equals(
            line_crossing_area((-118, -181, 773, 808), ((-634, 42), (693, 681))), True
        )
        test.assert_equals(
            line_crossing_area((-583, -151, 283, 442), ((-910, -885), (-657, -430))),
            False,
        )
        test.assert_equals(
            line_crossing_area((175, 727, 718, 123), ((-694, 317), (-908, 944))), False
        )
        test.assert_equals(
            line_crossing_area((398, -741, 594, 183), ((635, -939), (817, 742))), True
        )
        test.assert_equals(
            line_crossing_area((115, 195, 265, 253), ((224, -786), (-198, 900))), True
        )
        test.assert_equals(
            line_crossing_area((-360, -807, 112, 192), ((-991, -308), (-319, -989))),
            True,
        )
        test.assert_equals(
            line_crossing_area((264, -446, 520, 490), ((676, -651), (352, 239))), True
        )
        test.assert_equals(
            line_crossing_area((920, 956, 45, 7), ((-483, 415), (697, -139))), False
        )
        test.assert_equals(
            line_crossing_area((-131, -498, 612, 224), ((-486, -436), (694, 59))), True
        )
        test.assert_equals(
            line_crossing_area((557, -578, 221, 77), ((-853, 879), (628, 556))), False
        )
        test.assert_equals(
            line_crossing_area((325, 358, 81, 513), ((-747, 215), (383, 2))), False
        )
        test.assert_equals(
            line_crossing_area((388, -374, 316, 41), ((155, -635), (-719, -454))), False
        )
        test.assert_equals(
            line_crossing_area((-688, -329, 107, 404), ((-446, 863), (-794, -704))),
            True,
        )
        test.assert_equals(
            line_crossing_area((-657, -66, 292, 222), ((441, -655), (-837, -122))), True
        )
        test.assert_equals(
            line_crossing_area((820, 919, 109, 70), ((-542, 277), (671, -2))), False
        )
        test.assert_equals(
            line_crossing_area((216, 726, 701, 140), ((533, 796), (879, 22))), True
        )
        test.assert_equals(
            line_crossing_area((-881, 838, 27, 160), ((624, 87), (226, -449))), False
        )
        test.assert_equals(
            line_crossing_area((-758, -234, 223, 307), ((-769, -441), (707, -196))),
            False,
        )
        test.assert_equals(
            line_crossing_area((-851, -275, 54, 325), ((975, -431), (-260, 292))), False
        )
        test.assert_equals(
            line_crossing_area((-49, -197, 484, 396), ((137, 58), (-227, -242))), True
        )
        test.assert_equals(
            line_crossing_area((267, 265, 332, 466), ((758, -183), (109, -665))), False
        )
        test.assert_equals(
            line_crossing_area((-171, -493, 434, 379), ((652, -593), (-213, -571))),
            True,
        )
        test.assert_equals(
            line_crossing_area((759, -599, 85, 0), ((-42, 767), (495, 22))), False
        )
        test.assert_equals(
            line_crossing_area((-624, -198, 75, 514), ((195, -227), (-576, 528))), False
        )
        test.assert_equals(
            line_crossing_area((471, 243, 279, 718), ((-634, -203), (946, 234))), True
        )
        test.assert_equals(
            line_crossing_area((406, -709, 66, 160), ((465, 856), (130, 801))), False
        )
        test.assert_equals(
            line_crossing_area((-581, -740, 379, 236), ((-268, -832), (-851, -926))),
            True,
        )
        test.assert_equals(
            line_crossing_area((238, 685, 691, 196), ((-278, 893), (90, 432))), True
        )
        test.assert_equals(
            line_crossing_area((637, 159, 275, 541), ((895, 632), (-484, -915))), True
        )
        test.assert_equals(
            line_crossing_area((-298, 257, 568, 413), ((-663, 514), (334, -360))), True
        )
        test.assert_equals(
            line_crossing_area((582, -628, 225, 218), ((35, -446), (777, -696))), True
        )
        test.assert_equals(
            line_crossing_area((792, -856, 127, 143), ((133, 161), (-15, 118))), False
        )
        test.assert_equals(
            line_crossing_area((-435, 119, 204, 158), ((-905, 471), (184, -227))), True
        )
        test.assert_equals(
            line_crossing_area((567, -44, 199, 139), ((-506, 89), (577, 211))), False
        )

    @test.it("Edge Cases")
    def edge_cases():
        test.assert_equals(
            line_crossing_area((100, 100, 10, 20), ((-100, -100), (-100, 100))), False
        )
        test.assert_equals(
            line_crossing_area((100, 100, 10, 20), ((100, -100), (-100, -100))), False
        )
        test.assert_equals(
            line_crossing_area((100, 100, 200, 200), ((-100, -100), (100, 100))), True
        )
        test.assert_equals(
            line_crossing_area((0, 0, 250, 20), ((-100, -100), (-100, 100))), True
        )
        test.assert_equals(
            line_crossing_area((0, 0, 10, 250), ((100, -100), (-100, -100))), True
        )

    @test.it("Random Tests")
    def random_tests():
        for entry in gen_tests():
            test.assert_equals(line_crossing_area(entry[0][0], entry[0][1]), entry[1])
