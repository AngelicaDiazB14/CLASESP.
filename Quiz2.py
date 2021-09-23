"""
Nombre: esCapicua
Entrada: recibe un número entero positivo
Salida: retorna True si se le aplica invertirNumero al número original y este da como resultado
el mismo número, o False si esto el número inverso es diferente al original
Restricciones: el número debe ser de tipo entero positivo
"""


def esCapicua(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return True
        else:
            return esCapicua_aux(num)
    else:
        return "Error: el número debe ser de tipo entero"

def esCapicua_aux(num):
    if(invertirNumero(num) == num):
        return True
    else:
        return False


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

def digitos(n):
    if(isinstance(n,int) and n >= 0):
        if(n < 10):
            return 1
        else:
            return 1 + digitos( n//10)
        
    else:
        return "Error: en número debe ser entero positivo"


"""
Nombre: dividirMitades
Entrada: recibe un número entero
Salida: retorna el número dividido en dos partes, si la cantidad de dígitos es par entonces el número se divide
en partes iguales, pero si es impar, el dígito del medio del número será compartido por ambas partes
Restricciones: debe ser un número entero, si el número es negativo, su signo se debe distribuir en ambas partes.
"""



def dividirMitades(n):
    if(isinstance(n,int)):
        if(n < 0):
            n*= -1
            return dividirMitadesN_aux(n)
        else:
            return dividirMitadesP_aux(n)
    else:
        return "Error: Tipo de dato inválido"

def dividirMitadesN_aux(n):
    largo = digitos(n)
    if(largo == 1):
        n *= -1
        return f"{n}"
    elif(largo % 2 == 0):
        mitad1 = n // (10 ** (largo // 2))
        mitad2 = n % (10 ** (largo // 2))
        mitad1 *= -1
        mitad2 *= -1
        return f"{mitad1} y {mitad2}"
    else:
         mitad1 = n // (10 ** (largo // 2))
         mitad2 = n % (10 ** ((largo // 2)+ 1))
         mitad1 *= -1
         mitad2 *= -1
         return f"{mitad1} y {mitad2}"



def dividirMitadesP_aux(n):
     largo = digitos(n)
     if(largo==1):
         return f"{n}"
     if(largo % 2 == 0):
        mitad1 = n // (10 ** (largo // 2))
        mitad2 = n % (10 ** (largo // 2))
        return f"{mitad1} y {mitad2}"
     else:
        mitad1 = n // (10 ** (largo // 2))
        mitad2 = n % (10 ** ((largo // 2)+ 1))
        return f"{mitad1} y {mitad2}"



"""
Nombre: construirNumeroEspecial
Entrada: un número entero positivo
Salida: retorna un número nuevo a partir del cálculo del factorial del número "sumado" con el factorial del mismo número
Restricciones: el número debe ser entero positivo
"""
        
def construirNumeroEspecial(num):
    if(isinstance(num,int) and num >= 0):
        num1 = Fibonacci(num)
        num2 = factorial(num)
        return construirNumeroEspecial_aux(num1,num2)
    else:
        return "Error: el número debe ser entero positivo"

def construirNumeroEspecial_aux(num1,num2):
    largo = digitos(num1)
    return num2 * 10 ** largo + num1
            
"""
Nombre: Factorial
Entrada: un número
Salida: el resultado de la multiplicación del número hasta 0
Restricciones: solo se permiten números enteros mayores a cero

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
Nombre: Fibonacci
Entradas: un número entero positivo
Salidas: el resultado de la suma recursiva propia del Fibonacci del número ingresado
Restricciones: el número debe ser entero positivo
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
