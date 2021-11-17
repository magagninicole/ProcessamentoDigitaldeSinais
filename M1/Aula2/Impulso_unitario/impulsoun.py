import numpy 
import matplotlib.pyplot as mp

#### IMPULSO UNITÁRIO #######
def impulso_un(pos_x,pos_y):
    y = 0 
    for pointer in pos_x: #se n =0, y = 1 e se n =/= 0 y = 0
        if pointer == 0:
            pos_y[y] = 10000
        y = y+1

tam = int(input("Entre com o tamanho:"))

pos_x = numpy.linspace(-tam,(tam-1), num=2*tam, dtype = float) #cria vetor para o eixo x
pos_y = numpy.zeros(tam*2, dtype=float) #cria vetor de 0 para o eixo y

impulso_un(pos_x,pos_y)
mp.stem(pos_x,pos_y)  #plota as funções dependentes de eixo xx e y
mp.show()

with open('impulsoun.pcm', 'wb') as fid:
    numpy.array(pos_y, dtype=numpy.int16).tofile(fid)
fid.close()
