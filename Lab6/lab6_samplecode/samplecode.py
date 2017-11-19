import ogr
import gdalconst
import sys

filename1 = 'sample_line.shp'
filename2 = 'sample_polygon.shp'

# get driver
driver = ogr.GetDriverByName('ESRI Shapefile')

# open file
lineDS = driver.Open(filename1, gdalconst.GA_ReadOnly)
polygonDS = driver.Open(filename2, gdalconst.GA_ReadOnly)

# verify the file was opened, exit if not
if lineDS is None:
    print 'Failed to open', filename1
    sys.exit()
if polygonDS is None:
    print 'Failed to open', filename2
    sys.exit()

# get data layer
lineLayer = lineDS.GetLayer(0) # 0 indicates the first layer

# get spatial reference
print lineLayer.GetSpatialRef()
print

# get feature
lineFeat = lineLayer.GetFeature(0) # 0 indicates the first line feature

# get geometry
lineGeom = lineFeat.GetGeometryRef()

# get number of points on line
linePC = lineGeom.GetPointCount()
print 'number of points on sample line:', linePC

# get coordinate of the points
x = lineGeom.GetX(0)
y = lineGeom.GetY(0) # 0 indicates the first point
print 'coordinate of the first point on samole line:', x, ',', y

# get length of line
lineLen = lineGeom.Length()
print 'length of sample line:', lineLen

print

# get information of shapefile fields (from the sample polygon)
polygonLayer = polygonDS.GetLayer(0)
polygonLayerDefn = polygonLayer.GetLayerDefn()
fCount = polygonLayerDefn.GetFieldCount()
print 'Name\tType\tWidth\tPrecision'
for i in range(fCount):
    fDefn = polygonLayerDefn.GetFieldDefn(i)
    fName = fDefn.GetName()
    fTypeCode = fDefn.GetType()
    fType = fDefn.GetFieldTypeName(fTypeCode)
    fWidth = fDefn.GetWidth()
    fPrecision = fDefn.GetPrecision()
    print fName + '\t' + fType + '\t' + str(fWidth) + '\t' + str(fPrecision)

# get values of feature fields
polygonFeat = polygonLayer.GetFeature(0)
print polygonFeat.GetField(1) # get field by id (1 indicates the second field)
print polygonFeat.GetField('name') # get field by fieldname

print

# check if one feature intersects with another
for i in range(fCount):
    polygonFeat = polygonLayer.GetFeature(i)
    polygonGeom = polygonFeat.GetGeometryRef()
    if polygonGeom.Intersects(lineGeom):
        print 'yes'
    else:
        print 'no'

lineDS = None
polygonDS = None
