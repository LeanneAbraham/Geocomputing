print "This program tells where a place is relative to the equator\n"

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
            lat = float(input("Please enter the latitude of your location "))
            longitude = float(input("Please enter the longitude of your location "))

            #find and describe the relative location to the equator
            if (lat == 0):
                print "That location is on the equator."
            elif (lat > 0 and lat <= 90):
                print "That location is north of the equator."
            elif (lat >= -90 and lat < 0):
                print "That location is south of the equator."
            elif (lat < -90 and lat > 90):
                print "\nThat location does not have a valid latitude!"


            #find and describe the relative logitude to the prime meridian
            if (longitude == 0):
                print "That location is on the prime meridian."
            elif (longitude > 0 and lat <= 180):
                print "That location is east of the prime meridian."
            elif (longitude >= -180 and lat < 0):
                print "That location is west of the prime meridian."
            elif (longitude < -180 and lat > 180):
                print "\nThat location does not have a valid longitude!"
                
            else:
                print "Please enter a valid latitude and longitude\n"
                
        #stop the loop after receiving usable information
        break

    #provide the user with an error if they enter text
    except:
        print "\nYou must enter a number\n"
