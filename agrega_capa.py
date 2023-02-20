#importamos las librerias de pyQGIS
from PyQt5.QtCore import QVariant
from qgis.core import *

#cargamos la capa de trabajo
shp = r"D:\CURSO_Introduccion_python_para_GIS\MODULO_04\Datos para Practicar\Datos PyQGIS\SHP"
layer = QgsVectorLayer(shp,'clipLagunas','ogr')

#Agregar Campos
campos = layer.dataProvider()
campos.addAttributes([QgsField('Clase', QVariant.String), QgsField('Area_m2', QVariant.Double)])

print("campos creados")