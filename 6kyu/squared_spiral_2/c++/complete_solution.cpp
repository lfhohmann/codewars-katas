int squaredSpiral(int x, int y)
{
    int xDist = 1;
    int yDist = 1;
    int xMin = -1;
    int yMin = -1;
    int xMax = 1;
    int yMax = 1;

    int xPos = 0;
    int yPos = 0;

    char direction = 'e';
    int counter = 0;

    while ((x != xPos) || (y != yPos))
    {
        if (direction == 'e')
        {
            xPos++;

            if (xPos == xMax)
            {
                direction = 'n';
                yMax = yPos + yDist;
                xDist++;
            }
        }
        else if (direction == 'n')
        {
            yPos++;

            if (yPos == yMax)
            {
                direction = 'w';
                xMin = xPos - xDist;
                yDist++;
            }
        }
        else if (direction == 'w')
        {
            xPos--;

            if (xPos == xMin)
            {
                direction = 's';
                yMin = yPos - yDist;
                xDist++;
            }
        }
        else if (direction == 's')
        {
            yPos--;

            if (yPos == yMin)
            {
                direction = 'e';
                xMax = xPos + xDist;
                yDist++;
            }
        }

        counter++;
    }

    return counter;
}