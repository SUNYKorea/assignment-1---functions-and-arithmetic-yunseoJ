def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area1 = x1*y2 + x2*y3 + x3*y1
    area2 = x1*y3 + x2*y1 + x3*y2
    area = abs((area1 - area2) / 2)
    return area

def dist(x1, y1, x2, y2):
    dx = (x1 - x2)**2
    dy = (y1-y2)**2
    return (dx+dy)**0.5

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
#    P를 다 더한건 compute_triangle_periemter
    s1 = dist(x1,y1,x2,y2)
    s2 = dist(x2,y2,x3,y3)
    s3 = dist(x3,y3,x1,y1)

    return s1+s2+s3

x1, x2, x3, y1, y2, y3 = 1, 2, 3, 4, 5, 6
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )