import pickle

      
file1=open("archivo_peliculas.bin","rb")
seguir =True  ## con este codigo evito poner todos los .load de cada pickle##
while seguir:
      try:
            elem=pickle.load(file1)
      except EOFError:
            seguir=False
      else:
            print(elem)


      



    
            

