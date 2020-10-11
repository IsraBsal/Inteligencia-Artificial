import random
import math
import numpy as np
import time

start_time = time.time() #Para calcular el tiempo

#funcion objetivo (Es la funcion que va evaluar en las dos coordenadas x,y)

def funcion_Objetivo(solucion):
    x=solucion[0] #a
    y=solucion[1] #b

    f=418.9829*2-x*math.sin(math.sqrt(abs(x)))-y*math.sin(math.sqrt(abs(y)))

    return f

#-------------------------------------------------------------------------------

#Definir el vecindario----------------------------------------------------
def vecindario(SolActual,epsilon): #Regresa un arreglo de tamano 2, contiene las coordenadas de la sol vecina

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
#print("Arreglo que contiene las cordenadas de la solucion actual",SolActual)
epsilon=10
CostoVecina=0
MejorCosto=0
#print("Costo actual= ",CostoActual)

#Nuevas variables (Sirven como contadores)
TIinicial=100 #Float
TFinal=0.001 #Float
alfa=0.95 #Float
Iter=110 #Int 


#Comienza la busqueda

SolActual=np.array([random.uniform(-500,500),random.uniform(-500,500)]) #Generamos de forma aleatoria la solucion actual
CostoActual=funcion_Objetivo(SolActual) #Calculamos el costo de SolActual
MejorSol=SolActual
MejorCosto=CostoActual
Temp=TIinicial





while(SinMejora<500000 and Ciclos<400000): #Ciclos se le puede dar mas tiempo y la corrida no debe tardar mas de 30 segundos
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

print("El mejor costo fue= ",round(CostoActual,4))
#print("Ciclos=",Ciclos)
#print("SinMejora=",SinMejora)
print("Tiempo de ejecucion %s seconds" %round((time.time() - start_time),1) )
