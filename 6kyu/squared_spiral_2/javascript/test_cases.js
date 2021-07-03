const chai = require("chai");
const assert = chai.assert;

const squaredSpiralSolution = (x, y) => {
  let x_dist = 1;
  let y_dist = 1;

  let x_min = -1;
  let y_min = -1;
  let x_max = 1;
  let y_max = 1;

  let direction = "east";
  let counter = 0;
  let x_pos = 0;
  let y_pos = 0;

  while ((x != x_pos) | (y != y_pos)) {
    switch (direction) {
      case "east":
        x_pos++;

        if (x_pos == x_max) {
          direction = "north";
          y_max = y_pos + y_dist;
          x_dist++;
        }
        break;

      case "north":
        y_pos++;

        if (y_pos == y_max) {
          direction = "west";
          x_min = x_pos - x_dist;
          y_dist++;
        }
        break;

      case "west":
        x_pos--;

        if (x_pos == x_min) {
          direction = "south";
          y_min = y_pos - y_dist;
          x_dist++;
        }
        break;

      case "south":
        y_pos--;

        if (y_pos == y_min) {
          direction = "east";
          x_max = x_pos + x_dist;
          y_dist++;
        }
        break;
    }
    counter++;
  }

  return counter;
};

describe("Tests", function () {
  it("Fixed Tests", function () {
    assert.strictEqual(squaredSpiral(24, -17), 2215);
    assert.strictEqual(squaredSpiral(-92, -63), 34011);
    assert.strictEqual(squaredSpiral(41, -44), 7917);
    assert.strictEqual(squaredSpiral(-66, -93), 34809);
    assert.strictEqual(squaredSpiral(68, 13), 18305);
    assert.strictEqual(squaredSpiral(-24, 68), 18452);
    assert.strictEqual(squaredSpiral(-47, 53), 11230);
    assert.strictEqual(squaredSpiral(-55, -62), 15507);
    assert.strictEqual(squaredSpiral(10, 1), 371);
    assert.strictEqual(squaredSpiral(-21, 67), 17910);
    assert.strictEqual(squaredSpiral(-47, 56), 12535);
    assert.strictEqual(squaredSpiral(-75, 71), 22504);
    assert.strictEqual(squaredSpiral(50, 31), 9881);
    assert.strictEqual(squaredSpiral(8, -77), 23955);
    assert.strictEqual(squaredSpiral(-83, -1), 27640);
    assert.strictEqual(squaredSpiral(-15, -90), 32655);
    assert.strictEqual(squaredSpiral(77, 100), 39823);
    assert.strictEqual(squaredSpiral(23, -32), 4215);
    assert.strictEqual(squaredSpiral(-13, 73), 21256);
    assert.strictEqual(squaredSpiral(-39, -39), 6162);
    assert.strictEqual(squaredSpiral(58, 12), 13294);
    assert.strictEqual(squaredSpiral(-42, -21), 7119);
    assert.strictEqual(squaredSpiral(-97, 30), 37703);
    assert.strictEqual(squaredSpiral(-35, 31), 4904);
    assert.strictEqual(squaredSpiral(92, 8), 33588);
    assert.strictEqual(squaredSpiral(88, 27), 30739);
    assert.strictEqual(squaredSpiral(-80, 73), 25607);
    assert.strictEqual(squaredSpiral(64, -36), 16156);
    assert.strictEqual(squaredSpiral(-38, -57), 13129);
    assert.strictEqual(squaredSpiral(-97, -14), 37747);
    assert.strictEqual(squaredSpiral(-12, -68), 18688);
    assert.strictEqual(squaredSpiral(72, 60), 20580);
    assert.strictEqual(squaredSpiral(96, 31), 36607);
    assert.strictEqual(squaredSpiral(-93, -27), 34716);
    assert.strictEqual(squaredSpiral(4, -97), 37931);
    assert.strictEqual(squaredSpiral(91, 82), 32933);
    assert.strictEqual(squaredSpiral(16, 86), 29482);
    assert.strictEqual(squaredSpiral(-61, 48), 14897);
    assert.strictEqual(squaredSpiral(-73, -24), 21413);
    assert.strictEqual(squaredSpiral(-8, 90), 32318);
    assert.strictEqual(squaredSpiral(33, -47), 9010);
    assert.strictEqual(squaredSpiral(-79, 4), 25039);
    assert.strictEqual(squaredSpiral(12, -30), 3702);
    assert.strictEqual(squaredSpiral(-98, 26), 38488);
    assert.strictEqual(squaredSpiral(-78, 85), 28893);
    assert.strictEqual(squaredSpiral(26, -38), 5916);
    assert.strictEqual(squaredSpiral(62, 90), 32248);
    assert.strictEqual(squaredSpiral(37, -94), 35663);
    assert.strictEqual(squaredSpiral(6, 22), 1908);
    assert.strictEqual(squaredSpiral(-73, -25), 21414);
    assert.strictEqual(squaredSpiral(-48, 30), 9234);
    assert.strictEqual(squaredSpiral(50, 91), 32983);
    assert.strictEqual(squaredSpiral(-62, -20), 15458);
    assert.strictEqual(squaredSpiral(-24, -39), 6177);
    assert.strictEqual(squaredSpiral(-59, 82), 26873);
    assert.strictEqual(squaredSpiral(-27, -52), 10945);
    assert.strictEqual(squaredSpiral(10, -89), 31961);
    assert.strictEqual(squaredSpiral(-43, -63), 16022);
    assert.strictEqual(squaredSpiral(-67, 83), 27540);
    assert.strictEqual(squaredSpiral(21, -60), 14601);
    assert.strictEqual(squaredSpiral(-36, 32), 5188);
    assert.strictEqual(squaredSpiral(44, -33), 7579);
    assert.strictEqual(squaredSpiral(-54, -60), 14526);
    assert.strictEqual(squaredSpiral(87, 99), 39018);
    assert.strictEqual(squaredSpiral(-13, -95), 36372);
    assert.strictEqual(squaredSpiral(-74, -6), 21984);
    assert.strictEqual(squaredSpiral(93, 16), 34333);
    assert.strictEqual(squaredSpiral(-43, 36), 7403);
    assert.strictEqual(squaredSpiral(-10, 20), 1590);
    assert.strictEqual(squaredSpiral(35, 68), 18393);
    assert.strictEqual(squaredSpiral(29, -37), 5616);
    assert.strictEqual(squaredSpiral(-6, -90), 32664);
    assert.strictEqual(squaredSpiral(-20, -22), 1982);
    assert.strictEqual(squaredSpiral(-77, 12), 23781);
    assert.strictEqual(squaredSpiral(75, 44), 22319);
    assert.strictEqual(squaredSpiral(-88, -99), 39413);
    assert.strictEqual(squaredSpiral(-10, -8), 418);
    assert.strictEqual(squaredSpiral(-69, 76), 23097);
    assert.strictEqual(squaredSpiral(-32, -74), 22094);
    assert.strictEqual(squaredSpiral(-36, -98), 38674);
    assert.strictEqual(squaredSpiral(-89, -99), 39412);
    assert.strictEqual(squaredSpiral(49, -80), 25889);
    assert.strictEqual(squaredSpiral(-20, -74), 22106);
    assert.strictEqual(squaredSpiral(97, 12), 37357);
    assert.strictEqual(squaredSpiral(20, -33), 4475);
    assert.strictEqual(squaredSpiral(59, 56), 13803);
    assert.strictEqual(squaredSpiral(46, 96), 36722);
    assert.strictEqual(squaredSpiral(-28, -88), 31212);
    assert.strictEqual(squaredSpiral(35, -89), 31986);
    assert.strictEqual(squaredSpiral(-2, -58), 13628);
    assert.strictEqual(squaredSpiral(49, -13), 9444);
    assert.strictEqual(squaredSpiral(-63, -67), 18094);
    assert.strictEqual(squaredSpiral(65, -76), 23397);
    assert.strictEqual(squaredSpiral(66, -57), 17169);
    assert.strictEqual(squaredSpiral(46, 15), 8341);
    assert.strictEqual(squaredSpiral(96, 69), 36645);
    assert.strictEqual(squaredSpiral(83, 75), 27382);
    assert.strictEqual(squaredSpiral(33, -51), 10590);
    assert.strictEqual(squaredSpiral(-81, 3), 26322);
    assert.strictEqual(squaredSpiral(-91, 61), 33154);
  });

  it("Random Tests", function () {
    for (let i = 0; i < 500; i++) {
      let x = Math.floor(Math.random() * 200) - 100;
      let y = Math.floor(Math.random() * 200) - 100;

      assert.strictEqual(squaredSpiralSolution(x, y), squaredSpiral(x, y));
    }
  });
});
