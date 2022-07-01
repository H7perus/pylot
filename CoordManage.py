import math


def coordinates_to_heading(coord0, coord1):

    y = math.cos(coord1[0]) * math.sin(coord1[1] - coord0[1])

    x = math.cos(coord0[0]) * math.sin(coord1[0]) \
        - math.sin(coord0[0]) * math.cos(coord1[0]) * math.cos(coord1[1] - coord0[1])
    #print(x)
    #print(y)
    return math.atan2(x, y)
