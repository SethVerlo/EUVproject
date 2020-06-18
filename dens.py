import numpy as np
from scipy import constants

print('This script is for H-alpha Gaussian profile broadening.')

while True:
    try:
        lambda_V=float(input('please input the line FWHM broadening (nm):'))
        lambda_I=float(input('please input the instrument resolution (nm):'))
        T=float(input('please input the temperature (eV):'))
        break
    except(IOError, SyntaxError, TypeError, NameError):
        print('Value error, try again:')

####Gaussian FWHM (Doppler and Instrument)
T1=T*11605 #K
f0=constants.c/(656.279*1e-9)
f=f0*np.sqrt((8*constants.k*T1*np.log(2))/(constants.proton_mass*constants.c**2))
f1=f0+f
lambda_D=656.279-(constants.c/f1)*1e9
lambda_G=np.sqrt(lambda_I**2+lambda_D**2)

####Lorentzian FWHM (Stark)
lambda_V1=lambda_V*10 #nm to A
lambda_G1=lambda_G*10
lambda_L=(lambda_V1**2-lambda_G1**2)/lambda_V1
x=lambda_L/(7.4e-19*np.square(6562.79)*5)
ne=pow(x, 1.5)

#print(lambda_I)
#print(lambda_D)
#print(lambda_L)

print('The Gaussian broadening is {:g} cm-3'.format(lambda_G))
if ne < 0:
    print("Error: negative density!")
else:
    print('The electron density is {:g} cm-3'.format(ne))
