import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as sg
from scipy.optimize import curve_fit
import numpy as np
from scipy import fftpack

df = pd.read_csv('testdata.csv')
a=df.X*1.659824047+(656-2.83)
a1=a[575:591]
b1=df.Y[575:591]

def gaussian(x, Az, x0, sigma):
    return Az*np.exp(-(x-x0)**2/(2*sigma**2))

mean = sum(a1 * b1)/sum(b1)
sigma1 = np.sqrt(sum(b1 * (a1 - mean)**2)/sum(b1))
a2,b2=curve_fit(gaussian, a1, b1, p0 = [1, mean, sigma1])

mu=656.39
gauss = lambda x_1, sig: np.exp(-( (x_1-mu)/float(sig))**2 )

X2 = np.linspace(656.351335,656.434326, num=500)
#X2 = np.arange(-656,657,50)

#dec=sg.deconvolve(gaussian(a1, *a2),gauss(X2,0.02))
#dec=fftpack.rfft(gaussian(a1, *a2),gauss(X2,0.02))

print(dec)
#print(gaussian(a1, *a2)/38)
plt.subplots_adjust(hspace=0.5)
plt.subplot(311)
plt.plot(a1, b1, color = 'b', linewidth=0.5, label = 'data')
plt.legend()
plt.subplot(312)
plt.plot(a1, gaussian(a1, *a2), color = 'r', linewidth=0.5, label = 'data fit')
plt.legend()
plt.subplot(313)
plt.plot(X2, gauss(X2,0.02), color = 'g', linewidth=0.5, label = 'gauss filter')
plt.legend()
plt.show()
#plt.subplot(414)
#plt.plot(dec, color = 'b', linewidth=0.5, label = 'deconvolution')
#plt.legend()
#plt.show()
