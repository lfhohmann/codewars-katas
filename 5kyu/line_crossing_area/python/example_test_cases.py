import codewars_test as test


@test.describe("Tests")
def tests():
    @test.it("Fixed Tests")
    def fixed_tests():
        test.assert_equals(line_crossing_area((0, 0, 10, 10), ((-3, -4), (5, 6))), True)
        test.assert_equals(
            line_crossing_area((-10, 20, 30, 40), ((-100, 100), (10, -10))), True
        )
        test.assert_equals(
            line_crossing_area((100, 100, 10, 20), ((-100, -100), (-101, 100))), False
        )
        test.assert_equals(
            line_crossing_area((0, 100, 200, 10), ((-500, -500), (-400, -400))), False
        )
        test.assert_equals(
            line_crossing_area((0, 100, 200, 10), ((-50, 50), (25, 25))), False
        )
