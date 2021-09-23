#Taller de Programación
                                                      #Tarea 1 Registro de llamadas telefónicas
                                                                #Angélica Díaz Barrios

#====================================================================================================================================================================

#================================================================== MENÚ PRINCIPAL ==================================================================================


"""
Nombre: menu
Entrada: no recibe una entrada directamente, pero recibe un input de un número en string según la opción que el usuario quiera realizar.
Salida: retorna a los siguientes submenús (registro_llamadas, busquedas_avanzadas, total_llamadas o salir), según la opción seleccionada por el usuario.
Restricciones: la entrada debe ser un número de tipo string
"""

def menu():
    print("=======================================================================")
    print("\n                           MENÚ PRINCIPAL\n")
    print("Opciones:\n")
    print("  (1) Registro de llamadas telefónicas\n"," (2) Búsquedas avanzadas\n"," (3) Total llamadas\n"," (9) Salir\n")
    opcion = input("Seleccione la opción que desea realizar: ")

    if(opcion == "1"):
        return registro_llamadas()
    elif(opcion == "2"):
        return busquedas_avanzadas()
    elif(opcion == "3"):
        return total_llamadas()
    elif(opcion == "9"):
        print("\n")
        return print("                            ¡HASTA LUEGO!")
    else:
        print("\nNo fue posible reconocer la opción seleccionada\n")
        return menu()

#====================================================================================================================================================================
        
#========================================================================= SUBMENÚS ================================================================================

"""
Nombre: registro_llamadas
Entradas: no recibe una entrada directamente, la recibe a través de un input como un número de tipo string según la opción que el usuario quiera realizar.7
Salida: retorna a otras funciones(registrar_llamadas,borrar_llamada, modificar_registro, ver_llamadas o retornar), según la opción seleccionada por el usuario
Restricciones: la entrada debe ser un número de tipo string
"""

def registro_llamadas():
    print("=======================================================================")
    print("\n                 REGISTRO DE LLAMADAS TELEFÓNICAS\n")
    print("Opciones:\n")
    print("  (11) Registrar llamadas\n"," (12) Borrar llamada\n"," (13) Modificar registro\n"," (14) Ver todas las llamadas\n"," (15) Retornar\n")
    opcion = input("Seleccione la opción que desea realizar: ")
    
    if(opcion == "11"):
        return registrar_llamadas()
    elif(opcion == "12"):
        codigo = input("\ningrese el código de la llamada que desea borrar: ")
        if(codigo != ""):
            return borrar_llamada(codigo)
        else:
            print("\nError: espacio vacío")
            return registro_llamadas()
    elif(opcion == "13"):
        codigo = input("\ningrese el código de la llamada que desea modificar: ")
        if(codigo != ""):
            return modificar_registro(codigo)
        else:
            print("\nError: espacio vacío")
            return registro_llamadas()
    elif(opcion == "14"):
        listaLlamadas = obtenerRegistroLLamada()
        total_indices = cantidadDeIndices(listaLlamadas)
        print("\n======================= VIENDO TOTAL DE LLAMADAS =====================\n")
        return ver_llamadas(listaLlamadas, total_indices,0)
    elif(opcion == "15"):
        return menu()
    else:
        print("\nNo fue posible reconocer la opción seleccionada\n")
        return registro_llamadas()


"""
Nombre:  busquedas_avanzadas
Entradas: no recibe una entrada directamente, la recibe a través de un input como un número de tipo string según la opción que el usuario quiera realizar.
Salida: retorna a otras funciones(buscar_por_nombre,buscar_por_telefono, buscar_por_tipo_de_llamada, buscarPorFecha o retornar),
según la opción seleccionada por el usuario
Restricciones: la entrada debe ser un número de tipo string
"""

