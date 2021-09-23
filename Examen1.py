
# (1) ===========================================================================================================================================================
"""
Nombre: numeroAbundante

Entrada: recibe un número entero positivo llamado num

Salida: retorna True si la suma de los divisores del num es mayor al num original por 2(el duplo del num) o
False si la suma de los divisores del num, es menor al num original por 2(el duplo del num)

Restricciones: el número de entrada debe ser de tipo entero positivo
"""



def numeroAbundante(num):
    if(isinstance(num,int) and num >= 0):
        if(num == 0):
            return 0
        else:
            sumadivisores = numeroAbundante_aux(num,num)
            if((num*2) > sumadivisores):
                return True
            else:
                return False
    else:
        return "Error: La entrada, debe ser número positivo"
        
    
def numeroAbundante_aux(num, divisor):
    if(divisor == 0):
        return 0
    else:
        if((num % divisor) == 0):
            return divisor + numeroAbundante_aux(num // 10,divisor-1) 
        else:
            return numeroAbundante_aux(num, divisor - 1)



# (2) ===========================================================================================================================================================


"""
Nombre: adyacentesImpares

Entrada: recibe un número entero positivo llamado num

Salida: retorna True en caso de que todas las sumas de dos dígitos adyacentes sean impares o
retornar False en caso de que alguna suma de adyacentes no sea impar.

Restricciones: el número de entrada debe ser de tipo entero positivo
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
            return True and adyacentesImpares_aux(num // 100)  #  n//100 quita los últimos dos dígito del número
            
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

Salida: retorna un nuevo número, en donde el total de dígitos del num debe ser impar, se obtine el dígito del medio y a ese
número se eleva al exponente ingresado, al extremo izquierdo del dígito se utilizan los números impares se une estos con el
resultado del digito elevado al exponete y luego a su extremo derecho irá los dígitos que son pares, pero si no existen pares
o impares en el num, el resultado será cero.

Restricciones: el largo de los dígitos de num debe ser impar, el num y el exponente deben ser de tipo entero
"""

def convertirNumero(num, exponente):
    if(isinstance(num,int) and isinstance(exponente,int)):
        numero = largo(num)
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
            return 0
    else:
        return "Error: Debe ser entero"

def convertirNumero_aux(num,exponente):
    return dividirMitadesP_aux(num)



def dividirMitadesP_aux(n):
     largo2 = largo(n)
     if(largo2==1):
         return f"{n}"
     if(largo2 % 2 == 0):
        mitad1 = n // (10 ** (largo2 // 2))
        mitad2 = n % (10 ** (largo2 // 2))
        return f"{mitad1} y {mitad2}"
     else:
        mitad1 = n // (10 ** (largo2 // 2))
        mitad2 = n % (10 ** ((largo2 // 2)+ 1))
        return mitad1, mitad2
    

#Cuenta la cantidad de dígitos que tiene un número
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


# (4) ===========================================================================================================================================================



"""
Nombre: comprimirNumero

Entradas: recibe un número entero llamado num.

Salida: retorna un nuevo número quitando solo los dígitos que se repiten

Restricciones: el número de entrada debe ser de tipo entero
"""



def comprimirNumero(num):
    if(isinstance(num,int)):
       return comprimirNumero_aux(num,0)
    else:
        return "Error: Debe ser entero"

def comprimirNumero_aux(num,pos):
    if(num == 0):
        return 0
    if(num%10 == num%10
       return num%10*(10**pos)
