import arcpy

# set up working environment
arcpy.env.workspace = "c:\data"
arcpy.env.overwriteOutput = True

# set feature class name
fc1 = ".\data\sample_line.shp"
fc2 = ".\data\sample_polygon.shp"

# get feature class description
desc = arcpy.Describe(fc2)
print 'featureType:   ', desc.featureType
print 'shapeFieldName:', desc.shapeFieldName
print 'shapeType:     ', desc.shapeType
print 'extent:        ', desc.extent
print 'path:          ', desc.path
print


# get fields from feature class
print '\nThe fields are:'
for field in desc.fields:
    fldName       = field.name
    fldWidth      = field.length  #is "Width" in OGR
    fldPrecision  = field.precision
    fldTypeS      = field.type    #is an integer in OGR

    values = (fldName,fldTypeS,fldWidth,fldPrecision)
    fmt    = '%s: %s (%d.%d)'
    print fmt % values
print

# get feature count
nFeatures = arcpy.GetCount_management(fc2)[0]
print "number of features in", fc2, ":", nFeatures
print

# Using cursors to access features
cursor = arcpy.SearchCursor(fc2)
shapefieldname = desc.ShapeFieldName # get the name of the shape field 
for row in cursor:
    print "feature id:", row.getValue("FID")
    shape = row.getValue(shapefieldname)
    for pnt in shape.getPart(0):
         print pnt.X, pnt.Y
print

# buffer analysis
arcpy.MakeFeatureLayer_management(fc1, "sample_line_lyr") # the buffer analysis requires the input to be a feature layer
arcpy.Buffer_analysis("sample_line_lyr", "sample_line_buffer", "5000 feet") # can add more optional parameters 

# select feature by location
arcpy.MakeFeatureLayer_management(fc2,"sample_polygon_lyr")
arcpy.MakeFeatureLayer_management("sample_line_buffer.shp","sample_line_buffer_lyr")
arcpy.SelectLayerByLocation_management("sample_polygon_lyr","INTERSECT","sample_line_buffer_lyr")
# For lab assignment, find the appropriate keyword from the official documentation.

# create output feature class 
sr = arcpy.Describe("sample_polygon_lyr").spatialReference
arcpy.CreateFeatureclass_management(arcpy.env.workspace, "polygon_intersect.shp", "POLYGON", fc2, "SAME_AS_TEMPLATE", "SAME_AS_TEMPLATE", sr) # spatial reference
# add selection to output feature class
arcpy.Append_management("sample_polygon_lyr","polygon_intersect.shp")
