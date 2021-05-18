import codewars_test as test
from random import randint


def squared_spiral_solution(x_target, y_target):
    x_dist, y_dist = 1, 1
    x_min, y_min = -1, -1
    x_max, y_max = 1, 1
    direction = "east"
    counter = 0
    x_pos, y_pos = 0, 0

    while x_target != x_pos or y_target != y_pos:
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


@test.describe("Tests")
def tests():
    @test.it("Fixed Tests")
    def fixed_tests():
        test.assert_equals(squared_spiral(24, -17), 2215)
        test.assert_equals(squared_spiral(-92, -63), 34011)
        test.assert_equals(squared_spiral(41, -44), 7917)
        test.assert_equals(squared_spiral(-66, -93), 34809)
        test.assert_equals(squared_spiral(68, 13), 18305)
        test.assert_equals(squared_spiral(-24, 68), 18452)
        test.assert_equals(squared_spiral(-47, 53), 11230)
        test.assert_equals(squared_spiral(-55, -62), 15507)
        test.assert_equals(squared_spiral(10, 1), 371)
        test.assert_equals(squared_spiral(-21, 67), 17910)
        test.assert_equals(squared_spiral(-47, 56), 12535)
        test.assert_equals(squared_spiral(-75, 71), 22504)
        test.assert_equals(squared_spiral(50, 31), 9881)
        test.assert_equals(squared_spiral(8, -77), 23955)
        test.assert_equals(squared_spiral(-83, -1), 27640)
        test.assert_equals(squared_spiral(-15, -90), 32655)
        test.assert_equals(squared_spiral(77, 100), 39823)
        test.assert_equals(squared_spiral(23, -32), 4215)
        test.assert_equals(squared_spiral(-13, 73), 21256)
        test.assert_equals(squared_spiral(-39, -39), 6162)
        test.assert_equals(squared_spiral(58, 12), 13294)
        test.assert_equals(squared_spiral(-42, -21), 7119)
        test.assert_equals(squared_spiral(-97, 30), 37703)
        test.assert_equals(squared_spiral(-35, 31), 4904)
        test.assert_equals(squared_spiral(92, 8), 33588)
        test.assert_equals(squared_spiral(88, 27), 30739)
        test.assert_equals(squared_spiral(-80, 73), 25607)
        test.assert_equals(squared_spiral(64, -36), 16156)
        test.assert_equals(squared_spiral(-38, -57), 13129)
        test.assert_equals(squared_spiral(-97, -14), 37747)
        test.assert_equals(squared_spiral(-12, -68), 18688)
        test.assert_equals(squared_spiral(72, 60), 20580)
        test.assert_equals(squared_spiral(96, 31), 36607)
        test.assert_equals(squared_spiral(-93, -27), 34716)
        test.assert_equals(squared_spiral(4, -97), 37931)
        test.assert_equals(squared_spiral(91, 82), 32933)
        test.assert_equals(squared_spiral(16, 86), 29482)
        test.assert_equals(squared_spiral(-61, 48), 14897)
        test.assert_equals(squared_spiral(-73, -24), 21413)
        test.assert_equals(squared_spiral(-8, 90), 32318)
        test.assert_equals(squared_spiral(33, -47), 9010)
        test.assert_equals(squared_spiral(-79, 4), 25039)
        test.assert_equals(squared_spiral(12, -30), 3702)
        test.assert_equals(squared_spiral(-98, 26), 38488)
        test.assert_equals(squared_spiral(-78, 85), 28893)
        test.assert_equals(squared_spiral(26, -38), 5916)
        test.assert_equals(squared_spiral(62, 90), 32248)
        test.assert_equals(squared_spiral(37, -94), 35663)
        test.assert_equals(squared_spiral(6, 22), 1908)
        test.assert_equals(squared_spiral(-73, -25), 21414)
        test.assert_equals(squared_spiral(-48, 30), 9234)
        test.assert_equals(squared_spiral(50, 91), 32983)
        test.assert_equals(squared_spiral(-62, -20), 15458)
        test.assert_equals(squared_spiral(-24, -39), 6177)
        test.assert_equals(squared_spiral(-59, 82), 26873)
        test.assert_equals(squared_spiral(-27, -52), 10945)
        test.assert_equals(squared_spiral(10, -89), 31961)
        test.assert_equals(squared_spiral(-43, -63), 16022)
        test.assert_equals(squared_spiral(-67, 83), 27540)
        test.assert_equals(squared_spiral(21, -60), 14601)
        test.assert_equals(squared_spiral(-36, 32), 5188)
        test.assert_equals(squared_spiral(44, -33), 7579)
        test.assert_equals(squared_spiral(-54, -60), 14526)
        test.assert_equals(squared_spiral(87, 99), 39018)
        test.assert_equals(squared_spiral(-13, -95), 36372)
        test.assert_equals(squared_spiral(-74, -6), 21984)
        test.assert_equals(squared_spiral(93, 16), 34333)
        test.assert_equals(squared_spiral(-43, 36), 7403)
        test.assert_equals(squared_spiral(-10, 20), 1590)
        test.assert_equals(squared_spiral(35, 68), 18393)
        test.assert_equals(squared_spiral(29, -37), 5616)
        test.assert_equals(squared_spiral(-6, -90), 32664)
        test.assert_equals(squared_spiral(-20, -22), 1982)
        test.assert_equals(squared_spiral(-77, 12), 23781)
        test.assert_equals(squared_spiral(75, 44), 22319)
        test.assert_equals(squared_spiral(-88, -99), 39413)
        test.assert_equals(squared_spiral(-10, -8), 418)
        test.assert_equals(squared_spiral(-69, 76), 23097)
        test.assert_equals(squared_spiral(-32, -74), 22094)
        test.assert_equals(squared_spiral(-36, -98), 38674)
        test.assert_equals(squared_spiral(-89, -99), 39412)
        test.assert_equals(squared_spiral(49, -80), 25889)
        test.assert_equals(squared_spiral(-20, -74), 22106)
        test.assert_equals(squared_spiral(97, 12), 37357)
        test.assert_equals(squared_spiral(20, -33), 4475)
        test.assert_equals(squared_spiral(59, 56), 13803)
        test.assert_equals(squared_spiral(46, 96), 36722)
        test.assert_equals(squared_spiral(-28, -88), 31212)
        test.assert_equals(squared_spiral(35, -89), 31986)
        test.assert_equals(squared_spiral(-2, -58), 13628)
        test.assert_equals(squared_spiral(49, -13), 9444)
        test.assert_equals(squared_spiral(-63, -67), 18094)
        test.assert_equals(squared_spiral(65, -76), 23397)
        test.assert_equals(squared_spiral(66, -57), 17169)
        test.assert_equals(squared_spiral(46, 15), 8341)
        test.assert_equals(squared_spiral(96, 69), 36645)
        test.assert_equals(squared_spiral(83, 75), 27382)
        test.assert_equals(squared_spiral(33, -51), 10590)
        test.assert_equals(squared_spiral(-81, 3), 26322)
        test.assert_equals(squared_spiral(-91, 61), 33154)

    @test.it("Random Tests")
    def random_tests():
        for _ in range(0, 500):
            x = randint(-100, 100)
            y = randint(-100, 100)
            test.assert_equals(squared_spiral(x, y), squared_spiral_solution(x, y))
