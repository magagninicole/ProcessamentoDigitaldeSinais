import numpy 
import pylab #Importa pylab

data = numpy.memmap("impulsoun.pcm", dtype='h', mode='r')
Fs = float(input("Fs:"))
D = float(input("D:"))
a0 = float(input("A0:"))
a1 = float(input("A1:"))
n = int(Fs * D)
saida = numpy.zeros(len(data))

for pointer in range(len(data)):
    saida[pointer] = (a0 * data[pointer] + a1 * saida[pointer - n])


pylab.plot(data,'b')
pylab.plot(saida,'r')
pylab.show()


with open('eco.pcm', 'wb') as fid:
    numpy.array(saida, dtype=numpy.int16).tofile(fid)
fid.close()
