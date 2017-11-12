import Funciones_Peliculas
import Funciones_Usuarios
import pickle

def dic_vistas(peliculas):
    dic_v = {}
    for pelicula in dic_v:
        if peliculas not in dic_v:
            dic_v[peliculas] = 1
        else:
            dic_v[peliculas] += 1


def top_x_genero():
    user_m = open("usuario_maestro.csv", "r")
    id, nombre, fecha, peliculas, estado = Funciones_Usuarios.leer_usuario(user_m)
    while peliculas != 0:
        dic_vistas(peliculas)
