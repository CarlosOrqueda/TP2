# egbusquin@gmail.com mandenme el nombre del grupo y los integrantes
# busqueda de usuario inexistente y menu sin recursividad
# acotar el top 5 a 5


def leer_linea(arch, default):
    linea = arch.readline()
    return linea if linea else default


def leer_usuario(arch):
    linea = leer_linea(arch, "end,0,0,0,0")
    id, nombre, fecha, peliculas, estado = linea.strip().split(",")
    return id, nombre, fecha, peliculas, estado

#Devuelve un diccionario de usuarios y fecha de nacimiento
def auxiliar_diccionario():
    maestro=open("usuario_maestro.bin", "r+")
    usuarios={}
    id, usuario, fecha, peliculas, estado=leer_usuario(maestro)
    while id!="end":
        usuarios[usuario]=fecha
        id, usuario, fecha, peliculas, estado=leer_usuario(maestro)
    maestro.close()
    return usuarios

#Ingresa usuario y fecha de nacimiento a grabar, verifica si estan en archivo y devuelve un valor booleano.
def existe_usuario(nombre, fecha):
    usuarios=auxiliar_diccionario()
    if nombre in usuarios and fecha in usuarios.values():
        return True
    else:
        return False

def grabar_usu(arch, id, nombre, fecha, peliculas, estado):
    arch.write(id + ',' + nombre + ',' + fecha + ',' + peliculas + ',' + estado + '\n')

def grabarError(arch, nombre, dato1, dato2):
    lista = dato1.split(";")
    aux = dato2.split(";")
    for campo in aux:
        if campo not in aux:
            lista.append(aux)
    unir = ';'
    pelis = unir.join(lista)
    arch.write(nombre + ',' + pelis + '\n')


def verificarDatos(nombre1, fecha1, peliculas1, nombre2, fecha2, peliculas2, nombre3, fecha3, peliculas3):
    errores = open("long.txt", "r+")
    if nombre1 == nombre2:
        if fecha1 != fecha2:
            grabarError(errores, nombre1, peliculas1, peliculas2)
    elif nombre2 == nombre3:
        if fecha2 != fecha3:
            grabarError(errores, nombre2, peliculas2, peliculas3)
    elif nombre3 == nombre1:
        if fecha3 != fecha2:
            grabarError(errores, nombre3, peliculas3, peliculas1)
        

def merge():
    usu1 = open("usuarios1.csv", "r")
    usu2 = open("usuarios2.csv", "r")
    usu3 = open("usuarios3.csv", "r")
    usu_m = open("usuario_maestro.bin", "w")

    id1, nombre1, fecha1, peliculas1, estado1 = leer_usuario(usu1)
    id2, nombre2, fecha2, peliculas2, estado2 = leer_usuario(usu2)
    id3, nombre3, fecha3, peliculas3, estado3 = leer_usuario(usu3)

    verificarDatos(nombre1, fecha1, peliculas1, nombre2, fecha2, peliculas2, nombre3, fecha3, peliculas3)

    while id1 != "end" or id2 != "end" or id3 != "end":
        menor = min(id1, id2, id3)
        if id1 == menor:
            grabar_usu(usu_m, id1, nombre1, fecha1, peliculas1, estado1)
            id1, nombre1, fecha1, peliculas1, estado1 = leer_usuario(usu1)
            verificarDatos(nombre1, fecha1, peliculas1, nombre2, fecha2, peliculas2, nombre3, fecha3, peliculas3)
        elif id2 == menor:
            grabar_usu(usu_m, id2, nombre2, fecha2, peliculas2, estado2)
            id2, nombre2, fecha2, peliculas2, estado2 = leer_usuario(usu2)
            verificarDatos(nombre1, fecha1, peliculas1, nombre2, fecha2, peliculas2, nombre3, fecha3, peliculas3)
        else:
            grabar_usu(usu_m, id3, nombre3, fecha3, peliculas3, estado3)
            id3, nombre3, fecha3, peliculas3, estado3 = leer_usuario(usu3)
            verificarDatos(nombre1, fecha1, peliculas1, nombre2, fecha2, peliculas2, nombre3, fecha3, peliculas3)
    print("Archivo unificado correctamente")
    enter = input("Presione Enter para continuar...")
    usu_m.close()


