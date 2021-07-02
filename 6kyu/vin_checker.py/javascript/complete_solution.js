LETTERS = {
  A: 1,
  B: 2,
  C: 3,
  D: 4,
  E: 5,
  F: 6,
  G: 7,
  H: 8,
  J: 1,
  K: 2,
  L: 3,
  M: 4,
  N: 5,
  P: 7,
  R: 9,
  S: 2,
  T: 3,
  U: 4,
  V: 5,
  W: 6,
  X: 7,
  Y: 8,
  Z: 9,
};

WEIGHTS = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2];

const checkVin = (vin) => {
  if (vin.length != 17) {
    return false;
  }

  let sum = 0;

  for (let i = 0; i < vin.length; i++) {
    if (vin[i] in LETTERS) {
      sum += LETTERS[vin[i]] * WEIGHTS[i];
    } else if ((vin[i] >= 0) & (vin[i] <= 9)) {
      sum += vin[i] * WEIGHTS[i];
    } else {
      return false;
    }
  }

  let check_digit = sum % 11;

  if (check_digit == 10) {
    return vin[8] == "X";
  } else {
    return vin[8] == check_digit;
  }
};

let result = checkVin("7JTRH08L5EJ234829");

console.log(result);
