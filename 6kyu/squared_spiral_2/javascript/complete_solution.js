const squaredSpiral = (x, y) => {
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
