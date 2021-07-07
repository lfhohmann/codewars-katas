const chai = require("chai");
const assert = chai.assert;

describe("Tests", function () {
  it("Fixed Tests", function () {
    assert.deepEqual(squaredSpiral(0), [0, 0]);
    assert.deepEqual(squaredSpiral(6), [-1, -1]);
    assert.deepEqual(squaredSpiral(10), [2, 0]);
    assert.deepEqual(squaredSpiral(12), [2, 2]);
    assert.deepEqual(squaredSpiral(30), [3, 3]);
  });
});
