const chai = require("chai");
const assert = chai.assert;

const squaredSpiralSolution = (n) => {
  let sqrt = Math.floor(Math.sqrt(n));
  let remaining = n - sqrt ** 2;

  let x;
  let y;

  if (sqrt % 2 == 0) {
    x = -Math.trunc(sqrt / 2) + Math.max(remaining - sqrt, 0);
    y = Math.trunc(sqrt / 2) - Math.min(remaining, sqrt);
  } else {
    x = Math.ceil(sqrt / 2) - Math.max(remaining - sqrt, 0);
    y = -Math.floor(sqrt / 2) + Math.min(remaining, sqrt);
  }

  return [x, y];
};

const randomTests = (tests_number, min_n, max_n) => {
  for (let i = 0; i < tests_number; i++) {
    let n = min_n + Math.floor(Math.random() * (max_n - min_n + 1));

    assert.deepEqual(squaredSpiral(n), squaredSpiralSolution(n));
  }
};

describe("Tests", function () {
  it("Small Numbers Fixed Tests", function () {
    assert.deepEqual(squaredSpiral(25155), [-46, -79]);
    assert.deepEqual(squaredSpiral(50264), [-112, 24]);
    assert.deepEqual(squaredSpiral(70713), [-90, 133]);
    assert.deepEqual(squaredSpiral(577), [-12, 11]);
    assert.deepEqual(squaredSpiral(63979), [97, -126]);
    assert.deepEqual(squaredSpiral(22890), [76, 14]);
    assert.deepEqual(squaredSpiral(42235), [98, 103]);
    assert.deepEqual(squaredSpiral(17885), [4, 67]);
    assert.deepEqual(squaredSpiral(33834), [-70, 92]);
    assert.deepEqual(squaredSpiral(81482), [143, 115]);
    assert.deepEqual(squaredSpiral(75915), [123, 138]);
    assert.deepEqual(squaredSpiral(46069), [-48, -107]);
    assert.deepEqual(squaredSpiral(18343), [68, 51]);
    assert.deepEqual(squaredSpiral(44362), [-53, -105]);
    assert.deepEqual(squaredSpiral(21785), [45, 74]);
    assert.deepEqual(squaredSpiral(35424), [-94, 14]);
    assert.deepEqual(squaredSpiral(83293), [-83, -144]);
    assert.deepEqual(squaredSpiral(10879), [-52, -11]);
    assert.deepEqual(squaredSpiral(92006), [152, 46]);
    assert.deepEqual(squaredSpiral(62774), [-101, -125]);
    assert.deepEqual(squaredSpiral(3481), [30, -29]);
    assert.deepEqual(squaredSpiral(36709), [59, 96]);
    assert.deepEqual(squaredSpiral(3995), [32, -5]);
    assert.deepEqual(squaredSpiral(34212), [80, -92]);
    assert.deepEqual(squaredSpiral(93363), [120, 153]);
    assert.deepEqual(squaredSpiral(81921), [-143, 18]);
    assert.deepEqual(squaredSpiral(76741), [139, -126]);
    assert.deepEqual(squaredSpiral(41085), [-22, -101]);
    assert.deepEqual(squaredSpiral(38089), [98, -33]);
    assert.deepEqual(squaredSpiral(80933), [-142, -135]);
    assert.deepEqual(squaredSpiral(7583), [44, -29]);
    assert.deepEqual(squaredSpiral(50763), [113, 26]);
    assert.deepEqual(squaredSpiral(63005), [126, -121]);
    assert.deepEqual(squaredSpiral(34967), [92, -93]);
    assert.deepEqual(squaredSpiral(44784), [54, 106]);
    assert.deepEqual(squaredSpiral(7772), [-44, 16]);
    assert.deepEqual(squaredSpiral(33203), [-91, 12]);
    assert.deepEqual(squaredSpiral(14104), [3, -59]);
    assert.deepEqual(squaredSpiral(28804), [11, 85]);
    assert.deepEqual(squaredSpiral(79014), [141, -87]);
    assert.deepEqual(squaredSpiral(85593), [-109, -146]);
    assert.deepEqual(squaredSpiral(81894), [-143, 45]);
    assert.deepEqual(squaredSpiral(61004), [119, -123]);
    assert.deepEqual(squaredSpiral(49812), [112, -28]);
    assert.deepEqual(squaredSpiral(27851), [46, -83]);
    assert.deepEqual(squaredSpiral(43255), [-95, 104]);
    assert.deepEqual(squaredSpiral(21450), [-73, -61]);
    assert.deepEqual(squaredSpiral(88045), [-15, -148]);
    assert.deepEqual(squaredSpiral(71021), [-133, -132]);
    assert.deepEqual(squaredSpiral(47596), [-109, 37]);
  });
  it("Large Numbers Fixed Tests", function () {
    assert.deepEqual(squaredSpiral(73675754793584), [-4291729, 735909]);
    assert.deepEqual(squaredSpiral(66288332443894), [-800448, -4070882]);
    assert.deepEqual(squaredSpiral(43199132314168), [-885554, -3286302]);
    assert.deepEqual(squaredSpiral(82359145702528), [-4102489, 4537597]);
    assert.deepEqual(squaredSpiral(35977848247785), [160854, 2999077]);
    assert.deepEqual(squaredSpiral(39369855261896), [-3137270, 86974]);
    assert.deepEqual(squaredSpiral(6007863262222), [-1225547, -239839]);
    assert.deepEqual(squaredSpiral(11661107483351), [-1707418, -869037]);
    assert.deepEqual(squaredSpiral(41615838749705), [-2306066, 3225517]);
    assert.deepEqual(squaredSpiral(22193157959304), [2355481, 2060303]);
    assert.deepEqual(squaredSpiral(54435586582743), [2018537, 3689024]);
    assert.deepEqual(squaredSpiral(82125255847302), [-2786949, -4531149]);
    assert.deepEqual(squaredSpiral(17846712873966), [2112269, -2102671]);
    assert.deepEqual(squaredSpiral(46617081944395), [-3413835, -901660]);
    assert.deepEqual(squaredSpiral(37862282969899), [2612240, 3076617]);
    assert.deepEqual(squaredSpiral(85338251002745), [-4618935, -4246910]);
    assert.deepEqual(squaredSpiral(82967050585952), [4554313, -3358985]);
    assert.deepEqual(squaredSpiral(3271573421279), [904375, -428096]);
    assert.deepEqual(squaredSpiral(32614377351262), [-1396712, 2855450]);
    assert.deepEqual(squaredSpiral(87151785892359), [-4667756, 3077541]);
    assert.deepEqual(squaredSpiral(81775328529550), [4521486, -498776]);
    assert.deepEqual(squaredSpiral(1642732712295), [640846, 251969]);
    assert.deepEqual(squaredSpiral(75532298629502), [-3946344, 4345466]);
    assert.deepEqual(squaredSpiral(8362467434403), [1445897, -766342]);
    assert.deepEqual(squaredSpiral(61403863897412), [-147599, 3918031]);
    assert.deepEqual(squaredSpiral(15983739292044), [1157939, -1998983]);
    assert.deepEqual(squaredSpiral(82739525491343), [3639278, -4548063]);
    assert.deepEqual(squaredSpiral(82647824367499), [2435817, -4545542]);
    assert.deepEqual(squaredSpiral(62485890730340), [-23537, 3952401]);
    assert.deepEqual(squaredSpiral(38780286993097), [-3113691, 2694518]);
    assert.deepEqual(squaredSpiral(19051083547448), [-480199, -2182377]);
    assert.deepEqual(squaredSpiral(28951145312991), [1090176, -2690313]);
    assert.deepEqual(squaredSpiral(36557189310422), [-3023127, 1145221]);
    assert.deepEqual(squaredSpiral(86012195031428), [-4344390, 4637138]);
    assert.deepEqual(squaredSpiral(94825875601327), [-2042092, 4868929]);
    assert.deepEqual(squaredSpiral(35266652105800), [2969287, -139815]);
    assert.deepEqual(squaredSpiral(64975373388963), [-4030365, -1225698]);
    assert.deepEqual(squaredSpiral(36312092624719), [1868609, 3012976]);
    assert.deepEqual(squaredSpiral(95782585727575), [-1108840, 4893429]);
    assert.deepEqual(squaredSpiral(72888835018634), [-1337366, 4268748]);
    assert.deepEqual(squaredSpiral(95821291924059), [4894418, -3627583]);
    assert.deepEqual(squaredSpiral(45014414291710), [-3354639, 344213]);
    assert.deepEqual(squaredSpiral(68109436178371), [-4126422, 2036387]);
    assert.deepEqual(squaredSpiral(62720291783740), [-3959807, -1914937]);
    assert.deepEqual(squaredSpiral(70828165325708), [4207974, -2789074]);
    assert.deepEqual(squaredSpiral(70157848620634), [-4188014, 624164]);
    assert.deepEqual(squaredSpiral(7100811216061), [-71796, -1332367]);
    assert.deepEqual(squaredSpiral(81397925718587), [-2703227, 4511040]);
    assert.deepEqual(squaredSpiral(9047922706079), [-1422461, -1503988]);
    assert.deepEqual(squaredSpiral(87267178112260), [-4670845, -1385315]);
  });

  it("Small Numbers Random Tests", function () {
    randomTests(500000, 0, 100000);
  });

  it("Large Numbers Random Tests", function () {
    randomTests(500000, 100000000000, 100000000000000);
  });
});
