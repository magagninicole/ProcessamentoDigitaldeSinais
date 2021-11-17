import numpy 
import pylab #Importa pylab


TAM = 25
data = numpy.memmap("impulsoun.pcm", dtype='h', mode='r')

def media_movel(data, w):
  return numpy.convolve(data, numpy.ones(w), 'valid') / w



w = int(input("Digite o número de elementos:"))

pylab.plot(data,'b')
pylab.plot(media_movel(data,w),'r')  #plota as funções dependentes de eixo xx e y
pylab.show()

with open('mediamovel.pcm', 'wb') as fid:
    numpy.array(data, dtype=numpy.int16).tofile(fid)
fid.close()
