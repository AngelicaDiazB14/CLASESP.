"""
para cambiar lo que tengo en una cadena, algún valor que tenga hgao lo siguiente:

>>>c = [45,78,32,0]
>>>c[1] = 100
>>>c
[45,100,32,0]

type sirve para saber qué tipo de dato estoy usando
"""

#Entrada: dos variables tipo de dato entero mayor a cero
#Salidas: la suma de las variables a y b
#Restricciones: deben ser enteros, mayor a cero. No nulos

def sumar(a,b):
    if(isinstance(a,int) and isinstance(b,int)):
        if(a >= 0 and b >= 0):
            return a + b
        else:
            return "Error: las variables a y b deben ser mayores a cero"
    else:
        return "Error: las variables a y b deben ser tipo de dato entero"
    

"""
#Entrada: dos variables tipo de dato enetero mayor a cero
#Salidas: la resta de las variables a y b
#Restricciones: deben ser enteros, mayor a cero. No nulos
"""
def restar(a,b):
    if(isinstance(a,int) and isinstance(b,int)):
        if(a > 0 and b > 0):
            return a - b
        else:
            return "Error: las variables a y b deben ser mayores a cero"
    else:
        return "Error: las variables a y b deben ser tipo de dato entero"



def dividir(a,b):
    if(isinstance(a,int) and isinstance(b,int)):
        if(b > 0):
            return a / b
        else:
            return "Error: el parámetro b debe ser mayor a cero"
    else:
        return "Error: las variables a y b deben ser tipo de dato entero"

def multiplicar(a,b):
    if(isinstance(a,int) and isinstance(b,int)):
        return a * b
    else:
        return "Error: las variables a y b deben ser tipo de dato entero"



def potencia(a,b):
    return a ** b


"""
>>>a = -5
>>>a
-5
>>> abs(a) #representa el valor absoluto
5
"""

#########################################################################################
#Ambas cuentan la cantidad de dígitos de un número, utilizan recursividad de PILA
def cantidadDigitos(num):
    if(isinstance(num,int) and num >= 0):
        if(num < 10):
            return 1
        else:
            return cantidadDigitos_aux(num,0)
    else:
        return "El número ingresado debe ser entero positivo"

