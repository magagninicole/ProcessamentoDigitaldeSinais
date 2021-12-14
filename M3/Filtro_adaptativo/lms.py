import numpy as np
import matplotlib.pyplot as py

with open('ruidobranco.pcm', 'rb') as fid:
    x = np.fromfile(fid, np.int16)
fid.close()

n = len(x)

with open('Coef_MM_8.dat', 'r') as fid:
    coefs= np.fromfile(fid, np.float64)
fid.close()

d = np.zeros(n) #saida desejada
y = np.zeros(n) #saida do filtro

k = 8
w = np.zeros(k)
erro = np.zeros(n)


i = 0
j = 0

convolucao_d = np.zeros(len(coefs))
i = 0
#SAIDA DESEJADA
for i in range(len(x)):
    for j in range(len(coefs)):
        if(i - j)>=0:
            convolucao_d[j] = x[i-j] * float(coefs[j])
    
    d[i] = convolucao_d.sum()

convolucao_y = np.zeros(len(w))

passo = 0.0000000005

for i in range(len(x)):
    for j in range(len(w)):
        if (i - j) >= 0:
            convolucao_y[j] = x[i-j] * float(w[j])
    y[i] = convolucao_y.sum()

    erro[i] = d[i] - y[i]

    for k in range(len(w)):
        if (i - k) >= 0:
            w[k] = w[k] + (passo * erro[i] * x[i-k])


py.subplot(3,1,1)
py.plot(d, 'b')
py.title("Entrada")
py.subplot(3,1,2)
py.plot(y, 'r')
py.title("Saída")
py.subplot(3,1,3)
py.plot(erro, 'r')
py.title("Erro")
py.tight_layout()
py.show()



