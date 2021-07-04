const squaredSpiral = (n) => {
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
