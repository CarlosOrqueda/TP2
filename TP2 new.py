user1=open("usuarios1.csv","r")
user2=open("usuarios2.csv","r")
user3=open("usuarios3.csv","r")
import pickle
########### LEER ARCHIVO ##############
def linea_archivo(arch,default):
          linea=arch.readline()
          return linea if linea else default     

def leer_usuario(arch):
          linea=linea_archivo(arch,"end,0,0,0,0")
          id,nombre,fecha,peliculas,estado=linea.strip().split(',')
          return id,nombre,fecha,peliculas,estado

########## GRABAR ARCHIVO ############          
def grabar_usuario(arch,id,nombre,fecha,peliculas_vistas,estado):
          arch.write(id+','+nombre+','+fecha+','+peliculas_vistas+','+estado+'\n')
          
####################################
def merge():
                    user_m=open("usuario_maestro.bin","w") 
                    id1,nombre1,fecha1,peliculas1,estado1 = leer_usuario(user1)
                    id2,nombre2,fecha2,peliculas2,estado2 = leer_usuario(user2)
                    id3,nombre3,fecha3,peliculas3,estado3 = leer_usuario(user3)

                    while id1 != 'end' or id2 != 'end' or id3 != 'end':
                              menor = min(id1,id2,id3)
                              if id1 == menor:
                                        grabar_usuario(user_m,id1,nombre1,fecha1,peliculas1,estado1)
                                        id1,nombre1,fecha1,peliculas1,estado1 = leer_usuario(user1)
                              if id2 == menor:
                                        grabar_usuario(user_m,id2,nombre2,fecha2,peliculas2,estado2)
                                        id2,nombre2,fecha2,peliculas2,estado2=leer_usuario(user2)
                              if id3 == menor:
                                        grabar_usuario(user_m,id3,nombre3,fecha3,peliculas3,estado3)
                                        id3,nombre3,fecha3,peliculas3,estado3 = leer_usuario(user3)
                    print("Merge Realizado Correctamente")
                    enter=input("Enter para continuar ...")
                    user_m.close()
                    sub_menu_user()
############### ALTA DE USUARIO #######################                    
def buscar_id():
      arch_user=open("usuario_maestro.bin","r")
      id,nombre,fecha,peliculas,estado = leer_usuario(arch_user)
      while id != 'end':
                    id_anterior=id
                    id,nombre,fecha,peliculas,estado = leer_usuario(arch_user)
                    
      num=int(id_anterior[1:4])
      if num < 999:
                vocal= id_anterior[0]
                num+= 1
                nuevo_id = vocal + str(num)
      elif num == 999:
                vocal= chr(ord(id_anterior[0])+1)
                num=100
                nuevo_id= vocal + str(num)                
      arch_user.close()
      return nuevo_id
          
def alta_user():
          id=buscar_id()
          arch_user=open("usuario_maestro.bin","r+")
          arch_user.readlines()
          
          nombre=input('Nombre y Apellido: ')
          fecha=input('Fecha de nacimiento ddmmaaaa: ')
          peliculas=' '
          estado = 'a'
          grabar_usuario(arch_user,id,nombre,fecha,peliculas,estado)
          
          print("Usuario dado de alta satisfactoriamente.")
          enter=input("Enter para continuar ...")
          
          arch_user.close()
          sub_menu_user()
          
############ BAJA DE USUARIO ###################
def buscar_posicion(buscado):
      arch=open("usuario_maestro.bin","r")
      id,nombre,fecha,peliculas,estado = leer_usuario(arch)
      while nombre != buscado:
            pos=arch.tell()
            id,nombre,fecha,peliculas,estado = leer_usuario(arch)
      arch.close()
      return pos,id,nombre,fecha,peliculas
            
def baja_user():
          buscado=input('Ingrese nombre: ')
          baja= 'b'
          pos,id,nombre,fecha,peliculas=buscar_posicion(buscado)
          arch=open("usuario_maestro.bin","r+")
          arch.seek(pos)
          grabar_usuario(arch,id,nombre,fecha,peliculas,'b')
          print("Usuarios dado de Baja Satisfactoriamente.")
          enter=input("Enter para continuar ...")
          arch.close()
          sub_menu_user()
############ MOSTRAR LISTADO #################
def mostrar_listado():
          arch=open("usuario_maestro.bin","r")
          id,nombre,fecha,peliculas,estado = leer_usuario(arch)
          print("                LISTADO DE USUARIOS.")
          while id != 'end':
                    print("{}|{}|{}|{}|{}|".format(id,nombre,fecha,peliculas,estado))
                    id,nombre,fecha,peliculas,estado = leer_usuario(arch)
          arch.close()
          enter=input("Enter para continuar ...")
          sub_menu_user()
          
