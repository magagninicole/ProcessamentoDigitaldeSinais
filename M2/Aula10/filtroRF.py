import numpy 
import matplotlib.pyplot as plt
from scipy import signal as sf
import math


def geraRF():
    X = numpy.zeros(4999)
    Y = numpy.zeros(4999)

    X2 = numpy.zeros(4999)
    Y2 = numpy.zeros(4999)

    Fs = int(input("Fs: "))
    fcb = int(input("fcb: "))
    fcb = float(fcb/Fs)
    Bw = int(input("Bw: "))
    M = int(4/(Bw/Fs))
    H1 = numpy.zeros(M)
  

   
    fca = int(input("Fca: "))
    fca = float(fca/Fs)
    H2 = numpy.zeros(M)

    for i in range(len(H1)):
        if(i - M/2) == 0:
            H1[i] = 2 * numpy.pi * fcb
        if(i - M/2) != 0:
            H1[i] = numpy.sin(2 * numpy.pi * fcb * (i - M/2)) / (i - M/2)
        H1[i] = H1[i] * (0.54 - 0.46 * numpy.cos(2 * numpy.pi * i / M))

    SUMb = 0

    for i in range(len(H1)): 
        SUMb += H1[i]

    for i in range(len(H1)):
        H1[i] = H1[i]/SUMb

    for j in range(100,4999):
        Y2[j] = 0
        for i in range(len(H1)):
            Y2[j] = Y2[j] + X2[j - i] * H1[i]



    for i in range(len(H2)):
        if(i - M/2) == 0:
            H2[i] = 2 * numpy.pi * fca
        if(i - M/2) != 0:
            H2[i] = numpy.sin(2 * numpy.pi * fca * (i - M/2)) / (i - M/2)
        H2[i] = H2[i] * (0.54 - 0.46 * numpy.cos(2 * numpy.pi * i / M))

    SUM = 0

    for i in range(len(H2)): 
        SUM += H2[i]

    for i in range(len(H2)):
        H2[i] = H2[i]/SUM

    for j in range(100,4999):
        Y[j] = 0
        for i in range(len(H2)):
            Y[j] = Y[j] + X[j - i] * H2[i]

    for k in range(M):
        H2[k] = H2[k] * -1
        if( k == M/2):
            H2[k] += 1


    for l in range(len(H2)):
        reject =  H2[l] + H1[l]
        H2[l] = reject

    return(H2)


saida = geraRF()


Hsaida = saida

plt.title("H")
plt.plot(Hsaida, 'r')
plt.grid()

plt.tight_layout()
plt.show()


with open("Coef_RF.dat", "w") as f:
    for s in saida:
        f.write(str(s) +",\n")


[w, Hsaida] = sf.freqz(Hsaida, 1, 8000)
plt.plot(w*8000/(2*numpy.pi), 20*numpy.log10(abs(Hsaida)))
plt.show()