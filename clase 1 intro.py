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
        if(n == 0):
            return 0
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
        if(n == 0):
            return 0
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
            print(n)
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


#======================================================================CLASE  5 DE INTRODUCCIÓN======================================================================
                                                                             #SEMANA 3
#PARA RECCORRER y descomponer EL NÚMERO LO QUE SE HACE ES LA DIVISIÓN ENTERA DE 10 O EL MÓDULO DE DIEZ, como contar dígitos


"""
Nombre: esMayoriaPar
Entrada: un número entero positivo
Salida: el resultado de True si en el número ingresado hay más dígitos pares que impares o False si no lo es
Restricciones: el número debe ser entero positivo
"""

#CON LA RESOLUCIÓN DEL PROFESOR
#OTRA SOLUCIÓN LO QUE SE PUEDE HACER ES CREAR UNA FUNCIÓN QUE CUENTE PARES Y LA QUE CUENTE IMPARES
def esMayoriaPar(n):
    if(isinstance(n,int) and n >= 0):
        totalDigitos = digitos(n)
        totalPares = esMayoriaPar_aux(n)
        if(totalPares >= (totalDigitos / 2)):
            return True
        else:
            return False
    else:
        return "Error: el número debe ser entero positivo"

def esMayoriaPar_aux(n):
    if(n < 10):
        if((n % 10) % 2 == 0):
            return 1
        else:
            return 0
    else:
        if((n%10) % 2 == 0):
            return 1 + esMayoriaPar_aux(n//10)
        else:
            return esMayoriaPar_aux(n//10)
    
#========================================================================================
#CON OTRAS FUNCIONES SI LA CANTIDAD DE NÚMEROS PAR ES IGUAL A LA DE NÚMEROS IMPAR DA TRUE
def esMayoriaPar2(n):
    if(isinstance(n,int) and n >= 0):
        return esMayoriaPar2_aux(n)
    else:
        return "Error: el número debe ser entero positivo"

def esMayoriaPar2(n):
    par = contarDigitosPar(n)
    impar = contarDigitosImpar(n)
    if(par >= impar):
        return True
    else:
        return False
        
    

def contarDigitosPar(n):
    if(isinstance(n,int) and n >= 0):
        if(n == 0):
            return 1
        else:
            return contarDigitosPar_aux(n)
    else:
        return "El número debe ser entero positivo"


def contarDigitosPar_aux(n):
    if(n == 0):
        return 0
    else:
        if(n % 2 == 0):
            return 1 + contarDigitosPar_aux(n//10)
        else:
            return contarDigitosPar_aux(n//10)

#...........................................................................
def contarDigitosImpar(n):
    if(isinstance(n,int) and n >= 0):
        if(n == 0):
            return 0
        else:
            return contarDigitosImpar_aux(n)
    else:
        return "El número debe ser entero positivo"


def contarDigitosImpar_aux(n):
    if(n == 0):
        return 0
    else:
        if(n % 2 != 0):
            return 1 + contarDigitosImpar_aux(n//10)
        else:
            return contarDigitosImpar_aux(n//10)


#OTRA SOLUCIÓN SIN UTILIZAR LA FUNCIÓN DE CONTAR DÍGITOS, NO HAGO TANTOS RECORRIDOS, ESTE ES MÁS EFECIENTE, NO ME APOYO DE FUNCIONES APARTE
# SE UTILIZA LE SUMO -1 SI ES UN NÚMERO IMPAR Y 1 SI ES PAR, AL FINAL SI EN LA FUNCIÓN AUXILIAR LA CANTIDAD DE TODO DIO NEGATIVO ENTONCES
#ES FALSO Y SI ES MAYOR O IGUAL QUE CERO ENTONCES ES TRUE

def esMayoriaPar3(n):
    if(isinstance(n,int) and n >= 0):
        totalPares = esMayoriaPar3_aux(n)
        if(totalPares >= 0):
            return True
        else:
            return False
    else:
        return "Error: el número debe ser entero positivo"

def esMayoriaPar3_aux(n):
    if(n < 10):
        if((n % 10) % 2 == 0):
            return 1
        else:
            return -1
    else:
        print(n)
        if((n%10) % 2 == 0):
            return 1 + esMayoriaPar3_aux(n//10)
        else:
            return -1 +esMayoriaPar3_aux(n//10)
    

#===========================================================================================================

#EJERCICIOS DE COMPOSICIÓN, RECORRER EL NÚMERO Y FORMAR OTRO A PARTIR DE ESE.Próxima semana


#======================================================================CLASE  6 DE INTRODUCCIÓN======================================================================
                                                                             #SEMANA 4




#EJERCICIO COMPOSICIÓN

"""
n = 3214
n == 0? NO
              
               potencia = 0
               sacar un dígito
               3214 % 10 = 4
               4 es par? ((4%2 == 0)
                   4*(10**potencia)? 4 *(10**0) = 4 * 1 = 4

n = 321
n == 0? NO
              
               potencia = 1
               sacar un dígito
               321 % 10 = 1
               1 es par? ((1%2 == 0)
                else:
                    pasa a la siguiente recursión (321//10) = 32
                   
n = 32
n == 0? NO
              
               potencia = 1
               sacar un dígito
               32 % 10 = 2
               2 es par? ((2%2 == 0)
                2*(10**potencia) ? 2 *(10**1) = 2 * 10 = 20
n = 3
n == 0? NO
              
               potencia = 2
               sacar un dígito
               3 % 10 = 3
               3 es par? ((3%2 == 0)
               else:
                   pasa a la siguiente recursión (3//10) = 0
                   
n = 0
n == 0? sí Fin de la recursión
              
               potencia = 2
               0 + 4 *(10**0) +  2 *(10**1) = 24                         
                   
                
>>>(2*(10**1)) + (4*(10**0)
24

"""


"""
Nombre: construirPares
Entrada: recibe un número entero positivo
Salida: retorna un nuevo número formado apartir de los dígitos pares que contenía el número original
Restricciones: el número debe ser entero positivo
"""

def construirPares(n):
    if(isinstance(n,int) and n >= 0):
        if(n == 0):
            return 0
        else:
            return construirPares_aux(n,0)
    else:
            return "Error: solo se permiten números enteros positivos"

def construirPares_aux(n,potencia):
    if(n == 0):
        return 0
    else:
        digito = (n%10) #obtengo el último dígito del número
        if((digito % 2) == 0):#si el dígito que obtuve anteriormente es par, entonces hago el siguiente return 
            return (digito *(10**potencia)) + construirPares_aux(n//10,potencia + 1) # el módulo de 10 le quita el último dígito y aumento en uno la potencia
        else:                                                                        #para que se vayan contando las unidades, decenas, centenas y así sucesivamente
            return construirPares_aux(n//10,potencia)# si no encuentra un número par, simplemente quita el dígito y la patencia se mantiene

"""
Nombre: construirImpares
Entrada: recibe un número entero positivo
Salida: retorna un nuevo número formado apartir de los dígitos impares que contenía el número original
Restricciones: el número debe ser entero positivo
"""

def construirImpares(n):
    if(isinstance(n,int) and n >= 0):
        if(n == 0):
            return 0
        else:
            return construirImpares_aux(n,0)
    else:
            return "Error: solo se permiten números enteros positivos"

def construirImpares_aux(n,potencia):
    if(n == 0):
        return 0
    else:
        digito = (n%10) #obtengo el último dígito del número
        if((digito % 2) != 0):#si el dígito que obtuve anteriormente es par, entonces hago el siguiente return 
            return (digito *(10**potencia)) + construirImpares_aux(n//10,potencia + 1) # el módulo de 10 le quita el último dígito y aumento en uno la potencia
        else:                                                                        #para que se vayan contando las unidades, decenas, centenas y así sucesivamente
            return construirImpares_aux(n//10,potencia)# si no encuentra un número par, simplemente quita el dígito y la patencia se mantiene
        
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



#======================================================================CLASE  7 DE INTRODUCCIÓN======================================================================
                                                                             #SEMANA 5
# sin recursión
"""
Nombre: construirNumero
Entrada: m(millares), c(centenas), d(decenas), u(unidades)
Salida: retorna un número de 4 dígitos a partir de los parámetros ingresados
Restricciones: no hay
"""

def construirNumero(m, c, d, u): # 5,6,9,6
    resultado = 0
    resultado = u  * (10**0)     # resultado = 6*(10**0) = 6
    resultado += d * (10**1)     # resultado += 9*(10**1)  => 90 = 96
    resultado += c * (10**2)     # resultado += 6*(10**2)  => 600 = 696
    resultado += m * (10**3)     # resultado += 5*(10**3)  => 5000 = 5696

    return resultado             # 5696 resultado



"""
Nombre: esNumeroPrimo
Entrada: recibe un número entero 
Salida: True si es número primo o False si no lo es
Restricciones: el número debe ser entero positivo
"""

def esNumeroPrimo(num):
    if(isinstance(num,int)):
        if(num == 1 or num == 0):
            return False
        elif(num == 2):
            return True
        else:
            if(num < 0):
                num = -1 * num
                return esNumeroPrimo_aux(num,2)
            else:
                return esNumeroPrimo_aux(num,2)
    else:
        return "Error: el número ingresado debe ser de tipo entero"

def esNumeroPrimo_aux(num,digito):
    if(num == digito):
        return True
    else:
        if((num % digito) == 0):
            return False
        else:
            return  True and esNumeroPrimo_aux(num, digito + 1) # con pila, se puede hacer así con operaciones boolenas
                    #True and True and True = True
                    #True an False = False
    

"""
Nombre: invertirNumero
Entrada: recibe un número entero positivo
Salida: retorna el número ingresado, pero de forma invertida
Restricciones: el número debe ser entero positivo
"""

def invertirNumero(num):
    if isinstance(num, int):
        if (num >= 0):
            if (num <= 10):
                return num
            else:
                return invertirNumero_aux(num, digitos(num)) # digitos es la función de contar cuantos dígitos tiene el número
        else:
            return "Error: elnúmero ingresado debe ser positivo"
    else:
        return "Error: debe ingresar un número entero positivo"


def invertirNumero_aux(num, largo):
    if(largo == 0):
        return 0
    else:
        return (num % 10) * (10 ** (largo - 1))+ invertirNumero_aux(num // 10, largo - 1)


"""
Nombre: construirPrimos
Entrada: un número entero positivo
Salida: retorna un nuevo número formado por los dígitos primos que conforman el dígito original
Restricciones: el número debe ser entero positivo
"""

def construirPrimos(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return 0
        else:
            return construirPrimos_aux(num,0)
    else: "Error: el número debe ser entero positivo"

def construirPrimos_aux(num,potencia):
    if(num == 0):
        return 0
    else:
        digito = num%10
        if(esNumeroPrimo(digito)):
            return (digito *(10**potencia))+ construirPrimos_aux(num//10,potencia+1)
        else:
            return construirPrimos_aux(num//10,potencia)
        




def construirPares(n):
    if(isinstance(n,int) and n >= 0):
        if(n == 0):
            return 0
        else:
            return construirPares_aux(n,0)
    else:
            return "Error: solo se permiten números enteros positivos"

def construirPares_aux(n,potencia):
    if(n == 0):
        return 0
    else:
        digito = (n%10) #obtengo el último dígito del número
        if((digito % 2) == 0):#si el dígito que obtuve anteriormente es par, entonces hago el siguiente return 
            return (digito *(10**potencia)) + construirPares_aux(n//10,potencia + 1) # el módulo de 10 le quita el último dígito y aumento en uno la potencia
        else:                                                                        #para que se vayan contando las unidades, decenas, centenas y así sucesivamente
            return construirPares_aux(n//10,potencia)# si no encuentra un número par, simplemente quita el dígito y la patencia se mantiene

#con for
def divisoresNum():
    print("introduzca el número")
    numero = int(input())
    contador = 0
    print("los divisores de",numero)
    for divisor in range(1,numero+1):
        if(numero % divisor)== 0:
            print(divisor," es divisor")
            contador += 1
    print("el número ",numero,"tiene",contador,"divisores")







#======================================================================CLASE  8 DE INTRODUCCIÓN======================================================================
                                                                             #SEMANA 5
"""
Nombre: digitoMayor
Entrada: recibe un número entero positivo
Salida: retorna el dígito mayor del número
Restricciones: el número debe ser entero positivo
"""

#HECHO POR EL PROFE
def digitoMayor(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return 0
        else:
            return digitoMayor_aux(num)
    else:
        return "Error: el número debe ser entero positivo"

def digitoMayor_aux(num):
    if(num == 0):
        return 0
    else:
        digito = num%10
        return mayor(digito, digitoMayor_aux(num//10))
       
        
def mayor(a,b):
    if(a>= b):
        return a
    else:
        return b

"""
Nombre: triosDigitosMayores
Entrada: un número entero positivo
Salida: retorna el trío de 3 dígitos que sea el mayor del número original
Restricciones: el número debe ser entero positivo
"""

def triosDigitosMayores(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return 0
        else:
            return triosDigitosMayores_aux(num)
    else:
        return "Error: el número debe ser entero positivo"

def triosDigitosMayores_aux(num):
    if(num == 0):
        return 0
    else:
        digito = num%1000
        return mayor(digito, triosDigitosMayores_aux(num//1000))
       


"""
Nombre: tieneCeros
Entrada: un número entero positivo
Salida: retorna True si existe al menos un cero en el número ingresado o False si no es así
Restricciones: el número debe ser entro positivo
"""
def tieneCeros(n):
    if(isinstance(n, int)):
        if(n == 0):
            return True
        else:
            return tieneCeros_aux(n)
    else:
        return "El número debe ser entero"

def tieneCeros_aux(n):
    print(n)
    if(n == 0):
        return False
    else:
        if((n%10) == 0):
            return True
        else:
            return tieneCeros_aux(n//10)

"""
Nombre: contarCeros
Entrada: un número entero positivo
Salida: retorna la cantidad de ceros que tiene el número ingresado
Restricciones: el número debe ser entro positivo
"""
def contarCeros(n):
    if(isinstance(n, int)):
        if(n == 0):
            return 1
        else:
            return contarCeros_aux(n)
    else:
        return "El número debe ser entero"

def contarCeros_aux(n):
    if(n == 0):
        return 0
    else:
        if((n%10) == 0):
            return 1 + contarCeros_aux(n//10)
        else:
            return contarCeros_aux(n//10)

"""
Nombre: potencia
Entrada: recibe un número entero(n) y un exponente entero
Salida: retorna la potencia del número(n) según indique su exponente.
Restricciones: ambos parámetros deben ser enteros positivos, no se puede utilizar el simbolo ** para hacer la potencia
"""
def potencia(n,exponente):
    if(isinstance(n,int) and isinstance(exponente,int)):
        if(exponente == 0):
            return 1
        elif(exponente == 1):
            return n
        
        else:
            return potencia_aux(n,exponente)
    else:
        return "Error: ambos parámetros deben ser de tipo entero positivo"

def potencia_aux(n, exponente):
    if(exponente == 0):
        return 1
    else:
        return n * potencia_aux(n, exponente-1)



"""
Nombre: sumarMitades
Entrada: recibe un número entero
Salida: retorna la suma de las dos mitades del número original
Restricciones: el número debe ser de tipo entero
"""

def sumarMitades(n):
    if(isinstance(n,int)):
        if(n < 0):
            n*= -1
            return sumarMitadesN_aux(n)
        else:
            return sumarMitadesP_aux(n)
    else:
        return "Error: Tipo de dato inválido"

def sumarMitadesN_aux(n):
    largo = digitos(n)
    if(largo == 1):
        n *= -1
        return f"{n}"
    elif(largo % 2 == 0):
        mitad1 = n // (10 ** (largo // 2))
        mitad2 = n % (10 ** (largo // 2))
        mitad1 *= -1
        return mitad1 + mitad2
    else:
         mitad1 = n // (10 ** (largo // 2))
         mitad2 = n % (10 ** ((largo // 2)+ 1))
         mitad1 *= -1
         return mitad1 + mitad2


def sumarMitadesP_aux(n):
     largo = digitos(n)
     if(largo==1):
         return f"{n}"
     if(largo % 2 == 0):
        mitad1 = n // (10 ** (largo // 2))
        mitad2 = n % (10 ** (largo // 2))
        return mitad1 + mitad2
     else:
        mitad1 = n // (10 ** (largo // 2))
        mitad2 = n % (10 ** ((largo // 2)+ 1))
        return mitad1 + mitad2

#Cuenta la cantidad de divisores que tiene un número
def contardivisores(num):
    if(isinstance(num,int)):
        return contardivisores_aux(num,1)
    else:
        return "Error: el número debe ser de tipo entero"

def contardivisores_aux(num,divisor):
    if(num == divisor):
        return 1
    else:
        if((num % divisor) == 0):
            if(esNumeroPrimo(divisor)):
                return 1+ contardivisores_aux(num,divisor+1)
            else:
                return contardivisores_aux(num,divisor+1)
                
        else:
            return contardivisores_aux(num,divisor+1)



           
#Esta función verifica si los dígitos de un número están ordenados de forma asdescendente
def validarSiEsOrdenado(num):
    if(isinstance(num,int)):
        if num == 0:
            return 0
        elif (digitos(num)<2):
            return True
        elif((num%10)<((num//10)%10)):
            return False
        else:
            return validarSiEsOrdenado(num//10)
    else:
        return print("Debe ingresar como parámetro una lista")


def divisoresNum():
    print("introduzca el número")
    numero = int(input())
    contador = 0
    print("los divisores de",numero)
    for divisor in range(1,numero+1):
        if(numero % divisor)== 0:
            print(divisor," es divisor")
            contador += 1
    print("el número ",numero,"tiene",contador,"divisores")


#FORMA EN LA QUE LA HIZO EL TUTOR LUISK
def divisores(num):
    if(isinstance(num,int) and num >= 0):
        return divisores_aux(num,1,1)
    else:
        return "Error: el número debe ser de tipo entero"

def divisores_aux(num,divisor,i):
    if(num == divisor and num < 20):
        return num * i
    elif(num == divisor and num >= 20):
        return num * i * 10
    else:
        if((num % divisor) == 0):
            return (divisor * i) + divisores_aux(num,divisor + 1, i * 10)
        else:
            return divisores_aux(num,divisor + 1, i) 




#====================================================================== CLASE  9 DE INTRODUCCIÓN ======================================================================
                                                                             #SEMANA 6

"""
Nombre: superImpar
Entrada: recibe un número entero positivo llamada num
Salida: retorna True si la cantidad de dígitos impares es mayor a la cantidad de dígitos pares o False si no es así
Restricciones: el número de entrada debe ser de tipo entero
"""

def superImpar(num):
    if(isinstance(num,int) and num >= 0):
        totalImpares = superImpar_aux(num)
        if(totalImpares > 0): #Si dio positivo(mayor a cero) el resultado significa que la cantidad de números impares es mayor a la de los pares
            return True
        else:
            return False
    else:
        return "Error en la entrada"

def superImpar_aux(num):
    if(num < 10):
        if((num % 10) % 2 != 0):
            return 1
        else:
            return -1 #va restando cuando el numero es par 
    else:
        if((num % 10) % 2 != 0):
            return 1 + superImpar_aux(num // 10)
        else:
            return -1 + superImpar_aux(num // 10)



"""
Nombre: paresEnRango
Entrada: recibe un número entero(num), recibe una posición inicial(ini) y una posición final(fin)
Salida: debe retornar un número formado desde la posición inicial hasta la posición final, tomando en cuenta solo los números pares
Restricciones: ls posiciones empiezan en 1 de derecha a izquierda, el num, ini y fin deben ser de tipo entero.
"""

def paresEnRango(num, ini, fin):
    if(isinstance(num,int) and isinstance(ini,int) and isinstance(fin,int)):
        if(largo(num) < fin):
            return "Las posiciones no son válidas"
        elif(ini > fin or largo(num) < ini):
            return "No es posible formar ese número"
        elif(num < 0):
            return paresEnRango_aux(num * -1, ini, fin)*-1
        elif(ini < 0):
            return paresEnRango_aux(num, ini * -1, fin)
        elif(fin < 0):
            return  paresEnRango_aux(num, ini, fin * -1)
        elif(largo(num) < fin):
            return "Las posiciones no son válidas"
        else:
            return paresEnRango_aux(num, ini, fin)
    else:
        return "Error: los parámetros deben ser de tipo entero"


def paresEnRango_aux(num, ini, fin):
    numero = (num//10 ** (ini - 1)) % (10 ** (fin - 1))
    return construirPares_aux(numero,0) #La función está arriba
    

def largo(num):
    if(isinstance(num,int)):
        if(num == 0):
            return 0
        elif(num <0):
            num = num * -1
            return largo_aux(num,0)
        else:
            return largo_aux(num,0)
    else:
        return "El número ingresado debe ser entero "

def largo_aux(num, contador):
    if(num == 0):
        return contador
    else:
        return 1 + largo_aux(num //10, contador)






def desencriptar(num, ini, fin,llave):
    if(isinstance(num,int) and isinstance(ini,int) and isinstance(fin,int) and isinstance(llave,int)):
        if(llave > 0 and llave < 10):
            if(largo(num) < fin):
                return "Las posiciones no son válidas"
            elif(ini > fin or largo(num) < ini):
                return "No es posible formar ese número"
            elif(num < 0):
                return desencriptar_aux(num * -1, ini, fin, llave)*-1
            elif(ini < 0):
                return desencriptar_aux(num, ini * -1, fin, llave)
            elif(fin < 0):
                return  desencriptar_aux(num, ini, fin * -1,llave)
            elif(largo(num) < fin):
                return "Las posiciones no son válidas"
            else:
                return desencriptar_aux(num, ini, fin,llave)
        else:
            return "Error: la llave debe estar entre 1 y 9"
    else:
        return "Error: los parámetros deben ser de tipo entero"


def desencriptar_aux(num, ini, fin,llave):
    numero = (num//10 ** (ini - 1)) % (10 ** (fin - 1))
    return resultado_aux(numero,llave,0) 
    
def resultado_aux(numero,llave,pos):
    if(numero == 0):
        return 0
    else:
        digito = ((numero % 10)%llave)
        return digito ** (10 ** pos) + resultado_aux(numero//10,llave, pos + 1)
    
def corrimientoAEntero(num):
     if(isinstance(num,float) and num > 0 ):
          return int (num * corrimientoAEntero_aux(num))
     else:
          return print("El número ingresado debe ser escrito con decimales y debe ser mayor a cero")
     


 
def corrimientoAEntero_aux(num):
     entero = int(num)
     resta = entero - num
     if(resta == 0):
          return 1
     else:
          return 10 * corrimientoAEntero_aux(num * 10)


"""
Nombre: eliminarDigito
Entradas: dos números enteros positivos, uno será el número y el otro el dígito que deseamos eliminar del número.
Salidas: El número, pero sin el dígito que eliminamos.
Restricciones: el número y el dígito deben ser enteros positivos y el número debe ser diferente de cero.
"""

def eliminarDigito(numero, digito):
     if(isinstance(numero,int) and isinstance(digito,int) and numero >= 0 and digito >= 0):
          if(numero != 0):
               numero=str(numero)
               digito=str(digito)
               return eliminarDigito_aux(numero,digito,"")
          else:
               return print("Error, el número no puede ser cero")
     else:
          return print("Error, ambos números ingresados deben ser enteros positivos")

def eliminarDigito_aux(numero, digito,nuevoNumero):
     if(numero == ""):
          return int(nuevoNumero)
     elif(numero[0] == digito):
        return eliminarDigito_aux(numero[1:], digito, nuevoNumero)
     else:
          return eliminarDigito_aux(numero[1:], digito, nuevoNumero + numero[0])

"""
Nombre: eliminarDigito
Entradas: dos números enteros positivos, uno será el número y el otro el dígito que deseamos eliminar del número.
Salidas: El número, pero sin el dígito que eliminamos.
Restricciones: el número y el dígito deben ser enteros positivos y el número debe ser diferente de cero.
"""

def eliminarDigito(numero, digito):
     if(isinstance(numero,int) and isinstance(digito,int) and numero >= 0 and digito >= 0):
          if(numero != 0):
               numero=str(numero)
               digito=str(digito)
               return eliminarDigito_aux(numero,digito,"")
          else:
               return print("Error, el número no puede ser cero")
     else:
          return print("Error, ambos números ingresados deben ser enteros positivos")

def eliminarDigito_aux(numero, digito,nuevoNumero):
     if(numero == ""):
          return int(nuevoNumero)
     elif(numero[0] == digito):
        return eliminarDigito_aux(numero[1:], digito, nuevoNumero)
     else:
          return eliminarDigito_aux(numero[1:], digito, nuevoNumero + numero[0])



#===================================================================================================================================================================
#===================================================================================================================================================================
                                      #SEMANA 7 CLASE NÚMERO 10 RECURSIVIDAD DE COLA MARTES  7 DE SEPTIEMBRE DEL 2021

#CUANDO UTILIZAMOS UN PROGRAMA, HAY DOS PARTES DE MEMORIA, EN UNA ALMACENA LOS DATOS Y VUELVE A LLAMAR A LA FUNCIÓN CUANDO ES
#CON RECURSIVIDAD DE PILA


#ES MÁS EFICIENTE QUE LA RECURSIVIDAD DE PILA
#USO DE LA MEMORIA, MENOS USO DE LOS RECURSOS INTERNOS
# LOS VALORES QUE ESTAMOS SUMANDO LOS PUEDO ALMACENAR EN UNA VARIABLE( OTRO PARÁMETRO) Y NO EN MEMORIA COMO EN LA RECURSIVIDAD DE PILA
#POR ESTA RAZÓN NO VOY
#DEBEMOS HACER TODOS LOS CÓDIGOS QUE HEMOS HECHO EN RECURSIVIDAD DE PILA A COLA

#SOLO HABLAMOS ESO

#===================================================================================================================================================================

#===================================================================================================================================================================
                                      #SEMANA 7 CLASE NÚMERO 11 RECURSIVIDAD DE COLA JUEVES  9 DE SEPTIEMBRE DEL 2021

#Con recursividad de cola
"""
Nombre: sumarDigitos
Entrada: un número entero positivo
Salida: la suma de los dígitos del número
Restricciones: El número ingresado debe ser entero y positivo
"""

def sumarDigitosCola(n):
    if(isinstance(n,int) and n >= 0):
        if(n == 0):
            return 0
        else:
            return sumarDigitosCola_aux(n//10, n % 10)
    else:
        return "Error: el parámetro debe ser de tipo entero positivo"

def sumarDigitosCola_aux(num, resultado):
    if(num == 0):
        return resultado
    else:
        return sumarDigitosCola_aux(num // 10, resultado + num%10)
    
  

#Con cola
"""
Nombre: sumatoria
Entradas: un número entero positivo
Salida: la suma desde el número hasta cero
Restricciones: el número debe ser entero positivo 

Algoritmo:

a) empezar desde el número original, restarle 1 y a ese resultado sumarle el número anterior, hasta llegar al número 0,
para que al final se dé el resultado de la sumatoria.
"""
#SUMATORIA ASCENDENTE DESDE EL NÚMERO HASTA CERO
def sumatoriaCola(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return 0
        else:
            return sumatoriaCola_aux(num, 0)
    else:
        return "El número debe ser entero positivo"

def sumatoriaCola_aux(num,resultado):
    if(num == 0):
        return resultado
    else:
        return sumatoriaCola_aux(num-1,resultado + num)

    
#Tarea moral hacer hacer la sumatoria de forma ascendente y convertirlo a recursión de cola.


#Cola
"""
Nombre: sumatoriaDescendente
Entradas: un número entero positivo
Salida: la suma desde cero hasta el número
Restricciones: el número debe ser entero positivo
"""
#SUMATORIA A NIVEL ASCENDENTE DESDE 0 HASTA EL NÚMERO
def sumatoriaDescendente(num):
    if(isinstance(num,int) and num >= 0):
        return sumatoriaDescendente_aux(0, num, 0)
    else:
        return "El número debe ser entero positivo"


def sumatoriaDescendente_aux(inicio, fin, resultado):
    if(inicio > fin):
        return resultado
    else:
        print("el valor de num es: ", inicio)
        return sumatoriaDescendente_aux(inicio + 1, fin, resultado + inicio)




#CON COLA    
"""
Nombre: Factorial
Entrada: un número
Salida: el resultado de la multiplicación del número hasta 0
Restricciones: solo se permiten números enteros mayores a cero

"""

def factorialCola(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return 0
        else:
            return factorialCola_aux(num,1)
    else:
        return "Error: el número ingresado debe ser entero positivo"

def factorialCola_aux(num,resultado):
    if(num == 0):
        return resultado
    else:
        return factorialCola_aux(num-1,resultado*num)


"""
Nombre: contarDigitosCola
Entrada: un número entero positivo
Salida: la cantidad de dígitos que posee el número ingresado
Restricciones: El número ingresado debe ser entero y positivo
"""
# cuenta la cantidad de dígitos de un número, utiliza recursividad de cola

def contarDigitosCola(num):
    if(isinstance(num,int) and num >= 0):
        if(num < 10):
            return 1
        else:
            return contarDigitosCola_aux(num,0)
    else:
        return "El número ingresado debe ser entero positivo"

def contarDigitosCola_aux(num, contador):
    if(num == 0):
        return contador
    else:
        return contarDigitosCola_aux(num //10, contador + 1)

#Cola
"""
Nombre: contarDigitosMayores4Cola
Entradas: un número entero positivo
Salida: la cantidad de dígitos mayores a 4 que tiene el número
Restricciones: el número debe ser entero positivo
"""

def contarDigitosMayores4Cola(n):
    if(isinstance(n,int) and n >= 0):
        return contarDigitosMayores4Cola_aux( n,0)
    else:
        return "Error: en número debe ser entero positivo"

          
def contarDigitosMayores4Cola_aux(n, contador):
    if(n == 0):
        return contador
    else:
        if(n%10 > 4):
            return contarDigitosMayores4Cola_aux( n//10, contador + 1)
        else:
            return contarDigitosMayores4Cola_aux( n//10,contador)

"""
Nombre: sumarDigitosMayores4Cola
Entradas: un número entero positivo
Salida: la suma de los dígitos mayores a 4 que tiene el número
Restricciones: el número debe ser entero positivo
"""
def sumarDigitosMayores4Cola(n):
    if(isinstance(n,int) and n >= 0):
        return sumarDigitosMayores4Cola_aux( n, 0)
    else:
        return "Error: en número debe ser entero positivo"

def sumarDigitosMayores4Cola_aux(n,resultado):
    if(n == 0):
        return resultado
    else:
        if(n%10 > 4):
            return sumarDigitosMayores4Cola_aux( n//10, resultado+ n%10)
        else:
            return sumarDigitosMayores4Cola_aux( n//10, resultado)



"""
Nombre: FibonacciCola
Entradas: un número entero positivo
Salidas: el resultado de la suma recursiva propia del Fibonacci del número ingresado
Restricciones: el número debe ser entero positivo
"""

def FibonacciCola(n):
    if(isinstance(n,int) and n >= 0):
        if(n == 0):
            return 0
        elif(n == 1):
            return 1
        else:
            return  FibonacciCola_aux(n,0)           
    else:
        return "El número entero debe ser entero positivo"

def FibonacciCola_aux(n,resultado):
    if(n == 0):
        return resultado
    else:
        print(n-1 + n-2)
        return FibonacciCola_aux(n-1,resultado + n-1 + n-2)

#Arreglar
    
   
#======================================================================CLASE  12 DE INTRODUCCIÓN======================================================================
                                                                             #SEMANA 8



"""
Nombre: invertirNumeroCola
Entrada: recibe un número entero positivo
Salida: retorna el número ingresado, pero de forma invertida
Restricciones: el número debe ser entero positivo
"""

def invertirNumeroCola(num):
    if isinstance(num, int):
        if (num >= 0):
            if (num <= 10):
                return num
            else:
                return invertirNumeroCola_aux(num, digitos(num),0) # digitos es la función de contar cuantos dígitos tiene el número
        else:
            return "Error: elnúmero ingresado debe ser positivo"
    else:
        return "Error: debe ingresar un número entero positivo"


def invertirNumeroCola_aux(num, largo,resultado):
    if(largo == 0):
        return resultado
    else:
        resultado += (num % 10) * (10 ** (largo - 1))
        return invertirNumeroCola_aux(num // 10, largo - 1, resultado)

def digitos(n):
    if(isinstance(n,int) and n >= 0):
        if(n < 10):
            return 1
        else:
            return 1 + digitos( n//10)
        
    else:
        return "Error: en número debe ser entero positivo"


"""
Nombre: sonImparesCola
Entrada: recibe como parámetro un número entero positivo llamado (num)
Salida: retorna True si se encuentra al menos un dígito impar en el número original
Restriciones: el número debe ser de tipo entero
"""


def sonImparesCola(num):
    if(isinstance(num,int)):
        return sonImparesCola_aux(num)
    else:
        return "Error: Tipo de parámetro es incorrecto"

def sonImparesCola_aux(num):
    if(num == 0):
        return True
    elif(num < 10):
        if((num%2) == 0):
            return False
        else:
            return True
    else:
        if(((num % 10)% 2) == 0):
            return False
        else:
            return sonImparesCola_aux(num//10)


"""
Nombre: construirNumeroCola
Entrada: un número entero(n) y un divisor el cual tiene que ser mayor a 0 y menor a 10
Salida: retorna un nuevo número a partir de los dígitos que sean divisibles por el parámetro divisor
Restricciones: solo números enteros positivos, el cero no cuenta.
"""

def construirNumeroCola(n,divisor):
    if(isinstance(n,int) and isinstance(divisor,int)):
        if(n >= 0):
            if(divisor > 0 and divisor < 10):
                return construirNumeroCola_aux(n,divisor,0,0)
            else:
                return "Error: el número divisor debe ser mayor que cero y menor que 10"
        else:
            return "Error: el número debe ser positivo mayor que cero"
    else:
        return "Error: el número debe ser de tipo entero"

def construirNumeroCola_aux(n,divisor,potencia,resultado):
    if(n == 0):
        return resultado
    else:
        digito = (n%10) 
        if(digito != 0):
            if((digito % divisor) == 0):
                resultado += (digito *(10**potencia))
                return construirNumeroCola_aux(n//10,divisor,potencia + 1, resultado)
            else:                                                                       
                return construirNumeroCola_aux(n//10,divisor,potencia, resultado)
        else:                                                                       
            return construirNumeroCola_aux(n//10,divisor,potencia,resultado)


#======================================================================CLASE  13 DE INTRODUCCIÓN======================================================================
#LISTAS                                                                       #SEMANA 9


"""
Listas: son como conjuntos

En un lista se inicia en el índice 0 de izquierda a derecha
>>> a = [23,"23",False,23.1,[52,1,[],88,"A"]]
>>> a[2]
False
>>> a[4]
[52, 1, [], 88, 'A']


De derecha a izquierda se empieza con -1, son números negativos
>>> a[-1]
[52, 1, [], 88, 'A']

Para hacer cortes en las listas de izquierda a derecha, escribo en donde inicio y en donde quiero finalizar

>>> a[2:4]
[False, 23.1]

Para hacer cortes de derecha a izquierda en las listas , escribo en donde inicio y en donde quiero finalizar, pero con negativos
>>> a[-4:-2]
['23', False]
>>>


>>> a[1:]
['23', False, 23.1, [52, 1, [], 88, 'A']]
>>> a[2:]
[False, 23.1, [52, 1, [], 88, 'A']]

"""

#EJERCICIOS REALIZADOS POR EL PROFESOR

"""
Nombre: largoLista
Entrada: lista: lista de elementos
Salidas: Retorna la cantidad de elementos que contiene la lista
Restricciones: la entrada tiene que ser lista
"""

def largoLista(lista):
    if(isinstance(lista,list)):
        return largoLista_aux(lista,0)
    else:
        return "Error: tipo de dato diferente a lista"

def largoLista_aux(lista,resultado):
    if(lista == []):
        return resultado
    else:
        return largoLista_aux(lista[1:],resultado + 1)  #[1:] le quita el primer elemento de la lista y devuelve los elementos que están depués de
                                                             #ese indice
                                                            
"""
Nombre: sumarElementosLista
Entrada: lista: lista de elementos
Salidas: Retorna la suma de cada uno de los elementos numéricos que contiene la lista
Restricciones: la entrada tiene que ser lista
"""        
       
def sumarElementosLista(lista):
    if(isinstance(lista,list)):
        return sumarElementosLista_aux(lista,0)
    else:
        return "Error: tipo de dato diferente a lista"

def sumarElementosLista_aux(lista,resultado):
    if(lista == []):
        return resultado
    else:
        return sumarElementosLista_aux(lista[1:],resultado + lista[0]) #[1:] le quita el primer elemento de la lista y devuelve los elementos que están depués de
                                                             #ese indice
"""
Nombre: numeroMayorLista
Entrada: lista: lista de elementos
Salidas: Retorna el dígito mayor que contiene la lista
Restricciones: la entrada tiene que ser lista
"""                                                              
        
def numeroMayorLista(lista):
    if(isinstance(lista,list)):
        return numeroMayorLista_aux(lista,0)
    else:
        return "Error: tipo de dato diferente a lista"

def numeroMayorLista_aux(lista,resultado):
    if(lista == []):
        return resultado
    elif(lista[0]>resultado):
        return numeroMayorLista_aux(lista[1:], lista[0])
    else:
        return numeroMayorLista_aux(lista[1:], resultado)
        
"""
nombre: eliminarRepetidos
entrada: lista=una lista
salida: la lista pero sin los datos repetidos
restrincciones: debe ser una lista el dato a ingresar y que no sea una lista vacio
"""

    
def eliminarRepetidos(lista):
    if(isinstance(lista,list)and lista!=[]):
        return eliminarRepetidos_aux(lista[1:],[lista[0]])
        
    else:
        print("Error, Ingrese una lista y que no este vacio")

#--------------------------------------------------------
"""
nombre: eliminarRepetidos_aux
entrada:lista y un []
salidad: una lista sin datos repetido
restricciones: 


"""

def eliminarRepetidos_aux(lista,result):
    if(lista==[]):
        return result
    elif(comprobarSiExiste(lista,result)==0):
        return eliminarRepetidos_aux(lista[1:],result)
    else:
        return eliminarRepetidos_aux(lista[1:],result+[lista[0]])

"""
nombre: comprobarSiExiste
entrada: lista y result = a dos lista
salida: 0 o 1,return 0 si en la lista result esta el dato del indice 0 de la lista
y 1 en caso que no se encuentre.
restrincciones: debe ser listas
"""
def comprobarSiExiste(lista,result):
    if(result==[]):
        return 1
    elif(lista[0] == result[0]):
        return 0
    else:
        return comprobarSiExiste(lista,result[1:])


