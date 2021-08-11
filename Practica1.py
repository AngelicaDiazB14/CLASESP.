"""
Nombre: contarDigitosPares
Entradas: recibe un número(n) entero 
Salida: retorna la cantidad de dígitos pares que componen el número
Restricciones: el número debe ser entero 
"""

def contarDigitosPares(n):
    if(isinstance(n,int)):
        if(n == 0):
            return 1
        elif(n >= 0):
            return contarDigitosPares_aux(n)
        else:
            n1 = -1* n
            return contarDigitosPares_aux(n1)
    else:
        return "Error: Solo es permitido número de tipo entero"
    
def contarDigitosPares_aux(n):
    if(n == 0):
        return 0
    else:
        if((n%2) == 0):
            return 1 + contarDigitosPares_aux(n//10)
        else:
            return contarDigitosPares_aux(n//10)

"""
Nombre: contarTriosDeDigitos
Entrada: recibe un número(n) entero 
Salida: retorna la cantidad de grupos de 3 dígitos que contiene el número ingresado"
Restricciones: Solo se permiten números enteros
"""

def contarTriosDeDigitos(n):
    if(isinstance(n,int)):
        if(n >= 0):
            return contarTriosDeDigitos_aux(n)
        elif(largo(n) < 3):
            return 0
        else:
            n1 = -1* n
            return contarTriosDeDigitos_aux(n1)
    else:
        return "Error: Solo es permitido número de tipo entero"

def contarTriosDeDigitos_aux(n):
    if(largo(n) <= 2):
        return 0
    else:
        if(n%1000 ):
            return 1 + contarTriosDeDigitos_aux(n//1000)
        else:
            return  contarTriosDeDigitos_aux(n//1000)

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


"""
Nombre: sumatoriaParcial
Entrada: recibe un número entero de inicio(ini) y un número entero final(fin)
Salida: retorna el resultado de la sumatoria desde el número de inicio hasta el número final
Resticciones: solo se permiten números enteros, el parámetro "fin" debe ser mayor o igual a "ini"
"""

def sumatoriaParcial(ini,fin):
    if(isinstance(ini,int) and isinstance(fin,int)):
        if(ini > fin):
            return "Error: El parámetro Fin debe ser mayor o igual que Ini"
        else:
            return sumatoriaParcial_aux(ini,fin)
    else:
        return "Error: Solo es permitido número de tipo entero"

def sumatoriaParcial_aux(ini,fin):
    if(ini > fin):
        return 0
    else:
        return ini + sumatoriaParcial_aux(ini + 1, fin)



"""
Nombre: multiplicacion
Entradas: recibe un número entero positivo llamado "op1" y otro número entero positivo "op2"
Salida: retorna la multiplicación del "op1" por medio de la recursión suma, tantas veces indique el "op2"
Restricciones: ambos parámetros deben ser de tipo entero positivo
"""

def multiplicacion(op1,op2):
    if(isinstance(op1,int) and isinstance(op2,int)):
        if(op1 >= 0 and op2 >= 0):
            return multiplicacion_aux(op1,op2)
        else:
            return "Error: solo se permiten números enteros"
    else:
        return "Error: Solo es permitido número de tipo entero"

def multiplicacion_aux(op1,op2):
    if(op2 == 0):
        return 0
    elif(op2 == 1):
        return op1
    else:
        return op1 + multiplicacion_aux(op1, op2 - 1)
        


    

