import Peliculas
import Usuarios
import pickle

#Recibe el genero a comparar y una lista de listas. Donde cada lista tiene la info de las peliculas
#Devuelve una lista de listas con info de las peliculas ya filtradas.
def filtrar_x_genero(genero, listas):
    peli_v = []
    for elemento in listas:
    
        if elemento[3] == genero:
            peli_v.append(elemento)
    return peli_v

#Devuelve el top 5 de peliculas por genero.
def top_5(peli_v, genero):
    print("Top por {}: ".format(genero))
    top=0
    for pelicula in peli_v:
        if top<5:
            print("{} del director {} con {}/10 de puntaje ".format(pelicula[1].capitalize(), pelicula[2].capitalize(), pelicula[4]))
            top+=1
    input("Presione una tecla para continuar...")
#Verifica la existencia de genero en la base de datos
def existe_genero():
    gen=[]
    generos=open("archivo_peliculas.bin","rb")
    seguir=True
    while seguir:
        try:
            linea = pickle.load(gen)
            lista.append(gen[3])
        except EOFError:
            seguir = False
            return lista_gen


#Funcion del sub menu recomendaciones, organiza las sub funciones. Llama a la funcion top_5 para imprimir.
def top_x_genero():
    lista_gen = Peliculas.carga_lista()
    genero_ingresado = input("Ingresar genero: ")
    if genero_ingresado not in lista_gen:
        print("No hay peliculas cargadas con su eleccion...")
    else:
        pelis_x_genero = filtrar_x_genero(genero_ingresado, lista)
        pelis_x_genero.sort(key=lambda x: x[4], reverse=True)
        top_5(pelis_x_genero, genero_ingresado)

#Funcion del Sub menu recomendaciones
def recomendar_pelicula():
    nombre = input("Ingrese el nombre de usuario: ")
    usuarios=Usuarios.formarLista()
    if nombre in usuarios:
        pos, id, nombre, fecha, peliculas, estado = Usuarios.buscar_usu(nombre)
        lista_p = peliculas.split(";")
        dic_v = peliculas_vistas()
        filtrar(lista_p, dic_v)
        lista_recomendada = sorted(dic_v.items(), key=lambda x: x[1], reverse=True)
        peli_a_recomendar = lista_recomendada[0]
        dic = leer_pelis()
        peli_recomendada(peli_a_recomendar, dic)
    else:
        print("No existe el usuario")

#Devuelve la peli recomendada por usuario, recibe el primer elemento de la lista de peliculas (id) luego de filtrar
#Y una lista de dicionarios con info de cada pelicula. 
def peli_recomendada(peli, dic):
    for pelicula in dic:
        if peli[0] == pelicula['id']:
            print("La pelicula recomendada es {}, vista {} veces".format(pelicula['titulo'], peli[1]))
            input("Presione una tecla para continuar...")

#Recibe una lista con la info de todas las peliculas y un diccionario con codigos de peliculas y cantidad de vistas

def filtrar(lista_p, dic_v):
    for cod in lista_p:
        del dic_v[cod]

#Leé del archivo maestro las peliculas y devuelve la info de peliculas en una lista de diccionarios
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

def dic_vistas(aux, lista):
    for codigo_pelicula in lista:
        if codigo_pelicula not in aux:
            aux[codigo_pelicula] = 1
        else:
            aux[codigo_pelicula] += 1
#Devuelve un diccionario con codigo y cantidad de vistas de una pelicula
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

