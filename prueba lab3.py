from functools import partial #El módulo functools es para funciones de orden superior: funciones que actúan o retornan otras funciones.
                              #En general, cualquier objeto invocable puede ser tratado como una función para los propósitos de este módulo.
from tkinter import messagebox #Se importa este módulo para poder utilizar el paquete de cajas de texto
import tkinter as tk
import tkinter
from tkinter import *
from tkinter import ttk, font





#============================================================== MENÚ DEL REGISTRO DE LLAMADAS TELEFÓNICAS ============================================================

"""
Nombre: registro_llamadas
Entradas: no recibe una entrada directamente, la recibe a través de un input como un número de tipo string según la opción que el usuario quiera realizar.7
Salida: retorna a otras funciones(registrar_llamadas,borrar_llamada, modificar_registro, ver_llamadas o retornar), según la opción seleccionada por el usuario
Restricciones: no existen
"""
def registro_llamadas(ventanaRaiz):
    v1=Toplevel(ventanaRaiz) # Crea una ventana hija y entre los paréntesis va el nombre de la ventana raíz
    v1.title("Sistema de registro de llamadas telefónicas")
    v1.config(bd = 8) #cambia el grosor del borde
    v1.config(bg = "#00008B")#cambia el color del fondo de la ventana raíz
    v1.geometry("500x600")
    menu(v1)#llama a la función menu, la cual coloca la barra de menu en la ventana
    
    adicional = tk.LabelFrame(v1, text = "Menú registro de llamadas telefónicas",fg = "Black",bg="skyblue")
    adicional.pack(expand = 6,ipadx = 1,fill="both")   

    miFrame = tk.Frame(adicional) #Un Frame es un widget, que sirve como una especie de contenedor para los demás widgets, dentro de la ventana raíz.
   
    miFrame.config(bg = "white")
    miFrame.pack(expand = 6,ipadx = 1,fill="both")#Posicionamiento dentro de la ventana raíz
    
    labelMenuP1 = tk.Label(miFrame, text="Opciones disponibles",font = ("Calibri",15),bg="white", fg = "#252850")
    labelMenuP1.pack(ipadx = 50)          
    labelMenuP2 = tk.Radiobutton(miFrame, text="Registrar llamada",fg= "white",bd = "4",font = ("Times New Roman",16), variable=opcion, value=1,bg="#00008B",relief = "raised")
    labelMenuP2.pack(expand=6,ipadx = 40)
    labelMenuP3 = tk.Radiobutton(miFrame, text="Borrar llamada",fg= "white",bd = "5",font = ("Times New Roman",16), variable=opcion, value=2,bg="blue",relief = "raised")
    labelMenuP3.pack(expand=6,ipadx = 68)
    labelMenuP4 = tk.Radiobutton(miFrame, text="Modificar registro", bd = "5", variable=opcion,font = ("Times New Roman",16), value=3,  bg="light blue",relief = "raised")
    labelMenuP4.pack(expand=6,ipadx = 40)
    labelMenuP5 = tk.Radiobutton(miFrame, text="Modificar registro", bd = "5", variable=opcion,font = ("Times New Roman",16), value=4, bg="gray",relief = "raised")
    labelMenuP5.pack(expand=6,ipadx = 40)
    labelMenuP6 = tk.Radiobutton(miFrame, text="Volver", bd = "8",fg= "green", variable=opcion,font = ("Times New Roman",16), value=5,command=lambda: ejecutar(ocultar2(v1,ventanaRaiz)), bg="red2",relief = "raised")
    labelMenuP6.pack(expand=6,ipadx = 1)

   





#=========================================================== Funciones para ocultar y mostrar una ventana =============================================================

def mostrar(ventana): ventana.deiconify()# Muestra una ventana

def ocultar(ventana):
    ventana.withdraw()#Oculta una ventana
    return registro_llamadas(ventana)

def ejecutar(f): ventanaRaiz.after(200,f)#Lo que hace after es que pasados dos milisegundos en un momento dado del tiempo,
                                         #ejecuta f. f es el nombre de una función que queremos ejecutar.


def ocultar2(ventana,ventanaRaiz):
    ventana.withdraw()
    return mostrar(ventanaRaiz)




#========================================================= Función para la colocación de la barra del menú ============================================================
 
