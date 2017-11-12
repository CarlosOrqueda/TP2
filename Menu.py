import Funciones_Usuarios
import Funciones_Peliculas
########## MENUS Y SUB MENUS ##################

def menu_principal():
    palabra = '  Bienvenido a NetFlip  '
    print(palabra.center(50, "*"))
    print("1) Usuarios. \n2) Peliculas. \n3) Recomendaciones. \n4) Salir.")
    opc = input("Opcion: ")
    if opc == '1':
        sub_menu_user()
    elif opc == '2':
        sub_menu_peliculas()
    elif opc == '3':
        sub_menu_recomendaciones()
    elif opc == '4':
        return
    else:
        enter = input("Opcion Incorrecta, enter para continuar ...")
        menu_principal()


def sub_menu_peliculas():
    palabra = "Sub Menu Peliculas."
    print(palabra.center(50, "*"))
    print("1) Alta de Pelicula. \n2) Baja de Pelicula. \n3) Peliculas por Puntaje. \n4) Peliculas por Genero."
          "\n5) Asignar Pelicula a Usuario. \n6) Volver al Menu Principal.")
    opc = input("Opcion: ")
    if opc == '1':
        Funciones_Peliculas.alta_pelicula()
    elif opc == '2':
        Funciones_Peliculas.baja_pelicula()
    elif opc == '3':
        peliculas_puntaje()
    elif opc == '4':
        peliculas_genero()
    elif opc == '5':
        asignar_pelicula()
    elif opc == '6':
        menu_principal()
    else:
        enter = input("Opcion Incorrecta, enter para continuar ...")
        sub_menu_peliculas()
    sub_menu_peliculas()


def sub_menu_user():
    palabra = "Sub Menu Usuarios."
    print(palabra.center(50, "*"))
    print("1) Merge. \n2) Alta de Usuario. \n3) Baja de Usuario. \n4) Listar Usuarios."
          "\n5) Volver al Menu Principal.")
    opc = input("Opcion: ")
    if opc == '1':
        Funciones_Usuarios.merge()
    elif opc == '2':
        Funciones_Usuarios.alta_user()
    elif opc == '3':
        Funciones_Usuarios.baja_user()
    elif opc == '4':
        Funciones_Usuarios.mostrar_listado()
    elif opc == '5':
        menu_principal()
    else:
        enter = input("Opcion Incorrecta, enter para continuar ...")
        sub_menu_user()
    sub_menu_user()


######## BLOQUE PRINCIPAL ############

menu_principal()