def busquedas_avanzadas():
    print("=======================================================================")
    print("\n                     BÚSQUEDAS AVANZADAS\n")
    print("Opciones:\n")
    print("  (21) Buscar por nombre\n"," (22) Buscar por teléfono\n"," (23) Buscar por tipo de llamada\n"," (24) Buscar por fecha\n"," (25) Retornar\n")
    opcion = input("Seleccione la opción que desea realizar: ")

    if(opcion == "21"):
        nombre = input("Digite la parte del nombre a buscar: ")
        if(nombre != ""):
            return buscar_por_nombre(nombre)
        else:
            print("Error: espacio en blanco")
            return  busquedas_avanzadas()
    elif(opcion == "22"):
        telefono = input("Digite la parte del telefono a buscar: ")
        if(telefono != ""):
            return buscar_por_telefono(telefono)
        else:
            print("Error: espacio en blanco")
            return  busquedas_avanzadas()
    elif(opcion == "23"):
        tipollamada = input("Digite el tipo de llamada a buscar (E o S): ")
        if(tipollamada != ""):
            return buscar_por_tipo_de_llamada(tipollamada)
        else:
            print("Error: espacio en blanco")
            return  busquedas_avanzadas()
    
    elif(opcion == "24"):
        fecha = input("Digite parte de la fecha a buscar: ")
        if(fecha != ""):
            return buscarPorFecha(fecha)
        else:
            print("Error: espacio en blanco")
            return  busquedas_avanzadas() 
    elif(opcion == "25"):
        return menu()
    else:
        print("\nNo fue posible reconocer la opción seleccionada\n")
        return busquedas_avanzadas()


"""
Nombre: total_llamadas
Entrada: ninguna
Salida: retorna un número que indica la cantidad total de llamadas realizadas
Restricciones: no existen
"""

def total_llamadas():
    print("\n=======================================================================")
    print("\nEl total de llamadas registradas en el CallCenter es:\n")
    archivo = open("CallCenter.txt")
    datos = archivo.readlines()
    llamada = cantidadDeIndices(datos)//10
    print("\nTOTAL LLAMADAS: ",llamada)
    archivo.close()
    return menu()
    






#====================================================================================================================================================================

#============================================================ VALIDACIONES DE LOS PARÁMETROS DE ENTRADA =============================================================


#Esta función permite obtener los datos del archivo CallCenter.txt
def obtenerRegistroLLamada():
    registro = open("CallCenter.txt")
    datosllamadas = registro.readlines()
    registro.close()
    return datosllamadas

"""
Nombre: convertir_a_string
Entradas: lista
Salidas: un string con todos los datos de la entrada
Restricciones: la entrada debe ser una lista
"""


def convertir_a_string(lista):
    if isinstance(lista, list):
        string = ""
        for indice in lista:  # Se leen las lineas del archivo y guarda en un una variable
            string += indice
        return string
    else:
        print("Error: no se puede convertir a String, porque, el tipo de dato de entrada, no es una lista")



"""
Nombre: esValido
Entradas: opcion
Salidas: True si la entráda es un String. False si la entrada no es un String. 
Restricciones: La entrada debe ser un String.
"""


def esValido(opcion):
    if (isinstance(opcion, str) and opcion != ""):
        return True
    else:
        return False


"""
Nombre: cantidadDeindices
Entradas: string_o_lista
Salidas: cantidad de indices
Restricciones: no posee.
"""


def cantidadDeIndices(string_o_lista):
    if(string_o_lista == "" or string_o_lista == []):
        return 0
    else:
        return 1 + cantidadDeIndices(string_o_lista[1:])

"""
Nombre: seEncuentra
Entradads: buscar, string_o_lista
Salidas: True si buscar se encuentra en string_o_lista
Restricciones: no posee

Nota: funciona correctamente si solo recibe string o una lista que su contenido tenga únicamente strings.
"""
def seEncuentra(buscar, string_o_lista):
        indicesBuscar = cantidadDeIndices(buscar)
        if isinstance(string_o_lista, list):
            return seEncuentraAux(buscar, indicesBuscar, string_o_lista, 0)
        else:
            return seEncuentraEnString(buscar, string_o_lista, indicesBuscar)

def seEncuentraAux(buscar, indicesBuscar, lista, cont):
    if lista == []:
        return False
    else:
        if seEncuentraEnString(buscar, lista[0], indicesBuscar):
            return True
        else:
            return seEncuentraAux(buscar, indicesBuscar, lista[1:], cont + 1)
            
