# Hydrogen plasma diagnostics
The files set will be a backup for an applied phyiscs project I am doing now (2019 April, maybe till 2020 summer). 
As a collaboration reserach with SRJ.

Basically, I am focusing on the atomic physics. 
Based on the OES system I built (PIMAX4 ICCD, SP2500 seris spectrometer and optical systems such as mirrors and lens),
We are going to measure the H atoms in the EUV produced Hydrogen plasma.
# Files
'temp_h.py' is used for calculating the plasma temperature with line ratio method (H-a & H-b).

'dens_h.py' is used for calculatiing the the plasma density, Stark and Doppler effects are considered.

'plt.py' is used for plotting the spectrum.

'spectrum.py' is calculated with ChiantiPy. There are three plasma parameter should be noticed: "n_e", 'T' and 'em'.
'em' is emission measure which is defined as the square of the number density of free electrons integrated over the volume of the plasma.
# Acknowledgement 
Thanks for the help from Dr. Tanaka and Dr. Zhu (ILE, Osaka Univ.) during the experiment.

Special thanks to Prof. Fujioka (ILE, Osaka Univ.).

C.Liu

19/12/12

UPDATING
