                                                      #PRIMER INVESTIGACIÓN-TALLER DE PROGRAMACIÓN
                                            #USO DE COMBOBOX, UBICACIÓN, FONT, TAMAÑO, COLOR, FONDO, EVENTOS

#Integrantes:
#Angélica Díaz Barrios
#Josué David Villafuerte



"""
COMBOBOX: es una combinación entre una lista y una caja de texto.

Es una forma útil de seleccionar una opción y podría ayudar de
muchas maneras en el análisis de datos


Funciones: permite al usuario escribir un valor que no se encuentre en la lista desplegable,
o le permite escoger algún valor que ya se encuentra dentro de la lista.
"""

"""
guiyet

Un widget es un pequeño programa o aplicación cuyo objetivo es dotar de información visual y facilitar el acceso
a las funciones que se utilizan de forma frecuente
Los widgets se utilizan en varios ámbitos, en una página de internet, en el escritorio de una computadora o en los dispositivos móviles
"""


from tkinter.ttk import * #El widget Combobox está en el módulo ttk
from tkinter import ttk #ttk proporciona acceso al conjunto de widgets temáticos Tk.
from tkinter import * #Primero se importa el paquete Tkinter
#===============================================================    CREACIÓN DE VENTANA      =========================================================================


ventana = Tk()                   #Se crea la ventana raíz
ventana.title("USO DE COMBOBOX") #Título que va a ir en la parte superior izquierda de la ventana
ventana.config(bg = "#E69DFB")   #Cambiar color de fondo
ventana.config(cursor = "hand2") #Cambiar el tipo de cursor
ventana.config(relief = "solid")#Cambiar el tipo de borde
ventana.config(bd = 8)           #Cambiar el grosor del borde
ventana.geometry("900x400")      #El primer valor de geometry representa el ancho horizontal y el segundo el largo de la ventana parte vertical.
#yiometry

"""

bg = background(fondo), cambia el color de fondo

fg= foreground(primer plano),cambia el color de las letras

font= fuente, cambia el tipo de letra
El tipo de fuente puede ser a gusto personal,como las letras establecidas en Word.

bd = borderwidth(ancho del borde), cambia el tamaño del borde

relief = tipo de relieve del borde, pueden ser: flat, groove = gruf ranura, raised reist elevado, ridge= rich, solid, o sunken = sonken hundido

"""

#=================================================================    EJEMPLO COMBOBOX 1      ========================================================================

def mostrarDato():
    etiquetaMostrar.config(text = combo1.get())



etiqueta0 = Label(ventana, text = "Su valor es:",background = "#E69DFB",foreground ="black",borderwidth = 2,font = ("Bell MT", 15))
etiqueta0.grid(column = 1, row = 9)

etiquetaMostrar = Label(ventana, text = "",background = "#E69DFB",foreground ="black",borderwidth = 8,font = ("Bell MT", 15))
etiquetaMostrar.grid(column = 1, row = 11)


etiqueta1 = Label(ventana, text = "Valores en Tupla",background = "green",foreground ="yellow",relief = "groove",borderwidth = 2,font = ("Bell MT", 14))
etiqueta1.grid(column = 1, row = 0)

boton = Button(ventana,text = "Mostrar",background = "pink",foreground = "red4",font = ("Arial", 13),borderwidth = 8,relief = "raised",command = mostrarDato)
boton.grid(column = 1,row = 7)


combo1 = Combobox(ventana, foreground ="green",font = ("Chiller", 13)) #Se agrega el widget Combobox y se le indica en dónde estará
combo1["values"] = (1, 2, 3,"Angélica", "David",123.5, True, False) #Se pueden introducir una tupla
combo1.current(5) #Permite obtener y mostrar un valor  deseado de la lista de primero según su indice, empieza desde la posición 0
combo1.grid(column = 1, row = 4) #La posión del widget dentro de la ventana, puede ser .grid, .pack o .place

#grid = grillas, tipo tabla de la ventana
#row, indica la fila (posición horizontal) en la ventana




