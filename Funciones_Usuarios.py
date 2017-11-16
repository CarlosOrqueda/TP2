user1 = open("usuarios1.csv", "r")
user2 = open("usuarios2.csv", "r")
user3 = open("usuarios3.csv", "r")

########### LEER ARCHIVO ##############

def linea_archivo(arch, default):
    linea = arch.readline()
    return linea if linea else default


def leer_usuario(arch):
    linea = linea_archivo(arch, "end,0,0,0,0")
    id, nombre, fecha, peliculas, estado = linea.strip().split(',')
    return id, nombre, fecha, peliculas, estado


########## GRABAR ARCHIVO ############

def grabar_usuario(arch, id, nombre, fecha, peliculas_vistas, estado):
    arch.write(id + ',' + nombre + ',' + fecha + ',' + peliculas_vistas + ',' + estado + '\n')


####################################

def merge():
    user_m = open("usuario_maestro.bin", "w")
    id1, nombre1, fecha1, peliculas1, estado1 = leer_usuario(user1)
    id2, nombre2, fecha2, peliculas2, estado2 = leer_usuario(user2)
    id3, nombre3, fecha3, peliculas3, estado3 = leer_usuario(user3)

    while id1 != 'end' or id2 != 'end' or id3 != 'end':
        menor = min(id1, id2, id3)
        if id1 == menor:
            grabar_usuario(user_m, id1, nombre1, fecha1, peliculas1, estado1)
            id1, nombre1, fecha1, peliculas1, estado1 = leer_usuario(user1)
        if id2 == menor:
            grabar_usuario(user_m, id2, nombre2, fecha2, peliculas2, estado2)
            id2, nombre2, fecha2, peliculas2, estado2 = leer_usuario(user2)
        if id3 == menor:
            grabar_usuario(user_m, id3, nombre3, fecha3, peliculas3, estado3)
            id3, nombre3, fecha3, peliculas3, estado3 = leer_usuario(user3)
    print("Merge Realizado Correctamente")
    enter = input("Enter para continuar ...")
    user_m.close()


def buscar_id():
    arch_user = open("usuario_maestro.bin", "r")
    id, nombre, fecha, peliculas, estado = leer_usuario(arch_user)
    while id != 'end':
        id_anterior = id
        id, nombre, fecha, peliculas, estado = leer_usuario(arch_user)

    num = int(id_anterior[1:4])
    if num < 999:
        vocal = id_anterior[0]
        num += 1
        nuevo_id = vocal + str(num)
    elif num == 999:
        vocal = chr(ord(id_anterior[0]) + 1)
        num = 100
        nuevo_id = vocal + str(num)
    arch_user.close()
    return nuevo_id


def alta_user():
    id = buscar_id()
    arch_user = open("usuario_maestro.bin", "r+")
    arch_user.readlines()
    nombre = input('Nombre y Apellido: ')
    fecha = input('Fecha de nacimiento ddmmaaaa: ')
    peliculas = ' '
    estado = 'a'
    grabar_usuario(arch_user, id, nombre, fecha, peliculas, estado)
    print("Usuario dado de alta satisfactoriamente.")
    enter = input("Enter para continuar ...")
    arch_user.close()


def buscar_posicion(buscado, arch):
    id, nombre, fecha, peliculas, estado = leer_usuario(arch)
    while nombre != buscado:
        pos = arch.tell()
        id, nombre, fecha, peliculas, estado = leer_usuario(arch)
    return pos, id, nombre, fecha, peliculas

def baja_user():
    arch = open("usuario_maestro.bin", "r+")
    buscado = input('Ingrese nombre: ')
    pos, id, nombre, fecha, peliculas = buscar_posicion(buscado, arch)
    arch.seek(pos)
    grabar_usuario(arch, id, nombre, fecha, peliculas, 'b')
    print("Usuarios dado de Baja Satisfactoriamente.")
    enter = input("Enter para continuar ...")
    arch.close()


def mostrar_listado():
    user_m = open("usuario_maestro.csv", "r")
    id, nombre, fecha, peliculas, estado = leer_usuario(user_m)
    print("                LISTADO DE USUARIOS.")
    while id != 'end':
        print("{}|{}|{}|{}|{}|".format(id, nombre, fecha, peliculas, estado))
        id, nombre, fecha, peliculas, estado = leer_usuario(user_m)
    user_m.close()
    enter = input("Enter para continuar ...")
