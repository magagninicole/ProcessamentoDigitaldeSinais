import numpy as numpy
import matplotlib.pyplot as mp

data_x = ""
data_h = ""

#x = numpy.memmap(data_x, dtype='h',mode='r')
#h = numpy.memmap(data_h, dtype='h',mode='r')

x = [1,0,0,0,0,0,0,0]
h = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

y = numpy.convolve(x, h)

mp.stem(y)
mp.show()