########## AlTAS DE PELICULAS ###############
def ultimo_id(): #### busca el ultimo id de las peliculas
      lista=[]
      file=open("archivo_peliculas.bin","rb")

      seguir =True  
      while seguir:
            try:
                  lista=pickle.load(file)
            except EOFError:
                  seguir=False
      ide=lista[0]
      file.close()
      return ide

def genera_id_pelicula(): ## genera el id subsiguiente al ultimo de las peliculas
      
      ide=ultimo_id()            
      numero=int(ide[2:5])
      numero_ant=numero
      letra=ide[0:2]
      if numero<999 :
            numero+=1
      else: 
            numero=0
            numero=str(numero).zfill(3)
            
            dere=ide[1]
            izqui=ide[0]
            
            if dere == "z" and numero_ant==999:
                  dere="a"
                  letra=chr(ord(izqui)+1)+dere
            else:
                  letra=izqui+chr(ord(dere)+1)
                
            
      id_pelicula=letra+str(numero).zfill(3)
      return id_pelicula

def pedir_datos(): ### carga de datos de la pelicula

      pelicula=[]
      id_pelicula=genera_id_pelicula()
      titulo=input("Titulo: ")
      director=input("Director: ")
      genero=input("Genero: ")
      puntaje=input("Puntaje: ")
      pelicula=[id_pelicula,titulo,director,genero,puntaje]
      return pelicula
      
def alta_pelicula():  ##alta de una pelicula de un archivo ya creado

      
      file = open("archivo_peliculas.bin","rb+")
      file.seek(0,2)
      lista=pedir_datos()
      pickle.dump(lista,file)
      file.close()
      enter=input("Enter para continuar ...")      
      sub_menu_peliculas()
          
############# BAJA DE PELICULAS ##############
def cargar_al_archivo(dic):

      file=open("archivo_peliculas.bin","wb")
      
      for clave in dic:
            lista=[clave,dic[clave][0],dic[clave][1],dic[clave][2],dic[clave][3]]
            pickle.dump(lista,file)
      file.close()

def mostrar_peliculas():
      
      file=open("archivo_peliculas.bin","rb")
      seguir =True  ## con este codigo evito poner todos los .load de cada pickle##
      print("CODIGO     PELICULA")
      while seguir:
            try:
                  elem=pickle.load(file)
            except EOFError:
                  seguir=False
            else:
                  print(elem[0].ljust(10),elem[1],end='\n')
      file.close()

def baja_pelicula():
      dic={}
      file1=open("archivo_peliculas.bin","rb")
      seguir =True  
      while seguir:
            try:
                  lista=pickle.load(file1)
                  dic[lista[0]]=[lista[1],lista[2],lista[3],lista[4]]     
            except EOFError:
                  seguir=False
      file1.close()
      mostrar_peliculas()

      codigo_pelicula=input("ingrese el codigo de la pelicula a dar de baja: ")
      del dic[codigo_pelicula]
      
      cargar_al_archivo(dic)
      enter=input("Enter para continuar ...")      
      sub_menu_peliculas()
      
######## MOSTAR PELICULAS POR PUNTAJE #######
def carga_lista():
      
      lista=[]
      file1=open("archivo_peliculas.bin","rb")
      seguir =True  
      while seguir:
            try:
                  l=pickle.load(file1)
                  lista.append({'ide':l[0],'titulo':l[1],'director':l[2],'genero':l[3],'puntaje':l[4]})     
            except EOFError:
                  seguir=False
      
      return lista

def mostrar_lista(lista):
         print("      {}              {}       {}".format('PELICULA'.ljust(22),'PUNTAJE'.ljust(12),'GENERO'))
         for pelicula in lista:
               print(pelicula['titulo'].ljust(50),pelicula['puntaje'].ljust(10),pelicula['genero'].rjust(20))



def pelicula_por_puntaje():
      lista=carga_lista()
      lista.sort(key=lambda x:(x['puntaje'],x['genero']), reverse=True)
      mostrar_lista(lista)
      enter=input("Enter para continuar ...")      
      sub_menu_peliculas()
########## SUB MENUS ##################
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
                  pelicula_por_puntaje()
            elif opc == '4':
                  pelicula_genero()
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
                  alta_user()
            elif opc == '3':
                  baja_user()
            elif opc == '4':
                  mostrar_listado()
            elif opc == '5':
                  menu_principal()
            else:
                  enter=input("Opcion Incorrecta, enter para continuar ...")
                  sub_menu_user()
def menu_principal():
            salir = False
            palabra='  Bienvenido a NetFlip  '
            print(palabra.center(50,"*"))
            print("1) Usuarios.")
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
######## BLOQUE PRINCIPAL ############                  
menu_principal()
            