def existe_archivo():
    try:
        arch = open("usuario_maestro.bin", "r+")
        valido = True
    except:
        arch = open("usuario_maestro.bin", "w")
        valido = False
    return arch, valido


def crear_id():
    arch, valido = existe_archivo()
    if valido == False:
        vocal = "a"
        num = "100"
        nuevo_id = vocal + num
    else:
        id, nombre, fecha, peliculas, estado = leer_usuario(arch)
        while id != "end":
            id_anterior = id
            id, nombre, fecha, peliculas, estado = leer_usuario(arch)
    num = int(id_anterior[1:4])
    if num < 999:
        vocal = id_anterior[0]
        num += 1
        nuevo_id = vocal + str(num)
    else:
        vocal = chr(ord(id_anterior[0]) + 1)
        num = "100"
        nuevo_id = vocal + str(num)

    return nuevo_id

#Da el alta un usuario por verificacion de nombre y fecha en base de datos, si ya existe lo da de alta.
def alta_usu():
    arch = open("usuario_maestro.bin", "r+")
    arch.seek(0, 2)
    peliculas = " "
    estado = "a"
    nombre = input("Nombre y Apellido: ").lower()
    fecha = input("Fecha de nacimiento ddmmaaaa: ")
    while nombre=="" and fecha=="":
        nombre = input("Nombre y Apellido: ").lower()
        fecha = input("Fecha de nacimiento ddmmaaaa: ")
    verificacion=existe_usuario(nombre, fecha)
    if verificacion:
        pos, id, nombre, fecha, peliculas,estado =buscar_usu(nombre)
        arch.seek(pos)
        grabar_usu(arch, id, nombre, fecha, peliculas, estado)
        print("El usuario que ingresó ya se encuentra en sistema...Se cambio el estado a alta.")
    else:
        id = crear_id()
        grabar_usu(arch, id, nombre, fecha, peliculas, estado)
        print("Su id es: ",id)
        print("Usuario dado de alta satisfactoriamente.")
    enter = input("Enter para continuar...")
    arch.close()
#Busca el usuario por nombre, devuelve la info del mismo
def buscar_usu(usu_buscado):
    arch = open("usuario_maestro.bin", "r")
    id, nombre, fecha, peliculas, estado = leer_usuario(arch)
    while nombre != usu_buscado:
        pos = arch.tell()
        id, nombre, fecha, peliculas, estado = leer_usuario(arch)
    arch.close()
    return pos, id, nombre, fecha, peliculas, estado

#Devuelve una lista de usuarios
def formarLista():
    lista = []
    arch = open("usuario_maestro.bin", "r")
    id, nombre, fecha, peliculas, estado = leer_usuario(arch)
    while id != 'end':
        lista.append(nombre)
        id, nombre, fecha, peliculas, estado = leer_usuario(arch)
    arch.close()
    return lista
#Funcion del submenu usuarios, busca la posicion del usuario y da la baja.
def baja_usu():
    listaNombres = formarLista()
    buscado = input('Ingrese nombre: ')
    if buscado in listaNombres:
        baja = 'b'
        pos, id, nombre, fecha, peliculas, estado = buscar_usu(buscado)
        arch = open("usuario_maestro.bin", "r+")
        arch.seek(pos)
        grabar_usu(arch, id, nombre, fecha, peliculas, baja)
        print("Usuario dado de Baja Satisfactoriamente.")
        enter = input("Enter para continuar ...")
        arch.close()
        return
    else:
        print("El nombre no se encuentra en nuestra Base de datos.")
        enter = input("Enter para continuar ...")
        #baja_usu()

def listado_usu():
    arch = open("usuario_maestro.bin", "r")
    id, nombre, fecha, peliculas, estado = leer_usuario(arch)
    while id != "end":
        print("{}|{}|{}|{}|{}".format(id, nombre, fecha, peliculas, estado))
        id, nombre, fecha, peliculas, estado = leer_usuario(arch)
    arch.close()
    enter = input("Enter para continuar ...")


def grabarError(arch, nombre, dato1, dato2):
    lista = dato1.split(";")
    aux = dato2.split(";")
    for campo in aux:
        if campo not in aux:
            lista.append(aux)
    unir = ';'
    pelis = unir.join(lista)
    arch.write(nombre + ',' + pelis + '\n')


