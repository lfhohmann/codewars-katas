import codewars_test as test
from random import choice


def vin_generator():
    LETTERS = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "M",
        "N",
        "P",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    structure = "NLLBBBBLCLLNNNNNN"
    chars = []

    for char in structure:
        if char == "N":
            chars.append(choice(NUMBERS))
        elif char == "L":
            chars.append(choice(LETTERS))
        elif char == "B":
            chars.append(choice(NUMBERS + LETTERS))
        elif char == "C":
            chars.append(choice(NUMBERS + ["X"]))

    return "".join(chars)


def check_vin_solution(number):
    LETTERS = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "J": 1,
        "K": 2,
        "L": 3,
        "M": 4,
        "N": 5,
        "P": 7,
        "R": 9,
        "S": 2,
        "T": 3,
        "U": 4,
        "V": 5,
        "W": 6,
        "X": 7,
        "Y": 8,
        "Z": 9,
    }

    WEIGHTS = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]

    if len(number) != 17:
        return False

    sum_ = 0

    for idx, char in enumerate(number):
        if char in LETTERS:
            sum_ += LETTERS[char] * WEIGHTS[idx]
        elif char in "01234567890":
            sum_ += int(char) * WEIGHTS[idx]
        else:
            return False

    check_digit = sum_ % 11

    if check_digit == 10:
        return number[8] == "X"

    return number[8] == str(check_digit)


