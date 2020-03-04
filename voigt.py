import numpy as np
from astropy.modeling.models import Voigt1D
import matplotlib.pyplot as plt
import pandas as pd

plt.figure()
df=pd.read_csv('7.csv')
x=df.X*5.692082111+(656-9.705)
y=df.Y
v1 = Voigt1D(x_0=657.2, amplitude_L=100, fwhm_L=0.02, fwhm_G=0.02)
plt.plot(x, v1(x),lw=0.7)
#plt.plot(x,y-12)
plt.show()
