#EJERCICIO 1
"""
Nombre: totalizarArchivo
Entradas: recibe el nombre de un archivo, el segundo parámetro será el día a totalizar y el tercer parámetro será
la categoría a totalizar(ejemplo: "comida","gasolina")
Salida: se imprime el contenido totalizado(sumado) según los parámetros indicados de la categoría en la entrada.
Restricciones: el archivo tendrá una estructura separada por comas, los parámetros de entrada deben ser de tipo string
"""


def totalizarArchivo(nombreArchivo,dia,categoria):
    if(isinstance(nombreArchivo,str)and isinstance(dia,str) and isinstance(categoria,str)):
        archivo = open(nombreArchivo,"r")
        contenido = archivo.read()
        contenido = str(contenido)
        archivo.close()
        if(contenido != ""):
            lista = transformar_aux(contenido, "", [])
            ordenar = ordenarDatos_aux(lista, [])
            linea = buscarDato_aux(ordenar, dia + categoria, 0)
            if(linea != -1): # si la variable es -1 significa que no encontró el dato
                agrupar2 = ordenar[linea + 1:]
                if((dia + categoria) in agrupar2):
                    linea2 = buscarDato_aux(agrupar2, dia + categoria,0)
                    print(f"Total para {dia} por concepto de {categoria} es: {(int(ordenar [linea + 1])) + (int(agrupar2 [linea2 + 1]))} colones.")
                else:
                    print(f"Total para {dia} por concepto de {categoria} es: {ordenar [linea + 1]}  colones.")
            else:
                return "Error: no se encuentra el dato"
        else:
            return "Error: el archivo esta vacío. "
    else:
        return "Error: los parámetros deben ser de tipo string"
   




#...................................................................................................................................................
"""
Une los datos provenientes de la función transformar_aux, uniendo el día junto con la categoría y manteniendo todo en una sola lista
para su fácil manipulación.
"""


#Ejemplo:

#Le ingresa como parámtero la siguiente lista, proveniente de la función transformar:

"""
['lunes', 'comida', '20000', 'lunes', 'gasolina', '5000','martes', 'comida', '15000', 'martes',
'comida', '3500', 'miercoles', 'servicios', '4000', 'jueves', 'comida', '8500.5', 'jueves', 'gasolina']
"""


#Como resultado la función retornará lo siguiente:

"""
['lunescomida', '20000', 'lunesgasolina', '5000', 'martescomida', '15000', 'martescomida', '3500', 'miercolesservicios', '4000', 'juevescomida', '8500.5']
"""

def ordenarDatos_aux(lista,result):
    if(lista == []):
        return result
    else:
        return ordenarDatos_aux(lista[3:],result+[lista[0]+lista[1]]+[lista[2]])       



#...................................................................................................................................................

#Sirve para buscar el dato deseado y retorna la posición en la que está

#Ejemplos:

"""
>>> lista = ['lunescomida', '20000', 'lunesgasolina', '5000', 'martescomida', '15000', 'martescomida', '3500',
'miercolesservicios', '4000', 'juevescomida', '8500.5']

>>> buscarDato_aux(lista,"miercoles"+"servicio",0)
False #(no encontró el dato)



>>> buscarDato_aux(lista,"miercoles"+"servicios",0)
8 #(encontró el dato y lo localizó en el índice 8
 
"""

def buscarDato_aux(lista, buscar, cont):
    if(lista == []):
        return -1
    elif(lista[0] == buscar):
        return cont
    else:
        return buscarDato_aux(lista[1:], buscar, cont+1)


#...................................................................................................................................................

#recorre los datos de la lista elemento por elemento
#pero a la misma vez une todas las líneas del archivo en una sola lista
#por esta razón se llama transformar

#Ejemplo de lo que retorna al final la función:

#['lunes', 'comida', '20000', 'lunes', 'gasolina', '5000','martes', 'comida', '15000', 'martes',
#'comida', '3500', 'miercoles', 'servicios', '4000', 'jueves', 'comida', '8500.5', 'jueves', 'gasolina']