#===============================================================     EJEMPLO COMBOBOX 2      ==========================================================================

def mostrarDato1():
    print("\n........................")
    print("Usted ha comprado:")
    print(combo2.get()) 

etiqueta2 = Label(ventana, text = "Valores en lista",background = "orange",foreground ="yellow",relief = "ridge",font = ("Broadway", 13))
etiqueta2.grid(column = 12 , row = 0)

#State = "readonly" impide que la persona ingrese un valor en la caja y solo pueda usar los datos de la lista.
combo2 = Combobox(ventana, state= "readonly",foreground ="orange",font = ("Forte", 13),postcommand = mostrarDato1) 
combo2["values"] = ["arroz", "frijoles", "azúcar", "café"]
combo2.current(0)
combo2.grid(column = 12, row = 4)



#===============================================================     EJEMPLO COMBOBOX 3      ==========================================================================

def obtener():
    print("\n",combo3.get())
    

etiqueta3 = Label(ventana, text = "Seleccionar transporte",background = "black",foreground ="yellow",borderwidth = 2,relief ="groove",font = ("Arial Black", 10))
etiqueta3.grid(column = 15, row = 0)

boton = Button(ventana,text = "Obtener",background = "red4",foreground = "pink",font = ("Arial", 13),borderwidth = 8,relief = "raised",command = obtener)
boton.grid(column = 15,row = 7)

combo3 = Combobox(ventana,foreground = "black",font = ("Arial", 12))
combo3["values"] = ["carro","moto","avión","barco","bicicleta"]
combo3.grid(column = 15, row = 4)


#===============================================================     EJEMPLO COMBOBOX 4      ==========================================================================

def mostrarDato3(dato):
    print("\nSu mes de cumpleaños es: ",combo4.get())
   
    
etiqueta4 = Label(ventana, text = "Elija su mes de cumpleaños",background = "blue",foreground ="yellow",borderwidth = 2,relief="solid",font = ("Forte", 11), )
etiqueta4.grid(column = 16, row = 0)

combo4 = Combobox(ventana, foreground ="purple",font = ("Broadway", 12))

meses = ["Enero","Febrero","Marzo", "Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre", "Diciembre"]

combo4["values"] = meses
combo4.bind("<<ComboboxSelected>>",mostrarDato3)# el método bind es la forma de enlazar la función con el combobox cuando el usuario selecciona un elemento de la lista
combo4.set("Enero") #Establece el contenido de la lista, es decir el valor que se mostrará primero al abrir la ventana
combo4.grid(column = 16, row = 4)
#baind = unir, enlazar

#La función "mainloop" llama al ciclo sin fin de la ventana.
#La ventana esperará cualquier interacción del usuario hasta que la cerremos.
ventana.mainloop()







#========================================= OTRA VENTANA PARA DEMOSTRAR EL CAMBIO DE COLOR DEL FONDO DE UN COMBOBOX ===================================================

from tkinter import *
from tkinter import ttk


ventana = Tk()                   
ventana.title("COLOR DE FONDO COMBOBOX") 
ventana.config(bg = "skyblue")   
ventana.config(cursor = "pencil") 
ventana.config(relief = "groove")
ventana.config(bd = 8)           
ventana.geometry("320x200")      
"""
nombre: fondo
Permite cambiar el color del fondo del combobox, pero solo se le puede dar el mismo color a todos los combobox
que existan en la misma ventana
"""

fondo= ttk.Style()
fondo.theme_use('alt') # los temas pueden ser calm, alt, default, classic, vista, winnative, xpnative.
fondo.configure("TCombobox", fieldbackground= "black", background= "blue")


label = ttk.Label(ventana, text= "Select a Car Model",background = "skyblue",foreground ="white", font= ('Aerial 20'))
label.pack(pady = 30)


combo = ttk.Combobox(ventana,foreground ="yellow",font = ("Chiller", 20),
values=["Honda", "Hyundai", "Wolkswagon", "Tata", "Renault", "Ford", "Chrevolet", "Suzuki","BMW", "Mercedes"])
combo.pack()

ventana.mainloop()
