import os
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")
import csv
#----------------------------------------------------
#parameters
inpFile=arcpy.GetParameterAsText(0)
out_file=arcpy.GetParameterAsText(1)
type_corte=arcpy.GetParameterAsText(2)
file_csv=arcpy.GetParameterAsText(3)


#----------------------------------------------------
#defs
def convert_file_to_tif(inpFile,out_file):
     arcpy.ASCIIToRaster_conversion(inpFile,out_file,"FLOAT")



# Select values cuts
def raster_calculator(file_csv,type_corte,rast,out_file):
     if type_corte=='Minimum training presence logistic threshold':
          prefix='MinTrgPlogisticThrs'
     if type_corte=='percentile training presence logistic threshold':
          prefix='PctTrgPrlogisticThrs'
     if type_corte=='Maximum training sensitivity plus specificity logistic threshold':
          prefix='MaxTrgSensSpeclogisticThrs'
     
     
     outout=unicode(""+os.path.splitext(out_file)[0]+'_'+prefix+'.tif')
     with open(file_csv, 'rb') as csvfile:
          spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
          cabecalho=''
          for row in spamreader:
               if cabecalho=='':
                    cabecalhotemp=', '.join(row)
                    cabecalho=cabecalhotemp.split(',')
                    
               row_resulttemp=', '.join(row)
          row_result=row_resulttemp.split(',')
     
     cont_row=0
     for i in cabecalho:
          if type_corte in i:
               Cut_value=float(row_result[cont_row])
          cont_row=cont_row+1       
     whereClause = "VALUE > %s "%Cut_value
     outCon = Con(rast,rast,'', whereClause)        
     outCon.save(outout)    
    
class principal:
     convert_file_to_tif(inpFile, out_file)
     raster_calculator(file_csv,type_corte,inpFile,out_file)