def seEncuentraEnString(buscar, cadena, indicesBuscar):
    if cadena == "":
        return False
    else:
            if buscar == cadena[0: indicesBuscar]:
                return True
            else:
                return seEncuentraEnString(buscar, cadena[1:], indicesBuscar)




"""
Nombre: validarCodigo
Entradas: recibe como parámetro el codigo, listaLlamadas
Salidas:  True si se cumplen las restricciones y el código no está en el registro de llamadas o False si no es así
Restricciones: no posee
"""


def validarCodigo(codigo, listaLlamadas):
    if (seEncuentra(codigo + "\n", listaLlamadas)):
        print("ERROR\nEl código ya se encuentra registrado")
        return False
    else:
        return True


"""
Nombre: eliminarInformacion
Entradas: listaLlamadas, indice, cont
Salidas: un sring que contenga la lista de las llamadas que no se eliminaron
Restricciones:  listaLlamadas debe ser una lista que contenga los contactos. indice tendrá
el valor del indice de la listaLlamadas en que se empieza a mostrar información de la llamada a eliminar
"""


def eliminarInformacion(listaLlamadas, indice, cont):
    if(cont == 10):
        return convertir_a_string(listaLlamadas)
    else:
        listaLlamadas.pop(indice)
        return eliminarInformacion(listaLlamadas, indice, cont + 1)

"""
Nombre: validarVacio
Entrada: recibe los siguientes parámetros provenientes de la función registar_llamada:
listaLlamadas,codigo,tipollamada,cedula,nombre,apellidos,sexo,telefono,fecha,comentario.
Salida: retorna a la función anotarDatosLLamada si todos los espacios de los parámetros fueron llenados
o retorna nuevamente al menú de registro_llamadas() si se dejó algún espacio sin rellenar
Restricciones: todos los parámetros deben ser llenados
"""



def validarVacio(listallamadas,codigo,tipollamada,cedula,nombre,apellidos,sexo,telefono,fecha,comentario):
    if(codigo != ""):
       if(tipollamada != ""):
          if(cedula != ""):
              if(nombre != ""):
                  if(apellidos != ""):
                      if(sexo != ""):
                          if(telefono != ""):
                              if(fecha != ""):
                                  if(comentario != ""):
                                      return anotarDatosLlamada(codigo,tipollamada,cedula,nombre,apellidos,sexo,telefono,fecha,comentario)
                                  else:
                                      print("\nError: el espacio del comentario está vacío")
                                      print("\nLa llamada no pudo ser registrada")
                                      return registro_llamadas()
                              else:
                                  print("\nError: el espacio de la fecha está vacío")
                                  print("\nLa llamada no pudo ser registrada")
                                  return registro_llamadas()
                          else:
                              print("\nError: el espacio del teléfono está vacío")
                              print("\nLa llamada no pudo ser registrada")
                              return registro_llamadas()
                      else:
                          print("\nError: el espacio de sexo está vacío")
                          print("\nLa llamada no pudo ser registrada")
                          return registro_llamadas()
                  else:
                      print("\nError: el espacio de apellidos está vacío")
                      print("\nLa llamada no pudo ser registrada")
                      return registro_llamadas()
              else:
                  print("\nError: el espacio del nombre está vacío")
                  print("\nLa llamada no pudo ser registrada")
                  return registro_llamadas()
          else:
              print("\nError: el espacio de cédula está vacío ")
              print("\nLa llamada no pudo ser registrada")
              return registro_llamadas()
       else:
           print("\nError: el espacio del tipo de llamada está  vacío")
           print("\nLa llamada no pudo ser registrada")
           return registro_llamadas()
    else:
        print("\nError: el espacio del código está vacío")
        print("\nLa llamada no pudo ser registrada")
        return registro_llamadas()

    



