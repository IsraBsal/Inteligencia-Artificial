import random
import math
import numpy as np
import time

start_time = time.time() #Para calcular el tiempo
#Paso 1 solucion inicial aleatoria
SolActual=np.array([random.uniform(-500,500),random.uniform(-500,500)]) #Mejorar con unifor(a,b),N) donde N es el numero de digitos del punto a al deracha
#--------------------------------- 

#Paso 2 Crear un funcion objetivo (Es la funcion que va evaluar en las dos coordenadas x,y)

def funcion_Objetivo(solucion):
    x=solucion[0] #a
    y=solucion[1] #b

    f=418.9829*2-x*math.sin(math.sqrt(abs(x)))-y*math.sin(math.sqrt(abs(y)))

    return f

#-------------------------------------------------------------------------------

#Paso 3 Definir el vecindario----------------------------------------------------

#Cuando sea necesario actualizamos el vector SolVecina
def vecindario(SolActual,epsilon): #Refresa un arreglo de tamano 2, contiene las coordenadas de la sol vecina

    epsilon_aleatorios= np.array([epsilon*random.uniform(-1,1),epsilon*random.uniform(-1,1)])
    #print(epsilon_aleatorios)
    SolVecina=np.array(SolActual+epsilon_aleatorios)

    #Reflejando para comprobar que nuestra sol vecina esta dentro del rango
    if (SolVecina[0]>500): #Comprobamos en x por arriba
        #print("Me pase por arriba en x")
        SolVecina[0]=500-(SolVecina[0]-500)
    else:
        if(SolVecina[0]<-500): #Comprobamos x por abajo
            #print("Me pase por abajo en x")
            SolVecina[0]=-500-(SolVecina[0]+500)
    
    if (SolVecina[1]>500): #Comprobamos en y por arriba
        #print("Me pase por arriba en y")
        SolVecina[1]=500-(SolVecina[1]-500)
    else:
        if(SolVecina[1]<-500): #Comprobamos y por abajo
            #print("Me pase por abajo en y")
            SolVecina[1]=-500-(SolVecina[1]+500)
    
    return SolVecina
#---------------------------------------------------------------------------------


#Variables requeridas
# SolActual y SolVecina son vectores en R2 floats   

#Comienza Main----------------------------------------------------------------------

#Mostramos las coordenadas generadas por SolActual
print("Arreglo que contiene las cordenadas de la solucion actual",SolActual)
epsilon=1000
CostoVecina=0
#Calculamos el costo de SolActual
CostoActual=funcion_Objetivo(SolActual)
print("Costo actual= ",CostoActual)

#Contadores
SinMejora=0
Ciclos=0


while(SinMejora<1000 and Ciclos<10000): #Ciclos se le puede dar mas tiempo y la corrida no debe tardar mas de 30 segundos
    Ciclos+=1
    #Generamos la solucion vecina
    SolVecina=vecindario(SolActual,epsilon)
    #print("Solucion vecina ",SolVecina)
    #Evaluamos costo vecina
    CostoVecina=funcion_Objetivo(SolVecina)
    if(CostoVecina<=CostoActual):
        CostoActual=CostoVecina
        SolActual=SolVecina
        if(CostoVecina<CostoActual):
            SinMejora=0
        else:
            SinMejora+=1
    else:
        SinMejora+=1

print("El mejor costo fue= ",CostoActual)
print("Ciclos=",Ciclos)
print("SinMejora=",SinMejora)
print("--- %s seconds ---" % (time.time() - start_time))