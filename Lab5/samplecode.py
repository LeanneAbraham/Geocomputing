import sys
import numpy as np
import gdal


# get driver
fmt = 'GTiff'
driver = gdal.GetDriverByName(fmt)

# open input dataset
ds1 = gdal.Open('landsat/L71026029_02920000609_B10_CLIP.TIF')
ds2 = gdal.Open('landsat/L71026029_02920000609_B20_CLIP.TIF')
if ds1 == None or ds2 == None:
	print "can't open file"
	sys.exit()
	
# create output dataset
cols = ds1.RasterXSize
rows = ds1.RasterYSize
dsOut = driver.Create('test.TIF', cols, rows, 1, gdal.GDT_Float32)

# set geotransform & projection
trans = ds1.GetGeoTransform()
prj = ds1.GetProjection()
dsOut.SetGeoTransform(trans)
dsOut.SetProjection(prj)

# calculate output array
arr1 = ds1.GetRasterBand(1).ReadAsArray().astype(np.float)
arr2 = ds2.GetRasterBand(1).ReadAsArray().astype(np.float)
outputArr = arr1 - arr2

# write band
band = dsOut.GetRasterBand(1)
band.SetColorInterpretation(gdal.GCI_GrayIndex)
band.WriteArray(outputArr)

# close

ds1 = None
ds2 = None
dsOut = None
