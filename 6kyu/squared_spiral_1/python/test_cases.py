import codewars_test as test
import random

import math


def squared_spiral_solution(n):

    sqrt = math.floor(math.sqrt(n))
    remaining = n - (sqrt ** 2)

    if sqrt % 2 == 0:
        x = -int(sqrt / 2) + max(remaining - sqrt, 0)
        y = int(sqrt / 2) - min(remaining, sqrt)

    else:
        x = math.ceil(sqrt / 2) - max(remaining - sqrt, 0)
        y = -math.floor(sqrt / 2) + min(remaining, sqrt)

    return x, y


def random_tests(tests, min_n, max_n):
    for _ in range(tests):
        n = random.randint(min_n, max_n)

        expected = squared_spiral_solution(n)
        actual = squared_spiral(n)

        if actual != expected:
            test.assert_equals(actual, expected)
            break

    else:
        test.pass_()


@test.describe("Tests")
def tests():
    @test.it("Small Numbers Fixed Tests")
    def small_numbers_fixed_tests():
        test.assert_equals(squared_spiral(25155), (-46, -79))
        test.assert_equals(squared_spiral(50264), (-112, 24))
        test.assert_equals(squared_spiral(70713), (-90, 133))
        test.assert_equals(squared_spiral(577), (-12, 11))
        test.assert_equals(squared_spiral(63979), (97, -126))
        test.assert_equals(squared_spiral(22890), (76, 14))
        test.assert_equals(squared_spiral(42235), (98, 103))
        test.assert_equals(squared_spiral(17885), (4, 67))
        test.assert_equals(squared_spiral(33834), (-70, 92))
        test.assert_equals(squared_spiral(81482), (143, 115))
        test.assert_equals(squared_spiral(75915), (123, 138))
        test.assert_equals(squared_spiral(46069), (-48, -107))
        test.assert_equals(squared_spiral(18343), (68, 51))
        test.assert_equals(squared_spiral(44362), (-53, -105))
        test.assert_equals(squared_spiral(21785), (45, 74))
        test.assert_equals(squared_spiral(35424), (-94, 14))
        test.assert_equals(squared_spiral(83293), (-83, -144))
        test.assert_equals(squared_spiral(10879), (-52, -11))
        test.assert_equals(squared_spiral(92006), (152, 46))
        test.assert_equals(squared_spiral(62774), (-101, -125))
        test.assert_equals(squared_spiral(3481), (30, -29))
        test.assert_equals(squared_spiral(36709), (59, 96))
        test.assert_equals(squared_spiral(3995), (32, -5))
        test.assert_equals(squared_spiral(34212), (80, -92))
        test.assert_equals(squared_spiral(93363), (120, 153))
        test.assert_equals(squared_spiral(81921), (-143, 18))
        test.assert_equals(squared_spiral(76741), (139, -126))
        test.assert_equals(squared_spiral(41085), (-22, -101))
        test.assert_equals(squared_spiral(38089), (98, -33))
        test.assert_equals(squared_spiral(80933), (-142, -135))
        test.assert_equals(squared_spiral(7583), (44, -29))
        test.assert_equals(squared_spiral(50763), (113, 26))
        test.assert_equals(squared_spiral(63005), (126, -121))
        test.assert_equals(squared_spiral(34967), (92, -93))
        test.assert_equals(squared_spiral(44784), (54, 106))
        test.assert_equals(squared_spiral(7772), (-44, 16))
        test.assert_equals(squared_spiral(33203), (-91, 12))
        test.assert_equals(squared_spiral(14104), (3, -59))
        test.assert_equals(squared_spiral(28804), (11, 85))
        test.assert_equals(squared_spiral(79014), (141, -87))
        test.assert_equals(squared_spiral(85593), (-109, -146))
        test.assert_equals(squared_spiral(81894), (-143, 45))
        test.assert_equals(squared_spiral(61004), (119, -123))
        test.assert_equals(squared_spiral(49812), (112, -28))
        test.assert_equals(squared_spiral(27851), (46, -83))
        test.assert_equals(squared_spiral(43255), (-95, 104))
        test.assert_equals(squared_spiral(21450), (-73, -61))
        test.assert_equals(squared_spiral(88045), (-15, -148))
        test.assert_equals(squared_spiral(71021), (-133, -132))
        test.assert_equals(squared_spiral(47596), (-109, 37))

    @test.it("Large Numbers Fixed Tests")
    def large_numbers_fixed_tests():
        test.assert_equals(squared_spiral(73675754793584), (-4291729, 735909))
        test.assert_equals(squared_spiral(66288332443894), (-800448, -4070882))
        test.assert_equals(squared_spiral(43199132314168), (-885554, -3286302))
        test.assert_equals(squared_spiral(82359145702528), (-4102489, 4537597))
        test.assert_equals(squared_spiral(35977848247785), (160854, 2999077))
        test.assert_equals(squared_spiral(39369855261896), (-3137270, 86974))
        test.assert_equals(squared_spiral(6007863262222), (-1225547, -239839))
        test.assert_equals(squared_spiral(11661107483351), (-1707418, -869037))
        test.assert_equals(squared_spiral(41615838749705), (-2306066, 3225517))
        test.assert_equals(squared_spiral(22193157959304), (2355481, 2060303))
        test.assert_equals(squared_spiral(54435586582743), (2018537, 3689024))
        test.assert_equals(squared_spiral(82125255847302), (-2786949, -4531149))
        test.assert_equals(squared_spiral(17846712873966), (2112269, -2102671))
        test.assert_equals(squared_spiral(46617081944395), (-3413835, -901660))
        test.assert_equals(squared_spiral(37862282969899), (2612240, 3076617))
        test.assert_equals(squared_spiral(85338251002745), (-4618935, -4246910))
        test.assert_equals(squared_spiral(82967050585952), (4554313, -3358985))
        test.assert_equals(squared_spiral(3271573421279), (904375, -428096))
        test.assert_equals(squared_spiral(32614377351262), (-1396712, 2855450))
        test.assert_equals(squared_spiral(87151785892359), (-4667756, 3077541))
        test.assert_equals(squared_spiral(81775328529550), (4521486, -498776))
        test.assert_equals(squared_spiral(1642732712295), (640846, 251969))
        test.assert_equals(squared_spiral(75532298629502), (-3946344, 4345466))
        test.assert_equals(squared_spiral(8362467434403), (1445897, -766342))
        test.assert_equals(squared_spiral(61403863897412), (-147599, 3918031))
        test.assert_equals(squared_spiral(15983739292044), (1157939, -1998983))
        test.assert_equals(squared_spiral(82739525491343), (3639278, -4548063))
        test.assert_equals(squared_spiral(82647824367499), (2435817, -4545542))
        test.assert_equals(squared_spiral(62485890730340), (-23537, 3952401))
        test.assert_equals(squared_spiral(38780286993097), (-3113691, 2694518))
        test.assert_equals(squared_spiral(19051083547448), (-480199, -2182377))
        test.assert_equals(squared_spiral(28951145312991), (1090176, -2690313))
        test.assert_equals(squared_spiral(36557189310422), (-3023127, 1145221))
        test.assert_equals(squared_spiral(86012195031428), (-4344390, 4637138))
        test.assert_equals(squared_spiral(94825875601327), (-2042092, 4868929))
        test.assert_equals(squared_spiral(35266652105800), (2969287, -139815))
        test.assert_equals(squared_spiral(64975373388963), (-4030365, -1225698))
        test.assert_equals(squared_spiral(36312092624719), (1868609, 3012976))
        test.assert_equals(squared_spiral(95782585727575), (-1108840, 4893429))
        test.assert_equals(squared_spiral(72888835018634), (-1337366, 4268748))
        test.assert_equals(squared_spiral(95821291924059), (4894418, -3627583))
        test.assert_equals(squared_spiral(45014414291710), (-3354639, 344213))
        test.assert_equals(squared_spiral(68109436178371), (-4126422, 2036387))
        test.assert_equals(squared_spiral(62720291783740), (-3959807, -1914937))
        test.assert_equals(squared_spiral(70828165325708), (4207974, -2789074))
        test.assert_equals(squared_spiral(70157848620634), (-4188014, 624164))
        test.assert_equals(squared_spiral(7100811216061), (-71796, -1332367))
        test.assert_equals(squared_spiral(81397925718587), (-2703227, 4511040))
        test.assert_equals(squared_spiral(9047922706079), (-1422461, -1503988))
        test.assert_equals(squared_spiral(87267178112260), (-4670845, -1385315))

    @test.it("Small Numbers Random Tests")
    def small_numbers_random_tests():
        random_tests(500_000, 0, 100_000)

    @test.it("Large Numbers Random Tests")
    def large_numbers_random_tests():
        random_tests(500_000, 100_000_000_000, 100_000_000_000_000)
