
# coding: utf-8
###NOTES FROM LAB####
import sys
import numpy as np
import gdal

#gdal cant use try/except to catch errors otherwise use an if statemnt
if ds1 == None or ds3 == None:
    print("can't open the file")
    sys.exit()
    
#get driver
fmt = "GTiff"
driver = gdal.GetDriverByName(fmt)

#create output dataset
dols = ds1.RasterXSize
cols = ds1.RasterYSize
dsOut = driver.Create('test.tif', cols, rows, 1, gdal.GDT_FLOAT32) #be careful about the float, for ex your data could
#have an int output, might have int division problems. The Division wont change the data type for you, 

#set geotransform & projection
trans = ds1.GetGeoTransform()
# prj = ...get

#missing more stuff

#.ReadAsArray() neans you read it as an array, changing data type to float gets rid of the division problem just in case
#you do raster math later

print(outputArr) #gives a truncated version of the raster, checks for values

#write band
band = dsOut.GetRasterBand(1)
band.SetColorInterpretation(gdal.GCI_GrayIndex)

#close
ds1 = None
# In[1]:


import sys
import numpy as np
from osgeo import gdal 

#open the two image files, because each band of the image is a seperate file
nir = gdal.Open('.\landsat\L71026029_02920000609_B40_CLIP.tif',0)
red = gdal.Open('.\landsat\L71026029_02920000609_B30_CLIP.tif',0)

#gdal cant use try/except to catch errors
#use an if statement to catch errors
if nir == None or red == None:
    print("can't open the file")
    sys.exit()
    
#get driver
# driver = red.GetDriver().LongName #why doesn't this work?
fmt = 'GTiff'
driver = gdal.GetDriverByName(fmt)

#create output dataset
#this step is neccessary to understand how big the output dataset needs to be
cols = nir.RasterXSize
rows = nir.RasterYSize

ndvi = driver.Create('ndvi.tif', cols, rows, 1, gdal.GDT_Float32)

#set geotransform & projection for the new raster file
#this is based off of one of the bands the tranformation will be generated from
trans = nir.GetGeoTransform()
prj = nir.GetProjection()
ndvi.SetGeoTransform(trans)
ndvi.SetProjection(prj)

#.ReadAsArray() means you read it as an array,
#changing data type to float gets rid of the division problem just in case
# calculate output array
nirArr = nir.GetRasterBand(1).ReadAsArray().astype(np.float)
redArr = red.GetRasterBand(1).ReadAsArray().astype(np.float)

#calculate ndvi
outputArr = (nirArr - redArr)/(nirArr + redArr)

#write the ndvi array to the (currently empty) raster cell by cell
#have to do this by writing these values to a single band within the raster

#write band
band = ndvi.GetRasterBand(1)
#make the raster greyscale
band.SetColorInterpretation(gdal.GCI_GrayIndex)
#write the data to the image
band.WriteArray(outputArr)


#close everything
nir = None
red = None
ndvi = None

