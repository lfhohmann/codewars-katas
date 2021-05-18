import codewars_test as test
from random import randint


def squared_spiral_solution(n):
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


@test.describe("Tests")
def tests():
    @test.it("Fixed Tests")
    def fixed_tests():
        test.assert_equals(squared_spiral(94245), (150, -153))
        test.assert_equals(squared_spiral(63991), (109, -126))
        test.assert_equals(squared_spiral(18874), (69, 37))
        test.assert_equals(squared_spiral(70603), (20, 133))
        test.assert_equals(squared_spiral(34404), (93, 87))
        test.assert_equals(squared_spiral(39955), (-55, 100))
        test.assert_equals(squared_spiral(5753), (-15, 38))
        test.assert_equals(squared_spiral(47216), (109, 19))
        test.assert_equals(squared_spiral(19041), (-66, 69))
        test.assert_equals(squared_spiral(6404), (-40, 36))
        test.assert_equals(squared_spiral(54074), (-98, -116))
        test.assert_equals(squared_spiral(77327), (-139, 96))
        test.assert_equals(squared_spiral(8716), (47, 21))
        test.assert_equals(squared_spiral(7706), (-6, 44))
        test.assert_equals(squared_spiral(33867), (-92, 81))
        test.assert_equals(squared_spiral(94392), (154, -10))
        test.assert_equals(squared_spiral(14498), (-60, -38))
        test.assert_equals(squared_spiral(82518), (144, 6))
        test.assert_equals(squared_spiral(23150), (-76, 30))
        test.assert_equals(squared_spiral(76749), (139, -118))
        test.assert_equals(squared_spiral(31877), (-74, -89))
        test.assert_equals(squared_spiral(56429), (96, 119))
        test.assert_equals(squared_spiral(16035), (-30, -63))
        test.assert_equals(squared_spiral(28949), (-85, 36))
        test.assert_equals(squared_spiral(92924), (52, -152))
        test.assert_equals(squared_spiral(4891), (-26, 35))
        test.assert_equals(squared_spiral(78454), (-140, 86))
        test.assert_equals(squared_spiral(91487), (-151, -132))
        test.assert_equals(squared_spiral(55584), (-6, 118))
        test.assert_equals(squared_spiral(51378), (-37, -113))
        test.assert_equals(squared_spiral(30301), (-87, 62))
        test.assert_equals(squared_spiral(12762), (50, -56))
        test.assert_equals(squared_spiral(37611), (-72, 97))
        test.assert_equals(squared_spiral(10893), (-52, -25))
        test.assert_equals(squared_spiral(92117), (147, 152))
        test.assert_equals(squared_spiral(13683), (53, -58))
        test.assert_equals(squared_spiral(48712), (-18, -110))
        test.assert_equals(squared_spiral(42723), (-22, -103))
        test.assert_equals(squared_spiral(61506), (-124, 122))
        test.assert_equals(squared_spiral(72915), (-135, 120))
        test.assert_equals(squared_spiral(41798), (-102, -80))
        test.assert_equals(squared_spiral(48586), (-110, -76))
        test.assert_equals(squared_spiral(2944), (-27, -1))
        test.assert_equals(squared_spiral(45867), (-107, 36))
        test.assert_equals(squared_spiral(21837), (-7, 74))
        test.assert_equals(squared_spiral(34889), (14, -93))
        test.assert_equals(squared_spiral(38542), (-98, -28))
        test.assert_equals(squared_spiral(66626), (-129, 67))
        test.assert_equals(squared_spiral(1218), (11, -17))
        test.assert_equals(squared_spiral(26865), (-51, 82))
        test.assert_equals(squared_spiral(53529), (116, 53))
        test.assert_equals(squared_spiral(74310), (-82, -136))
        test.assert_equals(squared_spiral(12092), (-47, 55))
        test.assert_equals(squared_spiral(43660), (84, -104))
        test.assert_equals(squared_spiral(86877), (0, -147))
        test.assert_equals(squared_spiral(91399), (-151, -44))
        test.assert_equals(squared_spiral(16484), (-64, -36))
        test.assert_equals(squared_spiral(5647), (38, -15))
        test.assert_equals(squared_spiral(22356), (69, 75))
        test.assert_equals(squared_spiral(5746), (-8, 38))
        test.assert_equals(squared_spiral(53862), (-116, 78))
        test.assert_equals(squared_spiral(83753), (145, 88))
        test.assert_equals(squared_spiral(65932), (12, -128))
        test.assert_equals(squared_spiral(42831), (86, -103))
        test.assert_equals(squared_spiral(37447), (92, 97))
        test.assert_equals(squared_spiral(56692), (-119, 71))
        test.assert_equals(squared_spiral(77723), (22, -139))
        test.assert_equals(squared_spiral(40747), (-44, 101))
        test.assert_equals(squared_spiral(33561), (92, -19))
        test.assert_equals(squared_spiral(43881), (105, 96))
        test.assert_equals(squared_spiral(82186), (-39, -143))
        test.assert_equals(squared_spiral(2271), (9, 24))
        test.assert_equals(squared_spiral(307), (8, 9))
        test.assert_equals(squared_spiral(40676), (27, 101))
        test.assert_equals(squared_spiral(36091), (-86, 95))
        test.assert_equals(squared_spiral(17145), (50, -65))
        test.assert_equals(squared_spiral(72666), (99, 135))
        test.assert_equals(squared_spiral(4891), (-26, 35))
        test.assert_equals(squared_spiral(53196), (-49, -115))
        test.assert_equals(squared_spiral(28869), (-54, 85))
        test.assert_equals(squared_spiral(58081), (121, -120))
        test.assert_equals(squared_spiral(19018), (-43, 69))
        test.assert_equals(squared_spiral(79292), (91, 141))
        test.assert_equals(squared_spiral(46817), (-108, -53))
        test.assert_equals(squared_spiral(26718), (82, 68))
        test.assert_equals(squared_spiral(67941), (-49, -130))
        test.assert_equals(squared_spiral(71679), (11, 134))
        test.assert_equals(squared_spiral(96388), (-155, -133))
        test.assert_equals(squared_spiral(54337), (117, -68))
        test.assert_equals(squared_spiral(6179), (-22, -39))
        test.assert_equals(squared_spiral(85842), (140, -146))
        test.assert_equals(squared_spiral(13773), (59, 26))
        test.assert_equals(squared_spiral(30678), (88, -34))
        test.assert_equals(squared_spiral(67835), (-130, -105))
        test.assert_equals(squared_spiral(95304), (-22, -154))
        test.assert_equals(squared_spiral(87767), (-148, -3))
        test.assert_equals(squared_spiral(32575), (-90, -85))
        test.assert_equals(squared_spiral(45816), (-107, 87))
        test.assert_equals(squared_spiral(97608), (-156, -108))
        test.assert_equals(squared_spiral(97538), (-156, -38))

    @test.it("Random Tests")
    def random_tests():
        for _ in range(200):
            n = randint(0, 100_000)
            test.assert_equals(squared_spiral(n), squared_spiral_solution(n))
