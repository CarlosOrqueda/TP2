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
          
#####################################
def  buscar(nombre_a_bajar):
          arch=open("usuario_maestro.csv","r")
          id,nombre,fecha,peliculas,estado = leer_usuario(arch)
          while id != 'end':                   
                    while nombre  != nombre_a_bajar:
                               id,nombre,fecha,peliculas,estado = leer_usuario(arch)
                    arch.close()
                    return id
                    
def baja_user():
          nombre_a_bajar=input("Nombre: ")
          id_buscado=buscar(nombre_a_bajar)
          arch=open("usuario_maestro.csv","r+")
          id,nombre,fecha,peliculas,estado = leer_usuario(arch)

          while id != id_buscado:
                    id,nombre,fecha,peliculas,estado = leer_usuario(arch)
                    print(id)
          arch.write(id+','+nombre+','+fecha+','+peliculas+','+'b'+'\n')
          arch.close()                   

baja_user()
