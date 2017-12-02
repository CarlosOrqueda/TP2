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

#Acceso entre usuario y aplicacion, solicita los datos para la carga de pelicula
def datos_peli():
    id_pelicula = crear_id_peli()
    while titulo=="" and director=="" and genero=="" and puntaje=="":
        print("No deje ningun campo vacio.")
        titulo = input("Titulo: ")
        director = input("Director: ")
        genero = input("Genero: ")
        puntaje = input("Puntaje: ")
    pelicula = [id_pelicula, titulo, director, genero, puntaje]
    return pelicula

#Funcion del sub menu peliculas, carga los datos al archivo peliculas
def alta_peli():
    arch = open("archivo_peliculas.bin", "rb+")
    arch.seek(0, 2)
    lista = datos_peli()
    pickle.dump(lista, arch)
    arch.close()
    print("Pelicula cargada correctamente.")
    input("Enter para continuar ...")


def cargar_archivo(dic):
    file = open("archivo_peliculas.bin", "wb")
    for clave in dic:
        lista = [clave, dic[clave][0], dic[clave][1], dic[clave][2], dic[clave][3]]
        pickle.dump(lista, file)
    file.close()


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

#Funcion sub menu peliculas.
def baja_peli():
    dic = {}
    file1 = open("archivo_peliculas.bin", "rb")
    seguir = True
    while seguir:
        try:
            lista = pickle.load(file1)
            dic[lista[0]] = [lista[1], lista[2], lista[3], lista[4]]
        except EOFError:
            seguir = False
    file1.close()
    mostrar_peliculas()
    codigo_pelicula = input("ingrese el codigo de la pelicula a dar de baja: ")
    while codigo_pelicula=="":
        codigo_pelicula = input("ingrese el codigo de la pelicula a dar de baja: ")
    del dic[codigo_pelicula]
    cargar_archivo(dic)
    input("Enter para continuar ...")


def cargar_lista():
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

def carga_lista():
    lista = []
    file1 = open("archivo_peliculas.bin", "rb")
    seguir = True
    while seguir:
        try:
            l = pickle.load(file1)
            lista.append(l)
        except EOFError:
            seguir = False
    return lista


def mostrar_lista(lista):
    print("      {}              {}       {}".format('PELICULA'.ljust(22), 'PUNTAJE'.ljust(12), 'GENERO'))
    for pelicula in lista:
        print(pelicula['titulo'].ljust(48), pelicula['puntaje'].ljust(12), pelicula['genero'].rjust(3))


def pelicula_por_puntaje():
    lista = cargar_lista()
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
    with open("archivo_peliculas_aux.bin", "rb") as file_film:
        lista = leer_archivo_binario(file_film)
        director, genero, puntaje = lista[2], lista[3], lista[4]
        while genero != ' ':
            total_genero = 0
            contador_genero = 0
            genero_anterior = genero
            print("Genero:", genero.upper())
            while genero != ' ' and genero == genero_anterior:
                total_puntaje = 0
                contador_director = 0
                director_anterior = director
                while genero != ' ' and genero == genero_anterior and director_anterior == director:
                    total_puntaje += int(puntaje)
                    contador_director += 1
                    lista = leer_archivo_binario(file_film)
                    director, genero, puntaje = lista[2], lista[3], lista[4]
                print("promedio de puntaje director: {} es {:.2f}".format(director_anterior,
                                                                          float(total_puntaje / contador_director)))
                total_genero += total_puntaje
                contador_genero += contador_director
            print("promedio por {} es {:.2f}".format(genero_anterior, float(total_genero / contador_genero)),"\n")


def carga_lista_archivo(lista):
    arch = open('archivo_peliculas_aux.bin', "wb")
    for campo in lista:
        pickle.dump(campo, arch)
    arch.close()


def pelis_por_genero():
    print("Promedio Genero/Director")
    lista = carga_lista()
    lista.sort(key=lambda x: (x[3], x[2]))
    carga_lista_archivo(lista)
    mostrar_lista_cortedecontrol()
    input("Enter para continuar ...")


def verifico(cod_peli, pelicula, lista):
    aux = pelicula.split(";")
    if cod_peli not in aux:
        aux.append(cod_peli)
        lista.append(aux)
        return True
    return False


def asignar_pelicula():
    usuario = input("Ingrese nombre de usuario: ").lower()
    lista=Usuarios.formarLista()
    if usuario in lista:
        pos, id, nombre, fecha, peliculas, estado = Usuarios.buscar_usu(usuario)
    else:
        print("Usuario incorrecto...")
        usuario = input("Ingrese nombre de usuario: ").lower()
    lista = []
    seguir = "s"
    mostrar_peliculas()
    while seguir == "s":
        cod_peli = input("Ingrese codigo de pelicula: ")
        if verifico(cod_peli, peliculas, lista):
            seguir = input("Cargar otra pelicula s/n: ")
        else:
            print("Pelicula ya esta en su Usuario")
            seguir = 's'
    unir = ";"
    agregar = unir.join(lista[0])
    arch = open("usuario_maestro.bin", "r+")
    arch.seek(pos)
    Usuarios.grabar_usu(arch, id, nombre, fecha, agregar, 'a')
    arch.close()