def cantidadDigitos_aux(num, contador):
    if(num == 0):
        return contador
    else:
        return 1 + cantidadDigitos_aux(num //10, contador)

#.......................................................................................
def digitos(n):
    if(isinstance(n,int) and n >= 0):
        if(n < 10):
            return 1
        else:
            return 1 + digitos( n//10)
    else:
        return "Error: en número debe ser entero positivo"
#########################################################################################

#TAREA MORAL HACER EL FACTORIAL

"""
Nombre: Factorial
Entrada: un número
Salida: el resultado de la multiplicación del número hasta 0
Restricciones: solo se permiten número enteros mayores a cero


Algoritmo

a) iniciar desde el número dado, ir restando el número de uno en uno y a la misma vez multiplicarlo con el anterior, hasta que el número original llegue
a ser cero, ese cero se convertirá en un 1



"""

def factorial(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return 1
        else:
            return num * factorial(num-1)
    else:
        return "Error: el número ingresado debe ser entero positivo"


#=================================================================  TERCERA CLASE TALLER   ==================================================================


"""
Nombre: esMayorEdad
Entrada: recibe la edad en un número entero positivo
Salida: un mensaje de texto indicando si la persona es mayor o no de edad
Restricciones: el número de la edad ingresada debe ser entero positivo
"""
def esMayorEdad():
    edad = input("Ingrese un valor numérico indicando su edad: ")
    if(esValidaEdad(edad)):
        edad = int(edad)
        if(edad < 0):
            return "La edad debe ser mayor o igual a cero años"
        elif(edad >= 18):
            return "Es mayor de edad"
        else:
            return "Es menor de edad"
    else:
        return "Error: el valor de la edad debe ser un número entero"
            


def esValidaEdad(valor):
    if(valor == ""):
        print("Error: el valor está vacío")
        return False
    valor = int(valor)
    if(valor < 0):
        print("Error: el valor mayor o igual a cero")
        return False
    return True

def validar(a,b):
    if(a != ""):
        if(b != ""):
            a = int(a)
            b = int(b)
            return True

        else:
            print("Error: el segundo operando está vacío")
            return False
    else:
        print("Error: el primer operando está vacío")
        return False


def calculadora():
    print("\n................BIENVENIDO A MI PRIMERA CALCULADORA..............\n")
    print("\nOpciones:\n")
    print("S: Sumar")
    print("R: Restar")
    print("M: Multiplicar")
    print("D: Dividir")
    print("P: Potencia")
    print("F: Salir")

    opcion = input("\nDigite la opción que desea realizar: ")
    print("")
    if(opcion == "F"):
        return print("Gracias por utilizar la calculadora")
    a = int(input("Ingrese el primer operando numérico: "))
    b = int(input("Ingrese el segundo operando numérico: "))
    if(isinstance(a,int) and isinstance(b,int)):
        if(opcion == "S"):
            print( sumar(a,b))
            return calculadora()
        elif(opcion == "R"):
            print(restar(a,b))
            return calculadora()
        elif(opcion == "M"):
            print(multiplicar(a,b))
            return calculadora()
        elif(opcion == "D"):
            print( dividir(a,b))
            return calculadora()
        elif(opcion == "P"):
            print(potencia(a,b))
            return calculadora()
        


############################################################################# CLASE 4 DE TALLER ###3#########################################################     
            
                
#HACER UN MENÚ ANIDADO

"""
Nombre: menu
Entrada: una letra
Salida: el retorno de otro menú, dependiendo de la opción seleccionada"
"""

def menu():
    print("=======================================================")
    print("\n             BIENVENIDO AL MENÚ PRINCIPAL")
    print("\nOpciones:\n")
    print("A: ARCHIVO")
    print("M: MANTENIMIENTO")
    print("B: BÚSQUEDAS\n")
    print("X: SALIR\n")
    
    opcion = input("Seleccione la opción que desea realizar: ")

    if(opcion == "A"):
        return menuArchivo()
    elif(opcion == "M"):
        return menuMantenimiento()
    elif(opcion == "B"):
        return menuBusquedas()
    else:
        return print("\nGracias por utilizar el menú")
        
"""
Nombre: menuMantenimiento
Entrada: una letra
Salida: el retorno al menú principal dependiendo de la opción seleccionada"
"""        
def menuMantenimiento():
    print("\n\n(R) RETORNAR AL MENÚ PRINCIPAL\n")
    opcion = input("Seleccione la opción que desea realizar: ")
    if(opcion == "R"):
        return menu()
"""
Nombre: menuBusquedas
Entrada: una letra
Salida: el retorno al menú principal dependiendo de la opción seleccionada"
""" 
def menuBusquedas():
    print("\n\n(R) RETORNAR AL MENÚ PRINCIPAL\n")
    opcion = input("Seleccione la opción que desea realizar: ")
    if(opcion == "R"):
        return menu()    
"""
Nombre: menuArchivo
Entrada: una letra
Salida: el retorno de otro menú, dependiendo de la opción seleccionada"
""" 
def menuArchivo():
    print("\n(N) NUEVO")
    print("(B) ABRIR")
    print("(C) CERRAR")
    print("(S) SALIR")
    opcion = input("\nSeleccione la opción que desea realizar: ")

    if(opcion == "S"):
        return menu()



    
#...........................................................................................................................


#                                                                        MANEJO DE ARCHIVOS DE PYTHON

#en este caso mi archivo se llama claseArchivo
def escribirArchivo(nombreArchivo,mensaje): #función para escribir en un archivo archivo
    file = open(nombreArchivo, "w") # open: abre el archivo,  w = write
    file.write(mensaje)#escribe en el archivo y si no existe el archivo lo crea
    file.close()#cierra el archivo


############################################################################# CLASE 5 DE TALLER ###3#########################################################     
                                                                                  #SEMANA 3

#EL SISTEMA OPERATIVO DE WINDOWS PERMITE EL MANEJO DE ARCHIVOS

#El archivo tiene dos tributos: el nombre del archivo y la extención de que tipo de archivo es, el sistema de operativo Windows
#interpreta que el archivo txt pueda ser leído mediante un blog de notas

def anexarArchivo(nombreArchivo,mensaje): #función para anexar en un archivo
    file = open(nombreArchivo, "a") # open: abre el archivo,  a = append anexa, agrega
    file.write(mensaje)#es5cribe en el archivo lo anexa al contenido del archivo ya creado
    file.close()#cierra el archivo

#escribo el archivo y antes le coloco el \n para hacer cambio de línea
#\n para que lo escrito cambie de línea, \t hace un espacio en la misma línea

def leerArchivo(nombreArchivo,mensaje): #función para anexar en un archivo
    file = open(nombreArchivo, "r") # open: abre el archivo,  r = read lectura, lee solo el archivo no se puede editar
    file.read()
    file.close()#cierra el archivo


#Solo copia y pega lo que hay en el archivo de texto
def leerArchivo2(nombreArchivo): #función para anexar en un archivo
    miArchivo = open(nombreArchivo, "r") # open: abre el archivo,  r = read lectura, lee solo el archivo no se puede editar
    miContenido = miArchivo.read()
    print(miContenido)
    miArchivo.close()#cierra el archivo
                 
def escribirArchivoX(nombreArchivo,mensaje): #función modo exclusivo el archivo no debe existir, para poder escribirlo
    file = open(nombreArchivo, "x") # open: abre el archivo,  x = exclusivo
    file.write(mensaje)#escribe en un archivo que no exista y lo crea
    file.close()#cierra el archivo

#=========================================================================================

#readlines lee línea por línea e incluye los caracteres que yo agregué como el salto de línea \n
# READLINES AGARRA TODO EL CONTENIDO DEL ARCHIVO Y LO METE EN UNA LISTA
#EJEMPLO:
# >>> leerArchivo3("claseArchivo.txt")
# ['Hola GuapaFEAhola2\n', '\n', 'hola2']            ESTO ES UNA LISTA
    
def leerArchivo3(nombreArchivo):
    miArchivo = open(nombreArchivo, "r") #read
    miContenido = miArchivo.readlines()
    print(miContenido)
    miArchivo.close()

#UNA LISTA ES CUANDO TIENE CORCHETES CUADRADOS Y CADA VALOR ESTÁ SEPARADO POR UNA COMA


"""
INDEXACIÓN: SE PUEDE RECORRER LA LISTA POR MEDIO DE LOS ARREGLOS- ÍNDICES
LAS POSICIONES SIEMPRE EMPIEZA POR CERO
"""
def leerArchivo4(nombreArchivo):
    miArchivo = open(nombreArchivo, "r") #read
    miContenido = miArchivo.readline() #le quité la "s", ahora está en singular readline por lo que me va a devolver solo una línea y no todas
    print(miContenido)
    miArchivo.close()



def leerArchivo5(nombreArchivo):
    miArchivo = open(nombreArchivo, "r") #read
    miContenido = miArchivo.readline() #le quité la "s", ahora está en singular readline por lo que me va a devolver solo una línea y no todas
    miContenido = miArchivo.readline() #aquí me va a retornar solo la segunda línea porque hice dos veces el readline, si quiero la tercera línea, le hago otra vez lo mismo
    print(miContenido)
    miArchivo.close()


#OTRA FORMA DE LEER EL ARCHIVO
def leerArchivo6(nombreArchivo):
    miArchivo = open(nombreArchivo,"r")

    miContenido = miArchivo.readlines()

    for miLinea in miContenido: # EN miLinea puedo escribir lo que yo quiera porque es una variable
        print(miLinea)

    miArchivo.close()

def BuscarContenidoExacto(nombreArchivo,lineaABuscar):
    miArchivo = open(nombreArchivo,"r")
    resultado = ""

    miContenido = miArchivo.readlines()

    for miLinea in miContenido: # EN miLinea puedo escribir lo que yo quiera porque es una variable
        if(miLinea == lineaABuscar):
            resultado = miLinea

    miArchivo.close()

    if(resultado == ""):
        return "Texto no encontrado en el archivo"
    else:
        return "Texto localizado"
"""
ESTO ES LO QUE HACE LA FUNCIÓN BuscarContenidoExacto

>>> BuscarContenidoExacto("angel.txt","hola")
'Texto localizado'
>>> BuscarContenidoExacto("angel.txt","holafea")
'Texto no encontrado en el archivo'
>>>
"""

#TAREA LEER EL ARCHIVO EN MODO RECURSIVO
#PISTA = a = [1,2,3,4,5]
    #a[1:]
    #[2,3,4,5]

"""

>>>mensaje = "Hola mundo"
>>>mensaje[-1] va de derecha a izquierda
"o"



MUTABILIDAD: ALGO PUEDE CAMBIAR

>>>mensaje="Hola Mundo"
>>>mensaje[0]
"H"
>>>mensaje[0]= "C"
da error porque un string no se puede cambiar las cosas de esta manera, solo los arreglos que están en una lista

>>>hola=[1,2,3,4]
>>>hola[0] = 5
>>>print(hola)
[5,2,3,4]
"""

############################################################################# CLASE 6 DE TALLER ###3#########################################################     
                                                                                  #SEMANA 4


#CONTINUACIÓN DE LA CLASE DE INTRO 6

"""
Nombre: construirNuevoNumero
Entrada: un número entero(n) y un divisor el cual tiene que ser mayor a 0 y menor a 10
Salida: retorna un nuevo número a partir de los dígitos que sean divisibles por el parámetro divisor
Restricciones: solo números enteros positivos, el cero no cuenta.
"""

def construirNuevoNumero(n,divisor):
    if(isinstance(n,int) and isinstance(divisor,int)):
        if(n >= 0):
            if(divisor > 0 and divisor < 10):
                return construirNuevoNumero_aux(n,divisor,0)
            else:
                return "Error: el número divisor debe ser mayor que cero y menor que 10"
        else:
            return "Error: el número debe ser positivo mayor que cero"
    else:
        return "Error: el número debe ser de tipo entero"

def construirNuevoNumero_aux(n,divisor,potencia):
    if(n == 0):
        return 0
    else:
        digito = (n%10) #obtengo el último dígito del número
        if(digito != 0):
            if((digito % divisor) == 0):#si el dígito que obtuve anteriormente módulo del divisor da 0, entonces hago el siguiente return 
                return (digito *(10**potencia)) + construirNuevoNumero_aux(n//10,divisor,potencia + 1) # el módulo de 10 le quita el último dígito y aumento en uno la potencia
            else:                                                                       
                return construirNuevoNumero_aux(n//10,divisor,potencia)
        else:                                                                       
                return construirNuevoNumero_aux(n//10,divisor,potencia)




"""
LISTAS

milista = [12,56,87]
milista[1:]
[56,87]

milista[2:]
[87]


Ejemplo de la corrida


Siempre cuenta el espacio
>>> largoTexto("Hola mundo")
10
"""

def largoTexto(miTexto):
    if(isinstance(miTexto,str)):
        return largoTexto_aux(miTexto)
    else:
        return "Error: Solo es permitido valores de tipo texto"

def largoTexto_aux(miTexto):
    if(miTexto == ""):
        return 0
    else:
        return 1 + largoTexto_aux(miTexto[1:])#1: quita el primer elemento


"""
Nombre: largoLista
Entrada: una lista
Salida: la cantidad de elementos que componen la lista
Restricciones: la lista no debe estar vacía y debe validarse que sea de tipo lista
"""

        
def largoLista(lista):
    if(isinstance(lista,list)):
        if(lista != []):
            return largoLista_aux(lista)
        else:
            return "Error: la lista no puede estar vacía"
    else:
        return "Error: Solo es permitido valores de tipo texto"

def largoLista_aux(lista):
    if(lista == []):
        return 0
    else:
        return 1 + largoLista_aux(lista[1:])#1: quita el primer elemento






"""
Nombre: buscarEnTexto
Entradas: miTexto, textoBuscar
Salida: el retorno de True si el texto a buscar fue encontrado o False si no lo es
Restricciones: miTexto y el textoBuscar deben ser de tipo string
"""

def buscarEnTexto(miTexto, textoBuscar):
    if(isinstance(miTexto, str)) and (isinstance(textoBuscar, str)):
        largo = largoTexto(textoBuscar)
        return buscarEnTexto_Aux(miTexto, textoBuscar, largo)
    else:
        return "Error: Es permitido valores de tipo texto"

def buscarEnTexto_Aux(miTexto, textoBuscar, largo):
    if(miTexto == ""):
        return False
    else:
        parte = miTexto[0:largo]
        if(textoBuscar == parte):
            return True
        else:
            return buscarEnTexto_Aux(miTexto[1:], textoBuscar, largo)




############################################################################# CLASE 7 DE TALLER ###3#########################################################     
                                                                                  #SEMANA 5

"""
#HACER UNA AGENDA DE CONTACTOS

#el archivo debe llamarse contactos.txt


Así debe se verse en el archivo = "Angelica Díaz", "Limón", "61344593", "Toyota"
"""


def menuPrincipal():
    print("=======================================================")
    print("\n           BIENVENID@ A SU AGENDA TELEFÓNICA\n")
    print("(N) Nuevo contacto")
    print("(S) Salir\n")
    opcion = input("Seleccione la opción que desea realizar: ")
    if(opcion == "N"):
        return nuevoContacto()
    elif(opcion == "S"):
        return "Gracias por utilizar la agenda telefónica"
    else:
        return "Error: la opción no fue posible reconocerla"

def nuevoContacto():
    print("-----------------Agregando Contacto------------------------")
    nombre = input("Nombre completo: ")
    provincia= input("Provincia: ")
    telefono = input("Teléfono: ")
    marcaVehiculo = input("Marca vehículo: ")
    return anexarContacto(nombre,provincia,telefono,marcaVehiculo)
    

def anexarContacto(nombre,provincia,telefono,marcaVehiculo):
    file = open("contactos.txt", "a") # open: abre el archivo,  a = append anexa, agrega
    file.write(nombre+", "+provincia+", "+telefono+", "+marcaVehiculo+"\n")
    print("\nSu contactacto fue agregado exitosamente")
    file.close()#cierra el archivo
    return menuPrincipal()





############################################################################# CLASE 8 DE TALLER ###3#########################################################     
                                                                                  #SEMANA 5



"""
TAREA REGISTRO DE LLAMADAS TELEFÓNICAS
CON PYTHON, CON MANEJO DE ARCHIVOSentregar el 6 de setiembre
Se pueden repetir cédulas
el código puede ser un número

"""

############################################################################# CLASE 9 DE TALLER ###3#########################################################     
                                                                                  #SEMANA 6

"""
nombre: reemplazarEnTexto
Entrada: recibe un texto, recibe la palabra a buscar, recibe la palabra a reemplazar
Salida: retorna el texto con la palabra reemplazada en la palabra buscada
Restricciones: los tres parámetros deben ser de tipo string
"""

def reemplazarEnTexto(texto, palabraBuscar, palabraReemplazar):
    if(isinstance(texto,str) and isinstance(palabraBuscar,str) and isinstance(palabraReemplazar,str)):
        buscar = buscarEnTexto(texto, palabraBuscar)
        if(texto == ""):
            return 0
        elif(palabraReemplazar == ""):
            return texto
        elif(palabraBuscar == ""):
            return texto
        else:
            largo = largoTexto(palabraBuscar)
            return reemplazarEnTexto_aux(texto, palabraBuscar, palabraReemplazar, largo, "")
    else:
        return "Los parámetros deben ser de tipo string"

def reemplazarEnTexto_aux(texto, palabraBuscar, palabraReemplazar, largo, nuevoTexto):
    if(texto == ""):
        return nuevoTexto
    else:
        if(texto[0:largo] == palabraBuscar):
            nuevoTexto += palabraReemplazar
            return  reemplazarEnTexto_aux(texto[largo:], palabraBuscar, palabraReemplazar, largo, nuevoTexto)
        else:
            nuevoTexto += texto[0]
            return  reemplazarEnTexto_aux(texto[1:], palabraBuscar, palabraReemplazar, largo, nuevoTexto)
        






def largoTextoa(miTexto):
    if(isinstance(miTexto,str)):
        largo = largoTexto(miTexto)
        return largoTextoa_aux(miTexto,largo,0)
    else:
        return "Error: Solo es permitido valores de tipo texto"

def largoTextoa_aux(miTexto,largo,pos):
    if(largo == 0):
        return True
    else:
        if(miTexto[pos] == "1" or miTexto[pos] == "2"or miTexto[pos] == "3"or miTexto[pos] == "4"or miTexto[pos] == "5"or miTexto[pos] == "6"or miTexto[pos] == "7" or miTexto[pos] == "8"or miTexto[pos] == "9"or miTexto[pos] == "0"):
            return  True and largoTextoa_aux(miTexto,largo-1,pos+1)#1: quita el primer elemento
        else:
            return False


############################################################################# CLASE 10 DE TALLER ###3#########################################################     
                                                                                  #SEMANA 8

"""
Proyecto1: quién quiere ser millonario
ir armando un vbanco de preguntas
puedo crear varias listas de juegos txt
las preguntas de deben estar en un archivo aparte txt
para cuando hago un juego, selecciono de manera aleatoria 15 preguntas nada más para un juego
no se puede utilizar append, find, random sí se puede usar

entrega 4 de octubre 
"""

############################################################################# CLASE 11 DE TALLER ###3#########################################################     
                                                                                  #SEMANA 9    

"""
laboratorio 3

crear una interfaz gráfica de la aplicación de la tarea 1
Hacer una simulación de como se vería
no van a haber que manipular archivos ni nada
no se calcula nada

Utilizar correctamente lo que hemos visto de witgets

si yo digo en la parte de agregar llamada, solo valido que los campos estén completos
y si no que tire un mesagebox de error que no se pudo agregaro un mesabox de aviso que si

subir al github
craer new file ponerle readme, ahí debo ingresarle las instrucciones de cómo se utiliza
y se ejecuta el código

"""

"""
Investigación por el profe

Accesibilidad y Usabilidad

Si programo un producto, debe llegar a toda la audiencia sin importar si es no vidente
o cualquier otro problema


¡Qué es accesibilidad?

Un sitio es accesible cuando su contenido está a disponibilidad de todos y literal cualquiera puede manejar su funcionalidad

También se refiere a la experiencia de los usuarios que pueden estar fuera del corto alcance de usuario "típico" que
puede acceder o interactuar con cosas de una manera distinta a la que esperas.

PROBLEMAS DE DISEÑO

Texto con poco contraste
Mucha separación en los elemntos de pantalla
La etiqueta "Remenber details?"
Los colores de la interfaz

Qué tipo de discapacidad encontramos?

visual
motriz
auditiva
cognitiva
edad

Benificios de tener un sitio web accesible

-Google me premia colocandome en una buena posición cuando alguien hace alguna búsqueda,
mi página puede aparecer en el primer lugar


-Mejora la indexación y localización del sitio por buscadores. Participación en la web semántica
-Reducción del mantenimiento(consistencia)
-Escabilidad,crecimiento: nuevas líneas de negocio
-Movilidad en diferentes dispositivos electrónicos
-El número de clientes






"""







           