"""
NOMBRE: validarInformacion

ENTRADAS: tiene como entrada los siguientes parámetros:(listaLlamadas,codigo,tipollamada,cedula, sexo, telefono,fecha,comentario).

SALIDAS: True si la información de cada parámetro es válida según su condición o False si no es así.

RESTRICCIONES: según cada parámetro, indicados por el profesor.
El tipo de llamada solo debe permitir una E o S, la cédula debe contener 9 dígitos en total, el sexo debe ser únicamente la letra H o M,
el teléfono debe contener 8 dígitos sin separadores y el comentario no puede tener más de 100 caracteres, el código no puede estar repetido.
"""


def validarInformacion(listaLlamadas,codigo,tipollamada,cedula, sexo, telefono,fecha,comentario):
    if(validarCodigo(codigo,listaLlamadas) == True):
        if(tipollamada == "E" or tipollamada == "S" or tipollamada == " S" or tipollamada == " E"):
            if(largoTexto(cedula) == 9 and verificaInt(cedula)):
                if(sexo == "M" or sexo == "H" or sexo == " H" or sexo == " M"):
                    if(largoTexto(telefono) == 8 and verificaInt(telefono) == True):
                        if(verificaFecha(fecha) == True):
                            if(largoTexto(comentario) <= 100):
                                return True
                            else:
                                print("\nError: el comentario debe tener un máximo de 100 caracteres.")
                                return False
                        else:
                            print("\nError: la fecha debe tener la estructura en donde el separador '/' debe estar en la posición 3 y 6 y el año debe tener solo 4 dígitos")
                            print("\nEjemplo de fecha: 01/12/2021")
                            return False
                    else:
                        print("\nError: Debe ingresar el número de teléfono con un límite de 8 dígitos y sin separadores entre ellos.")
                        return False
                else:
                     print("\nError: Debe ingresar únicamente los carácteres H o M cuando se le solicita ingresar el sexo.")
                     return False
            else:
                print("\nError: Debe ingresar el número de cédula con un límite de 8 dígitos y sin separadores entre ellos. ")
                return False
        else:
            print("\nError: Debe ingresar únicamente los carácteres E o S cuando se le solicita ingresar el tipo de llamada.")
            return False
    else:
        print("\nError: el código ya existe.")
        return False






"""
Nombre: largoTexto
Entrada: recibe miTexto de tipo string
Salida: retorna la cantidad de caracteres que contiene el texto ingresado
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
        return 1 + largoTexto_aux(miTexto[1:])

"""
Nombre: verificaInt
Entrada: recibe miTexto de tipo string
Salida: retorna True si en el texto ingresado solo hay números o False si en el texto ingresado encontró algún carácter diferente a números
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
        if(miTexto[pos] == "1" or miTexto[pos] == "2"or miTexto[pos] == "3"or miTexto[pos] == "4"or miTexto[pos] == "5"or miTexto[pos] == "6"or miTexto[pos] == "7" or miTexto[pos] == "8"or miTexto[pos] == "9"or miTexto[pos] == "0"):
            return  True and verificaInt_aux(miTexto,largo-1,pos+1)
        else:
            return False

"""
Nombre: verificaFecha
Entrada: recibe la fecha de tipo string
Salida: retorna True si en el la fecha ingresada solo hay números y  una barra inclinada "/" en las posiciones indicadas,
o retorna False si en la fecha ingresada encontró algún caracter o no encontró los separadores "/"
Restricciones: el parámetro de entrada debe ser de tipo string, el largo del año debe ser de 4 dígitos.
"""

def verificaFecha(fecha):
    if(isinstance(fecha,str)):
        largo = largoTexto(fecha)
        if(largo == 10):
            return verificaFecha_aux(fecha,largo,0)
        else:
            return False
    else:
        return "Error: Solo es permitido valores de tipo texto"


def verificaFecha_aux(fecha,largo,pos):
    if(largo == 0):
        return True
    else:
        if(fecha[pos] == "1" or fecha[pos] == "2"or fecha[pos] == "3"or fecha[pos] == "4"or fecha[pos] == "5"or fecha[pos] == "6"or fecha[pos] == "7" or fecha[pos] == "8"or fecha[pos] == "9"or fecha[pos] == "0"  or fecha[2] == "/" or fecha[5] == "/"):
            if(fecha[2] == "/" and fecha[5] == "/" and largoTexto(fecha[6:]) == 4):
                return  True and verificaFecha_aux(fecha,largo-1,pos+1)
            else:
                return False
        else:
            return False
