############### EQU 7 ######################

import numpy as np
import matplotlib.pyplot as plt

f=lambda a,b,x:a*(x**b)

x=np.array([61,26,7,2.6])
y=np.array([350,400,500,600])

plt.scatter(x,y,color='red',s=50)
n=len(x)

X=np.log10(x)
Y=np.log10(y)

sX = np.sum(X)
sy = np.sum(Y)
sX2 = np.sum(X**2)
sXy=np.dot(X,Y)

A=np.matrix(str(sX)+' '+str(n)+';'+str(sX2)+' '+str(sX))
b= np.matrix(str(sy)+';'+str(sXy))
sol=np.linalg.solve(A,b)

xplt=np.linspace(x[0],x[-1],200)
yplt=np.array([],float)

for i in xplt:
    yp=f(10**(sol[1,0]),sol[0],i)
    yplt=np.append(yplt,yp)

print(sol[0,0],10**(sol[1,0]))
plt.plot(xplt,yplt,color='black',linewidth=2)
plt.show()

