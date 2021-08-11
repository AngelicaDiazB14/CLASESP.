#================================================================= CLASE 1 DE INTRODUCCIÓN ========================================================================
#SUMATORIA
#FACTORIAL
#DÍGITOS
#TODOS CON RECURSIVIDAD DE PILA
 
"""
Nombre: sumatoria
Entradas: un número entero positivo
Salida: la suma desde el número hasta cero
Restricciones: el número debe ser entero positivo 

Algoritmo:

a) empezar desde el número original, restarle 1 y a ese resultado sumarle el número anterior, hasta llegar al número 0,
para que al final se dé el resultado de la sumatoria.
"""
def sumatoria(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return 0
        else:
            return num + sumatoria(num-1)
    else:
        return "El número debe ser entero positivo"
    
"""
Nombre: Factorial
Entrada: un número
Salida: el resultado de la multiplicación del número hasta 0
Restricciones: solo se permiten números enteros mayores a cero


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

"""
Nombre: cantidadDigitos
Entrada: un número entero positivo
Salida: la cantidad de dígitos que posee el número ingresado
Restricciones: El número ingresado debe ser entero y positivo

Algoritmo:

a) iniciar desde derecha a izquierda quitando dígito por dígito utilizando la división entera de 10, hasta que el número inicial sea 0
y cada vez que se haga una división entera, se va a acumular un 1 para que al final se puedan sumar los 1, los cuales van a indicar cuantos dígitos tenía
el número original
        
Ejemplo:

120 //10 = 12       1
12//10 = 1          1
1//10 = 0           1
                 +  3
"""
#.......................................................................................
# cuenta la cantidad de dígitos de un número, utiliza recursividad de cola
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
# cuenta la cantidad de dígitos de un número, utiliza recursividad de  Pila

def digitos(n):
    if(isinstance(n,int) and n >= 0):
        if(n < 10):
            return 1
        else:
            return 1 + digitos( n//10)
        
    else:
        return "Error: en número debe ser entero positivo"

"""
n = 123
return 1+ digitos(1+digitos(1))
return 1+ digitos(1 + 1)
return 1 + 2
return 3
expansión y después compresión

"""



#===========================================================================CLASE 2 DE INTRODUCCIÓN====================================================================
#SumarDigitos
#ContarDigitosMayores4
#sumarDigitosMayores4


#SE REALIZA UN PROCESO DE DESCOMPOSICIÓN DEL NÚMERO
"""
Nombre: sumarDigitos
Entrada: un número entero positivo
Salida: la suma de los dígitos del número
Restricciones: El número ingresado debe ser entero y positivo

Algoritmo:

el número original se debe obtener dígito por dígito de derecha a izquierda, luego de eso agarra el dígito que quitó y lo
va a tener guardado, luego para poder quitar el el dígito que ya agarró lo que se hace es al número original hacerle división
entera de 10, luego vuelve a obter el último dígito del resultado de la división entera y a ese número lo suma con el anterior
que ya había obtenido y así sucesivamente hasta que el número original sea menor que diez, ese número final también será sumado con
los módulos anteriores para que al final retorne el resultado de la suma de todos los dígitos del número


EJEMPLO:

el modulo de % 10 me da el último dígito del número.


123%10 (3) + 123//10=(12)
12%10  (2) + 12//10=(1)
1%10   (1) + 1//10=(0)
    + -----
       (6)
