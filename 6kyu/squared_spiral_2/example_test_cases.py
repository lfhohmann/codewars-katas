import codewars_test as test


@test.describe("Tests")
def tests():
    @test.it("Fixed Tests")
    def fixed_tests():
        test.assert_equals(squared_spiral(0, 0), 0)
        test.assert_equals(squared_spiral(1, 1), 2)
        test.assert_equals(squared_spiral(2, 0), 10)
        test.assert_equals(squared_spiral(2, 2), 12)
        test.assert_equals(squared_spiral(3, 3), 30)
