# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# teste_reclassy_script.py
# Created on: 2015-04-18 16:29:26.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------



# Import arcpy module
import os
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")

inpfolder=arcpy.GetParameterAsText(0)

#setando o arcgis para pasta
env.workspace=inpfolder

# ciando a lista de rasters
rasterList=arcpy.ListRasters()

#map feature polygon
mask=arcpy.GetParameterAsText(1)

#extension output extract

# outputfolder
output_folder=arcpy.GetParameterAsText(2)


env.workspace=output_folder
def extract_by_mask(rasterList,mask,output_folder):
    for i in rasterList:
        inpmap=inpfolder+'\\%s'%i
        outExtractByMask = ExtractByMask(inpmap, mask)
        outmap=unicode(""+os.path.splitext(i)[0]+"_asc.asc")
        outmap=output_folder+'\\%s'%outmap
        arcpy.RasterToASCII_conversion(outExtractByMask, outmap)
        
        
        
class extract_convert:
    extract_by_mask(rasterList, mask,output_folder)
    
    
   


