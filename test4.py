def deg2rad(deg):
    import math
    degree = (math.pi*int(deg))/180
    return degree

def apothem(number_sides, length_side):
    n = number_sides
    s = length_side
    import math
    angle = 180/n
    a = s / (2*math.tan(angle))
    return a

def polygon_area(number_sides, length_side):
    n = number_sides
    s = length_side
    a = apothem(n, s)
    area = (n * s * a)/2
    return area

number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))
