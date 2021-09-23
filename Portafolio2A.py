#(1) ===========================================================================================================================================================
"""
Nombre: numeroAbundante

Entrada: recibe un número entero positivo llamado num

Salida: retorna True si la suma de los divisores del num es mayor al num original por 2(el duplo del num) o
False si la suma de los divisores del num, es menor al num original por 2(el duplo del num)

Restricciones: el número de entrada debe ser de tipo entero positivo mayor o igual a cero
"""



def numeroAbundante(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return 0
        else:
            sumadivisores = numeroAbundante_aux(num,num,0)
            if((num*2) > sumadivisores):
                return True
            else:
                return False
    else:
        return "Error: La entrada, debe ser número positivo"
        
    
def numeroAbundante_aux(num, divisor,resultado):
    if(divisor == 0):
        return resultado
    else:
        if((num % divisor) == 0):
            return numeroAbundante_aux(num // 10,divisor-1, resultado + divisor) 
        else:
            return numeroAbundante_aux(num, divisor - 1,resultado)



#(2) ===========================================================================================================================================================


"""
Nombre: adyacentesImpares

Entrada: recibe un número entero positivo llamado num

Salida: retorna True en caso de que todas las sumas de dos dígitos adyacentes sean impares o
retornar False en caso de que alguna suma de adyacentes no sea impar.

Restricciones: el número de entrada debe ser de tipo entero positivo mayor o igual a cero
"""


        


def adyacentesImpares(num):
    if(isinstance(num,int) and num >= 0):
        return adyacentesImpares_aux(num)
    else:
        return "Error: Número debe ser positivo"


def adyacentesImpares_aux(num):
    digito = num %10
    suma = digito + (num//10)%10
    if(num == 0):
        return True
    elif(esImpar(suma) == False):
        return False
    else:
        if(esImpar(suma) == True):
            return adyacentesImpares_aux(num // 100)  #  n//100 quita los últimos dos dígito del número
            
        else:
            return False


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




# (3) ===========================================================================================================================================================


"""
Nombre: convertirNumero

Entradas: (num, exponente) recibe dos números enteros, ya sean positivos o negativos

Salida: retorna un nuevo número, en donde el total de dígitos del num debe ser impar, se obtiene el dígito del medio y a ese
número se eleva al exponente ingresado, al extremo izquierdo del dígito se utilizan los números impares se une estos con el
resultado del digito elevado al exponente y luego a su extremo derecho irá los dígitos que son pares, pero si no existen pares
o impares en el num, el resultado será cero.

Restricciones: el largo de los dígitos de num debe ser impar, el num y el exponente deben ser de tipo entero
"""

def convertirNumero(num, exponente):
    if(isinstance(num,int) and isinstance(exponente,int)):
        numero = largo(num)
        if(numero != 1):
            if((numero % 2) != 0):
                if(num < 0 and exponente < 0):
                    return convertirNumero_aux(num*-1, exponente*-1)*-1
                elif(num < 0):
                    return  convertirNumero_aux(num*-1, exponente)*-1
                elif(exponente < 0):
                    return  convertirNumero_aux(num, exponente*-1)
                else:
                    return convertirNumero_aux(num, exponente)
            else:
                return "Error: el largo del número debe ser impar"
        else:
            return num**exponente
    else:
        return "Error: Debe ser entero"

def convertirNumero_aux(num,exponente):
    indice = obtenerIndice_aux(num)
    potencia = indice**exponente
    izquierda = extremoIzquierdo_aux(num)
    derecha = extremoDerecho_aux(num)
    
    L = largo(derecha)
    potenciaMasDerecha = potencia * 10 ** L + derecha
    
    L2 = largo(potenciaMasDerecha)
    nuevoNumero = izquierda * 10 ** L2 + potenciaMasDerecha
    
    if(izquierda == 0):
        return potenciaMasDerecha
    else:
        return nuevoNumero

 
#Obtiene el índice del medio del número
def obtenerIndice_aux(n):
     largo2 = largo(n)
     if(largo2 == 1):
         return n
     else:
        indice = n // (10 ** (largo2 // 2))%10
        return indice

def extremoIzquierdo_aux(n):
     largo2 = largo(n)
     if(largo2 == 1):
         return n
     else:
        indice = n // (10 ** (largo2 // 2))//10
        return construirImpares_aux(indice,0,0)

def extremoDerecho_aux(n):
     largo2 = largo(n)
     if(largo2 == 1):
         return n
     else:
        indice = n % (10 ** (largo2 // 2))
        return construirPares_aux(indice,0,0)


"""
Nombre: construirPares_aux
Entrada: recibe un número entero positivo
Salida: retorna un nuevo número formado apartir de los dígitos pares que contenía el número original
Restricciones: el número debe ser entero positivo
"""


def construirPares_aux(n,potencia,resultado):
    if(n == 0):
        return resultado
    else:
        digito = (n%10) 
        if((digito % 2) == 0):
            resultado +=(digito *(10**potencia))
            return construirPares_aux(n//10,potencia + 1,resultado) 
        else:                                                                       
            return construirPares_aux(n//10,potencia,resultado)
"""
Nombre: construirImpares_aux
Entrada: recibe un número entero positivo
Salida: retorna un nuevo número formado apartir de los dígitos impares que contenía el número original
Restricciones: el número debe ser entero positivo
"""

def construirImpares_aux(n,potencia,resultado):
    if(n == 0):
        return resultado
    else:
        digito = (n%10) 
        if((digito % 2) != 0):
            resultado +=(digito *(10**potencia))
            return construirImpares_aux(n//10,potencia + 1,resultado) 
        else:                                                                       
            return construirImpares_aux(n//10,potencia,resultado)


#Cuenta la cantidad de dígitos que tiene un número
def largo(num):
    if(isinstance(num,int)):
        if(num == 0):
            return 1
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
        return largo_aux(num //10, contador + 1)






#(4)===========================================================================================================================================================


"""
Nombre: comprimirNumero

Entradas: recibe un número entero llamado num.

Salida: retorna un nuevo número quitando solo los dígitos que se repiten

Restricciones: el número de entrada debe ser de tipo entero
"""




def comprimirNumero(num):
    if(isinstance(num,int)):
        if(num > 0):
            if(num != 0):
                   num = str(num)
                   return comprimirNumero_aux(num[:-1],num[-1])
            else:
                return "Error, el número no puede ser cero"
        else:
            numN = num*-1
            num = str(numN)
            return comprimirNumero_aux(num[:-1],num[-1])*-1
            
    else:
        return "Error: Debe ser entero"

def comprimirNumero_aux(num,result):
    if(num == ""):
        return invertirNumero(int(result))
    elif(comprobarSiExiste(num,result)==0):
        return comprimirNumero_aux(num[:-1], result)
    else:
        return comprimirNumero_aux(num[:-1], result + num[-1])

"""
nombre: comprobarSiExiste
entrada: num y result 
salida: 0 o 1,return 0 si en el string result está el dato del indice 0 del numero
y 1 en caso que no se encuentre.
restrincciones: debe ser listas
"""
def comprobarSiExiste(num,result):
    if(result == ""):
        return 1
    elif(num[-1] == result[-1]):
        return 0
    else:
        return comprobarSiExiste(num, result[:-1])

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
                return invertirNumero_aux(num, largo(num),0) 
        else:
            return "Error: elnúmero ingresado debe ser positivo"
    else:
        return "Error: debe ingresar un número entero positivo"


def invertirNumero_aux(num, largo,resultado):
    if(largo == 0):
        return resultado
    else:
        resultado += (num % 10) * (10 ** (largo - 1))
        return invertirNumero_aux(num // 10, largo - 1, resultado)


#(5)========================================================================================================================================================


"""
Nombre: numeroHermano
Entrada: recibe un número entero positivo llamado num
Salida: retorna True si el número posee dos divisores primos o retornar False
en caso de que no sea así.
Restricciones: el número debe ser entero positivo, el 1 y el mismo número no se toman
en cuenta para los primos
"""

def numeroHermano(num):
    if(isinstance(num,int)):
        if(num >= 0):
            divisores = numeroHermano_aux(num,1)
            if(divisores >= 3):
                return True
            else:
                return False
        else:
            return "Error: El número debe ser positivo"
    else:
        return "Error: el número debe ser de tipo entero"



def numeroHermano_aux(num,divisor):
    if(num == divisor):
        return 1
    else:
        if((num % divisor) == 0):
            if(esNumeroPrimo(divisor)):
                return 1 + numeroHermano_aux(num,divisor+1)
            else:
                return numeroHermano_aux(num,divisor+1)
            
        else:
            return numeroHermano_aux(num,divisor+1)



#(6)========================================================================================================================================================
            
"""
Nombre: adyacentesPares
Entrada: recibe un número entero positivo
Salida: retorna True en caso de que las sumas de dos dígitos adyacentes sean pares o
retorna False en caso de que exista una sola suma que sea impar.
Restricciones: el número debe ser de tipo entero positivo
"""

def adyacentesPares(num):
    if(isinstance(num,int) and num >= 0):
        return adyacentesPares_aux(num)
    else:
        return "Número no se puede procesar"


def adyacentesPares_aux(num):
    digito = num %10
    suma = digito + (num//10)%10
    if(num == 0):
        return True
    elif(esImpar(suma) == True):
        return False
    else:
        if(esImpar(suma) == False):
            return adyacentesPares_aux(num // 100)  #  n//100 quita los últimos dos dígito del número
            
        else:
            return False








#(7)========================================================================================================================================================

"""
Nombre: convertirNumero2
Entrada: recibe dos parámetros de tipo entero uno llamado num y el otro factor

Salida: retorna un nuevo número, en donde el total de dígitos del num debe ser par, se obtiene los dos dígito del medio y a esos
dígitos se le multiplica por el factor ingresado, al extremo derecho del dígito se utilizan los números impares se unen estos con el
resultado de los dígitos ya multiplicados por el factor y luego a su extremo izquierdo irán los dígitos que son pares, pero si no existen pares
o impares en el num, el resultado será cero.

Restricciones: el num y el factor deben ser de tipo entero y el total de dígitos debe ser par
"""

def convertirNumero2(num, exponente):
    if(isinstance(num,int) and isinstance(exponente,int)):
        numero = largo(num)
        if(numero != 1):
            if((numero % 2) == 0):
                if(num < 0 and exponente < 0):
                    return convertirNumero2_aux(num*-1, exponente*-1)*-1
                elif(num < 0):
                    return  convertirNumero2_aux(num*-1, exponente)*-1
                elif(exponente < 0):
                    return  convertirNumero2_aux(num, exponente*-1)
                else:
                    return convertirNumero2_aux(num, exponente)
            else:
                return "Error: el largo del número debe ser par"
        else:
            return num*exponente
    else:
        return "Error: Debe ser entero"

def convertirNumero2_aux(num,exponente):
    indice = obtenerIndice2_aux(num)
    potencia = indice*exponente
    izquierda = extremoIzquierdo2_aux(num)
    derecha = extremoDerecho2_aux(num)
    
    L = largo(derecha)
    potenciaMasDerecha = potencia * 10 ** L + derecha
    
    L2 = largo(potenciaMasDerecha)
    nuevoNumero = izquierda * 10 ** L2 + potenciaMasDerecha
    
    if(izquierda == 0):
        return potenciaMasDerecha
    else:
        return nuevoNumero

 
#Obtiene el índice del medio del número
def obtenerIndice2_aux(n):
     largo2 = largo(n)
     if(largo2 == 1):
         return n
     else:
        indice = n // (10 ** ((largo2-1)// 2))%100
        return indice

def extremoIzquierdo2_aux(n):
     largo2 = largo(n)
     if(largo2 == 1):
         return n
     else:
        indice = n // (10 ** (largo2 // 2))//10
        return construirPares_aux(indice,0,0)

def extremoDerecho2_aux(n):
     largo2 = largo(n)
     if(largo2 == 1):
         return n
     else:
        indice = n % (10 ** ((largo2-1 )// 2))
        return construirImpares_aux(indice,0,0)


#(8)========================================================================================================================================================

"""
Nombre: superPrimo
Entrada: recibe un número entero positivo denominado num
Salida: retorna True si la suma de sus dígitos impares es primo o False en caso de que no sea así.
Restricciones: el número debe ser de tipo entero positivo
"""



def superPrimo(num):
    if(isinstance(num,int) and num >= 0):
        sumaImpar = superPrimo_aux(num,0)
        if(esNumeroPrimo(sumaImpar)):
            return True
        else:
            return False
    else:
        return "Error: El número debe ser positivo"


def superPrimo_aux(num, resultado):
    if(num == 0):
        return resultado
    else:
        if((num%2) != 0):
            resultado += (num % 10)
            return superPrimo_aux(num // 10, resultado) 
        else:
            return superPrimo_aux(num // 10, resultado)

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
            return  esNumeroPrimo_aux(num, digito + 1) 
                    

#(9)========================================================================================================================================================
"""
nombre: adyacentes
Entrada: recibe un número entero positivo denominado num
Salida: retorna True en caso de que todas las sumas de dos dígitos adyacentes sean divisibles entre 3
o retorna False en caso contrario de que alguna suma de adyacentes no sea par.
Restricciones: el número debe ser de tipo entero positivo
"""

def adyacentes(num):
    if(isinstance(num,int) and num >= 0):
        return adyacentes_aux(num)
    else:
        return "Error: Número debe ser positivo"


def adyacentes_aux(num):
    digito = num %10
    suma = digito + (num//10)%10
    if(num == 0):
        return True
    else:
        if((suma % 3) == 0):
            return adyacentes_aux(num // 100)  
        else:
            return False


#(10)========================================================================================================================================================

"""
Nombre: convertirNumero3
Entrada: recibe dos parámetros de tipo entero, uno denominado num y el otro factor

Salida:  retorna un nuevo número, en donde el total de dígitos del num debe ser par, se obtiene los dos dígito del medio y a esos
dígitos se le aplica división entera entre el factor ingresado, al extremo derecho del dígito se utilizan los números impares se unen estos con el
resultado de los dígitos ya divididos entre el factor y luego a su extremo izquierdo irán los dígitos que son pares, pero si no existen pares
o impares en el num, el resultado será cero.
"""
    
def convertirNumero3(num, exponente):
    if(isinstance(num,int) and isinstance(exponente,int)):
        numero = largo(num)
        if(numero != 1):
            if((numero % 2) == 0):
                if(num < 0 and exponente < 0):
                    return convertirNumero3_aux(num*-1, exponente*-1)*-1
                elif(num < 0):
                    return  convertirNumero3_aux(num*-1, exponente)*-1
                elif(exponente < 0):
                    return  convertirNumero3_aux(num, exponente*-1)
                else:
                    return convertirNumero3_aux(num, exponente)
            else:
                return "Error: el largo del número debe ser par"
        else:
            return num//exponente
    else:
        return "Error: Debe ser entero"

def convertirNumero3_aux(num,exponente):
    indice = obtenerIndice2_aux(num)
    potencia = indice//exponente
    izquierda = extremoIzquierdo2_aux(num)
    derecha = extremoDerecho2_aux(num)
    
    L = largo(derecha)
    potenciaMasDerecha = potencia * 10 ** L + derecha
    
    L2 = largo(potenciaMasDerecha)
    nuevoNumero = izquierda * 10 ** L2 + potenciaMasDerecha
    
    if(izquierda == 0):
        return potenciaMasDerecha
    else:
        return nuevoNumero


