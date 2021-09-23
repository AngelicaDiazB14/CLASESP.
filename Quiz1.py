#QUIZ 1 INTRODUCCIÓN
#ANGÉLICA D+IAZ BARRIOS
#2021044256

"""
Nombre: tieneDigitosImpares
Entrada: recibe como parámetro un número entero positivo llamado (num)
Salida: retorna True si se encuentra al menos un dígito impar en el número original
Restriciones: el número debe ser de tipo entero
"""


def tieneDigitosImpares(num):
    if(isinstance(num,int)):
        return tieneDigitosImpares_aux(num)
    else:
        return "Error: Tipo de parámetro es incorrecto"

def tieneDigitosImpares_aux(num):
    if(num == 0):
        return False
    else:
        if(num % 2 != 0):
            tieneDigitosImpares_aux(num//10)
            return True
        else:
            return tieneDigitosImpares_aux(num//10)





"""
Nombre: contarDigitosDivisores
Entrada: recibe un número entero llamado(num) y recibe otro número mayor a 0 y menor a 10 llamado(divisor)
Salida: retorna la cantidad de dígitos que son divisibles entre el divisor
Restricciones: el num debe ser de tipo entero, el parámetro divisor debe ser entero y estar entre 1 y 9 y el 0 se debe omitir
"""

def contarDigitosDivisores(num,divisor):
    if(isinstance(num,int)):
        if(isinstance(divisor,int)):
            if(divisor > 0 and divisor <10):
                return contarDigitosDivisores_aux(num,divisor)
            else:
                return "Error: el parámetro divisor debe estar entre un rango de 1 y 9"
        else:
            return "Error: Parámetro divisor es incorrecto"
    else:
        return "Error: Parámetro num es incorrecto"


def contarDigitosDivisores_aux(num,divisor):
    if(num == 0):
        return 0
    else:
        if((num%10) != 0):
            if((num%10) % divisor == 0):
                return 1 + contarDigitosDivisores_aux(num//10,divisor)
            else:
                return contarDigitosDivisores_aux(num//10,divisor)
        else:
                return contarDigitosDivisores_aux(num//10,divisor)

"""
Nombre: sumatoriaRango
Entrada: recibe un número entero positivo llamado (num) y recibe otro número entero positivo que representa la distancia
Salida: retorna la sumatoria del número desde 0 hasta el mismo número pero indicado por la distancia
Restricciones: ambos parámetros deben ser de tipo entero y el parámetro distancia debe ser menor o igual al número
"""

def sumatoriaRango(num,distancia):
    if(isinstance(num,int)):
        if(isinstance(distancia,int)):
            if(num >= 0 and distancia <= num):
                return sumatoriaRango_aux(0,num,distancia)
            else:
                return 0
        else:
            return "Error: Parámetro distancia es incorrecto"
    else:
        return "Error: Parámetro num es incorrecto"

def sumatoriaRango_aux(inicio,num,distancia):
    if(inicio > num):
        return 0 #Fin de la recursión
    else:
        return inicio + sumatoriaRango_aux(inicio + distancia, num, distancia)


       
"""
Nombre: contarGruposDeDigitos
Entrada: recibe un número entero llamado num y otro parámetro llamdo grupos
Salida: retorna la cantidad de grupos que hay en el número con respecto a la indicación dada por el parámetro grupos
Restricciones: ambos parámetros deben ser de tipo entero y el parámetro grupos debe ser mayor a 0 y menor a 10
"""

def contarGruposDeDigitos(num,grupos):
    if(isinstance(num,int) and isinstance(grupos,int)):
        if(grupos > 0 and grupos < 10):
            return contarGruposDeDigitos_aux(num,grupos)
        else:
            return "Error: el parámetro grupos debe ser mayor a 0 y menor a 10"
    else:
        return "Error: Solo es permitido número de tipo entero"

def contarGruposDeDigitos_aux(num,grupos):
    if(largo(num) < grupos):
        return 0
    else:
        if(num % (10 **grupos)):
            return 1 + contarGruposDeDigitos_aux(num//(10**grupos), grupos)
        else:
            return 1 + contarGruposDeDigitos_aux(num//(10**grupos), grupos)





"""
Nombre: largo
Entrada: un número entero
Salida: la cantidad de dígitos que posee un número
Restricciones: el número debe ser entero
"""
def largo(n):
    if(isinstance(n,int)):
        if(n == 0):
            return 0
        else:
            if(n >= 0):
                return 1 + largo(n//10)
            else:
                n = n * -1
                return 1 + largo(n//10)



                  