#====================================================================================================================================================================

#============================================================== FUNCIONES DEL SUBMENÚ REGISTRO LLAMADAS ============================================================



"""
Nombre: registrar_llamadas
Entrada: no recibe una entrada directamente, lo que recibe son entradas por medio de input, entre ellas están: el código de la llamada,
el tipo de llamada (E o S), la cédula, nombre, apellidos, sexo, teléfono, fecha y un comentario.
Salida: retorna a la función anotarDatosLLamada, para que esta guarde los datos en el archivo
Restricciones: en esta función no hay ninguna restricción.
"""

def registrar_llamadas():
    print("=======================================================================")
    print("\n               REGISTRANDO LLAMADA TELEFÓNICA...\n")
    codigo = input("Ingrese el código de la llamada, pueden ser números y letras: ")
    tipollamada = input("Ingrese el tipo de llamada E(entrante) o S(saliente): ")
    cedula = input("Ingrese el número de cédula sin separadores: ")
    nombre = input("Ingrese el nombre: ")
    apellidos= input("Ingrese los apellidos: ")
    sexo = input("Ingrese el sexo, H o M: ")
    telefono = input("Ingrese el número de teléfono sin separadores: ")
    fecha = input("Ingrese la fecha de la llamada: ")
    comentario = input("Escriba un comentario de la llamada: ")
    listaLlamadas =  obtenerRegistroLLamada
    return validarVacio(listaLlamadas,codigo,tipollamada,cedula,nombre,apellidos,sexo,telefono,fecha,comentario)


"""
Nombre: anotarDatosLlamada
Entrada: recibe los siguientes parámetros: codigo,tipollamada,cedula,nombre,apellidos,sexo,telefono,fecha,comentario
Salida: agrega la información de la llamada al archivo CallCenter.tx, si pasó todas las validaciones y retorna al menú de registro_llamadas(),
o no agrega la información al archivo si no pasó las validaciones y lo regresa al menú de registro_llamadas().
Restricciones: se deben validar los datos a agregar primero.
"""
        
def anotarDatosLlamada(codigo,tipollamada,cedula,nombre,apellidos,sexo,telefono,fecha,comentario):
    datos = obtenerRegistroLLamada()
    datosValidos = validarInformacion(datos,codigo,tipollamada,cedula, sexo, telefono,fecha,comentario)
    if(datosValidos == True):
        datosAgregar = open("CallCenter.txt", "a")
        # Escribir datos del nuevo contacto en el archivo, hacer salto de línea y escribir un separador por guiones
        datosAgregar.write(codigo + "\n")
        datosAgregar.write(tipollamada + "\n")
        datosAgregar.write(cedula + "\n")
        datosAgregar.write(nombre + "\n")
        datosAgregar.write(apellidos + "\n")
        datosAgregar.write(sexo + "\n")
        datosAgregar.write(telefono + "\n")
        datosAgregar.write(fecha + "\n")
        datosAgregar.write(comentario + "\n")
        datosAgregar.write("......................................................................." + "\n")
        datosAgregar.close()
        
        print("\nLa información fue agregada exitosamente")
        return registro_llamadas()
    else:
        print("\nLa información no pudo ser agregada")
        return registro_llamadas()


    
"""
Nombre: borrar_llamada
Entrada: recibe como parámetro el código de la llada que se quiere borrar
Salida: imprime si la llamada se pudo borrar(además la borra del archivo CallCenter.txt)
si no se cumplieron con las condiciones establecidas.
Restricciones: el código debe de existir en el archivo para poder borrar la llamada.
"""

def borrar_llamada(codigo):
    print("=======================================================================")
    print("                       BORRANDO LLAMADA...\n")
    llamadas = open("CallCenter.txt")
    listallamadas = llamadas.readlines()
    if(seEncuentra(codigo + "\n", listallamadas)):
        indice = listallamadas.index(codigo + "\n")
        mostrarLlamada(listallamadas, indice, 0)
        listallamadas = eliminarInformacion(listallamadas, indice, 0)
        llamadas.close()
        llamadas = open("CallCenter.txt", "w")
        llamadas.write(listallamadas)
        llamadas.close()
        print("\nLa llamada ha sido eliminada exitosamente\n")
        return registro_llamadas()
    else:
        print("\nNo hay ninguna llamada registrada con el código ", cedula)
        llamadas.close()
        return registro_llamadas()