"""


def sumarDigitos(n):
    if(isinstance(n,int) and n >= 0):
        if n < 10:
            return n #condición de parada
        else:
            return (n%10) + sumarDigitos(n // 10)
    else:
        return "Error"
#.......................................................................................
#1-PRÁCTICA- CONTARDIGITOSMAYORES4
#CONTAR DÍGITOS MAYORES A 4

"""
Nombre: contarDigitosMayores4
Entradas: un número entero positivo
Salida: la cantidad de dígitos mayores a 4 que tiene el número
Restricciones: el número debe ser entero positivo
"""
def contarDigitosMayores4(n):
    if(isinstance(n,int) and n >= 0):
        if(n < 10):
            return 1
        else:
            if(n%10 > 4):
                return 1 + contarDigitosMayores4( n//10,)
            else:
                return contarDigitosMayores4( n//10)
    else:
        return "Error: en número debe ser entero positivo"

#2-PRÁCTICA SUMARDIGITOSMAYORES4
# SUMA SOLO LOS DIGITOS QUE SEAN MAYORES QUE 4

"""
Nombre: sumarDigitosMayores4
Entradas: un número entero positivo
Salida: la suma de los dígitos mayores a 4 que tiene el número
Restricciones: el número debe ser entero positivo
"""
def sumarDigitosMayores4(n):
    if(isinstance(n,int) and n >= 0):
        if(n < 10):
            return n
        else:
            if(n%10 > 4):
                return (n%10)+ sumarDigitosMayores4( n//10,)
            else:
                return sumarDigitosMayores4( n//10)
    else:
        return "Error: en número debe ser entero positivo"


#======================================================================CLASE 3 DE INTRODUCCIÓN======================================================================

#Fibonacci
#fib_V2 con función auxiliar
#contarDigitos_V2 con función auxiliar
#sumatoria_V2 con función auxiliar

"""
Nombre: Fibonacci
Entradas: un número entero positivo
Salidas: el resultado de la suma recursiva propia del Fibonacci del número ingresado
Restricciones: el número debe ser entero positivo

Ejemplo de corrida del fibonacci de 3
fib(3)=
fib(3)=fib(2)   +  fib(1)
      =fib(2-1) + fib(2-2) + 1
      =fib(1)   + fib(0)   + 1
      = 1       +     0    + 1
      = 2

fib(3)=2


Ejemplo de fibonacci de 5

fib(5)=
fib(5)=           fib(4)                                             +             fib(3)
                  fib(3)    +    fib(2)                              +             fib(2)   +   fib(1)
                  fib(2)    +    fib(1) + fib(1) + fib(0)            +             fib(1)   +   fib(0) + 1
                    1       +      1    +   1    +    0              +               1      +     0    + 1
                                        3                            +                       2
                  ------------------------------------------------------------------------------------------
                                                                     5
