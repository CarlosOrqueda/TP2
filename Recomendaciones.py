import Peliculas
import Usuarios
import pickle


def filtrar_x_genero(genero, lista):
    peli_v = []
    for elemento in lista:
        if elemento[3] == genero:
            peli_v.append(elemento)
    return peli_v


def top_5(peli_v, genero):
    print("Top por {}: ".format(genero))
    for pelicula in peli_v:
        if len(peli_v) <= 5:
            print(pelicula[1], pelicula[3], pelicula[4])
        else:
            print(pelicula)
            if pelicula == 5:
                return


def top_x_genero():
    lista = Peliculas.carga_lista()
    genero_ingresado = input("Ingresar genero: ")
    pelis_x_genero = filtrar_x_genero(genero_ingresado, lista)
    pelis_x_genero.sort(key=lambda x: x[4], reverse=True)
    top_5(pelis_x_genero, genero_ingresado)


def recomendar_pelicula():
    nombre = input("Ingrese el nombre de usuario: ")
    pos, id, nombre, fecha, peliculas, estado = Usuarios.buscar_usu(nombre)
    lista_p = peliculas.split(";")
    dic_v = peliculas_vistas()
    filtrar(lista_p, dic_v)
    lista_recomendada = sorted(dic_v.items(), key=lambda x: x[1], reverse=True)
    peli_a_recomendar = lista_recomendada[0]
    dic = leer_pelis()
    peli_recomendada(peli_a_recomendar, dic)


def peli_recomendada(peli, dic):
    for pelicula in dic:
        if peli[0] == pelicula['id']:
            print("La pelicula recomendada es {}, vista {} veces".format(pelicula['titulo'], peli[1]))


def filtrar(lista_p, dic_v):
    for cod in lista_p:
        del dic_v[cod]


def leer_pelis():
    lista = []
    arch = open("archivo_peliculas.bin", "rb")
    seguir = True
    while seguir:
        try:
            elem = pickle.load(arch)
            lista.append({'id': elem[0], 'titulo': elem[1], 'director': elem[2], 'genero': elem[3], 'puntaje': elem[4]})
        except EOFError:
            seguir = False
    return lista


def peliculas_vistas():
    aux = {}
    arch = open("usuario_maestro.bin", "r")
    id, nombre, fecha, peliculas, estado = Usuarios.leer_usuario(arch)
    lista = peliculas.split(";")
    while id != 'end':
        dic_vistas(aux, lista)
        id, nombre, fecha, peliculas, estado = Usuarios.leer_usuario(arch)
        lista = peliculas.split(";")
    return aux


def dic_vistas(aux, lista):
    for cod in lista:
        if cod not in aux:
            aux[cod] = 1
        else:
            aux[cod] += 1
