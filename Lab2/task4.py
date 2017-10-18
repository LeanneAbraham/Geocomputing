import math

##Task 1, 2, 3, and  4
#create a function which returns inputed degrees, minutes,
#and seconds as decimal degrees
def dms2dd(d,m,s):
    #convert dms to dd
    
    #convert inputed values and add them together
    #to complete the converstion to a single value
    
    d = float(d)
    
    #ensure that if a negative degree is
    #used the other inputs are also negative
    if (d<0):
        m = float((m/60.0)*-1)
        s = float((s/3600.0)*-1)
    else:
        m = float(m/60.0)
        s = float(s/3600.0)
    
    #combine the converted values
    dd = s+m+d
    
    return dd

#function to convert decimal degrees to dms
def dd2dms(dd):
    
    #find the whole degrees and assign them to d
    d = int(math.floor(dd))
    
    #single out the remainder of the dd and convert to whole minutes
    remainder = dd-d
    m = int(math.floor(remainder*60.0))
    
    #find the remainder of the minutes and convert to seconds
    s = ((remainder*60)-m)*60
    
    #return the concatenated values
    return d, m, s


#add a main program that collects DD or DMS input from the user, then convert it to the other form and report the converted value
#create main function, allows program to be read into other programs

if __name__== "__main__":
    #request user input
    cord = input("Please enter a latitude or longitude value in DMS or DD format. ")
    #clean input string
    cordClean = cord.split(",")
    #return input as interger list
    results = list(map(float, cordClean))
        
    #test for dms or dd based on length of returned list
    if (len(results) > 1):
        #assign variables based on place in list
        d = results[0]
        m = results[1]
        s = results[2]
    
        print("\nThe input is in DMS form")
        #run through function to convert
        dd = dms2dd(d,m,s)
        print ("Its DD form is", dd)
        
    elif (len(results) == 1):
        print("\nThe input is in DD form")
        #convert
        dms = dd2dms(results[0])
        print ("Its DD form is", dms)


# Provided lists
city = ["Tokyo","New Delhi","Sao Paulo","Mumbai","Mexico City"]
population = [23.3,3.53,7.62,5.81,8.77]

#zip the two lists together using internal python function, convert to a dictonary
cityPop = dict(zip(city, population))
print(cityPop)
    
