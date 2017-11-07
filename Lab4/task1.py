#1st task
#REMEMBER, DONT NEED USER INPUT
#create class
class CityClass:
    def __init__(self, name, label, lat, lon, pop):
        #cname is the instance of the class
        self.cname = name
        self.clabel = label
        self.clat = lat
        self.clon = lon
        self.popValues = pop
    
#read file
try: 
    f = open("CityPop.csv", "r")
except: 
    print("Could not open the file")
    
#create empty list to populate with city instances 
Cities = []

#skip the header line by taking it out
header = f.readline()

#make a list of index numbers corresponding to the population in needed years years for later use
#this skips the first couple of non-population fields
yearIndex = list(range(5,14,1))

#make a list of available years
years = list(range(1970, 2015, 5))

#populate CityClass with attributes by reading in the csv
while True:
    line = f.readline()
    #skips the header line
    #stops the loop when finished reading the csv
    if len(line) == 0:
        break
    
    #clean the csv
    clist = line.strip().split(",")
    
    #create an empty list for the population numbers, then then populate it with csv values for each line
    population = []
    for i in yearIndex:
        population.append((clist[i]))
    
    #create dictonary to append to city class
    popValues = dict(zip(years, population))
    
    #create a city instance and attach attributes
    c = CityClass(clist[4], clist[3], clist[1], clist[2], popValues)
    
    #add instance to master list
    Cities.append(c)

f.close()


#printing out all attributes for all cities
for i in Cities:
    #print(i.__dict__)
    print(i.cname, i.clabel, i.clat, i.clon, i.popValues)

##### NOTES FROM LAB #####
# c2 = Cities[2]
# c1.printDistance(c2)
# c1.printPopChange('yr1990', "yr1995")

#getattr() This is a built in function that will
#retreive an attribute from an instance using the name of that attribute

#example
# cityname = getattr(c1, 'cname') #cname is because this is the name of the attribute in the class.
