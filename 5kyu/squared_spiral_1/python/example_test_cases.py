import codewars_test as test


@test.describe("Tests")
def tests():
    @test.it("Fixed Tests")
    def fixed_tests():
        test.assert_equals(squared_spiral(0), (0, 0))
        test.assert_equals(squared_spiral(6), (-1, -1))
        test.assert_equals(squared_spiral(10), (2, 0))
        test.assert_equals(squared_spiral(12), (2, 2))
        test.assert_equals(squared_spiral(30), (3, 3))