"""
def Fibonacci(n):
    if(isinstance(n,int) and n >= 0):
        if(n == 0):
            return 0
        elif(n == 1):
            return 1
        else:
            return  Fibonacci(n-1) + Fibonacci(n-2)
    else:
        return "El número entero debe ser entero positivo"

#...................................................................FUNCIONES CON FUNCIÓN AUXILIAR...................................................................


"""
Nombre: contarDigitos_V2
Entrada: un número entero positivo
Salida: la cantidad de dígitos que posee el número ingresado
Restricciones: El número ingresado debe ser entero y positivo
"""
def contarDigitos_V2(n):
    if(isinstance(n,int) and n >= 0):
        if(n == 0):
            return 0
        else:
            return contarDigitos_aux(n)
    else:
        return "El número debe ser entero positivo"


def contarDigitos_aux(n):
    if(n<10):
        return 1
    else:
        return 1 + contarDigitos_aux(n//10)

"""
Nombre: Fib_V2
Entradas: un número entero positivo
Salidas: el resultado de la suma recursiva propia del Fibonacci del número ingresado
Restricciones: el número debe ser entero positivo
"""
        

def fib_V2(n):
    if(isinstance(n,int)):
       if(n >= 0):
           return fib_V2_aux(n)
       else:
            return "El número debe ser positivo"
    else:
        return "El número debe ser entero "

def fib_V2_aux(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return  fib_V2_aux(n-1) + fib_V2_aux(n-2)


 
"""
Nombre: sumatoria_V2
Entradas: un número entero positivo
Salida: la suma desde cero hasta el número
Restricciones: el número debe ser entero positivo
"""
#SUMATORIA A NIVEL ASCENDENTE DESDE 0 HASTA EL NÚMERO
def sumatoria_V2(num):
    if(isinstance(num,int) and num >= 0):
        return sumatoriaV2_aux(0, num)
    else:
        return "El número debe ser entero positivo"


def sumatoriaV2_aux(inicio, fin):
    if(inicio > fin):
        return 0
    else:
        print("el valor de num es: ", inicio)
        return inicio + sumatoriaV2_aux(inicio + 1, fin)

#======================================================================CLASE 4 DE INTRODUCCIÓN======================================================================
                                                                             #SEMANA 3
#esPar
#esImpar



"""
Nombre: esPar
Entrada: n, un número entero positivo
Salida: el resultado de True si el número es par o False si no lo es
Restricciones: el número debe ser entero positivo mayor o igual a cero
"""

def esPar(n):
    if(isinstance(n,int) and n >= 0):
        if((n %2) == 0):
            return True
        else:
            return False
    else:
        return "Error el número debe ser entero positivo"

"""
Nombre: esImpar
Entrada: n, un número entero positivo
Salida: el resultado de True si el número es impar o False si no lo es
Restricciones: el número debe ser entero positivo mayor o igual a cero
"""

def esImpar(n):
    if(isinstance(n,int) and n >= 0):
        if((n %2) != 0):
            return True
        else:
            return False
    else:
        return "Error el número debe ser entero positivo"

#................................................................................
#Práctica

#Sumar dígitos impares

"""
Nombre: sumarDigitosImpares
Entrada:un número entero
Salida: el resultado de la suma de todos los digitos impares que componen el número
Restricciones: el número debe ser entero positivo
###
"""

def sumarDigitosImpares(n):
    if(isinstance(n,int) and n >= 0):
        return sumarDigitosImpares_aux(n)
    else:
        return "Error: el número debe ser entero positivo"


def sumarDigitosImpares_aux(n):
    if(n == 0):
        return 0
    else:
        if((n%2) != 0):
            return (n%10) + sumarDigitosImpares_aux(n // 10)  # n%10 obtengo el úñtimo dígito del número, n//10 quita el último dígito del número
        else:
            return sumarDigitosImpares_aux(n // 10)
"""
Nombre: sumarDigitosPares
Entrada:un número entero
Salida: el resultado de la suma de todos los digitos pares que componen el número
Restricciones: el número debe ser entero positivo
"""

def sumarDigitosPares(n):
    if(isinstance(n,int) and n >= 0):
        return sumarDigitosPares_aux(n)
    else:
        return "Error: el número debe ser entero positivo"


def sumarDigitosPares_aux(n):
    if(n == 0):
        return 0
    else:
        if((n%2) == 0):
            return (n%10) + sumarDigitosPares_aux(n // 10)  # n%10 obtengo el úñtimo dígito del número, n//10 quita el último dígito del número
        else:
            return sumarDigitosPares_aux(n // 10)

"""
Nombre: multiplicarDigitosPares
Entrada: un número entero positivo
Salida: el resultado de la multiplicación de todos los digitos pares que componen el número
Restricciones: el número debe ser entero positivo
"""

def multiplicarDigitosPares(n):
    if(isinstance(n,int) and n >= 0):
        return multiplicarDigitosPares_aux(n)
    else:
        return "Error: el número debe ser entero positivo"


def multiplicarDigitosPares_aux(n):
    if(n == 0):
        return 1
    elif((n%2) == 0):
        if((n%10) != 0):
            return (n%10) * multiplicarDigitosPares_aux(n // 10)  # n%10 obtengo el úñtimo dígito del número, n//10 quita el último dígito del número
        else:
            return multiplicarDigitosPares_aux(n // 10)
    else:
            return multiplicarDigitosPares_aux(n // 10)


"""
Nombre: multiplicarDigitosImpares
Entrada: un número entero positivo
Salida: el resultado de la multiplicación de todos los digitos impares que componen el número
Restricciones: el número debe ser entero positivo
"""

def multiplicarDigitosImpares(n):
    if(isinstance(n,int) and n >= 0):
        return multiplicarDigitosImpares_aux(n)
    else:
        return "Error: el número debe ser entero positivo"


def multiplicarDigitosImpares_aux(n):
    if(n == 0):
        return 1
    elif((n%2) != 0):
        if((n%10) != 0):
            return (n%10) * multiplicarDigitosImpares_aux(n // 10)  # n%10 obtengo el úñtimo dígito del número, n//10 quita el último dígito del número
        else:
            return multiplicarDigitosImpares_aux(n // 10)
    else:
            return multiplicarDigitosImpares_aux(n // 10)



##########################  HAY TAREA EN GIT HUB entregar el viernes
        
#contarTriosDeDigitos
#contarDigitosPares
#sumatoriaParcial tiene un inicio y un fin, si quiero contar de 3 a 5 y así sucesivamente. el dígito final debe ser mayor o igual al número inicial
#multiplicacion operador 1, operador 2 el primero es la cantidad de veces se que va a multiplicar el operador 2















    
