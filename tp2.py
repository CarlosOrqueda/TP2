usuarios=open("usuarios.csv","r+")
peliculas=open("peliculas.csv","r+")

def presentacion():
          print(' #### ##            ####       #######    ##########      ########         ####                #########  ')
          print(' #### ###         ####      #######    ##########      ########         ####                #########         ')
          print(' #########    ####      ###                       ####               ###                       ####                        ###   ')
          print(' ####       ## #####       #######            ####               ########         ####                       ###     ')
          print(' ####         #######      #######           ####               ########         ####                      ###')
          print(' ####           ######       ###                      ####               ####                    ####                      ###   ')
          print(' ####            ######      #######          ####               ####                    ########     ####### #')
          print(' ####               #####     #######          ####               ####                    ########     ####### #')

def linea_archivo(arch,default):
          linea=arch.readline()
          return linea if linea else default        

def leer_usuario(arch):
          linea=linea_archivo(arch,"end,0,0,0")
          id,nombre,fecha,peliculas=linea.strip().split(',')
          return id,nombre,fecha,peliculas     
          
def grabar_usuario(arch,id,nombre,fecha,peliculas_vistas):
          arch.readlines()
          arch.write(id+','+nombre+','+fecha+','+peliculas_vistas+'\n')

def grabar_pelicula(arch,id,nombre,director,genero,puntaje):
          arch.readlines()
          arch.readlines(id+','+nombre+','+director+','+genero+','+puntaje+'\n')
          
def alta_usuario(usuarios):
          id=input('ID: ')
          nombre=input('Nombre y Apellido: ')
          fecha=input('Fecha de nacimiento ddmmaaaa: ')
          peliculas_vistas=' '
          grabar_usuario(usuarios,id,nombre,fecha,peliculas_vistas)

def alta_pelicula(arch):
          id=input('ID: ')
          nombre=input('Nombre de Pelicula: ')
          director=input('Director: ')
          genero=input('Genero: ')
          puntaje=input('Puntaje: ')
          grabar_pelicula(arch,id,nombre,director,genero,puntaje)


def baja_usuario(usuarios):
          arch=open("bajas.csv","w")
          nombre_a_bajar=input('Ingrese nombre: ')
          id,nombre,fecha,peliculas = leer_usuario(usuarios)
          while id != 'end':
                    if nombre != nombre_a_bajar:                              
                              arch.write(id+','+nombre+','+fecha+','+peliculas+'\n')                              
                              id,nombre,fecha,peliculas=leer_usuario(usuarios)
                    elif nombre == nombre_a_bajar:
                              id,nombre,fecha,peliculas=leer_usuario(usuarios)
                              
          
def menu_principal(usarios,peliculas):
          salir=True
          while salir == True:
                    palabra='  Bienvenido a NetFlip  '
                    print(palabra.center(50,"*"))
                    print('1) Alta de Usuario')
                    print('2) Alta de Pelicula')
                    print('3) Baja de Usuario')
                    print('4) Baja de Pelicula')
                    print('5) Salir')
                    opc = input('Opcion: ')

                    if opc == '1':
                              alta_usuario(usuarios)
                    elif opc == '2':
                              alta_pelicula(peliculas)
                    elif opc == '3':
                              baja_usuario(usuarios)
                    elif opc == '4':
                              baja_pelicula(peliculas)
                    elif opc == '5':
                              salir = False
                              usuarios.close()
                              peliculas.close()
                    else:
                              print('Opcion Incorrecta .... enter para continuar')
                              enter=input('')

presentacion()
menu_principal(usuarios,peliculas)
