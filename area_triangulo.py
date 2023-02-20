import math
# Pedir que ingrese las coordendas del triángulo
X1 = float(input("Ingresar Coordenada X1: "))
Y1 = float(input("Ingresar Coordenada Y1: "))
X2 = float(input("Ingresar Coordenada X2: "))
Y2 = float(input("Ingresar Coordenada Y2: "))
X3 = float(input("Ingresar Coordenada X3: "))
Y3 = float(input("Ingresar Coordenada Y3: "))
#Función matemática para calcular el Área de un triángulo a partir
# de sus vértices ( 1/2 * | X1 * (Y2 - Y3) + X2 * (Y3 - Y1) + X3 * (Y1 - Y2) | )
area_triangulo = round((1/2 * abs(X1 * (Y2 - Y3) + X2 * (Y3 - Y1) + X3 * (Y1 - Y2))),4)
print ('El área del triángulo es: ', str(area_triangulo)+'m²')
print ("Hola Equipo de HelpGIS soy Ronald")


