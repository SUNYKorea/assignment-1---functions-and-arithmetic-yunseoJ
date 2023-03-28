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
    arr = [[x1,y1, x2, y2],[x2,y2, x3, y3],[x3,y3, x1, y1]]
    result = 0
    for i in range(len(arr)):
        a,b,c,d = arr[i]
        result += dist(a,b,c,d) 
    

    return result

x1, x2, x3, y1, y2, y3 = 1, 3, 5, 2, 4, 6
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )