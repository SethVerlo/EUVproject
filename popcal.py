from scipy import constants

cts=float(input("please input the H-alpha counts:"))
cts1=float(input("please input the H-beta counts:"))

sw=15e-4 #spectrometer slit width in cm
p=13e-4 #CCD pixel size in cm
ro=0.12 #radius of CCD observable region in cm
re=100e-4 #radius of EUV radiation volume in cm
rl=2.415 #radius of the first lens in cm
R=30 #distance of the first lens to TCC in cm

A_slt=94*p*sw # region size chosen on CCD in cm-2
A_obs=ro**2*constants.pi # observation emission area on CCD in cm-2, R=0.12 cm 
V_euv=(4*constants.pi*re**3)/3  #4.189e-6 # EUV volume in cm-3, R=0.01 cm
omega=(rl**2*constants.pi)/(R**2) # solid angle of the first lens, R=2.415 cm with d=30 cm

obs_n1=4*constants.pi*(((cts/A_slt)*A_obs)/900)/omega #H-alpha total counts
obs_n2=4*constants.pi*(((cts1/A_slt)*A_obs)/900)/omega  #H-beta total counts

n1=obs_n1/0.44123
n2=obs_n2/8.4193e-2

dens=(n1+n2)/V_euv 

print("the total counts of H-alpha is %.3e"%(obs_n1))
print("the total counts of H-beta is %.3e"%(obs_n2))
print("the population of n=3 is %.3e"%(n1))
print("the population of n=4 is %.3e"%(n2))
print("the H* density is %.3e cm-3"%(dens))
