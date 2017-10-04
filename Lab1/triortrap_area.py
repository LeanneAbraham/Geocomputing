# This program calculates the area of a triangle or trapezoid.

# This is a string that is printed when the program first runs,
#it tells you what the program does (ie, calculate the area of a triangle)
print "This program finds the area of a triangle or trapezoid."
#find out if this is a triangle or a trapezoid
shape = raw_input("Is this a triangle or a trapezoid? ")

#check the user input
#code to find the area if its a triangle
if (shape == "triangle"):

    # find the base and the height of the triangle
    height = input("Please enter the height of the triangle: ")
    base = input("Please enter the base length of the triangle: ")

    # This takes the user input of the base and the height of the triangle and finds the area (1/2bh)
    area = 0.5 * height * base

    # this writes the area in area in a readable sentance while reminding the user of their input
    print "The area of this ", shape ," is ", area ," units."

#code for if its a trapezoid
elif (shape == "trapezoid"):
    # find the top base, bottom base, and height of the trapezoid
    height = input("Please enter the height of the trapezoid: ")
    b1 = input("Please enter the top base of the trapezoid: ")
    b2 = input ("Please enter the bottom base of the trapezoid: ")

    # This takes the user input of the top and bottom of the trapezoid and multiplies it by the height to find the area
    area = ((b1 + b2)+height)/2

    # this writes the area of the trapezoid in readable units
    print "The area of this ", shape ," is ", area ," units."

else :
    print "This is not a shape"

print "END"
