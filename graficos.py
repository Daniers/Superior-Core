#primera parte
#import matplotlib.pyplot as plt
#x=range(6)
#plt.plot(x,[xi**2 for xi in x])
#plt.show()
 
#parte 2
#import matplotlib
#from matplotlib import pyplot
#x=range(6)
#y=[]
#for xi in x:
    #xi=xi**2
    #y.append(xi)
#print y
#pyplot.plot(x,y)
#pyplot.show()

#parte3
#import matplotlib
#import numpy
#from matplotlib import pylab
#x=range(6)
#y=[]
#for xi in x:
 #   xii=xi**2
 #   y.append(xii)
#print y
#pylab.plots(x,y)
#pylab.show()

#parte4 falta por hacer

#parte5

#import matplotlib.pyplot as plt
#plt.plot([1,3,2,4])
#plt.xlabel('This is the x axis')
#plt.ylabel('This is the y axis')
#plt.title('Graphics 1')
#plt.grid(True)
#plt.show()


#parte 6:leyendas o descripcion en las graficas

#import matplotlib.pyplot as plt
#import numpy
#x=numpy.arange(1,5,1)
#plt.plot(x,x*1.5,label='Normal')
#plt.plot(x,x*3.0,label='Fast')
#plt.plot(x,x/3.0,label='Slow')
#plt.legend()
#plt.xlabel('This is the x axis')
#plt.ylabel('This is the y axis')
#plt.title('Graphics 1')
#plt.grid(True)
#plt.show()

#parte 6.5 :ubicacion y uso de legendas; nofunciono loc

#import matplotlib.pyplot as plt
#import numpy
#x=numpy.arange(1,5,1)
#plt.plot(x,x*1.5)
#plt.plot(x,x*3.0)
#plt.plot(x,x/3.0)
#plt.legend(['Normal','Fast','Slow'])
#plt.legend(loc=1)
#plt.xlabel('This is the x axis')
#plt.ylabel('This is the y axis')
#plt.title('Graphics 1')
#plt.grid(True)
#plt.savefig('plot123png')
#guardar imagen
#plt.show()
#plot legends posiciones 0=best 1=derecho superior 2=izquierda superiror 4=izquierda inferior 5=derecha
#6=centro izquierda 7=centro derecha 8=centro inferior 9=centro superior 10=centro


#parte 7:colores
#b=blue,c=cyan,g=green,k=black,m=magenta,r=red,w=white,y=yellow
#import matplotlib.pyplot as plt
#import numpy as np
#y=np.arange(1,3)
#plt.plot(y,'y')
#plt.plot(y+1,'m')
#plt.plot(y+2,'c')
#plt.show()

#parte 8 stilos de lineas sin terminar
#import matplotlib.pyplot as plt
#import numpy as np
#y=np.arange(1,3)
#plt.plot(y,'--',y+1,'-',y+2,':')
#plt.show()

#parte 9 colores y abreviaciones al marcar.pyplot as plt no me sirvio
#import matplotlib.pyplot as plt
#import numpy as np
#y=np.arange(1,3,0,3)
#plt.plot(y,color='blue',linestyle='dashdot',linewidth=4,marker='o',markerfacecolor='red',markeredgecolor='black',markeredgewidth=3,markersize=12);
#plt.show()

#parte 10 histogramas
import matplotlib.pyplot as plt
import numpy as np
y=np.random.rand(1000)
plt.hist(y,25);
plt.show()

#graficas con subplots
import matplotlib as mpl 
mpl.rcParams['font size']=10
import matplotlib.pyplot as plt 
import numpy as np
x=np.aramge(0.,20,0.01)
fig=plt.figure()
ax1=fig.add_subplot(311)
y1=np.exp(x/6.)
ax1.plot(x,y1)
ax1.grid(True)
ax1.set_yscale('log')
ax1.set_ylabel('logY')
ax2=fig.add_subplot(312)
y2=np.cos(np.pi*x)
ax2.semilogx(x,y2);
ax2.set_xlim([0,20]);
ax2.grid(True)
ax2.set_ylabel('log X')
ax3=fig.add_subplot(313)
y3=np.exp(x/4.)
ax3.loglog(x,y3,basex=3);
ax3.grid(True)
ax3.set_ylabel('log X and Y');
plt.show()



