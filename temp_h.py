import numpy as np
from scipy import constants

print('This script is for 1200g/mm H-alpha & beta! Please confirm before calculation!')
print('The transition probablity and statistical weight is refer to CRC handbook')
while True:
    try:
        ha_origin=int(input('Please input the counts of H-alpha line:'))
        hb_origin=int(input('Please input the counts of H-beta line:'))
	break
    except(IOError, SyntaxError, TypeError, NameError):
        print('Error:the count must be integer,try again:')

ha = ha_origin/0.12/0.75/0.78/0.78
hb = hb_origin/0.15/0.80/0.76/0.76

A1=4.4101e-1
A2=8.4193e-2

g1=18
g2=32

E1=12.0875*1.6e-19 #J
E2=12.7485*1.6e-19

lamda_a=656.3
lamda_b=486.1

T=(E2-E1)/(constants.k*np.log((ha*A2*g2*lamda_b)/(hb*A1*g1*lamda_a)))
T1=T/11605
T_eV=round(T1,2)

if T_eV < 0:
    print('Error: Negitave temeperature! Please check the original data.')
else:
    print('The tempurature is {} eV'.format(T_eV))
