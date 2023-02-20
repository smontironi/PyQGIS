#importamos las librerias de pyQGIS
from PyQt5.QtCore import QVariant
from qgis.core import *

#cargamos la capa de trabajo
shp = r"D:\CURSO_Introduccion_python_para_GIS\MODULO_04\Datos para Practicar\Datos PyQGIS\SHP"
layer = QgsVectorLayer(shp,'clipLagunas','ogr')

#Agregar Campos
campos = layer.dataProvider()
campos.addAttributes([QgsField('Clase', QVariant.String), QgsField('Area_m2', QVariant.Double)])

print("campos creados y listos")

#Expresión para calcular area
expression1 = QgsExpression('$area')

#Creamos el contexto y cargamos la capa
context = QgsExpressionContext()
context.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))

#Activamos la edición de la capa
with edit(layer):
    #Recorremos cada entidad en la Capa
    for f in layer.getFeatures():
        #aplicamos la expresión a cada entidad
        context.setFeature(f)
        f['Area_m2'] = expression1.evaluate(context)
        #Guardamos la edición realizada
        layer.updateFeature(f)

print('Area calculada')


#Creamos una variable para el área total
total_area = 0

for laguna in layer.getFeatures():
    #Almaceno el area de cada laguna
    area = laguna["Area_m2"]
    #suma el area de cada laguna
    total_area += area

#mostramos el resultado
print ("Area Total: "+ str(total_area)+' m2')
print ('GRACIAS AL EQUIPO DE HelpGIS')
print ('Mi nombre es Sebastian Montironi')