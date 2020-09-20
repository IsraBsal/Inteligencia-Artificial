#comenzamos declarando nuestra clase Nodo para guardar los atributos
#Clase----------------------------------------------------
class Nodo:
    def __init__(self,estado):
        self.estado = estado
        self.padre = None
        self.costo = None
        self.profundidad = None
        self.camino = None
        self.test = None
        self.num_nodo = None

    def imprime_atributos(self):
        print("Nodo:",self.num_nodo)
        print("Estado",self.estado)
        print("Padre:",self.padre)
        print("Costo=",self.costo)
        print("Profundidad=",self.profundidad)
        print("Camino=",self.camino)
        print("Test=",self.test)

#-----------------------------------------------------------

#Funciones---------------------------

def pegar_camino(camino,camino_nuevo): #Copia el camino nuevo
    for num in camino_nuevo:
        camino.append(num)

def vecinos(estado): #Devuelve los vecinos de una estacion

    vecinos=[0,0]

    vecino_izq=estado-1
    vecino_der=estado+1

    if(vecino_izq<=0):
        vecinos[0]=0
    else:
        vecinos[0]=vecino_izq

    if(vecino_der>=20):
        vecinos[1]=0

    else:
        vecinos[1]=vecino_der

    return vecinos

#-------------------------------------

from collections import deque
#Main----------------------------------------------------------------------------------------------------


print("Bienvenido")
estado=int(input("Teclea el numero correspondiente a la estacion en la que te encuentras"))
destino=int(input("Teclea el numero correspondiente a la estacion a la que quieres llegar"))

#Creamos el primer nodo e inicializamos sus atributos

#nodo=Nodo(estado,0,0,camino0,0)
test=0

if(estado==destino):
    test=1
else:
    test=0

#nodo.imprime_atributos()
#------------------------

padre=deque([])
cola=deque([estado])


#print(nodos)
#Empieza la bsuqueda--------------
while(test==0):
        #print("Tam del arreglo de padres",len(padre))
        #print("EL arreglo de padres",padre)
        #print("Valores de cola",cola)

        if(len(padre)==0):
           # print("Entre a que el tamano de padres es 0, entro con valor de cola en", cola[0])
            nodo=Nodo(cola[0])
            nodo.costo=0
            nodo.profundidad=0
            camino=[estado]
            nodo.camino=camino
            nodo.test=test
            nodo.num_nodo=0
            nodos=deque([nodo])
            #print("Primer camino",nodos[0].camino)
            nodos[len(nodos)-1].imprime_atributos()#Imprimo el primer nodo
            print("")
            vecinos_arr=vecinos(nodo.estado)#Busca los vecinos del nodo generado
            cola.popleft()#Saco al primer elemento
            #Actualizo la cola
            cola.append(vecinos_arr[0])
            cola.append(vecinos_arr[1])
            #print("Cola actualizada: ",cola)
            #Actualizo el padre
            padre.append(nodo.num_nodo)
            padre.append(nodo.num_nodo)

        else:
            if(cola[0]==0):
               # print("if de estaciones 0")
                cola.popleft()
                padre.popleft()
            else:
               # print("Else de estaciones !=0, entro con valor de cola en", cola[0])
                nodo=Nodo(cola[0])
                nodo.costo=nodos[padre[0]].costo+1
                nodo.padre=padre[0]
                nodo.profundidad=nodos[padre[0]].profundidad+1
                #-------
                estado=cola[0]
                camino_padre=[nodos[padre[0]].camino]
                camino_padre.append(estado)
                #n=len(camino_padre)
                #camino_padre.insert(n-1,cola[0])
                nodo.camino=camino_padre
                #-------
                #print("",camino_padre)
                if(nodo.estado==destino):
                    nodo.test=1
                    test=1
                else:
                    nodo.test=0
                nodo.num_nodo=len(nodos) #Aqui modifique
                nodos.append(nodo)
                nodos[len(nodos)-1].imprime_atributos()#Imprimimos cada nodo por nivel
                print("")
                vecinos_arr=vecinos(nodo.estado)
                cola.popleft()
                padre.popleft()
                #Actualizo la cola
                cola.append(vecinos_arr[0])
                cola.append(vecinos_arr[1])
              #  print("Cola actualizada: ",cola)
                #Actualizo el padre
                padre.append(nodo.num_nodo)
                padre.append(nodo.num_nodo)
              #  print("Padres actualizados: ",padre)
               # print("NOdos creados",len(nodos))

print("")
print("")
print("")
#print("Numero de nodos generados",len(nodos))
print("El camino es ",nodos[len(nodos)-1].camino)
