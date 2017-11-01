#REMEMBER, DONT NEED USER INPUT
import math

import matplotlib.pyplot as plt

import numpy as np

#create class
class CityClass:
    def __init__(self, name, label, lat, lon, pop):
        #cname is the instance of the class
        self.cname = name
        self.clabel = label
        self.clat = lat
        self.clon = lon
        self.popValues = pop

    def printDistance(self, otherCity):
        #create function to find distance between two points

            #convert user inputs to radians and assign new value to variable
            lat1 = math.radians(float(self.clat))
            lat2 = math.radians(float(otherCity.clat))
            lon1 = math.radians(float(self.clon))
            lon2 = math.radians(float(otherCity.clon))
            
            #calculate the distance
            distance = math.acos((math.sin(lat1)*math.sin(lat2))+(math.cos(lat1)*math.cos(lat2)*math.cos((lon1-lon2))))

            #find the distance in km
            readableDistance = distance*6300
            #print
            return readableDistance
        
    #create a function that calculates population change
    def printPopChange(self, year1, year2):

        #ensure the value entered is a floating number
        year1 = self.popValues[year1]
        year2 = self.popValues[year2]

        #prevent dividing by zero
        try:
            #calculate the rate of change
            roc = (((year2-year1)/year1)*100)
            return roc

        #if there is an attempt to divide by zero, set value to NaN instead
        except:
            print("there was an attempt to divide by zero")
            roc = "NaN"
            return roc


#read file
try: 
    f = open("CityPop.csv", "r")
except: 
    print("Could not open the file")
    
#create empty list to populate with city instances 
Cities = []

#skip the header line by taking it out
header = f.readline()

#make a list of population index numbers years for later use
yearIndex = list(range(5,14,1))

#make a list of available years
years = list(range(1970, 2015, 5))

#populate CityClass with attributes by reading in the csv
while True:
    line = f.readline()
    #skip the header line
    if len(line) == 0:
        break
    #clean the csv
    clist = line.strip().split(",")
    
    #create an empty list for the population numbers, then 
    population = []
    for i in yearIndex:
        population.append(float(clist[i]))
    
    #create dictonary to append to city class
    popValues = dict(zip(years, population))
    
    #create a city instance and attach attributes
    c = CityClass(clist[4], clist[3], clist[1], clist[2], popValues)
    
    #add instance to master list
    Cities.append(c)

f.close()

#create two test city variables
c1 = Cities[2]
c2 = Cities[38]

#Task 3

#plot the population changes for two cities, ignoring zeros
#make the values of the two city years regular lists
p1 = list(c1.popValues.values())
p2 = list(c2.popValues.values())
 
#sort the resulting lists
p1.sort()
p2.sort()

plt.plot(years,p1)
plt.plot(years,p2)

#create the axis labels
#find min and max for the labels
c1Min = (min(c1.popValues.values()))
c1Max = (max(c1.popValues.values()))

c2Min = (min(c2.popValues.values()))
c2Max = (max(c2.popValues.values()))

if c1Max > c2Max:
    ymax = c1Max
else:
    ymax = c2Max
    
#create correctly labeled axis
plt.axis([min(years), max(years), 0, ymax+5])
plt.xlabel("Years")
plt.ylabel("Population (in Millions)")

#create the legend
plt.legend([c1.cname, c2.cname], loc='upper left')

#display the line graph
plt.show()

