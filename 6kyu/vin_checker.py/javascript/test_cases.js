const chai = require("chai");
const assert = chai.assert;

const checkVinSolution = (vin) => {
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

describe("Tests", function () {
  it("Fixed Tests", function () {
    assert.strictEqual(checkVin("8WXSY7WGXBM122383"), false);
    assert.strictEqual(checkVin("5HVA1C6ZXPA702445"), false);
    assert.strictEqual(checkVin("9PTA00RSXWH373766"), false);
    assert.strictEqual(checkVin("2JLCKU0S0YS201096"), true);
    assert.strictEqual(checkVin("9CT44CXJ1YX220312"), true);
    assert.strictEqual(checkVin("2CMF0G5L0YY934298"), true);
    assert.strictEqual(checkVin("1EDJ41HV7KF326530"), true);
    assert.strictEqual(checkVin("7YKBSFVR5TB558565"), true);
    assert.strictEqual(checkVin("1WC4LYBR5RK874756"), false);
    assert.strictEqual(checkVin("4NFX5ENL7DZ525772"), false);
    assert.strictEqual(checkVin("9HFHWMGM9SJ251055"), true);
    assert.strictEqual(checkVin("2ND4T3XR6JE970967"), false);
    assert.strictEqual(checkVin("8GK2CA2Z5AP533424"), false);
    assert.strictEqual(checkVin("7BZBLLVU3EL130833"), false);
    assert.strictEqual(checkVin("5CD9L6EN2MD274698"), true);
    assert.strictEqual(checkVin("3DXES9JW1EC617032"), false);
    assert.strictEqual(checkVin("0FBGTR5W8SJ542701"), false);
    assert.strictEqual(checkVin("0PATLYXD3KN563510"), false);
    assert.strictEqual(checkVin("2NVA0P0U1RH390282"), false);
    assert.strictEqual(checkVin("1RJ181NB2YW962396"), false);
    assert.strictEqual(checkVin("5KHURLTN6WV528741"), true);
    assert.strictEqual(checkVin("9HZU4VSX5KZ031176"), false);
    assert.strictEqual(checkVin("4ZVDHPUE5GU902313"), true);
    assert.strictEqual(checkVin("4MPJVJFR8BE133105"), false);
    assert.strictEqual(checkVin("4WMRXMTH3UH477404"), true);
    assert.strictEqual(checkVin("3EX1AX0L3MD401068"), false);
    assert.strictEqual(checkVin("1HRGDNKV6KW009030"), true);
    assert.strictEqual(checkVin("1GJCSFME9RL741893"), false);
    assert.strictEqual(checkVin("2RJ2US2A2YM866441"), true);
    assert.strictEqual(checkVin("5SNSGG7J3HG195840"), false);
    assert.strictEqual(checkVin("5TFWJZRY7NC295902"), true);
    assert.strictEqual(checkVin("3CAX3M0K6LT045429"), true);
    assert.strictEqual(checkVin("6JR7WLDZ5KY347813"), true);
    assert.strictEqual(checkVin("7RT6CHNZ6UR879111"), false);
    assert.strictEqual(checkVin("8EY8R32Z5BP900335"), false);
    assert.strictEqual(checkVin("2WEXBRGC9EV007793"), true);
    assert.strictEqual(checkVin("5MVCBNPV0VK133335"), false);
    assert.strictEqual(checkVin("9APUFSRR4LR651580"), true);
    assert.strictEqual(checkVin("9AKW9JVDXEK773124"), true);
    assert.strictEqual(checkVin("2RTNZTMS1PF300432"), false);
    assert.strictEqual(checkVin("3VN6WLZCXYF160649"), true);
    assert.strictEqual(checkVin("0WSB2EJF4EA551323"), false);
    assert.strictEqual(checkVin("7HULRFML2NN052449"), false);
    assert.strictEqual(checkVin("7PCWX5XH9FA770620"), false);
    assert.strictEqual(checkVin("0ZHLWWER9GM375190"), true);
    assert.strictEqual(checkVin("5DNXY9JY8CY330511"), false);
    assert.strictEqual(checkVin("9FXTZ5WJ2SJ089810"), true);
    assert.strictEqual(checkVin("0YKRW2YH8FY749941"), true);
    assert.strictEqual(checkVin("4DPW34WE3SS635298"), true);
    assert.strictEqual(checkVin("5LHX7F3X9BN392785"), true);
    assert.strictEqual(checkVin("5SPY75RHXSU975422"), true);
    assert.strictEqual(checkVin("0EHPGMRL5WX755627"), false);
    assert.strictEqual(checkVin("8UJULT5G1MD021642"), false);
    assert.strictEqual(checkVin("7DK366JX3PW769277"), true);
    assert.strictEqual(checkVin("9RDYPZHEXPV151828"), false);
    assert.strictEqual(checkVin("5EU04R5HXLK426831"), false);
    assert.strictEqual(checkVin("4WWGM84FXRL740410"), true);
    assert.strictEqual(checkVin("0US61D4L9AE171645"), true);
    assert.strictEqual(checkVin("9YGHY7EM0MV549578"), true);
    assert.strictEqual(checkVin("5HANRTWY8PF983354"), true);
    assert.strictEqual(checkVin("4NHC2WAG0UA314353"), true);
    assert.strictEqual(checkVin("2WG6S9SU9MG931289"), false);
    assert.strictEqual(checkVin("3YCA9UHN4DY721532"), false);
    assert.strictEqual(checkVin("2BJDNKPN5DE741192"), true);
    assert.strictEqual(checkVin("9ZPXZKKB9YF533114"), false);
    assert.strictEqual(checkVin("1EBEL8PB7EJ190480"), true);
    assert.strictEqual(checkVin("3YFMYR6F1RE223376"), true);
    assert.strictEqual(checkVin("5JJ4NADK7ZJ820934"), false);
    assert.strictEqual(checkVin("4MLVDX8W5VH617971"), true);
    assert.strictEqual(checkVin("0XFZL67J7ED137485"), false);
    assert.strictEqual(checkVin("1ABX35KG1YL960657"), false);
    assert.strictEqual(checkVin("7WCKSELX6VY881492"), true);
    assert.strictEqual(checkVin("7WM32GWH8UW301041"), true);
    assert.strictEqual(checkVin("5YDVA8CX2FZ982675"), false);
    assert.strictEqual(checkVin("9KDTKHJB5FY853427"), true);
    assert.strictEqual(checkVin("2YARG4VK2UD441579"), false);
    assert.strictEqual(checkVin("6XC9UM2U3FY102840"), false);
    assert.strictEqual(checkVin("8RXZSJFH0GB226315"), false);
    assert.strictEqual(checkVin("2YZ10G8F9RV500411"), true);
    assert.strictEqual(checkVin("5PJ4NFEZ5TM096509"), true);
    assert.strictEqual(checkVin("5YKDTZHTXZC702519"), false);
    assert.strictEqual(checkVin("6HMFLHXR5LE678174"), true);
    assert.strictEqual(checkVin("3WT563UY1JK400016"), true);
    assert.strictEqual(checkVin("8XEK1KTM2VT430323"), false);
    assert.strictEqual(checkVin("8RTGTLAS0YM164115"), true);
    assert.strictEqual(checkVin("7NMWERNN6DH556919"), false);
    assert.strictEqual(checkVin("1GZV8X5N8PK825204"), true);
    assert.strictEqual(checkVin("0PBWT7ZS6AZ908765"), true);
    assert.strictEqual(checkVin("8RV5YSUE9KV688464"), false);
    assert.strictEqual(checkVin("8UZ15L8H1ZB381415"), false);
    assert.strictEqual(checkVin("9EW1YSAW8KC683168"), false);
    assert.strictEqual(checkVin("2SCBX68M4YT219238"), false);
    assert.strictEqual(checkVin("0JALKL0A5HE928657"), true);
    assert.strictEqual(checkVin("5LT1EBZB4VH073268"), true);
    assert.strictEqual(checkVin("2RVRJDMFXRV137976"), false);
    assert.strictEqual(checkVin("4WSAU06L4AE283417"), false);
    assert.strictEqual(checkVin("4MXS42FJ2KX935186"), true);
    assert.strictEqual(checkVin("8XNMUH2B2YN224631"), true);
    assert.strictEqual(checkVin("5LZ2DY3M4WM555132"), false);
    assert.strictEqual(checkVin("9DZWZBDYXFZ985146"), true);
  });

  it("Input Validation Tests", function () {
    assert.strictEqual(
      checkVin("0eejhf0m8lr011530"),
      false,
      "Lower case letters are invalid"
    );
    assert.strictEqual(
      checkVin("5YJ3E1EAXHF0I0347"),
      false,
      "'I' is an invalid char for a VIN"
    );
    assert.strictEqual(
      checkVin("5YJ3E1EAXHF0O0347"),
      false,
      "'O' is an invalid char for a VIN"
    );
    assert.strictEqual(
      checkVin("5YJ3E1EAXHF0Q0347"),
      false,
      "'Q' is an invalid char for a VIN"
    );
    assert.strictEqual(
      checkVin("9PTA00RSXWH3737000"),
      false,
      "VINs must be exactly 17 chars long"
    );
    assert.strictEqual(
      checkVin("9PTA00RSXWH37370"),
      false,
      "VINs must be exactly 17 chars long"
    );
  });
});
