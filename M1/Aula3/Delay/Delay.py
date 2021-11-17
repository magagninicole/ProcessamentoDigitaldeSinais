import numpy 
import pylab #Importa pylab

data = numpy.memmap("impulsoun.pcm", dtype='h', mode='r')

Fs = int(input("Frequência de amostragem:"))
t1 = float(input("T1:"))
t2 = float(input("T2:"))
a0 = float(input("a0:"))
a1 = float(input("a1:"))
a2 = float(input("a2:"))
n1 = int(t1 * Fs)
n2 = int(t2 * Fs)

delay = numpy.zeros(n2)
saida = numpy.zeros(len(data))

for pointer in range(len(data)):
  delay[0] = data[pointer]
  y = a0 * delay[0] + a1 * delay[n1-1] + a2 * delay[n2-1]
  for i in range(n2):
    delay[n2-i-1] = delay[n2-i-2]
    saida[pointer] = y
  
pylab.plot(data,'b')
pylab.plot(saida,'r')
pylab.show()


with open('delay.pcm', 'wb') as fid:
    numpy.array(saida, dtype=numpy.int16).tofile(fid)
fid.close()