@test.describe("Tests")
def tests():
    @test.it("Fixed Tests")
    def fixed_tests():
        test.assert_equals(check_vin("8WXSY7WGXBM122383"), False)
        test.assert_equals(check_vin("5HVA1C6ZXPA702445"), False)
        test.assert_equals(check_vin("9PTA00RSXWH373766"), False)
        test.assert_equals(check_vin("2JLCKU0S0YS201096"), True)
        test.assert_equals(check_vin("9CT44CXJ1YX220312"), True)
        test.assert_equals(check_vin("2CMF0G5L0YY934298"), True)
        test.assert_equals(check_vin("1EDJ41HV7KF326530"), True)
        test.assert_equals(check_vin("7YKBSFVR5TB558565"), True)
        test.assert_equals(check_vin("1WC4LYBR5RK874756"), False)
        test.assert_equals(check_vin("4NFX5ENL7DZ525772"), False)
        test.assert_equals(check_vin("9HFHWMGM9SJ251055"), True)
        test.assert_equals(check_vin("2ND4T3XR6JE970967"), False)
        test.assert_equals(check_vin("8GK2CA2Z5AP533424"), False)
        test.assert_equals(check_vin("7BZBLLVU3EL130833"), False)
        test.assert_equals(check_vin("5CD9L6EN2MD274698"), True)
        test.assert_equals(check_vin("3DXES9JW1EC617032"), False)
        test.assert_equals(check_vin("0FBGTR5W8SJ542701"), False)
        test.assert_equals(check_vin("0PATLYXD3KN563510"), False)
        test.assert_equals(check_vin("2NVA0P0U1RH390282"), False)
        test.assert_equals(check_vin("1RJ181NB2YW962396"), False)
        test.assert_equals(check_vin("5KHURLTN6WV528741"), True)
        test.assert_equals(check_vin("9HZU4VSX5KZ031176"), False)
        test.assert_equals(check_vin("4ZVDHPUE5GU902313"), True)
        test.assert_equals(check_vin("4MPJVJFR8BE133105"), False)
        test.assert_equals(check_vin("4WMRXMTH3UH477404"), True)
        test.assert_equals(check_vin("3EX1AX0L3MD401068"), False)
        test.assert_equals(check_vin("1HRGDNKV6KW009030"), True)
        test.assert_equals(check_vin("1GJCSFME9RL741893"), False)
        test.assert_equals(check_vin("2RJ2US2A2YM866441"), True)
        test.assert_equals(check_vin("5SNSGG7J3HG195840"), False)
        test.assert_equals(check_vin("5TFWJZRY7NC295902"), True)
        test.assert_equals(check_vin("3CAX3M0K6LT045429"), True)
        test.assert_equals(check_vin("6JR7WLDZ5KY347813"), True)
        test.assert_equals(check_vin("7RT6CHNZ6UR879111"), False)
        test.assert_equals(check_vin("8EY8R32Z5BP900335"), False)
        test.assert_equals(check_vin("2WEXBRGC9EV007793"), True)
        test.assert_equals(check_vin("5MVCBNPV0VK133335"), False)
        test.assert_equals(check_vin("9APUFSRR4LR651580"), True)
        test.assert_equals(check_vin("9AKW9JVDXEK773124"), True)
        test.assert_equals(check_vin("2RTNZTMS1PF300432"), False)
        test.assert_equals(check_vin("3VN6WLZCXYF160649"), True)
        test.assert_equals(check_vin("0WSB2EJF4EA551323"), False)
        test.assert_equals(check_vin("7HULRFML2NN052449"), False)
        test.assert_equals(check_vin("7PCWX5XH9FA770620"), False)
        test.assert_equals(check_vin("0ZHLWWER9GM375190"), True)
        test.assert_equals(check_vin("5DNXY9JY8CY330511"), False)
        test.assert_equals(check_vin("9FXTZ5WJ2SJ089810"), True)
        test.assert_equals(check_vin("0YKRW2YH8FY749941"), True)
        test.assert_equals(check_vin("4DPW34WE3SS635298"), True)
        test.assert_equals(check_vin("5LHX7F3X9BN392785"), True)
        test.assert_equals(check_vin("5SPY75RHXSU975422"), True)
        test.assert_equals(check_vin("0EHPGMRL5WX755627"), False)
        test.assert_equals(check_vin("8UJULT5G1MD021642"), False)
        test.assert_equals(check_vin("7DK366JX3PW769277"), True)
        test.assert_equals(check_vin("9RDYPZHEXPV151828"), False)
        test.assert_equals(check_vin("5EU04R5HXLK426831"), False)
        test.assert_equals(check_vin("4WWGM84FXRL740410"), True)
        test.assert_equals(check_vin("0US61D4L9AE171645"), True)
        test.assert_equals(check_vin("9YGHY7EM0MV549578"), True)
        test.assert_equals(check_vin("5HANRTWY8PF983354"), True)
        test.assert_equals(check_vin("4NHC2WAG0UA314353"), True)
        test.assert_equals(check_vin("2WG6S9SU9MG931289"), False)
        test.assert_equals(check_vin("3YCA9UHN4DY721532"), False)
        test.assert_equals(check_vin("2BJDNKPN5DE741192"), True)
        test.assert_equals(check_vin("9ZPXZKKB9YF533114"), False)
        test.assert_equals(check_vin("1EBEL8PB7EJ190480"), True)
        test.assert_equals(check_vin("3YFMYR6F1RE223376"), True)
        test.assert_equals(check_vin("5JJ4NADK7ZJ820934"), False)
        test.assert_equals(check_vin("4MLVDX8W5VH617971"), True)
        test.assert_equals(check_vin("0XFZL67J7ED137485"), False)
        test.assert_equals(check_vin("1ABX35KG1YL960657"), False)
        test.assert_equals(check_vin("7WCKSELX6VY881492"), True)
        test.assert_equals(check_vin("7WM32GWH8UW301041"), True)
        test.assert_equals(check_vin("5YDVA8CX2FZ982675"), False)
        test.assert_equals(check_vin("9KDTKHJB5FY853427"), True)
        test.assert_equals(check_vin("2YARG4VK2UD441579"), False)
        test.assert_equals(check_vin("6XC9UM2U3FY102840"), False)
        test.assert_equals(check_vin("8RXZSJFH0GB226315"), False)
        test.assert_equals(check_vin("2YZ10G8F9RV500411"), True)
        test.assert_equals(check_vin("5PJ4NFEZ5TM096509"), True)
        test.assert_equals(check_vin("5YKDTZHTXZC702519"), False)
        test.assert_equals(check_vin("6HMFLHXR5LE678174"), True)
        test.assert_equals(check_vin("3WT563UY1JK400016"), True)
        test.assert_equals(check_vin("8XEK1KTM2VT430323"), False)
        test.assert_equals(check_vin("8RTGTLAS0YM164115"), True)
        test.assert_equals(check_vin("7NMWERNN6DH556919"), False)
        test.assert_equals(check_vin("1GZV8X5N8PK825204"), True)
        test.assert_equals(check_vin("0PBWT7ZS6AZ908765"), True)
        test.assert_equals(check_vin("8RV5YSUE9KV688464"), False)
        test.assert_equals(check_vin("8UZ15L8H1ZB381415"), False)
        test.assert_equals(check_vin("9EW1YSAW8KC683168"), False)
        test.assert_equals(check_vin("2SCBX68M4YT219238"), False)
        test.assert_equals(check_vin("0JALKL0A5HE928657"), True)
        test.assert_equals(check_vin("5LT1EBZB4VH073268"), True)
        test.assert_equals(check_vin("2RVRJDMFXRV137976"), False)
        test.assert_equals(check_vin("4WSAU06L4AE283417"), False)
        test.assert_equals(check_vin("4MXS42FJ2KX935186"), True)
        test.assert_equals(check_vin("8XNMUH2B2YN224631"), True)
        test.assert_equals(check_vin("5LZ2DY3M4WM555132"), False)
        test.assert_equals(check_vin("9DZWZBDYXFZ985146"), True)

    @test.it("Edge Cases")
    def fixed_tests():
        test.assert_equals(
            check_vin("0eejhf0m8lr011530"), False, "Lower case letters are invalid"
        )
        test.assert_equals(
            check_vin("5YJ3E1EAXHF0I0347"), False, "'I' is an invalid char for a VIN"
        )
        test.assert_equals(
            check_vin("5YJ3E1EAXHF0O0347"), False, "'O' is an invalid char for a VIN"
        )
        test.assert_equals(
            check_vin("5YJ3E1EAXHF0Q0347"), False, "'Q' is an invalid char for a VIN"
        )
        test.assert_equals(
            check_vin("9PTA00RSXWH3737000"), False, "VINs must be exactly 17 chars long"
        )
        test.assert_equals(
            check_vin("9PTA00RSXWH37370"), False, "VINs must be exactly 17 chars long"
        )

    @test.it("Random Tests")
    def random_tests():
        for _ in range(100):
            vin = vin_generator()
            test.assert_equals(check_vin(vin), check_vin_solution(vin))
