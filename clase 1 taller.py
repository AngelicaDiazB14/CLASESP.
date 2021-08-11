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

def escribirArchivo(nombreArchivo,mensaje): #función para escribir en un archivo archivo
    file = open(nombreArchivo, "w") # open: abre el archivo,  w = write
    file.write(mensaje)#escribe en el archivo
    file.close()#cierra el archivo














    



           
