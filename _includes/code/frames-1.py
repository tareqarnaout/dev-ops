import random
import math

def distance(x1, y1, x2, y2):
    xDiff = (x1 - x2) ** 2
    yDiff = (y1 - y2) ** 2
    return math.sqrt(xDiff + yDiff)

def area(cx, cy, px, py):
    r = distance(cx, cy, px, py)
    return math.pi * r ** 2

cx = random.randint(-100, 100)
cy = random.randint(-100, 100)
print("Center: (", cx, ", ", cy, ")")

px = random.randint(-100, 100)
py = random.randint(-100, 100)
print("Point: (", px, ",", py, ")")

a = area(cx, cy, px, py)
print("Area = ", a)