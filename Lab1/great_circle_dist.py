import math

print "This program tells the distance between two points\n"

loopCount = 0

#the user has four chances to enter a lat long correctly
while loopCount<=4:

    #increase loop count for each iteration
    loopCount += 1

    try:

        #notifcation of program failure
        if (loopCount == 5):
            print "You failed to provide a readable latlong, cannot find location"

            #run program
        else:
            lat1 = float(input("Please enter the latitude of your 1st location "))
            lon1 = float(input("Please enter the longitude of your 1st location "))
            lat2 = float(input("\nPlease enter the latitude of your 2nd location "))
            lon2 = float(input("Please enter the longitude of your 2nd location "))

            #convert user inputs to radians and assign new value to variable
            lat1 = math.radians(lat1)
            lat2 = math.radians(lat2)
            lon1 = math.radians(lon1)
            lon2 = math.radians(lon2)

            #calculate the distance
            distance = math.acos((math.sin(lat1)*math.sin(lat2))+(math.cos(lat1)*math.cos(lat2)*math.cos((lon1-lon2))))

            #find the distance in km
            readableDistance = distance*6300
            #print
            print "\nYour points are", readableDistance, "km apart"

            #end loop
            break

    #provide the user with an error if they enter something other than a number
    except:
        print "\nYou must enter a number\n"