"""
Nombre: modificar_registro
Entrada: recibe el código de la llamada que se desea modificar
Salida: imprime si el contacto pudo ser modificado o no y regresa al menú de registro_llamadas()
Restricciones: el código debe de existir para que la llamada pueda ser modificada solo podrá 
modificar cédula, Nombre, Apellidos, Sexo, teléfono y el comentario
"""



def modificar_registro(codigo):
    listaLlamadas = obtenerRegistroLLamada()
    if (seEncuentra(codigo + "\n", listaLlamadas)):
        indice = listaLlamadas.index(codigo + "\n")
        print("\nInformación del contacto seleccionado\n")
        mostrarLlamada(listaLlamadas, indice, 0)
        listaModificada = modificarLlamada_aux(listaLlamadas, indice + 1, 0)
        llamadas = open("CallCenter.txt", "w")
        llamadas.write(convertir_a_string(listaModificada))
        llamadas.close()
        print("La llamada ha sido modificada exitosamente")
        return registro_llamadas()
    else:
        print("No fue posible encontrar la llamada con el código ", codigo)
        return registro_llamadas()


def modificarLlamada_aux(llamadas, indice, cont):
    if(cont == 7 ):
        return llamadas
    else:
        if(cont == 0):
            nuevaInformacion = input("Escriba el tipo de llamada E o S: ")
            if(nuevaInformacion != ""):
                if(nuevaInformacion == "E" or nuevaInformacion == "S"):
                    llamadas[indice] = nuevaInformacion + "\n"
                    return modificarLlamada_aux(llamadas, indice+1, cont+1)
                else:
                    print("\nError: solo se permiten los valores E o S")
                    return modificarLlamada_aux(llamadas, indice, cont)
            else:
                print("\nError: espacio vacío")
                return modificarLlamada_aux(llamadas, indice, cont)
        
        elif(cont == 1):
            nuevaInformacion = input("Escriba la nueva cédula: ")
            if(nuevaInformacion != ""):
                if(largoTexto(nuevaInformacion) == 9 and verificaInt(nuevaInformacion) and nuevaInformacion != ""):
                    llamadas[indice] = nuevaInformacion + "\n"
                    return modificarLlamada_aux(llamadas, indice+1, cont+1)
                else:
                    print("\nError: Debe ingresar el número de cédula con un límite de 9 dígitos y sin separadores entre ellos.")
                    return modificarLlamada_aux(llamadas, indice, cont)
            else:
                print("\nError: espacio vacío")
                return modificarLlamada_aux(llamadas, indice, cont)
        elif(cont == 2):
            nuevaInformacion = input("Escriba el nuevo nombre: ")
            if(nuevaInformacion != ""):
                llamadas[indice] = nuevaInformacion + "\n"
                return modificarLlamada_aux(llamadas, indice+1, cont+1)
            else:
                print("\nError: espacio vacío")
                return modificarLlamada_aux(llamadas, indice, cont)
                
        elif(cont == 3):
            nuevaInformacion = input("Escriba los nuevos apellidos: ")
            if(nuevaInformacion != ""):
                llamadas[indice] = nuevaInformacion + "\n"
                return modificarLlamada_aux(llamadas, indice+1, cont+1)
            else:
                print("\nError: espacio vacío")
                return modificarLlamada_aux(llamadas, indice, cont)
                
        elif(cont == 4):
            nuevaInformacion = input("Escriba el sexo: ")
            if(nuevaInformacion != ""):
                if(nuevaInformacion == "M" or nuevaInformacion == "H"):
                    llamadas[indice] = nuevaInformacion + "\n"
                    return modificarLlamada_aux(llamadas, indice+1, cont+1)
                else:
                    print("\nError: solo se permiten los valores H o M")
                    return modificarLlamada_aux(llamadas, indice+1, cont+1)
            else:
                print("\nError: espacio vacío")
                return modificarLlamada_aux(llamadas, indice+1, cont+1)
        elif(cont == 5):
            nuevaInformacion = input("Escriba el teléfono: ")
            if(nuevaInformacion != ""):
                if(largoTexto(nuevaInformacion) == 8 and verificaInt(nuevaInformacion) == True):
                    llamadas[indice] = nuevaInformacion + "\n"
                    return modificarLlamada_aux(llamadas, indice+1, cont+1)
                else:
                    print("\nError: el teléfono debe tener 8 dígitos de tipo numérico")
                    return modificarLlamada_aux(llamadas, indice+1, cont)
            else:
                print("\nError: espacio vacío")
                return modificarLlamada_aux(llamadas, indice+1, cont)
        elif(cont == 6):
                nuevaInformacion = input("Escriba la fecha: ")
                if(nuevaInformacion != ""):
                    if(verificaFecha(nuevaInformacion) == True):
                        llamadas[indice] = nuevaInformacion + "\n"
                        return modificarLlamada_aux(llamadas, indice+1, cont+1)
                    else:
                        print("\nError: la fecha debe tener la estructura en donde el separador '/' debe estar en la posición 3 y 6 y el año debe tener solo 4 dígitos")
                        print("\nEjemplo de fecha: 01/12/2021")
                        return modificarLlamada_aux(llamadas, indice+1, cont)
                else:
                    print("\nError: espacio vacío")
                    return modificarLlamada_aux(llamadas, indice+1, cont)
        else:
            nuevaInformacion = input("Escriba el nuevo comentario: ")
            if(nuevaInformacion != ""):
                if(largoTexto(nuevaInformacion) <= 100):
                    llamadas[indice] = nuevaInformacion + "\n"
                    return modificarLlamada_aux(llamadas, indice+1, cont+1)
                else:
                    print("El máximo de caracteres del comentario es de 100")
                    return modificarLlamada_aux(llamadas, indice, cont)
            else:
                print("\nError: espacio vacío")
                return modificarLlamada_aux(llamadas, indice+1, cont)




