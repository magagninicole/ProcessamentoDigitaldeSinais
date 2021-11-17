import numpy
import scipy
from scipy import signal as sf
import matplotlib.pyplot as mp

passo = (numpy.pi/1000)
L = 8
Fs = 8000
w = numpy.arange(0, numpy.pi, passo)
a =numpy.complex64(1j)



#num = [(0.1),(0.2), (0.4), (0.2), (0.1)]
#den = 1

num = [0,6280,6280]
den = [0,22280,-9720]

[w, H] = sf.freqz(num, den,Fs)
mp.show()
#Freq = Fs * w / (2*numpy.pi)

mp.plot(w*Fs/(2*numpy.pi), 20*numpy.log10(abs(H)))
mp.title('Magnitude da resposta em frequencia')
mp.grid

mp.tight_layout()
mp.show()

