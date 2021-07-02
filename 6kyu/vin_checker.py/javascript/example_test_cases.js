const chai = require("chai");
const assert = chai.assert;

describe("Tests", function () {
  it("Fixed Tests", function () {
    assert.strictEqual(checkVin("5YJ3E1EA7HF000337"), true);
    assert.strictEqual(checkVin("5YJ3E1EAXHF000347"), true);
    assert.strictEqual(checkVin("5VGYMVUX7JV764512"), true);
    assert.strictEqual(checkVin("7WDMMTDV9TG739741"), false);
    assert.strictEqual(checkVin("7JTRH08L5EJ234829"), false);
  });
});
