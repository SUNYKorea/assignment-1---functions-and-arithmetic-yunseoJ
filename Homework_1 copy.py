# Name: Yunseo Jang
# SBUID: 115265194

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

# def fahrenheit2celsius(fahrenheit): 
#     F = fahrenheit
#     celsius = (F - 32) * 5 / 9
#     return celsius
    
# def what_to_wear(celsius):
#     a = int(celsius)
#     if a < -10:
#         print ("Puffy jacket")
#     if  -10 < a < 0:
#         print("Scarf")
#     if 0 < a < 20: 
#         print("Sweater")
#     else:
#         print("Light jacket")




            
# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area1 = x1*y2 + x2*y3 + x3*y1
    area2 = x1*y3 + x2*y1 + x3*y2
    Area = abs((area1 - area2) / 2)
    print (Area)
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
    

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


# def deg2rad(deg):
# #     import math
# #     pi = 22/7
# #     deg = 180 / pi

# def apothem(number_sides, length_side):
#     n = number_sides
#     s = length_side
#     import math
#     angle = 180/n
#     a = s / (2*tan(angle))

# def polygon_area(number_sides, length_side):
#     area = (n * s * a)/2


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
# fahrenheit = 40
# what_to_wear(fahrenheit2celsius(fahrenheit))

# # # Exercise 2 test
x1, x2, x3, y1, y2, y3 = 1, 2, 3, 4, 5, 6 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# # Exercise 3 test
# number_sides = 5
# length_side = 4
# print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

