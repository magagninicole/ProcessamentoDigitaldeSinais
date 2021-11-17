import numpy 
import matplotlib.pyplot as plt


w = numpy.arange(-numpy.pi, numpy.pi, numpy.pi/100) #W vai de menos pi até pi sobre 100 

Num = 2*numpy.cos(w) + 1 # Numerador
Den = 1  # - a*np.exp(-1j*w) Denominador
X = Num/Den #x = numerador/denominador

Mod_X = abs(X) #módulo corresponde ao módulo de X
Fase_X = numpy.angle(X) #Fase corresponde ao ângulo

#Plota o módulo/Magnitude
plt.subplot(2,1,1)
plt.plot(w, Mod_X,'r')
plt.title('Magnitude de X[n]')

#Plota a fase
plt.subplot(2,1,2)
plt.plot(w, Fase_X)
plt.title('Fase de X[n]')


plt.tight_layout()
plt.show()