# Line Crossing Area

In this Kata you should write a function that checks if a line is crossing or inside a rectangular area. The line is created by the (x,y) coordinates of two given points (p0,p1) and the rectangle (r) is created by the (x,y) coordinates of its center and width and height values. The function should return `True` if the line instersects the area and `False` otherwise.

![asdf](https://imgur.com/pJDSlm2.png)

The input is given by 2 parameters, parameter `rectangle` which is passed as a tuple in the format `(r_x, r_y, r_width, r_height)`. And the parameter `line` which is passed as a tuple of tuples in the format `((p0_x, p0_y),(p1_x, p1_y))`, the first tuple contains the (x,y) coordinates for point 0 (p0) and the second tuple contains the (x,y) coordinates for point 1 (p1).

### Note

All passed parameters are valid, there is no need to check them.