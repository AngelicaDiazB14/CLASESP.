"""
Nombre: divisores
Entrada: recibe un número entero(num) mayor o igual a cero
Salida: imprime los números divisores del num consultado
Restricciones: el número debe ser de tipo entero
"""



def divisores(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return 0
        else:
            return divisores_aux(num,num)
            
    else:
        return "El número debe ser mayor a cero y positivo"

def divisores_aux(num, divisor):
    if(divisor == 1):
        return str(divisor)
    else:
        if((num % divisor) == 0): 
            return str(str(divisor) + ", ") + divisores_aux(num, divisor - 1)
        else:
            return divisores_aux(num, divisor - 1)



"""
Nombre: potenciaRecusivo
Entrada: recibe un número entero(base) y un exponente entero
Salida: retorna la potencia del número(base) según indique su exponente.
Restricciones: ambos parámetros deben ser enteros positivos, no se puede utilizar el simbolo ** para hacer la potencia
"""
def potenciaRecursivo(base,exponente):
    if(isinstance(base,int) and isinstance(exponente,int) and base >= 0 and exponente >= 0):
        if(exponente == 0):
            return 1
        elif(exponente == 1):
            return base
        
        else:
            return potenciaRecursivo_aux(base,exponente)
    else:
        return "Error: ambos parámetros deben ser de tipo entero positivo"

def potenciaRecursivo_aux(base, exponente):
    if(exponente == 0):
        return 1
    else:
        return base * potenciaRecursivo_aux(base, exponente-1)

"""
Nombre: divisionRecusivo
Entrada: recibe un número entero llamado dividendo y otro número entero llamado divisor
Salida: retorna la división del número dividendo entre el divisor
Restricciones: amos parámetro deben ser de tipo entero positivos, la divión entre cero no existe.
"""

def divisionRecursivo(dividendo,divisor):
    if(isinstance(dividendo,int) and isinstance(divisor,int)):
        if(divisor >= 0 and dividendo >= 0):
            if(divisor != 0):
                return divisionRecursivo_aux(dividendo,divisor)
            else:
                return "Error: División entre cero"
        else:
            return "Error: el dígito debe ser positivo mayor a cero y el número a dividir debe ser mayor o igual a cero"
    else:
        return "Error: ambos parámetros deben ser de tipo entero"

def divisionRecursivo_aux(dividendo,divisor):
    if(divisor == 0):
        return 0
    elif(dividendo < 0):
        return -1
    else:
        return 1 + divisionRecursivo_aux(dividendo-divisor,divisor)

"""
Nombre: corrimientoAEntero
Entrada:recibe un número flotante
Salida: retorna el mismo número ingresado, pero sin la coma. Es decir se convierte en entero el número
Restricciones: el número debe ser de tipo flotante, puede ser positivo o negativo (se debe mantener el signo)
"""

def corrimientoAEntero(num):
    if(isinstance(num,float)):
        Num = num*10000000000
        Num = int(Num)
        if(num < 0):
            return corrimientoAEntero_aux(Num*-1)*-1
        else:
            return corrimientoAEntero_aux(Num)
    else:
        return "Error: el número debe ser de tipo flotante"

def corrimientoAEntero_aux(num):
    if(num==0):
        return 0
    elif(num % 10 == 0):
        return corrimientoAEntero_aux(num // 10)
    else:
        return num + corrimientoAEntero_aux(num % 10 // 10)


"""
Nombre: contarDigitosFlotante
Entrada: recibe un número de tipo flotante
Salida: retorna la cantidad de dígitos que tiene el número ingresado
Restricciones: el número debe ser de tipo flotante, ya sea negativo o positivo
"""

def contarDigitosFlotante(num):
    if(isinstance(num,float)):
        if(num < 0):
            numero = corrimientoAEntero(num*-1)
            return contarDigitosFlotante_aux(numero)
        else:
            numero = corrimientoAEntero(num)
            return contarDigitosFlotante_aux(numero)
    else:
        "Error: el número debe ser de tipo coma flotante"
        
def contarDigitosFlotante_aux(num):
    if(num == 0):
        return 0
    else:
        return 1 + contarDigitosFlotante_aux(num//10)


"""
Nombre: indiceNumero
Entrada: recibe un número entero positivo(num) y  un índice entero positivo(indice)
Salida: retorna el dígito que se encuentra según la posición del indice indicado
Restricciones: ambos parámetros deben ser de tipo entero positivo
"""


def indiceNumero(num,indice):
    if(isinstance(num,int)and num >= 0 and isinstance(indice,int)and indice >= 0):
        if(indice < largoNum(num-1)):
            largo = largoNum(num)
            comparar = num-1
            return indiceNumero_aux(num, indice+1, largo, comparar) #indice+1 porque los indices siempren empiezan en la posición cero, entonces al
        else:                                                 #indice original se le aumenta uno para que tome en cuenta el cero.
            return "Error: Indice fuera del rango del número"
    else:
        return "Error: ambos parámetros deben ser de tipo entero positivo"

def indiceNumero_aux(num, indice, largo, comparar):
    if(num == 0):
        return 0
    elif((num < comparar)and num > 10):
        return (num % 10) + indiceNumero_aux((num % 10)// 10, indice, largo, comparar)
    elif((num < comparar)and num < 10):
        return num + indiceNumero_aux(num//10, indice, largo, comparar)
    elif(indice == largo):
        return num % 10 + indiceNumero_aux((num % 10)//10, indice, largo, comparar)
    else:
        largo = largo-indice
        return indiceNumero_aux(num//(10 ** largo), indice, largo, comparar)



def largoNum(n):
    if(isinstance(n,int) and n >= 0):
        if(n < 10):
            return 1
        else:
            return 1 + largoNum( n//10)        
    else:
        return "Error: en número debe ser entero positivo"

"""
Nombre: cortarNumero
Entrada: recibe un número entero positivo(num), un número de inicio entero positivo(ini)  y un numero entero opositivo que represente el final(fin)
Salida: retorna un nuevo número formado por las posiciones que le indican el ini y el fin
Restricciones: los parámetros deben ser de tipo entero positivo
"""

def cortarNumero(num, ini, fin):
    if(isinstance(num,int) and isinstance(ini,int) and isinstance(fin,int)):
        if(num >= 0 and ini >= 0 and fin >= 0):
            if(validarSiEsOrdenado(num) == True):
                if(ini < largoNum(num-1) and fin < largoNum(num-1)):
                    ini = indiceNumero(num,ini)
                    fin = indiceNumero(num,fin)
                    return cortarNumero_aux(num, ini, fin)
                else:
                    return "Error: Indices fuera del rango del número"
            else:
                return "Error: los dígitos del num deben estar ordenados de forma ascendente"
        else:
            return "Error: los parámetros deben ser positivos"
    else:
        return "Error: los 3 parámetros debe ser de tipo entero"

def cortarNumero_aux(num, ini, fin):
    largo = largoNum(fin)
    return ini * 10 ** largo + fin       
    

#Nombre: validarSiEsOrdenado
#Entrada: un número entero
#Salida: True si los dígitos del numero están ordenados de forma ascendente o False si no es así
#Esta función verifica si los dígitos de un número están ordenados de forma ascendente
def validarSiEsOrdenado(num):
    if(isinstance(num,int)):
        if num == 0:
            return 0
        elif (largoNum(num)<2):
            return True
        elif((num%10)<((num//10)%10)):
            return False
        else:
            return validarSiEsOrdenado(num//10)
    else:
        return "Error: el parámetro num debe ser de tipo entero"




