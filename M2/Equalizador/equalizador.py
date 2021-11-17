import numpy 
import matplotlib.pyplot as plt
from scipy import signal as sf

Bw = int(input("Bw: "))
Fs = int(input("Fs: "))

def gerarPA(Fs,Bw):
    X = numpy.zeros(4999)
    Y = numpy.zeros(4999)

    passo = (numpy.pi/1000)
    fc = int(input("Fc passa-alta: "))
    amplifica = float(input("Amplificação passa-alta: "))
    fc = float(fc/Fs)
    M = int(4/(Bw/Fs))

    H = numpy.zeros(M)
    w = numpy.arange(0, numpy.pi, passo)


    for i in range(len(H)):
        if(i - M/2) == 0:
            H[i] = 1- (2 * numpy.pi * fc)
        if(i - M/2) != 0:
            H[i] = 0-(numpy.sin(2 * numpy.pi * fc * (i - M/2)) / (i - M/2))
        H[i] = H[i] * (0.54 - 0.46 * numpy.cos(2 * numpy.pi * i / M))

    SUM = 0

    for i in range(len(H)): 
        SUM += H[i]

    for i in range(len(H)):
        H[i] = H[i]/SUM



    for j in range(100,4999):
        Y[j] = 0
        for i in range(len(H)):
            Y[j] = Y[j] + X[j - i] * H[i]


    for k in range(M):
        H[k] = H[k] * -1
        if( k == M/2):
            H[k] +=1

    for i in range(len(H)):
        H[i] = H[i] * amplifica

    return(H)

def gerarPB(Fs,Bw):
        
    X = numpy.zeros(4999)
    Y = numpy.zeros(4999)
    fc = int(input("Fc passa-baixa: "))
    amplifica = float(input("Amplificação passa-baixa: "))
    fc = float(fc/Fs)
    M = int(4/(Bw/Fs))

    H = numpy.zeros(M)


    for i in range(len(H)):
        if(i - M/2) == 0:
            H[i] = 2 * numpy.pi * fc
        if(i - M/2) != 0:
            H[i] = numpy.sin(2 * numpy.pi * fc * (i - M/2)) / (i - M/2)
        H[i] = H[i] * (0.54 - 0.46 * numpy.cos(2 * numpy.pi * i / M))

    SUM = 0

    for i in range(len(H)): 
        SUM += H[i]

    for i in range(len(H)):
        H[i] = H[i]/SUM



    for j in range(100,4999):
        Y[j] = 0
        for i in range(len(H)):
            Y[j] = Y[j] + X[j - i] * H[i]

    for i in range(len(H)):
        H[i] = H[i] * amplifica
        
    return(H)
def geraPF(Fs,Bw):
    X = numpy.zeros(4999)
    Y = numpy.zeros(4999)

    X2 = numpy.zeros(4999)
    Y2 = numpy.zeros(4999)
    amplifica = float(input("Amplificação passa-banda: "))
    fcb = int(input("fcb passa-faixa: "))
    fcb = float(fcb/Fs)
    M = int(4/(Bw/Fs))
    H1 = numpy.zeros(M)
   
    fca = int(input("Fca passa-faixa: "))
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
            H2[k] +=1


    for l in range(len(H2)):
        reject =  H2[l] + H1[l]
        H2[l] = reject

    for k in range(len(H2)):
        H2[k] = H2[k] * -1
        if( k == M/2):
             H2[k] += 1
    
    for i in range(len(H2)):
        H2[i] = H2[i] * amplifica
    

    return(H2)

HighPass = gerarPA(Fs,Bw)
LowPass = gerarPB(Fs,Bw)
Passband = geraPF(Fs,Bw)

saida = []

for i in range(len(HighPass)):
    saida.append(float(HighPass[i] + Passband[i] + LowPass[i]))

with open("Equalizador.dat", "w") as f:
    for i in range(len(saida)):
        f.write(str(saida[i]) +",\n")