import pandas as pd
import matplotlib.pyplot as plt
print('This plot script is used for SP2500i&PIMAX4 spectrometer.')
print('please confirm you chose the correct image region(X-axis 1024p)!')

while True:
    try:
        file_name=raw_input("please input the file name (.csv):")
        df=pd.read_csv('./{}.csv'.format(file_name))
        break
    except (IOError, SyntaxError):
        print("File '{}.csv' does not exist!".format(file_name))

y1=df.Y[0:539]
y2=df.Y[601:1023]
ay1=y1.mean()
ay2=y2.mean()
ay=(ay1+ay2)/2
y = df.Y-ay	

ya=y.head(550)
ya[abs(ya)>9]=0
ya
yb=y.tail(400)
yb[abs(yb)>9]=0
yb

while True:
    try:
        gr=int(input('please input the gratings (150,1200,2400):'))
        cwavelength=float(input('please input the center wavelength (nm):'))
	if gr == 150:
            a=df.X*51.02346041+(cwavelength-86.995)
	elif gr == 1200:
	    a=df.X*5.692082111+(cwavelength-9.705)
	elif gr == 2400:
	    a=df.X*1.659824047+(cwavelength-2.83)
        else:
	    print('grating does not exist,please input again:')
	    continue
	break
    except (TypeError,NameError):
        print('input error! try again:')

plt.plot(a, y, color='b', linewidth=0.5, label='c={}nm'.format(cwavelength))
#plt.savefig('./{}.png'.format(file_name),dpi=300)
plt.show()
