# Line Crossing Area

In this Kata you should write a function that checks if a line segment is crossing or inside a rectangular area. The line segment is created by the (x,y) coordinates of two given points (p0,p1) and the rectangle (r) is created by the (x,y) coordinates of its center and width and height values. The function should return `True` if the line segment instersects the area and `False` otherwise.

![image](https://imgur.com/pJDSlm2.png)

The input is given by 2 parameters, parameter `rectangle` which is passed as a tuple in the format `(r_x, r_y, r_width, r_height)`. And the parameter `line` which is passed as a tuple of tuples in the format `((p0_x, p0_y),(p1_x, p1_y))`, the first tuple contains the (x,y) coordinates for point 0 (p0) and the second tuple contains the (x,y) coordinates for point 1 (p1).

### Note

A line segment touching one of the rectangle vertices should return `True`.
