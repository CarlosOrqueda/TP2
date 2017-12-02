import Usuarios
import Peliculas
import Recomendaciones


########## SUB MENUS ##################

def sub_menu_peliculas():
    palabra = "Sub Menu Peliculas."
    print(palabra.center(50, "*"))
    opc=""
    while opc!="6":
        print("1) Alta de Pelicula. \n2) Baja de Pelicula. \n3) Peliculas por Puntaje. \n4) Peliculas por Genero."
              "\n5) Asignar Pelicula a Usuario. \n6) Volver al Menu Principal.")
        opc = input("Opcion: ")
        if opc == '1':
            Peliculas.alta_peli()
        elif opc == '2':
            Peliculas.baja_peli()
        elif opc == '3':
            Peliculas.pelicula_por_puntaje()
        elif opc == '4':
            Peliculas.pelis_por_genero()
        elif opc == '5':
            Peliculas.asignar_pelicula()
        elif opc == '6':
            print("Volviendo al menu...")
            return True
        else:
            input("Opcion Incorrecta, enter para continuar ...")
            sub_menu_peliculas()
    sub_menu_peliculas()


def sub_menu_user():
    palabra = "Sub Menu Usuarios."
    print(palabra.center(50, "*"))
    opc=""
    while opc!="5":
        print("1) Merge. \n2) Alta de Usuario. \n3) Baja de Usuario. \n4) Listar Usuarios."
          "\n5) Volver al Menu Principal.")
        opc = input("Opcion: ")
        if opc == '1':
            Usuarios.merge()     
        elif opc == '2':
            Usuarios.alta_usu()
        elif opc == '3':
            Usuarios.baja_usu()
        elif opc == '4':
            Usuarios.listado_usu()
        elif opc == '5':
            return True
        else:
            enter = input("Opcion Incorrecta, enter para continuar ... ")
            sub_menu_user()
    sub_menu_user()
   


def sub_menu_recomendaciones():
    palabra = "Sub Menu Recomendadas."
    print(palabra.center(50, "*"))
    opc=""
    while opc!='3':
        print("1) Top 5 por Genero. \n2) Recomendacion por Usuario. \n3) Volver al Menu Principal.")
        opc = input("Opcion: ")
        if opc == '1':
            Recomendaciones.top_x_genero()
        elif opc == '2':
            Recomendaciones.recomendar_pelicula()
        elif opc == '3':
            return True
        else:
            input("Opcion Incorrecta, enter para continuar ...")
            sub_menu_recomendaciones()
    sub_menu_recomendaciones()
    


######## BLOQUE PRINCIPAL ############

iniciar=True
while iniciar:
    palabra = '  Bienvenido a NetFlip  '
    print(palabra.center(50, "*"))
    print("1) Usuarios. \n2) Peliculas. \n3) Recomendaciones. \n4) Salir.")
    opc = input("Opcion: ")
    if opc == '1':
        iniciar=sub_menu_user()
    elif opc == '2':
        iniciar=sub_menu_peliculas()
    elif opc == '3':
        iniciar=sub_menu_recomendaciones()
    elif opc == '4':
        iniciar=False
        print("Saliendo...")
        input("Presione una tecla para continuar...")
    else:
        input("Opcion Incorrecta, enter para continuar ...")
        iniciar=True
