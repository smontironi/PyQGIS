import math
# solicitar los grados minutos y segundos
grados = int(input("Ingrese los grados: "))
minutos = int(input("Ingrese los minutos: "))
segundos = float(input("Ingrese los segundos: "))
# convertiremos los segundos a minutos
# estos serán sumados a los minutos iniciales
min1 = segundos/60 + minutos
# los minutos sumados los convertimos a grados
# estos grados de resultado se suman a los grados iniciales
grados1 = round(((min1)/60 + grados),4)
# imprimer en pantalla el resultado
print("El resultado es: ", str(grados1)+"°")
print("Hola equipo de HelpGIS")
print("Saludos de parte de Sebastian Montironi")