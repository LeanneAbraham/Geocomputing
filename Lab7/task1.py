##Task 1##

import arcpy

# set up working environment
arcpy.env.workspace = r"c:\data\lab_data.gdb"
#make sure files can be overwritten for when running code many times
arcpy.env.overwriteOutput = True

# create variables that correspeond to feature classes in gdb
powerline = "PowerLine"
parcels = "Parcels"

#create output feature class for buffer
powerlineBuffer = r"c:\data\lab_data.gdb\powerline_buffer"

# buffer analysis
# the buffer analysis requires the input to be a feature layer
arcpy.MakeFeatureLayer_management(powerline, "powerline_lyr")

#use the powerline lyr to perform a buffer into the buffer feature class, specify distance 
arcpy.Buffer_analysis("powerline_lyr", powerlineBuffer, "250 feet")

# select feature by location
#Make parcels a layer for analysis
arcpy.MakeFeatureLayer_management(parcels,"parcels_lyr")

#create layer for buffer output
arcpy.MakeFeatureLayer_management(powerlineBuffer,"powerline_buffer_lyr")

#select the parcels that are completely within the buffer
arcpy.SelectLayerByLocation_management("parcels_lyr","COMPLETELY_WITHIN","powerline_buffer_lyr")

#note the spatial reference of the buffer layer so it can be matched
sr = arcpy.Describe("powerline_buffer_lyr").spatialReference

# add selection to output feature class using same sr
arcpy.CreateFeatureclass_management(arcpy.env.workspace, "powerline_intersect", "POLYGON", parcels, "SAME_AS_TEMPLATE", "SAME_AS_TEMPLATE", sr)


#append the feature classes into the empty feature class
arcpy.Append_management("parcels_lyr","powerline_intersect")
