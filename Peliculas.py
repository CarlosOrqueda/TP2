import pickle
import Usuarios


def ultimo_id():
    lista = []
    arch = open("archivo_peliculas.bin", "rb")
    seguir = True
    while seguir:
        try:
            lista = pickle.load(arch)
        except EOFError:
            seguir = False
    id = lista[0]
    arch.close()
    return id


def crear_id_peli():
    id = ultimo_id()
    num = int(id[2:5])
    num_anterior = num
    letra = id[0:2]
    if num < 999:
        num += 1
    else:
        num = 0
        num = str(num).zfill(3)
        dere = id[1]
        izq = id[0]

        if dere == "z" and num_anterior == 999:
            dere = "a"
            letra = chr(ord(izq) + 1) + dere
        else:
            letra = izq + chr(ord(dere) + 1)
    id_pelicula = letra + str(num).zfill(3)
    return id_pelicula


def datos_peli():
    id_pelicula = crear_id_peli()
    titulo = input("Titulo: ")
    director = input("Director: ")
    genero = input("Genero: ")
    puntaje = input("Puntaje: ")
    pelicula = [id_pelicula, titulo, director, genero, puntaje]
    return pelicula


def alta_peli():
    arch = open("archivo_peliculas.bin", "rb+")
    arch.seek(0, 2)
    lista = datos_peli()
    pickle.dump(lista, arch)
    arch.close()
    print("Pelicula cargada correctamente.")
    enter = input("Enter para continuar ...")


def cargar_archivo(dic):
    arch = open("archivo_peliculas.bin", "wb")

    for clave in dic:
        lista = [clave, dic[clave][0], dic[clave][1], dic[clave][2], dic[clave][3]]
        pickle.dump(lista.arch)
    arch.close()


def mostrar_peliculas():
    arch = open("archivo_peliculas.bin", "rb")
    seguir = True
    while seguir:
        try:
            elem = pickle.load(arch)
        except EOFError:
            seguir = False
        else:
            print(elem[0].ljust(10), elem[1], end='\n')
    arch.close()


def baja_peli():
    dic = {}
    arch = open("archivo_peliculas.bin", "rb")
    seguir = True
    while seguir:
        try:
            elem = pickle.load(arch)
        except EOFError:
            seguir = False
    arch.close()
    mostrar_peliculas()
    codigo_pelicula = input("Ingrese el codigo de la pelicula a borrar: ")
    del dic[codigo_pelicula]

    cargar_archivo(dic)
    print("Pelicula borrada correctamente")
    enter = input("Enter para continuar ...")


def carga_lista():
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


def mostrar_lista(lista):
    print("      {}              {}       {}".format('PELICULA'.ljust(22), 'PUNTAJE'.ljust(12), 'GENERO'))
    for pelicula in lista:
        print(pelicula['titulo'].ljust(25), pelicula['puntaje'].ljust(10), pelicula['genero'].rjust(20))


def pelicula_por_puntaje():
    lista = carga_lista()
    lista.sort(key=lambda x: (x['puntaje'], x['genero']), reverse=True)
    mostrar_lista(lista)
    enter = input("Enter para continuar ...")


def leer_archivo_binario(file_film):
    try:
        lista = pickle.load(file_film)
        return lista
    except EOFError:
        lista = [" ", " ", " ", " ", 0]
        return lista


def mostrar_lista_cortedecontrol():
    with open("archivo_peliculas.bin", "rb") as arch:
        lista = leer_archivo_binario(arch)
        director, genero, puntaje = lista[2], lista[3], lista[4]

        while genero != " ":
            total_genero = 0
            contador_genero = 0
            genero_anterior = genero
            print("Genero: ", genero.upper())
            while genero != " " and genero == genero_anterior:
                total_puntaje = 0
                contador_director = 0
                director_anterior = director
                while genero != ' ' and genero == genero_anterior and director_anterior == director:
                    total_puntaje = int(puntaje)
                    contador_director += 1
                    lista = leer_archivo_binario(arch)
                    director, genero, puntaje = lista[2], lista[3], lista[4]
                print("promedio de puntaje director: {} es {:.2f}".format(director_anterior,
                                                                          float(total_puntaje / contador_director)))
                total_genero += total_puntaje
                contador_genero += contador_director
            print("promedio por {} es {:.2f}".format(genero_anterior, float(total_genero / contador_genero)))


def carga_lista_archivo(lista):
    arch = open('archivo_peliculas_aux.bin', "wb")
    for campo in lista:
        pickle.dump(campo, arch)
    arch.close()


def pelis_por_genero():
    print("Pomedio Genero/Director")
    lista = carga_lista()
    lista.sort(key=lambda x: (x[3], x[2]))
    carga_lista_archivo(lista)
    mostrar_lista_cortedecontrol()


def verifico(cod_peli, pelicula, lista):
    aux = pelicula.split(";")
    if cod_peli not in aux:
        aux.append(cod_peli)
        lista.append(aux)
        return True
    return False


def asignar_pelicula():
    usuario = input("Ingrese nombre de usuario: ")
    pos, id, nombre, fecha, peliculas = Usuarios.buscar_usu(usuario)
    lista = []
    seguir = "s"
    mostrar_peliculas()
    while seguir == "s":
        cod_peli = input("Ingrese codigo de pelicula")
        if verifico(cod_peli, peliculas, lista):
            enter = input("Pelicula agregada correctamente...   enter para continuar.")
            seguir = 'n'
        else:
            print("Pelicula ya esta en su Usuario")
            seguir = 's'
    unir = ";"
    agregar = unir.join(lista[0])
    arch = open("usuario_maestro.bin", "r+")
    arch.seek(pos)
    Usuarios.grabar_usu(arch, id, nombre, fecha, agregar, 'a')
    arch.close()
