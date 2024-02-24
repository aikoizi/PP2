import math

def area(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area
num_sides = int(input())
side_length = int(input())
polygon_area = area(num_sides, side_length)
print("The area of the polygon is:", polygon_area)