"""
Nombre: ver_llamadas
Entrada:recibe los siguientes parámetros listaLlamadas, total_indices, indice
Salida: la impresión de todas las llamadas que hay en el archivo
Restricciones: total_indices debe ser mayor a indice
"""

def ver_llamadas(listaLlamadas, total_indices, indice):
    if(total_indices == indice):
        input("Estas son todas sus llamadas.\nPresione enter para continuar...")
        return registro_llamadas()
    else:
        mostrarLlamada(listaLlamadas, indice, 0)
        return ver_llamadas(listaLlamadas, total_indices, indice + 10)

    






#====================================================================================================================================================================

#================================================================ FUNCIONES DEL SUBMENÚ BÚSQUEDAS AVANZADAS =========================================================


"""
Nombre: mostrarLlamada
Entradas: recibe la listallamadas
Salidas: imprime la información de la llamada 
Restricciones: si el contador es mayor al índice, entonces imprime el separador
"""


def mostrarLlamada(listaLlamadas, indice, cont):
    if(cont > 8):
        print(".......................................................................")
    else:
        if(cont == 0):
            print("Código: " + listaLlamadas[indice][0:-1])
            return mostrarLlamada(listaLlamadas, indice + 1, cont + 1)
        elif(cont == 1):
            print("Tipo de llamada: ", listaLlamadas[indice][0:-1])
            return mostrarLlamada(listaLlamadas, indice + 1, cont + 1)
        elif(cont == 2):
            print("Cédula: ", listaLlamadas[indice][0:-1])
            return mostrarLlamada(listaLlamadas, indice + 1, cont + 1)
        elif(cont == 3):
            print("Nombre: ", listaLlamadas[indice][0:-1])
            return mostrarLlamada(listaLlamadas, indice + 1, cont + 1)
        elif(cont == 4):
            print("Apellidos: ", listaLlamadas[indice][0:-1])
            return mostrarLlamada(listaLlamadas, indice + 1, cont + 1)
        elif(cont == 5):
            print("Sexo: ", listaLlamadas[indice][0:-1])
            return mostrarLlamada(listaLlamadas, indice + 1, cont + 1)
        elif(cont == 6):
            print("Teléfono: ", listaLlamadas[indice][0:-1])
            return mostrarLlamada(listaLlamadas, indice + 1, cont + 1)
        elif(cont == 7):
            print("Fecha: ", listaLlamadas[indice][0:-1])
            return mostrarLlamada(listaLlamadas, indice + 1, cont + 1)
        else:
            print("Comentario: ", listaLlamadas[indice][0:-1])
            return mostrarLlamada(listaLlamadas, indice + 1, cont + 1)