"""
Nombre: menu
Entrada: recibe el nombre de la ventana en la cual se desea posicionar la barra de menú
Salida: posiciona la barra de menu con sus respectivas etiquetas dentro de la ventana indicada
"""

def menu(ventanaRaiz):
    #Se crea la cinta del menú
    mi_menu = tk.Menu(ventanaRaiz)

    #Agregamos opciones
    #add_command puede recibir un segundo parámetro que
    #permite ejecuar una función cuando se hace click en una opción del menu creado
    mi_menu.add_command(label="Archivo")
    mi_menu.add_command(label="Editar")
    mi_menu.add_command(label="Opciones")
    ventanaRaiz.config(menu=mi_menu)
    mi_menu.add_cascade(label="Ayuda")
    mi_menu.add_command(label="Salir",command = quit)



    


#======================================================== Creando ventana raíz en donde irá el Menú Principal ========================================================
ventanaRaiz = tk.Tk()
ventanaRaiz.title("Sistema de registro de llamadas telefónicas")
ventanaRaiz.config(bd = 8) #cambia el grosor del borde
ventanaRaiz.config(bg = "white")#cambia el color del fondo de la ventana raíz
ventanaRaiz.geometry('1100x600')#el primer valor de geometry representa el ancho y el segundo el largo de la ventana.








#================================================== Funciona para CENTRAR la ventana en la pantalla de la computadora ================================================
ventanaRaiz.update_idletasks()
w=ventanaRaiz.winfo_width()
h=ventanaRaiz.winfo_height()
extraW=ventanaRaiz.winfo_screenwidth()-w
extraH=ventanaRaiz.winfo_screenheight()-h
ventanaRaiz.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))
#=====================================================================================================================================================================




menu(ventanaRaiz)#hace el llamado a la función menu, la cual sirve para colocar la barra de menu dentro de la ventana

miFrame = tk.Frame() #Un Frame es un widget que sirve como una especie de contenedor para los demás widgets, dentro de la ventana raíz.
miFrame.config(bg = "white")
miFrame.pack(side = "left", fill = "y",)#Posicionamiento dentro de la ventana raíz




#======================================================== Este evento permite colocar una imagen en la ventana =======================================================

img = tk.PhotoImage(file="0001-8510507307_20210923_102449_0000.png")#Importar foto
fondo = tk.Label(ventanaRaiz,bg = "#252850",relief="flat",image=img)
fondo.pack(anchor= "ne")
opcion = tk.IntVar()




#======================================================= ETIQUETAS PARA EL MENÚ PRINCIPAL DEL PROGRAMA ===============================================================

labelMenuP1 = tk.Label(miFrame, text=" BIENVENID@ AL MENÚ PRINCIPAL",font = ("Calibri",15),bg="white", fg = "#252850")
labelMenuP1.pack(ipadx = 50)
labelMenuP2 =tk.Label(miFrame, text="Seleccione la opción que desea realizar:",bd = "5",font = ("arial"), bg="white", fg = "grey")
labelMenuP2.pack(ipadx = 15 , padx=1) 
labelMenuP3 = tk.Radiobutton(miFrame, text="Registro de llamadas telefónicas",fg= "white",bd = "4",font = ("Times New Roman",16), variable=opcion, value=1, command=lambda: ejecutar(ocultar(ventanaRaiz)) ,bg="#00008B",relief = "raised")
labelMenuP3.pack(expand=6,ipadx = 40)
labelMenuP4 = tk.Radiobutton(miFrame, text="Búsquedas avanzadas",bd = "5",font = ("Times New Roman",16), variable=opcion, value=2,bg="light blue",relief = "raised")
labelMenuP4.pack(expand=6,ipadx = 68)
labelMenuP5 = tk.Radiobutton(miFrame, text="Total de llamadas telefónicas", bd = "5", variable=opcion,font = ("Times New Roman",16), value=3, bg="gray",relief = "raised")
labelMenuP5.pack(expand=6,ipadx = 40)
labelMenuP6 = tk.Radiobutton(miFrame, text="Salir", bd = "8",fg="black", variable=opcion,font = ("arial black",11), value=3,command = quit, bg="red2",relief = "raised")
labelMenuP6.pack(expand=6,ipadx = 1)
#=====================================================================================================================================================================

ventanaRaiz.mainloop()# Al final del código se mantiene a la ventana raíz esperando a que el usuario realice una acción
