import numpy
import scipy
from scipy import signal as sf
import matplotlib.pyplot as mp

#Projeto do filtro PB RC
# y[n] = a x[n] + a x[n-1] - b y[n-1]
data = numpy.memmap("sweep.pcm", dtype='h', mode='r')

ynm1 = 0
xnm1 = 0

#calculando os parametros Wc = 2*pi*Fc
Fc = 100
Fs = 8000
Wc = 2 * numpy.pi * Fc

Fli = 2 * Fs
a =  Wc / (Fli + Wc)
b =  (Wc - Fli) / (Fli + Wc)

tamaloop = len(data)
vet_saida =[]


j=1

for j  in range(tamaloop):
    input = data[j]
    
    y = a * input + a * xnm1 - b * ynm1
    
    #Desloca o vetor de delay
    ynm1 = y
    xnm1 = input
    
    vet_saida.append(y)


with open('Transferencia.pcm', 'wb') as fid:
    numpy.array(vet_saida, dtype=numpy.int16).tofile(fid)
fid.close()


mp.plot(data,'b')
mp.plot(vet_saida,'r')
mp.grid
mp.show()
