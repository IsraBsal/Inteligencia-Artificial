import random
import math
import numpy as np
import time

start_time = time.time() #Para calcular el tiempo

#funcion objetivo (Es la funcion que va evaluar en las dos coordenadas x,y)
def funcion_Objetivo(x,y):

    f=418.9829*2-x*math.sin(math.sqrt(abs(x)))-y*math.sin(math.sqrt(abs(y)))

    return f
#-------------------------------------------------------------------------------

#Funcion para rellenar la matriz con las soluciones aleatorias, devuelve una matriz de 13,2
def generar_Poblacion():
    p=np.zeros((13,2))
    for i in range(13):
        for j in range(2):
            p[i][j]=random.uniform(-500,500)
    return p
#---------------------------------------------------------------

#Funcion para rellenar el arreglo de costos de cada individuo de la poblacion, devuelve un arreglo de tamanio 13
def costo_Poblacion(p):
    
    costo=np.zeros((13))
    for i in range(13):
        for j in range(2):
            if(j==0):
                costo_x=p[i][j]
            else:
                costo_y=p[i][j]
        costo[i]=funcion_Objetivo(costo_x,costo_y)
    return costo
#-----------------------------------------------------------------------------

#Funcion para generar el mutante, necesita la matriz para sacar cada poblador con sus cordenadas en x,y. i,j y k sirven para escoger el renglon.
def generar_Mutante(p,i,j,k):
    
    #Definimos a los pobladores
    p1=np.array([p[i][0],p[i][1]])
    p2=np.array([p[j][0],p[j][1]])
    p3=np.array([p[k][0],p[k][1]])
    #-----------------------------
    
    F=0.5

    #Calculamos las coordenadas del mutante
    Mutante=np.zeros((2))
    Mutante[0]=p1[0]+F*(p2[0]-p3[0])
    Mutante[1]=p1[1]+F*(p2[1]-p3[1])
    #-------------------------------------

    #Reflejando para comprobar que nuestro Solucion mutante esta dentro del rango
    if (Mutante[0]>500): #Comprobamos en x por arriba
        #print("Me pase por arriba en x")
        Mutante[0]=500-(Mutante[0]-500)
    else:
        if(Mutante[0]<-500): #Comprobamos x por abajo
            #print("Me pase por abajo en x")
            Mutante[0]=-500-(Mutante[0]+500)
    
    if (Mutante[1]>500): #Comprobamos en y por arriba
        #print("Me pase por arriba en y")
        Mutante[1]=500-(Mutante[1]-500)
    else:
        if(Mutante[1]<-500): #Comprobamos y por abajo
            #print("Me pase por abajo en y")
            Mutante[1]=-500-(Mutante[1]+500)


    return Mutante
#----------------------------------------------------------------------------

#Funcion para generar el hijo-----------------------------------
def GenerarHijo(p,m,Mutante):
    Hijo=np.zeros((2))
    Cr=0.5
    i=random.randint(0,1) #Entrada heredada del mutante 
    for j in range(2):
        if(random.uniform(0,1)<Cr):
            Hijo[j]=Mutante[j]
        else:
            Hijo[j]=Mutante[j]
    Hijo[i]=p[m][j]
    return Hijo
#-----------------------------------------------------------------








