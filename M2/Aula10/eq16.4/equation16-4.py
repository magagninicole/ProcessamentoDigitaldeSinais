import numpy 
import matplotlib.pyplot as plt
from scipy import signal as sf


#data = numpy.memmap("degrauun.pcm", dtype='h', mode='r')

M = int(input("M:"))
K = int(input("K:"))
fc = float(input("Fc:"))
a = M/2
h = numpy.zeros(M)
Fs = 8000
passo = (numpy.pi/1000)
w = numpy.arange(0, numpy.pi, passo)




for i in range(len(h)):
     if(i==a): 
          h[i] = (2*numpy.pi*fc)*K
     else: 
          h[i] = K * (numpy.sin(2*numpy.pi*fc*(i-a))/(i-a)) * ((0.42 - 0.5 * numpy.cos((2*numpy.pi)*i/M)) + 0.08*numpy.cos((4*numpy.pi*i)/M))
   




plt.plot(h, 'r')
plt.grid()

plt.tight_layout()
plt.show()
 
[w, h] = sf.freqz(h, 1,Fs)
plt.plot(w*Fs/(2*numpy.pi), 20*numpy.log10(abs(h)))
plt.title('Magnitude da resposta em frequencia')
plt.grid()
plt.tight_layout()
plt.show()