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
def grabar_usuario(arch,id,nombre,fecha,peliculas,estado):
          arch.write(id+','+nombre+','+fecha+','+peliculas+','+estado+'\n')
          
###################################
def grabarError(arch,nombre,dato1,dato2):
          lista=dato1.split(";")
          aux=dato2.split(";")
          for campo in aux:
                    if campo not in aux:
                              lista.aapend(aux)
          unir=';'
          pelis=unir.join(lista)
          arch.write(nombre + ',' + pelis  + '\n')
          
def verifcarDatos():
      errores=open("long.txt","r+")
      if nombre1 == nombre2:
            if fecha1 != fecha2:
                  grabarError(errores,nombre1,peliculas1,peliculas2)


      elif  nombre2 == nombre3:
            if fecha2 != fecha3:
                  grabarEror(errores,nombre2,peliculas2,peliculas3)

      elif nombre3 == nombre1 :
            if fecha3 != fecha2:
                  grabarError(errores,nombre3,peliculas3,peliculas1)


          
def merge(): #AGREGE ACA
                    user1=open("usuarios1.csv","r")
                    user2=open("usuarios2.csv","r")
                    user3=open("usuarios3.csv","r")                    
                    user_m=open("usuario_maestro.bin","w")
                    
                    id1,nombre1,fecha1,peliculas1,estado1 = leer_usuario(user1)
                    id2,nombre2,fecha2,peliculas2,estado2 = leer_usuario(user2)
                    id3,nombre3,fecha3,peliculas3,estado3 = leer_usuario(user3)

                    while id1 != 'end' or id2 != 'end' or id3 != 'end':
                              menor = min(id1,id2,id3)
                              #verificarDatos(nombre1,nombre2,nombre3)
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
def   validoArchivo(): #AGREGE ACA
      try:
            arch=open("usuario_maestro.bin","r+")
            valido=True
      except:
            arch=open("usuario_maestro.bin","w")
            valido=False
      return arch,valido
                    
def buscar_id():  #MODIFIQUE
      arch,valido=validoArchivo()
      if valido == False:
            vocal='a'
            num='100'
            nuevo_id=vocal+num
            
      elif valido == True:
            id,nombre,fecha,peliculas,estado = leer_usuario(arch)
            while id != 'end':
                    id_anterior=id
                    id,nombre,fecha,peliculas,estado = leer_usuario(arch)
                    
            num=int(id_anterior[1:4])
            if num < 999:
                vocal= id_anterior[0]
                num+= 1
                nuevo_id = vocal + str(num)
            elif num == 999:
                vocal= chr(ord(id_anterior[0])+1)
                num=100
                nuevo_id= vocal + str(num)

      
      return nuevo_id
          
def alta_user():
          id=buscar_id()
          arch=open("usuario_maestro.bin","r+")
          arch.seek(0,2)
          
          nombre=input('Nombre y Apellido: ')
          fecha=input('Fecha de nacimiento ddmmaaaa: ')
          peliculas=' '
          estado = 'a'
          grabar_usuario(arch,id,nombre,fecha,peliculas,estado)
          
          print("Usuario dado de alta satisfactoriamente.")
          enter=input("Enter para continuar ...")
          
          arch.close()
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
               print(pelicula['titulo'].ljust(25),pelicula['puntaje'].ljust(10),pelicula['genero'].rjust(20))

def pelicula_por_puntaje():
      lista=carga_lista()
      lista.sort(key=lambda x:(x['puntaje'],x['genero']), reverse=True)
      mostrar_lista(lista)
      enter=input("Enter para continuar ...")      
      sub_menu_peliculas()
      
############ PROMEDIO DE PUNTAJES DE LAS PELICULAS #####

def carga_lista(): # SE REPITE  EN MOSTAR PELI POR PUNTAJE SI LO QUITO ME TIRA ERROR
      
      lista=[]
      file1=open("archivo_peliculas.bin","rb")
      seguir =True  
      while seguir:
            try:
                  l=pickle.load(file1)
                  lista.append(l)     
            except EOFError:
                  seguir=False
      return lista

def leer_archivo_binario(file_film):
      try:
            lista =pickle.load(file_film)
            return lista
      except EOFError:
            lista=[" "," "," "," ",0]
            return lista

      
def mostrar_lista_cortecontrol():
      
      with open("archivo_peliculas_aux.bin","rb") as file_film:
            lista=leer_archivo_binario(file_film)
            director,genero,puntaje=lista[2],lista[3],lista[4]

            total_peliculas=0
            while genero != ' ':
                  total_genero=0
                  contador_genero=0
                  genero_anterior=genero
                  print("Genero:",genero.upper())
                  while genero != ' ' and genero == genero_anterior:
                        total_puntaje=0
                        contador_director=0
                        director_anterior=director
                        while genero != ' ' and genero == genero_anterior and director_anterior == director:
                              total_puntaje +=int(puntaje)
                              contador_director+=1
                              lista=leer_archivo_binario(file_film)
                              director,genero,puntaje=lista[2],lista[3],lista[4]
                        print("promedio de puntaje director: {} es {:.2f}".format(director_anterior,float(total_puntaje/contador_director)))
                        total_genero+=total_puntaje
                        contador_genero+=contador_director
                  
                  print("promedio por {} es {:.2f}".format(genero_anterior,float(total_genero/contador_genero)))
                  print(" ")


