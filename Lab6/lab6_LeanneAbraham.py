
import ogr
import gdalconst
import sys
import math

#create function to find distance between two points
def distance(lat1, lon1, lat2, lon2):

    #calculate the distance
    distance = math.sqrt((lat2 - lat1)**2+(lon2 - lon1)**2)

    return distance

#read in files
powerlinesFile = "./data/PowerLine.shp"
parcelsFile = "./data/Parcels.shp"

#get driver
driver = ogr.GetDriverByName("Esri Shapefile")

#open file
powerlines = driver.Open(powerlinesFile, gdalconst.GA_ReadOnly)
parcels = driver.Open(parcelsFile, gdalconst.GA_ReadOnly)

#make sure file was opened
if powerlines is None:
    print "Failed to open", powerlinesFile
    sys.exit()
if parcels is None:
    print "Failed to open", parcelsFile
    sys.exit()

#get data layer
powerLayer = powerlines.GetLayer(0)
parcelsLayer = parcels.GetLayer(0)

#get spatial reference
# print powerLayer.GetSpatialRef()

#get feature and geometry
powerFeature = powerLayer.GetFeature(0)
powerGeom = powerFeature.GetGeometryRef()

parcelFeature = parcelsLayer.GetFeature(0)
parcelGeom = parcelFeature.GetGeometryRef()

#find the number of points in the file
powerPointCount = powerGeom.GetPointCount()

coordinates = []

#find all point coordinates
for i in range(powerPointCount):
    x = powerGeom.GetX(i)
    y = powerGeom.GetY(i)
    coordinates.append([x,y])
    
length = 0

#find the distance between each point
for i in range(powerPointCount):
    j = i+1
    if j == 4:
        break
    else: 
        dist = distance(coordinates[i][0],coordinates[i][1],coordinates[j][0], coordinates[j][1])
        length = length+dist
        
#return the distance between all points in miles
print "My result: ",length/5280, "miles","\n"
#check against the results of the length method
print powerGeom.Length()/5280, "miles", "\n"

#Task 2

#print out the names of attribute data types of the layer,  not values!

parcelsDef = parcelsLayer.GetLayerDefn()

parcelAttribues = parcelsDef.GetFieldCount()

#get the info about each field
for i in range(0,parcelAttribues):
    attribute = parcelsDef.GetFieldDefn(i)
    fname       = attribute.GetNameRef()#gets the name of attribute field
    ftype       = attribute.GetType()#gets the int type of each field
    ftypeS      = attribute.GetFieldTypeName(ftype)#convert integer ftype to text equiv
    values      = (fname,ftypeS)
    print values

#find the number of indivdual parcels
parcelsLayerCount = parcelsLayer.GetFeatureCount()

#loop through the parcels and check to see if they intersect the powerline
for i in range(0,parcelsLayerCount): 
    #get the features of the parcels
    individualParcels = parcelsLayer.GetFeature(i)
    
    #access the geometry to check for intersection
    allParcelsGeom = individualParcels.GetGeometryRef()
    
    #if it does intersect, return the address and area
    if allParcelsGeom.Intersects(powerGeom):
        print "\n",individualParcels.GetField("SITUSADDR")
        print individualParcels.GetField("AREA")
    else:
        continue

#close files
powerlines = None
parcels = None

