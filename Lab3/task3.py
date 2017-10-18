
import math

#create function to find distance between two points
def distance(lat1, lon1, lat2, lon2):
    
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
    return readableDistance


##########################
# Open the file to be read, it is in the same folder as the file
f = open('CityPop.csv',"r")

#create an empty containers to add all city data to
allCities = []
cityKey = []

#create year keys to search by


#set up a loop to cycle through entire csv
while True:
    #create a single line for each city as csv is looped through
    line = f.readline()
    
    #skip any empty lines
    if len(line) == 0:
        break
    
    #clean the data
    data = line.strip( ).split(",")

    
    #append just the city names to a seperate list
    cityKey.append(data[4])
    
    #create a list with all the city data
    allCities.append(data)

#combine into a dictonary with city names as keys
cityDict = dict(zip(cityKey,allCities))

#set up user query
city1 = input("Please enter a city ")
# city1 = "Mexico City"
city2 = input("Please enter a different city ")
# city2 = "Lima"

#return the list of attributes for requested cities
city1Info = cityDict.get(city1)
city2Info = cityDict.get(city2)

# convert lat lons to floating numbers
lat1 = float(city1Info[1])
lon1 = float(city1Info[2])
lat2 = float(city2Info[1])
lon2 = float(city2Info[2])

#tell user results
print ("The distance between", city1,"and",city2,"is",distance(lat1, lon1, lat2, lon2),"km")

#close csv
f.close()
