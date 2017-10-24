import math

# Open the file to be read, it is in the same folder as the file
f = open('CityPop.csv',"r")

#f.readline() #headers

#create an empty containers to add all city data to
allCities = []
cityKey = []

#create year keys to search by

#read in 
#set up a loop to cycle through entire csv
while True:
    #create a single line for each city as csv is looped through
    line = f.readline()
    
    #skip any empty lines
    if len(line) == 0:
        break
    
    #clean the data
    data = line.strip().split(",")
    
    #append just the city names to a seperate list
    cityKey.append(data[4])
    
    #create a list with all the city data
    allCities.append(data)

#combine into a dictonary with city names as keys
cityDict = dict(zip(cityKey,allCities))


# create function to return correctly indexed year
def popYear(requestYear):
    #make sure input is int
    requestYear = int(requestYear)
    
    if requestYear == 1970:
        return 5
    if requestYear == 1975:
        return 6
    if requestYear == 1980:
        return 7
    if requestYear == 1985:
        return 8
    if requestYear == 1990:
        return 9
    if requestYear == 1995:
        return 10
    if requestYear == 2000:
        return 11
    if requestYear == 2005:
        return 12
    if requestYear == 2010:
        return 13

#set up user query
requestCity = raw_input("Please enter a city ")
# requestCity = "Mexico City"
requestYear = int(input("Please enter a year "))
# requestYear = 2010

year = popYear(requestYear)

#return the list of attributes for requested city
city1 = cityDict.get(requestCity)

#use 
population = float(city1[year])

#tell the user the results
print("The population of", requestCity, "in", requestYear, "was", population)

f.close()
