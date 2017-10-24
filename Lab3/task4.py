import math

# Open the file to be read, it is in the same folder as the file
f = open('CityPop.csv',"r")

#f.readline() #headers

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

        
#create a function that calculates population change
def popChange(year1, year2):
    
    #ensure the value entered is a floating number
    year1 = float(year1)
    year2 = float(year2)
    
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

#function to check if user year is one listed in csv
def yearCheck(year):
    
    while True:
        #check to see if user supplied year is in the range of possible years
        if int(year) in range(1970, 2015, 5):
            break
        else:
            #prompt user to supply new year
            print("This is not a valid year")
            year  = input("Enter a different year ")


#prompt for input and check the input
year1 = input("Please enter a starting year ")

#check if year is in csv
yearCheck(year1)

#request second user input
year2 = input("Please enter an ending year ")

#check if year is in csv
yearCheck(year2)

#find corresponding place in the items() list in citDict
year1Index = popYear(year1)
year2Index = popYear(year2)

#use loop to calculate rate of change for each city
for key in cityDict:
    #check if it is the "header" row, create custom header
    if (key == "label"):
        x = "PopChange"
        
    #use popChange function to calculate eachthe rate of change
    else:
        #find the rate of change for the specified years based on predetermined index in the nested list
        x = popChange(cityDict[key][year1Index],cityDict[key][year2Index])
    
    #while looping through add in the new calculated value to attributes
    cityDict[key].append(x)

csv = []

#loop through the appended dict and sort to just show the the columns of interest and
#append the formated results to a new list
for key in cityDict:
    line = [cityDict[key][0],",",cityDict[key][4],",",cityDict[key][year1Index],",",cityDict[key][year2Index],",",str(cityDict[key][14]),"\n"]
    csv.append(line)

rows = []

#loop through the formated results to put everything into a single array (with linebreaks)
#that can then be written to the empty/new csv
for i in csv:
    for x in i:
        rows.append(x)
        
#create csv to write to
new = open('CityPopChg.csv', "w")

#write the now formatted single list to the csv
new.writelines(rows)
    
#close csv
new.close()

