def sub_menu_peliculas():
            palabra="Sub Menu Peliculas."
            print(palabra.center(50,"*"))
            print("1) Alta de Pelicula.")
            print("2) Baja de Pelicula.")
            print("3) Peliculas por Puntajes.")
            print("4) Peliculas por Genero.")
            print("5) Asignar Pelicula a Usuarios.")
            print("6) Volver al Menu Principal.")
            opc = input("Opcion: ")
            if opc == '1':
                  alta_pelicula()
            elif opc == '2':
                  baja_pelicula()
            elif opc == '3':
                  peliculas_puntaje()
            elif opc == '4':
                  peliculas_genero()
            elif opc == '5':
                  asignar_pelicula()
            elif opc == '6':
                  menu_principal()
            else:
                  enter=input("Opcion Incorrecta, enter para continuar ...")
                  sub_menu_peliculas()
            
def sub_menu_user():
            palabra="Sub Menu Usuarios."
            print(palabra.center(50,"*"))
            print("1) Merge.")
            print("2) Alta de Usuario.")
            print("3) Baja de Usuario.")
            print("4) Listas los Usuarios.")
            print("5) Volver al Menu Principal.")
            opc = input("Opcion: ")
            if opc == '1':
                  merge()
            elif opc == '2':
                  alta_usuario()
            elif opc == '3':
                  baja_usuarios()
            elif opc == '4':
                  lista_usuarios()
            elif opc == '5':
                  menu_principal()
            else:
                  enter=input("Opcion Incorrecta, enter para continuar ...")
                  sub_menu_user()
def menu_principal():
            salir = False
            palabra='  Bienvenido a NetFlip  '
            print(palabra.center(50,"*"))
            print("1) Usurios.")
            print("2) Peliculas.")
            print("3) Recomendaciones.")
            print("4) Salir.")
            opc = input("Opcion: ")
            if opc == '1':
                  sub_menu_user()
            elif opc == '2':
                  sub_menu_peliculas()
            elif opc == '3':
                  sub_menu_recomendaciones()
            elif opc == '4':
                  salir = True
            else:
                  enter=input("Opcion Incorrecta, enter para continuar ...")
                  menu_principal()
                  
menu_principal()
            
