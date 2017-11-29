import arcpy
import os
arcpy.CheckOutExtension("Spatial")

arcpy.env.workspace = 'c:\data'


# describe raster
desc = arcpy.Describe('elevation.tif')
print desc.bandCount
print desc.compressionType
print desc.format
rows = desc.height
cols = desc.width

# calculate slope
inraster = arcpy.Raster("elevation.tif")
outraster = arcpy.sa.Slope("elevation.tif")

# hillshade
myShade = arcpy.sa.Hillshade("elevation.tif", 270, 45)  #sun az 270, elev 45

#get min and max
arcpy.CalculateStatistics_management(inraster)
MINResult = arcpy.GetRasterProperties_management(inraster, "MINIMUM")
zMin = float(MINResult.getOutput(0))
MAXResult = arcpy.GetRasterProperties_management(inraster, "MAXIMUM")
zMax = float(MAXResult.getOutput(0))

# create output
outName = 'SlopeColored.tif'
if os.path.exists(outName):
     os.remove(outName)

#create raster of scaled elevations
f = ((inraster -zMin)/(zMax-zMin))
#create the red raster
R = 255* (inraster/inraster)
#green and blue raster values are identical
G = f * 255
B = f * 255
 
#Compose single band datasets to a TIFF format raster file
arcpy.CompositeBands_management(str(R)+';'+str(G)+';'+str(B),outName)
