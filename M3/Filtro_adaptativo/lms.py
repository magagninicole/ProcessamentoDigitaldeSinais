import numpy 
import matplotlib.pyplot as py

with open('ruidobranco.pcm', 'rb') as fid:
    x = numpy.fromfile(fid, numpy.int16)
fid.close()

n = len(x)

with open('Coef_PB.dat', 'r') as fid:
    coeficientes= numpy.fromfile(fid, numpy.float64)
fid.close()

d = numpy.zeros(n) 
y = numpy.zeros(n) 

k = 8
w = numpy.zeros(k)
e = numpy.zeros(n)


i = 0
j = 0

saidaD = numpy.zeros(len(coeficientes))
i = 0

for i in range(len(x)):
    sum=0
    for j in range(len(coeficientes)):
        if(i - j)>=0:
            sum += x[i-j] * float(coeficientes[j])
    
    d[i] = sum

saidaY = numpy.zeros(len(w))

passo = 0.0000000005

for i in range(len(x)):
    sum2 =0
    for j in range(len(w)):
        if (i - j) >= 0:
           sum2 += x[i-j] * float(w[j])
    y[i] = sum2

    e[i] = d[i] - y[i]

    for k in range(len(w)):
        if (i - k) >= 0:
            w[k] = w[k] + (passo * e[i] * x[i-k])


py.subplot(3,1,1)
py.plot(d, 'b')
py.title("Entrada")
py.subplot(3,1,2)
py.plot(y, 'g')
py.title("Saída")
py.subplot(3,1,3)
py.plot(e, 'r')
py.title("Erro")
py.tight_layout()
py.show()



