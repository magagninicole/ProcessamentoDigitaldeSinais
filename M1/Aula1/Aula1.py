import numpy #Importa numpy
import pylab #Importa pylab
from scipy.io.wavfile import write as scipy


ganho = 0.5 #ganho de 0.5
processamento = [] #Cria vetor dinâmico vazio
data = numpy.memmap("audiovoz.pcm", dtype='h', mode='r') #Lê o áudio
#print (data) 


for point in data:
    processamento.insert(len(processamento), point * ganho) #Multiplica o sinal pelo ganho e insere
    #em outro vetor

pylab.title("Processamento digital de sinais", 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 18})
pylab.plot(data, 'b') #Imprime o sinal do som
pylab.plot(processamento, 'r') 
pylab.show()

processamento = numpy.array(processamento)


with open('processamento.pcm', 'wb') as fid:
    numpy.array(processamento, dtype=numpy.int16).tofile(fid)
fid.close()

