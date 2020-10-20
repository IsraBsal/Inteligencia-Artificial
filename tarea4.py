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

#Funcion para rellenar la matriz con las soluciones aleatorias
def generar_Poblacion():
    p=np.zeros((13,2))
    for i in range(13):
        for j in range(2):
            p[i][j]=random.uniform(-500,500)
    return p
#---------------------------------------------------------------