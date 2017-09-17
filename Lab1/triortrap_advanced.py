 # This program calculates the area of a triangle or trapezoid.

# This is a string that is printed when the program first runs,
#it tells you what the program does (ie, calculate the area of a triangle)
print "This program finds the area of a triangle or trapezoid."

#set loop count to zero and increase each time the loop is run (ie, the program conditions are unmet by the user input)
loopCount = 0
# The "while" statement keeps looping until its condition (loopCount<4) made False.
while loopCount<4:
    # loopCount will increase 1 for each loop
    loopCount += 1

    #find out if this is a triangle or a trapezoid
    shape = raw_input("Is this a triangle or a trapezoid? ")

    try:
        #check the user input
        if (shape == "triangle"):

            # find the base and the height of the triangle
            height = input("Please enter the height of the triangle: ")
            base = input("Please enter the base length of the triangle: ")

            # This takes the user input of the base and the height of the triangle and finds the area (1/2bh)
            area = 0.5 * height * base

            # this writes the area in area in a readable sentance while reminding the user of their input
            print "The area of this ", shape ," is ", area ," units."
            break

        elif (shape == "trapezoid"):
            # find the top base, bottom base, and height of the trapezoid
            height = input("Please enter the height of the trapezoid: ")
            b1 = input("Please enter the top base of the trapezoid: ")
            b2 = input ("Please enter the bottom base of the trapezoid: ")

            # This takes the user input of the top and bottom of the trapezoid and multiplies it by the height to find the area
            area = ((b1 + b2)+height)/2

            # this writes the area of the trapezoid in readable units
            print "The area of this ", shape ," is ", area ," units."
            break

        else :
            print "\nThis is not a shape"
            print 'please enter either "triangle" or "trapezoid" to continue\n'

    # If the user does not provide a triangle or a trapezoid the program will give them another chance
    # 	and continue to a new loop.
    #it never gets to this point becuase of the elif
    except:
        print 'nothing'
