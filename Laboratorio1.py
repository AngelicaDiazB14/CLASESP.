"""
Nombre: contarCaracteres
Entrada: recibe como parámetro de entrada el nombre del archivo de texto a consultar
Salida: retorna la cantidad de caracteres que posee el archivo de texto consultado
Restricciones: no utilizar palabras built-in, hacer uso de la recursión
"""

def contarCaracteres(nombreArchivo):
    miArchivo = open(nombreArchivo, "r")
    contenido = miArchivo.readline()
    "contenido = str(contenido)//No es necesario esa linea.Esta de mas."
    if(isinstance(contenido,str)):
        if(contenido != ""):
            return contarCaracteres_aux(contenido)
        else:
            return 0
    else:
        return "Error: solo se permiten archivos con contenido de tipo texto"
   
    
def contarCaracteres_aux(contenido):
    if(contenido == ""):
        return 0
    else:
        return 1 + contarCaracteres_aux(contenido[1:])#1: quita el primer elemento





       
"""
Nombre: contarPalabras
Entrada: recibe como parámetro el nombre del archivo y también recibe un archivo con el carácter a buscar
Salida: rectorna la cantidad de veces que se repite la palabra o carácter buscado dentro del archivo.
Restricciones: evitar el uso de las palabras built-in, se debe utilizar la recursión.
"""

def contarPalabras(nombreArchivo, palabraContar):
    miArchivo = open(nombreArchivo, "r")
    contenido = miArchivo.readlines() 
    contenido = str(contenido)
    if(isinstance(palabraContar,str)):
        if(contenido != "" and palabraContar != ""):
            largo = largoTexto(palabraContar)
            return contarPalabras_aux(contenido, palabraContar,largo)
        else:
            return 0
    else:
        return "Error: el segundo parámetro debe ser de tipo texto"

def contarPalabras_aux(contenido, palabraContar, largo):
    if(contenido == ""):
        return 0
    else:
        if(contenido[0:largo] == palabraContar):
            return 1 + contarPalabras_aux(contenido[largo:],palabraContar,largo)
        else:
            return contarPalabras_aux(contenido[1:],palabraContar,largo)
            

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
Nombre: concatenarArchivos
Entrada: recibe tres parámetros de entrada, el nombre de un archivo1, archivo2 y el nombre del nuevo archivo
Salida: el nuevo archivo será la concatenación del contenido del archivo1 y archivo2. 
Restricciones: evitar el uso de las palabras built-in, se debe utilizar la recursión. El archivo1 y archivo2 deben de existir.
"""

def concatenarArchivos(archivo1, archivo2, nuevoArchivo):
    primerArchivo = open(archivo1, "r")
    contenido1 = primerArchivo.read()
    """
    En vez de usar readlines use read().porque readlines solo lee una linea,
    en cambio el read lee todo el texto.
    """
    primerArchivo.close()
    segundoArchivo = open(archivo2, "r")
    contenido2 = segundoArchivo.read()
    segundoArchivo.close()
    "contenido1 = str(contenido1)"
    "contenido2 = str(contenido2)"
    archivo = ""
    archivo += contenido1 + " " +contenido2
    if(contenido1 != ""):
        if(contenido2 != ""):
            return concatenarArchivos_aux(nuevoArchivo,archivo)
        else:
            return "Error: el archivo2 no existe"
    else:
        return "Error: el archivo1 no existe"


def concatenarArchivos_aux(nuevoArchivo,archivo):
    mensaje = archivo
    f = open (nuevoArchivo,'w') 
    f.write(mensaje)
    print(mensaje)
    f.close()

       