def transformar_aux(datos,suma,result):
    if(datos == ""):
        return result+[suma]
    elif(datos[0]=="'"):
        return transformar_aux(datos[1:],suma,result)
    elif(datos[0]==","):
        return transformar_aux(datos[1:],"",result+[suma])
    elif(datos[0]==" "):
        return transformar_aux(datos[1:],suma,result)
    elif(datos[0]=="\n"):
        return transformar_aux(datos[1:],"",result+[suma])
    elif(datos[0]=="''"):
        return transformar_aux(datos[1:],suma,result)
    else:
        return transformar_aux(datos[1:],suma+datos[0],result)


#=====================================================================================================================================================

# EJERCICIO 2



"""
Nombre:
        ordenarArchivos

Entradas:
        archivo1: es el nombre del archivo existente al cual queremos ordenar
        archivo2: es el nombre del archivo existente al cual también queremos ordenar, debe ser distinto al primero
        nuevoArchivo: es el nombre del nuevo archivo que contendrá el contenido de los dos anteriores
Salidas: el retorno de un nuevo archivo que contenga los números ordenados de menor a mayor provenientes del archivo1
         y archivo2
Restricciones:
            el archivo1 y el archivo2 deben de existir previamente
            los archivos solo pueden tener números enteros positivos
            y solo se permite un número por línea.
"""

def ordenarArchivos(archivo1,archivo2,nuevoArchivo):
    if(isinstance(archivo1,str) and isinstance(archivo2,str) and isinstance(nuevoArchivo,str)):
       archivo1 = open(archivo1,"r")
       contenidoArchivo1 = archivo1.read()
       archivo1.close()
       archivo2 = open(archivo2,"r")
       contenidoArchivo2 = archivo2.read()
       archivo2.close()
       if(contenidoArchivo1 != ""):
           if(contenidoArchivo2 != ""):
               if(verificaInt(contenidoArchivo1) == True):
                   if(verificaInt(contenidoArchivo2) == True):
                       return ordenarArchivos_aux(contenidoArchivo1,contenidoArchivo2,nuevoArchivo)
                   else:
                       return "Error: el archivo2 no contiene números de tipo entero positivo o no hay un solo número por línea"
               else:
                   return "Error: el archivo1 no contiene números de tipo entero positivo o no hay un solo número por línea"
           else:
               return "Error: el archivo2 está vacío"
       else:
           return "Error: el archivo1 está vacío"

    else:
        return "Error: los parámetros de entrada deben ser de tipo string"
       
       
def ordenarArchivos_aux(datos1,datos2,nuevoArchivo):
    nuevoArchivo = open(nuevoArchivo,"w")
    nuevoArchivo.write(datos1+"\n"+datos2)
    nuevoArchivo.close()
    print("El contenido del nuevo archivo es:")
    print(datos1 + "\n" + datos2) 
       




"""
Nombre: largoTexto
Entrada: recibe miTexto de tipo string
Salida: retorna la cantidad de carácteres que contiene el texto ingresado
Restricciones: el parámetro de entrada debe ser de tipo string
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
Nombre: verificaInt
Entrada: recibe miTexto de tipo string
Salida: retorna True si en el texto ingresado solo habían números o False si en el texto ingresado encontró algún caracter
Restricciones: el parámetro de entrada debe ser de tipo string
"""

def verificaInt(miTexto):
    if(isinstance(miTexto,str)):
        largo = largoTexto(miTexto)
        return verificaInt_aux(miTexto,largo,0)
    else:
        return "Error: Solo es permitido valores de tipo texto"


def verificaInt_aux(miTexto,largo,pos):
    if(largo == 0):
        return True
    else:
        if(miTexto[pos] == "1" or miTexto[pos] == "2"or miTexto[pos] == "3"or miTexto[pos] == "4"or miTexto[pos] == "5"or miTexto[pos] == "6"or miTexto[pos] == "7" or miTexto[pos] == "8"or miTexto[pos] == "9"or miTexto[pos] == "0" or miTexto[pos]=="\n" or miTexto[pos] == ""):
            return  True and verificaInt_aux(miTexto,largo-1,pos+1)
        else:
            return False


