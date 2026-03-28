import math

# (1) Read the coordinates of c (the center point)
print("Reading circle 1's center.")
cx = int(input("Enter x: "))
cy = int(input("Enter y: "))

# (2) Read the coordiantes of p (a point on the perimeter)
print("Reading a point on the perimeter of circle 1.")
px = int(input("Enter x: "))
py = int(input("Enter y: "))

# (3) Compute the distance between c and p to find the radius
xDiff = (cx - px) ** 2
yDiff = (cy - py) ** 2
r = math.sqrt(xDiff + yDiff)

# (4) Compute the area
a = math.pi * r ** 2

# (5) Print c, p, and the area
print("Center: (", cx, ", ", cy, ")")
print("Point: (", px, ",", py, ")")
print("Area 1 = ", a)

# (6) Read the coordinates of c (the center point)
print("Reading circle 2's center.")
cx = int(input("Enter x: "))
cy = int(input("Enter y: "))

# (7) Read the coordiantes of p (a point on the perimeter)
print("Reading a point on the perimeter of circle 2.")
px = int(input("Enter x: "))
py = int(input("Enter y: "))

# (8) Compute the distance between c and p to find the radius
xDiff = (cx - px) ** 2
yDiff = (cy - py) ** 2
r = math.sqrt(xDiff + yDiff)

# (9) Compute the area
a = math.pi * r ** 2

# (10) Print c, p, and the area
print("Center: (", cx, ", ", cy, ")")
print("Point: (", px, ",", py, ")")
print("Area 2 = ", a)