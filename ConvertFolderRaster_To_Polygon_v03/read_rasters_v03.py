import os
import arcpy
from arcpy import env




# pasta onde estao os arquivos a serem convertidos
inpfolder=arcpy.GetParameterAsText(0)

#setando o arcgis para pasta
env.workspace=inpfolder

#criando lista com tods os rasters da pasta
rt=arcpy.ListRasters()

#criando pasta de saida
outputfolder=arcpy.GetParameterAsText(1)

#seta o arcgis para a pasta de saida
env.workspace=outputfolder

# parametro de simplify
field=arcpy.GetParameterAsText(2)

SIMPLIFY=arcpy.GetParameterAsText(3)

# recebe se vai ser ou nao simplificado os poligonos
if SIMPLIFY=="false":
    SIMPLIFY='NO_SIMPLIFY'
if SIMPLIFY=='true' :
    SIMPLIFY='SIMPLIFY'




# faz a conversao da pasta
for i in rt:
    #elimina o extencao 
    out=unicode(""+os.path.splitext(i)[0]+"_vect")
    # criando o input
    inp=inpfolder+'\\%s'%i  
    #converte
    arcpy.RasterToPolygon_conversion(inp,out,SIMPLIFY,field)
    
