# This program calculates the area of a triangle.

# This is a string that is printed when the program first runs,
#it tells you what the program does (ie, calculate the area of a triangle)
print "This program finds the area of a triangle."
print

# This portion of the program creates the two variables that will be used to calculate the area of the triangle
#based on numerical user input
height = input("Please enter the height of the triangle: ")
base = input("Please enter the base length of the triangle: ")

# This takes the user input of the base and the height of the triangle and finds the area (1/2bh)
area = 0.5 * height * base

# this writes the area in area in a readable sentance while reminding the user of their input
print "The area of a triangle with height", height, "and base", base, "is", area, "."