def carga_lista_archivo(lista):

      lista_aux=[]
      file=open('archivo_peliculas_aux.bin',"wb")
      for campo in lista:
            pickle.dump(campo,file)
      file.close()


def pelis_por_genero():
      print("PROMEDIO POR GENERO-DIRECTOR")
      lista=carga_lista()
      lista.sort(key=lambda x:(x[3],x[2]))
      carga_lista_archivo(lista)
      mostrar_lista_cortecontrol()
      enter=input("Enter para continuar ...")
      sub_menu_peliculas()
     
      
############ASIGNAR PELICULA A USUARIO##############
def verifico(eleccion,pelicula,lista): #AGREGE
          aux=pelicula.split(';')
          if eleccion not in aux:
                    aux.append(eleccion)
                    lista.append(aux)
                    
                    return True
          return False
         
def asignar_pelicula(): #AGREGE
      usuario=input("Ingrese nombre de usuario: ")
      pos,id,nombre,fecha,peliculas=buscar_posicion(usuario)
      lista=[]
      seguir = 's'
      mostrar_peliculas()  
      while seguir == 's':                     
                    eleccion=input("Ingrese Codigo de Pelicula : ")                    
                    if verifico(eleccion,peliculas,lista):
                              enter=input("Pelicula agregada correctamente...   enter para continuar.")
                              seguir= 'n'
                    else:
                              print("Pelicula ya esta en su Usuario")
                              seguir = 's'                       
      unir = ";"
      agregar=unir.join(lista[0])
      arch=open("usuario_maestro.bin","r+")
      arch.seek(pos)
      grabar_usuario(arch,id,nombre,fecha,agregar,'a')
      arch.close()
      sub_menu_peliculas()
################# RECOMENDACIONES##############
def puntoFinal():
          dic={}
          arch=open("archivo_peliculas.bin","rb")
          lista=leer_archivo_binario(arch)
          cod,nombrePelicula = lista[0],lista[1]
          while cod != " ":
                    dic[cod] = nombrePelicula
                    lista=leer_archivo_binario(arch)
                    cod,nombrePelicula = lista[0],lista[1]

          return dic

def convertir(dic):
          aux=[]
          dicAux={}
          for clave in dic:
                    campo=[clave,dic[clave]]
                    aux.append(campo)
                    
          aux.sort(key=lambda x:x[1],reverse=True)
          
          for campo in aux:
                    dicAux[campo[0]]=campo[1]
                    
          return dicAux
                    
          
def peliculasVistas(dic):
          aux={}
          arch=open("usuario_maestro.bin","r")
          id,nombre,fecha,peliculas,estado = leer_usuario(arch)
          lista=peliculas.split(";")

          while id !='end':
                    for cod in lista:
                              nombrePeli =dic[cod]
                              if nombrePeli not in aux:
                                        aux[nombrePeli]= 1
                              else:
                                        aux[nombrePeli] += 1
                    id,nombre,fecha,peliculas,estado = leer_usuario(arch)
                    lista=peliculas.split(";")
          aux=convertir(aux)
          return aux

def recomendarPelis(peliculas,pelisVistas,dic):
          lista=peliculas.split(";")
          ultimo=lista[-1]
          ultimo=dic[ultimo]
          cant=pelisVistas[ultimo]

          for clave in pelisVistas:
                    if pelisVistas[clave] <= cant:
                              return clave,pelisVistas[clave]
                    
def recomendar_pelicula():
          dic=puntoFinal()
          pelisVistas=peliculasVistas(dic)
          user=input("Ingrese Nomre de Usuario : ")
          pos,id,nombre,fecha,peliculas=buscar_posicion(user)
          nombrePeli,cant= recomendarPelis(peliculas,pelisVistas,dic)
          print("La Recomendacion es {} que fue vistas {} veces.".format(nombrePeli,cant))
          enter=input("Enter para continuar ....")
          sub_menu_recomendaciones()
          
          
########### SUB MENU RECOMENDACIONES ########
def sub_menu_recomendaciones():
          palabra="Sub Menu Recomendaciones."
          print(palabra.center(50,"*"))
          print("1) Recomendar las 5 Peliculas  mas vistas por Genero.")
          print("2) Recomendarte Pelicula.")
          print("3) Volver al menu principal")
          opc = input("Opcion: ")

          if opc== '1':
                    recomendar_generos()
          elif opc == '2':
                    recomendar_pelicula()
          elif opc == '3':
                    menu_principal()
          else:
                    enter=input("Opcion incorrecta .. enter para continuar")
                    sub_menu_recomendaciones()
                    
          
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
                  pelis_por_genero() #CAMBIE ACA
            elif opc == '5':
                  asignar_pelicula()
            elif opc == '6':
                  menu_principal()
            else:
                  enter=input("Opcion Incorrecta, enter para continuar ...")
                  sub_menu_peliculas()
            
def sub_menu_user():
            errores=open("long.txt","w")
            palabra="Sub Menu Usuarios."
            print(palabra.center(50,"*"))
            print("1) Generar Archivo.") #CAMBIE
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
            
