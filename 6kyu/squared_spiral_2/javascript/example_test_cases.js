const chai = require("chai");
const assert = chai.assert;

describe("Tests", function () {
  it("Fixed Tests", function () {
    assert.strictEqual(squaredSpiral(0, 0), 0);
    assert.strictEqual(squaredSpiral(1, 1), 2);
    assert.strictEqual(squaredSpiral(2, 0), 10);
    assert.strictEqual(squaredSpiral(2, 2), 12);
    assert.strictEqual(squaredSpiral(3, 3), 30);
  });
});
