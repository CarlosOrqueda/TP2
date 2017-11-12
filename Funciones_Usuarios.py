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
    user_m = open("usuario_maestro.csv", "w")
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
    arch_user = open("usuario_maestro.csv", "r+")
    id, nombre, fecha, peliculas, estado = leer_usuario(arch_user)
    while id != 'end':
        id_anterior = id
        id, nombre, fecha, peliculas, estado = leer_usuario(arch_user)
    vocal = chr(ord(id_anterior[0]) + 1)
    num = str(int(id_anterior[1:4]) + 1)
    nuevo_id = vocal + num
    return nuevo_id


def alta_user():
    id = buscar_id()
    arch_user = open("usuario_maestro.csv", "r+")
    arch_user.readlines()
    nombre = input('Nombre y Apellido: ')
    fecha = input('Fecha de nacimiento ddmmaaaa: ')
    peliculas = ' '
    estado = 'a'
    grabar_usuario(arch_user, id, nombre, fecha, peliculas, estado)
    print("Usuario dado de alta satisfactoriamente.")
    enter = input("Enter para continuar ...")
    arch_user.close()


def baja_user():
    user_m = open("usuario_maestro.csv", "r")
    nombre_a_bajar = input('Ingrese nombre: ')
    baja = 'b'
    actualizado = open("usuarios_actualizados.csv", "w")
    id, nombre, fecha, peliculas, estado = leer_usuario(user_m)
    while id != 'end':
        if nombre == nombre_a_bajar:
            grabar_usuario(actualizado, id, nombre, fecha, peliculas, baja)
            print("Usuario dado de baja.")
            id, nombre, fecha, peliculas, estado = leer_usuario(user_m)
        else:
            grabar_usuario(actualizado, id, nombre, fecha, peliculas, estado)
            id, nombre, fecha, peliculas, estado = leer_usuario(user_m)
    enter = input("Enter para continuar ...")
    user_m.close()
    actualizado.close()


def mostrar_listado():
    user_m = open("usuario_maestro.csv", "r")
    id, nombre, fecha, peliculas, estado = leer_usuario(user_m)
    print("                LISTADO DE USUARIOS.")
    while id != 'end':
        print("{}|{}|{}|{}|{}|".format(id, nombre, fecha, peliculas, estado))
        id, nombre, fecha, peliculas, estado = leer_usuario(user_m)
    user_m.close()
    enter = input("Enter para continuar ...")
