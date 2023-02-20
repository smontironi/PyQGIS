#Importar la libreria math
import math
#Importar la libreria tkinter (Sirve para crear ventanas ejecutables,
# para que nuestros usuarios puejan ejecutar nuestro código)
import tkinter


#Definimos la variable radio y la obtenemos desde la caja donde se ingresa
# luego realizamos la fórmula para calcular el área del círculo y lo redondeamos
# Finalmente usamos return para mostrar el resultado
def radio():
    radio=float(caja_text.get())
    resultado=round(((radio**2)*math.pi),2)
    return var.set(resultado)

#Creamos la ventana
ventana=tkinter.Tk()

#Colocamos su titúlo a nuestra ventana
ventana.title ("MI NOMBRE ES RONALD RUPAY")

#Definimos el tamañaño de nuestra ventana
ventana.geometry("400x200+450+200")

#Creamos la variable que nos ayudará amostrar en pantalla y la definimos como
# un Double (Número con decimales)
var=tkinter.DoubleVar()

#creamos la descripción de nuestra venta
text2=tkinter.Label(ventana, text="Esta ventana te permiete calcular el área de un círculo", bg='blue', fg='white')
text2.pack()

#Creamos el texto que se imprime en pantalla
#para solicitar el radio
#Acomodamos el texto en la ventana
text1=tkinter.Label(ventana, text="Ingrese el Radio: ")
text1.pack()

#Creamos una caja, donde el usuario ingresará el radio
#Acomodamos la caja en la ventana
caja_text=tkinter.Entry(ventana, fg='blue')
caja_text.pack()

#Creamos una botón, para que el usuario presione y hacemos un
# llamado al radio que ingresa el usiario
#Acomodamos el boton en la ventana
boton1=tkinter.Button(ventana,text="Calcular el Área",command=radio)
boton1.pack()

#Creamos una caja para la salida del resultado y llamamos al resultado
#Acomodamos la caja para mostrar el resultado en la ventana
caja_resultado=tkinter.Label(ventana,textvariable=var)
caja_resultado.pack()

#Finalizamos la ventana
ventana.mainloop()