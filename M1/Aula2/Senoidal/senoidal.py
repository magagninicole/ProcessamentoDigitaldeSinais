import numpy 
import matplotlib.pyplot as mp


f0 = int(input("Entre com a frequência:"))
fs = int(input("Entre com a frequência de amostragem:"))
tempo = int(input("Tempo de execução:"))

##### SEQUÊNCIA SENOIDAL ######
def seq_senoidal(n, pos_y,f0,fs): 

    pos_y = (16000 *numpy.cos(2*numpy.pi*n*(f0/fs))) #Iguala o eixo y a função dividindo a frequência pelo tamanho do eixo
    
    mp.stem(pos_y) #plota
    mp.show()


min = 0
max = (min + tempo)
n = numpy.arange(min, max, 1)
pos_y = numpy.zeros(fs*2, dtype=float) #cria vetor de 0 para o eixo y

seq_senoidal(n,pos_y,f0,fs)


with open('senoidal.pcm', 'wb') as fid:
    numpy.array(pos_y, dtype=numpy.int16).tofile(fid)
fid.close()
