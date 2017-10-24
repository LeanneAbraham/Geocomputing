import math

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
    data = line.strip().split(",")
    
    #append just the city names to a seperate list
    cityKey.append(data[4])
    
    #create a list with all the city data
    allCities.append(data)

#combine into a dictonary with city names as keys
cityDict = dict(zip(cityKey,allCities))
    


# In[3]:


# create function to return correctly indexed year
def popYear(requestYear):
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

#function to check if user year is one listed in csv
def yearCheck(year):
    year = str(year)
    count = 0
    
    while count < len(cleanYear):
        #check to see if the entered year is one in the csv
        #if the year is valid, break the loop and move on
        if year == cleanYear[count]:
            break
        #if the loop goes through all possible years without finding a match,
        #give the user a second chance
        elif count == 13:
            print("This is not a valid year, please try again")
            break
        #if a match isn't found try again
        elif year != cleanYear[count]:
            count = count+1
            pass
        
#create a function that calculates population change
def popChange(year1, year2):
    #remove year letters
    year1 = year1.replace("yr","")
    year2 = year2.replace("yr","")
    #ensure number
    year1 = float(year1)
    year2 = float(year2)
    
    #prevent dividing by zero
    if (year1, year2 == 0):
        return 1
    
    #calculate the rate of change
    roc = ((year2-year1)/year1)*100
    return roc

#create function that iterates over all items at a specified index in dictonary for each key and returns a value
def indexMatch(input):
    for key in cityDict:
        print(cityDict[key][input])


# In[113]:


#set up user query
requestCity = input("Please enter a city ")
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


# In[114]:


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


# In[5]:


#create empty list to push cleaned years into for later use
cleanYear = []
for i in cityDict["label"]:
    #loop through to remove the yr suffix
    x = i.replace("yr","")
    #push the cleaned variables to their own list
    cleanYear.append(x)

#check the user input
year1 = 1970
# year1 = input("Please enter a starting year ")
#check if year is in csv
yearCheck(year1)

year2 = 2010
# year2 = input("Please enter an ending year ")
#check if year is in csv
yearCheck(year2)

year1Index = popYear(year1)
year2Index = popYear(year2)

#create empty lists to hold the starting values and ending values, indexed by corresponding city
# startPop = []
# endPop = []

        
# for i in allCities:
    
#     x = i[year1Index]
#     startPop.append(x)
    
#     #repeat for end year
#     y = i[year2Index]
#     endPop.append(y)

#create csv to write to
new = open('CityyPopChg.csv', "w")

#create empty list for change values
change = []

#loop over start and end pop lists, use PopChange function to find rate of change between the two years
index = 1

for key in cityDict:
    print(cityDict[key][year1Index])
    x = float(popChange(cityDict[key][year1Index],cityDict[key][year2Index]))
#     print (x)
    
    csvRow = (cityDict[key]).append(x)
#     print (csvRow)
#     new.writelines()
#     print(startPop[index])

# #     change.append(x)
    index = index + 1
    
# for key in cityDict:
#     print(cityDict[key])

    
# cityChange = cityDict + {"percentChange":popChange(startPop[index],endPop[index])}

