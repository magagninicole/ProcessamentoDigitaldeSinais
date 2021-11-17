import numpy 
import matplotlib.pyplot as mp




A= float(input("A:"))
tam = int(input("Entre com o tamanho:"))
yn =[]


###### SEQUÊNCIA EXPONENCIAL #####
def seq_exponencial(n,A):
    for pointer in range(len(n)):
        yn.append(A**(n[pointer]))
    return yn
    




n = numpy.arange(0, tam, 1)
seq_exponencial(n,A)

mp.stem(n,yn)  #plota as funções dependentes de eixo xx e y
mp.show()

with open('senoidal.pcm', 'wb') as fid:
    numpy.array(yn, dtype=numpy.int16).tofile(fid)
fid.close()
