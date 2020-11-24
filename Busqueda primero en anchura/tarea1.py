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


#Main----------------------------------------------------------------------------------------------------
from collections import deque

print("Bienvenido")
estado=int(input("Teclea el numero correspondiente a la estacion en la que te encuentras \n"))
destino=int(input("Teclea el numero correspondiente a la estacion a la que quieres llegar \n"))



#Logica para empezar la busqueda
test=0
if(estado==destino):
    test=1
else:
    test=0
#----------------------------------

#Creamos los arreglos de la sugerencia
padre=deque([])
cola=deque([estado])
#-------------------------------------


#Empieza la busqueda------------------
while(test==0):
        #Para crear el primer nodo de la busqueda
        if(len(padre)==0):
           #Inicializando todos los atributos
            nodo=Nodo(cola[0])
            nodo.costo=0
            nodo.profundidad=0
            camino=[estado]
            nodo.camino=camino
            nodo.test=test
            nodo.num_nodo=0
            nodos=deque([nodo])
            #Imprimo el primer nodo
            nodos[len(nodos)-1].imprime_atributos()
            print("")
            #Busca los vecinos del nodo generado
            vecinos_arr=vecinos(nodo.estado)
            #Saco al primer elemento
            cola.popleft()
            #Actualizo la cola
            cola.append(vecinos_arr[0])
            cola.append(vecinos_arr[1])
            #print("Cola actualizada: ",cola)
            #Actualizo el padre
            padre.append(nodo.num_nodo)
            padre.append(nodo.num_nodo)

        else:
            if(cola[0]==0):
               # print("if de estaciones 0") Si entra en este if quiere decir que en la cola habia una estacion que no existe en la linea 
                cola.popleft()
                padre.popleft()
            else:
               # Creacion de nodo (Se llenan los atributos del nodo)
                nodo=Nodo(cola[0])
                nodo.costo=nodos[padre[0]].costo+1
                nodo.padre=padre[0]
                nodo.profundidad=nodos[padre[0]].profundidad+1
                estado=cola[0]
                camino_padre=[nodos[padre[0]].camino]
                camino_padre.append(estado)
                #n=len(camino_padre)
                #camino_padre.insert(n-1,cola[0])
                nodo.camino=camino_padre
                #print("",camino_padre)
                if(nodo.estado==destino):
                    nodo.test=1
                    test=1
                else:
                    nodo.test=0
                nodo.num_nodo=len(nodos) 
                nodos.append(nodo)
                #Imprimimos cada nodo por nivel
                nodos[len(nodos)-1].imprime_atributos()
                print("")
                #Busca los vecinos del nodo generado
                vecinos_arr=vecinos(nodo.estado)
                #Saco al elemento de la cola que atendi
                cola.popleft()
                padre.popleft()
                #Actualizo la cola
                cola.append(vecinos_arr[0])
                cola.append(vecinos_arr[1])
                #print("Cola actualizada: ",cola)
                #Actualizo el padre
                padre.append(nodo.num_nodo)
                padre.append(nodo.num_nodo)
                #print("Padres actualizados: ",padre)
                #print("NOdos creados",len(nodos))

print("")
print("")
print("")
#print("Numero de nodos generados",len(nodos))
print("El camino es ",nodos[len(nodos)-1].camino)
