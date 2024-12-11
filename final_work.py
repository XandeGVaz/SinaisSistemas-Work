### Trabaho final de sinais e sistemas

## Alunos:
# Pedro Gasparelo Leme - 14602421
# Vitor Alexandre Garcia Vaz - 14611432


# Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.interpolate import interp1d


# Integral de uma função
def intg_s(a,b,N,f):
    h=(b-a)/N ##calcula tamanho das partições
    som=0 ##somatório da fórmula

    x=np.zeros(N+1)
    x[0]=a

    for k in range(1,N+1):
        x[k]=a+h*k ## valores de x a cada partição h
    
    for k in range (1,N+1):##cálculo do somatório
        xb=(x[k-1]+x[k])/2
        som=som+f(x[k-1])+4*f(xb)+f(x[k]) 

    return ((h/6)*som)