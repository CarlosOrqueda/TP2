import pickle

def cargar_al_archivo(dic):

      file=open("archivo_peliculas.bin","wb")
      
      for clave in dic:
            lista=[dic[clave],clave[1],clave[2],clave[3],clave[4]]
            print(lista)
            pickle.dump(lista,file)

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

      print(" ")

      cargar_al_archivo(dic)


baja_pelicula()
