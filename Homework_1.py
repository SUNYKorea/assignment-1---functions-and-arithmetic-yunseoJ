# Name: Yunseo Jang
# SBUID: 115265194
##################### SCORE ######################
####### good work with the variables and functions Score:  8/10
#################################################

# your output:
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/yunseoJ/Homework_1.py"
# Sweater
# The area of the triangle is : 0.0 , its perimeter is : 5.656854249492381 --> wrong
# The area of the polygon is : 27.527638409423474
# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
    F = fahrenheit
    celsius = (F - 32) * 5 / 9
    return celsius

def what_to_wear(celsius):
    a = int(celsius)
    if a < -10:
        print ("Puffy jacket")
    elif  -10 <= a < 0:
        print("Scarf")
    elif 0 <= a < 10: 
        print("Sweater")
    elif 10 <= a < 20:
        print("Light jacket")
    else:
        print("T-shirt")

  

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area1 = x1*y2 + x2*y3 + x3*y1
    area2 = x1*y3 + x2*y1 + x3*y2
    area = abs((area1 - area2) / 2)
    return area

def euclidean_distance(x1, y1, x2, y2):
    dx = (x1 - x2)**2
    dy = (y1 - y2)**2
    return (dx+dy)**0.5

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
#    P를 다 더한건 compute_triangle_periemter
    s1 = euclidean_distance(x1,y1,x2,y2)
    s2 = euclidean_distance(x2,y2,x3,y3)
    s3 = euclidean_distance(x3,y3,x1,y1)

    return s1+s2+s3

    

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

def deg2rad(deg):
    degree = (math.pi * int(deg)) / 180
    return degree

def apothem(number_sides, length_side):
    n = number_sides
    s = length_side
    d = deg2rad(180/n)
    a = s / (2 * math.tan(d))
    return a

def polygon_area(number_sides, length_side):
    n = number_sides
    s = length_side
    a = apothem(n, s)
    area = (n * s * a) / 2
    return area


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# # # Exercise 2 test
x1, x2, x3, y1, y2, y3 = 1, 2, 3, 4, 5, 6 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# # Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

