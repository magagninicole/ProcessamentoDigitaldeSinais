import numpy as numpy
import matplotlib.pylab as mp



data = numpy.memmap("impulsoun.pcm", dtype='h',mode='r')

y = []
entrada = len(data) - 1

for i in range( len(data) - 1):
    y.append(data[entrada - i])


mp.plot(data, 'r')
mp.plot(y, 'b')
mp.show()
