## Task 2 ##
import arcpy
import os
arcpy.CheckOutExtension("Spatial")

#set workspace to lab folder
arcpy.env.workspace =  r"C:\Users\lfabr\OneDrive - UW-Madison\School\Madison\courses\2017-03-Fall\GEOG 378\labs\Lab7\data"
#ensure that new files can be overwritten as the code is run
arcpy.env.overwriteOutput = True

#calculate slope,
#set the inraster to the eleveation dem
inraster = arcpy.Raster("elevation.tif")

#calculate slope using this dem
outraster = arcpy.sa.Slope("elevation.tif")

#save the new slope raster file by specifying what the new raster is called
outraster.save(r"C:\Users\lfabr\OneDrive - UW-Madison\School\Madison\courses\2017-03-Fall\GEOG 378\labs\Lab7\data\slope.tif")

#use arcpy to read this raster as a variable that can be used in further code
slope = arcpy.Raster('slope.tif')

#get min and max by first calculating the stats on the raster
arcpy.CalculateStatistics_management(slope)
MINResult = arcpy.GetRasterProperties_management(slope, "MINIMUM")

#make sure the value can be divided by, ie, its float
zMin = float(MINResult.getOutput(0))
MAXResult = arcpy.GetRasterProperties_management(slope, "MAXIMUM")
zMax = float(MAXResult.getOutput(0))


# create output file
output = 'SlopeColored.tif'

#remove raster if it already exists
if os.path.exists(output):
     os.remove(output)

#create new raster of scaled elevations
f = ((slope-zMin)/(zMax-zMin))

#create the red raster
#ensure red values are somewhere between 0 and 255
R = (255*slope)/slope

#green and blue raster values are identical, makes a red raster
G = 255*f
B = 255*f

#Compose single band datasets to a TIFF format raster file
arcpy.CompositeBands_management(str(R)+';'+str(G)+';'+str(B),output)

print 'program finished'
