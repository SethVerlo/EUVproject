import ChiantiPy.core as ch
import ChiantiPy.tools.filters as chfilters
import numpy as np
import matplotlib.pyplot as plt

temp = 15087
dens = 3e13
em = 1e26
dwvl = 0.01
nwvl = (6500.- 4000.)/dwvl
wvl = 4500. + dwvl*np.arange(nwvl+1)

bnch2=ch.bunch(temp, dens, wvlRange=[wvl.min(),wvl.max()], elementList=['H'], abundance='unity', keepIons=1, em=em)
bnch2.convolve(wvl,filter=(chfilters.gaussian,0.2))

plt.plot(wvl, bnch2.Spectrum['intensity'])#[4],label='Total')
plt.xlabel(r'Wavelength ($\AA$)')
plt.ylabel(r'erg cm$^{-2}$ s$^{-1}$ sr$^{-1} \AA^{-1}$')
plt.title('Spectrum')#= %10.2e for t[6]'%(t[4]))
#plt.savefig('Mult_ions.png',dpi=300)
plt.show()
