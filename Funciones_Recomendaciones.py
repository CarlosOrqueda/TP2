import Funciones_Peliculas
import Funciones_Usuarios
import pickle

def dic_vistas(peliculas):
    dic_v = {}
    for campo in peliculas:
        for campo in dic_v:
            if campo not in dic_v:
                dic_v[campo] = 1
            else:
                dic_v[campo] += 1


def top_x_genero():
    user_m = open("usuario_maestro.bin", "r")
    id, nombre, fecha, peliculas, estado = Funciones_Usuarios.leer_usuario(user_m)
    while id != "end":
        pelicula = peliculas.split(";")
        dic_vistas(pelicula)
        id, nombre, fecha, peliculas, estado = Funciones_Usuarios.leer_usuario(user_m)
    top = sorted(dic_vistas(), key=lambda x :x[1])
    print(top[0:5])

    #llamaria metodo mostrar en funciones peliculas

