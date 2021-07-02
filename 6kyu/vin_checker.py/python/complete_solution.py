from random import choice, shuffle

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


def check_vin(number):
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
