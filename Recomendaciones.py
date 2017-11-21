import Peliculas
import Usuarios


def dic_recomedaciones():
    dic = {}
    arch = open("archivo_peliculas.bin", "rb")
    lista = Peliculas.leer_archivo_binario(arch)
    cod, nombrePelicula = lista[0], lista[1]
    while cod != " ":
        dic[cod] = nombrePelicula
        lista = Peliculas.leer_archivo_binario(arch)
        cod, nombrePelicula = lista[0], lista[1]
    return dic


def convertir(dic):
    dicAux = {}
    lista = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for campo in lista:
        dicAux[campo[0]] = campo[1]
    return dicAux


def peliculas_vistas(dic):
    aux = {}
    arch = open("usuario_maestro.bin", "r")
    id, nombre, fecha, peliculas, estado = Usuarios.leer_usuario(arch)
    lista = peliculas.split(";")
    while id != 'end':
        for cod in lista:
            nombrePeli = dic[cod]
            if nombrePeli not in aux:
                aux[nombrePeli] = 1
            else:
                aux[nombrePeli] += 1
        id, nombre, fecha, peliculas, estado = Usuarios.leer_usuario(arch)
        lista = peliculas.split(";")
    aux = convertir(aux)
    return aux


def recomendar_pelis(peliculas, pelis_vistas, dic):
    lista = peliculas.split(";")
    ultimo = lista[-1]
    ultimo = dic[ultimo]
    cant = pelis_vistas[ultimo]

    for clave in pelis_vistas:
        if pelis_vistas[clave] <= cant:
            return clave, pelis_vistas[clave]


def recomendar_pelicula():
    dic = dic_recomedaciones()
    pelis_vistas = peliculas_vistas(dic)
    user = input("Ingrese Nomre de Usuario : ")
    pos, id, nombre, fecha, peliculas = Usuarios.buscar_usu(user)
    nombre_peli, cant = recomendar_pelis(peliculas, pelis_vistas, dic)
    print("La Recomendacion es {} que fue vistas {} veces.".format(nombre_peli, cant))
    enter = input("Enter para continuar ....")


def dic_vistas(aux, dic_v):
    for campo in aux:
        if campo not in dic_v:
            dic_v[campo] = 1
        else:
            dic_v[campo] += 1
    return dic_v


def filtrar_x_genero(genero, lista, dic_v):
    aux = []
    for tipo_genero in lista:
        if tipo_genero[3] == genero:
            aux.append(tipo_genero)
    dic_aux = dic_vistas(aux, dic_v)
    dic_aux = sorted(dic_aux.items(), key=lambda x: x[1])
    return dic_aux


def top_x_genero():
    dic_v = {}
    lista = Peliculas.carga_lista()
    genero_ingresado = input("Ingresar genero: ")
    pelis_x_genero = filtrar_x_genero(genero_ingresado, lista, dic_v)
    print(pelis_x_genero[0:5])
