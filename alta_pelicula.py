import pickle

## este codigo genera al subsiguiente apartir de aa001 hasta zz999


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
##############################################################
      

'''def cargar_al_archivo(dic):

      for clave in dic:
            dic[clave]=

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

      codigo_pelicula=input("ingrese el codigo de la pelicula a dar de baja")
      del dic[codigo_pelicula]
      print(dic)
      #cargar_al_archivo(dic)


alta_pelicula()
baja_pelicula()
'''
alta_pelicula()
