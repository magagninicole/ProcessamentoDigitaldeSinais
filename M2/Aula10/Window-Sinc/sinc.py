import numpy 
import matplotlib.pyplot as plt
from scipy import signal as sf

#data = numpy.memmap("degrauun.pcm", dtype='h', mode='r')
M = int(input("M:"))
Fs = 8000

passo = (numpy.pi/1000)
Fc = float(input("Fc:"))
w = numpy.arange(0, numpy.pi, passo)
saida = numpy.zeros(M)
x = numpy.arange(-M/2, M/2, 1)


for i in range(M):
    if(i == M/2):
        saida[i] = 1
    if(i < M/2):
        saida[i] = (numpy.sin(2 * numpy.pi * Fc * (-i+M/2))) / ((-i+M/2) * numpy.pi)
    elif(i > M/2):
        saida[i] = (numpy.sin(2 * numpy.pi * Fc * (i-M/2))) / ((i-M/2) * numpy.pi)

plt.plot(x,saida,'r')
plt.grid()
plt.show()


[w, saida] = sf.freqz(saida, 1,Fs)
plt.plot(w*Fs/(2*numpy.pi), 20*numpy.log10(abs(saida)))
plt.title('Magnitude da resposta em frequencia')
plt.grid()
plt.tight_layout()
plt.show()
