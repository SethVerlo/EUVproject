import numpy as np
from scipy import constants

print('This script is for 2400g/mm H-alpha! Please confirm before calculation!')

while True:
    try:
        lamda=float(input('please input the line FWHM broadening (nm):'))
        T=float(input('please input the temperature (eV):'))
	break
    except(IOError, SyntaxError, TypeError, NameError):
        print('Value error, try again:')

T1=T*11605 #K
f0=constants.c/(656.3*1e-9)
f=f0*np.sqrt((8*constants.k*T1*np.log(2))/(constants.proton_mass*constants.c**2))
f1=f0+f
lamda_T=656.283-(constants.c/f1)*1e9
lamda_n=(lamda-lamda_T)*10
x=lamda_n/(7.4e-19*np.square(6562.83)*5)
ne=pow(x, 1.5)

if ne < 0:
    print("Error: negative density! Please check the original data.")
else:
    print('The electron density is {:g} cm-3'.format(ne))
