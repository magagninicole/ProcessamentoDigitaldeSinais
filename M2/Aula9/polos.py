import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

def zplane(b, a):

    # get a figure/plot
    ax = plt.subplot(111)

    # create the unit circle
    uc = patches.Circle((0, 0), radius=1, fill=False, color='black', ls='dashed')
    ax.add_patch(uc)

    # Get the poles and zeros
    p = np.roots(a)
    z = np.roots(b)

    # Plot the zeros and set marker properties
    t1 = plt.plot(z.real, z.imag, 'go', ms=10)
    plt.setp(t1, markersize=10.0, markeredgewidth=1.0, markeredgecolor='k', markerfacecolor='g')

    # Plot the poles and set marker properties
    t2 = plt.plot(p.real, p.imag, 'rx', ms=10)
    plt.setp(t2, markersize=12.0, markeredgewidth=3.0, markeredgecolor='r', markerfacecolor='r')

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # set the ticks
    r = 1.5
    plt.axis('scaled')
    plt.axis([-r, r, -r, r])
    ticks = [-1, -.5, .5, 1]
    plt.xticks(ticks)
    plt.yticks(ticks)
    plt.title('Pole/Zero Plot Example')
    plt.show()
#      z³    z²   z    c
Num = [16000, -16000]
Den = [0, 22280, -9720]

zplane(Num,Den)