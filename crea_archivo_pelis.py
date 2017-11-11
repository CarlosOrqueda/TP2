'''
lista1 = ["aa001","spiderman","Roger Braun","ficcion",8]
lista2 = ["aa002","el conjuro","Susan Bler","terror",6]
lista3 = ["aa003","rapidos y furiosos","Thor Himan","accion",9]
lista4 = ["aa004","no respires","Stephen kiman","terorr",7]
lista5 = ["aa005","el planeta de los simios","Bler turnner","ficcion",6]
lista6 = ["aa006","chucky","roger Braun","ficcion",8]
lista7 = ["aa007","everest","Thor Himan","ficcion",6]
'''

import pickle
     
def pedir_datos():

      pelicula=[]
      id_pelicula="aa001"
      titulo=input("Titulo: ")
      director=input("Director: ")
      genero=input("Genero: ")
      puntaje=input("Puntaje: ")
      pelicula=[id_pelicula,titulo,director,genero,puntaje]
      return pelicula


## carga UNA pelicula en un archivo binario vacio
file = open("archivo_peliculas.bin","wb")
file.seek(0,2)
pedir=input("¿desea ingresar una pelicula?.. S/N ")
while pedir == "s":
      lista=pedir_datos()
      pickle.dump(lista,file)
      pedir=input("desea ingresar datos de la pelicula??.. S/N ")
file.close()