"""
Nombre: buscarLlamada
Entradas: listaLlamadas, parte, indice, alMenosUnRegistro, primerLineaLlamada
Salidas: toda la información de la llamada al que pertenece el indice
Restricciones: indice debe ser menor a la cantidad de indices de listaLamadas
"""


def buscarLlamada(listaLlamadas, parte, indice, alMenosUnRegistro, primerLineaLlamada):
    if(indice > cantidadDeIndices(listaLlamadas)):
        if(alMenosUnRegistro):
            input("\nEstas son todas las llamadas que tienes con la parte : {parte}\n")
            return busquedas_avanzadas()
        else:
            input("\nNo se encontraron llamadas con la parte : {parte}")
            return busquedas_avanzadas()
    else:
        if(seEncuentra(parte, listaLlamadas[indice])):
            mostrarLlamada(listaLlamadas, indice - primerLineaLlamada, 0)
            return buscarLlamada(listaLlamadas, parte, indice + 10, True,primerLineaLlamada)
        else:
            return buscarLlamada(listaLlamadas, parte, indice + 10, alMenosUnRegistro, primerLineaLlamada)

"""
Nombre: buscar_por_tipo_de_llamada
Entrada: recibe una E o S(tipo de llamada) dependiendo que desee buscar el usuario
Salida: imprime las llamadas que encontró con las letras indicadas
Restricciones: no posee
"""

def buscar_por_tipo_de_llamada(tipoLlamada):
    print("=======================================================================")
    print("...........BUSCANDO POR ",tipoLlamada," DEL TIPO DE LLAMADA............")
    listaLlamadas = obtenerRegistroLLamada()
    buscarLlamada(listaLlamadas, tipoLlamada,1, False, 1)
    return busquedas_avanzadas()


"""
Nombre: buscar_por_nombre
Entrada: recibe el nombre o parte de el 
Salida: imprime las llamadas que encontró con esa parte del nombre
Restricciones: no posee
"""

def buscar_por_nombre(nombre):
    print("=======================================================================")
    print(".........BUSCANDO POR PARTE ", nombre," DEL NOMBRE.........")
    listaLlamadas = obtenerRegistroLLamada()
    buscarLlamada(listaLlamadas, nombre,3, False, 3)
    return busquedas_avanzadas()
    


"""
Nombre: buscar_por_telefono
Entrada: recibe el número de teléfono o parte de el 
Salida: imprime las llamadas que encontró con esa parte del teléfono
Restricciones: no posee
"""

def buscar_por_telefono(telefono):
    print("=======================================================================")
    print(".........BUSCANDO POR PARTE ",telefono," DEL NÚMERO DE TELÉFONO.........")
    listaLlamadas = obtenerRegistroLLamada()
    buscarLlamada(listaLlamadas, telefono,6, False, 6)
    return busquedas_avanzadas()




"""
Nombre: buscarPorFecha
Entrada: recibe una parte de la fecha
Salida: imprime las llamadas que encontró con esa parte de la fecha
Restricciones: no posee
"""

def buscarPorFecha(fecha):
    print("=======================================================================")
    print("............BUSCANDO POR PARTE ",telefono," DE LA FECHA.................")
    listaLlamadas = obtenerRegistroLLamada()
    buscarLlamada(listaLlamadas, fecha,7, False, 7)
    return busquedas_avanzadas()

    
menu()

