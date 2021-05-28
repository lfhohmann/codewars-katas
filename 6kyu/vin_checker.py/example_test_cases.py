import codewars_test as test


@test.describe("Tests")
def tests():
    @test.it("Fixed Tests")
    def fixed_tests():
        test.assert_equals(check_vin("5YJ3E1EA7HF000337"), True)
        test.assert_equals(check_vin("5YJ3E1EAXHF000347"), True)
        test.assert_equals(check_vin("5VGYMVUX7JV764512"), True)
        test.assert_equals(check_vin("7WDMMTDV9TG739741"), False)
        test.assert_equals(check_vin("7JTRH08L5EJ234829"), False)
