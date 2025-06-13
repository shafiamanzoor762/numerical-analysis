import numpy as np
import matplotlib.pyplot as plt


f=lambda a,b,x:a*x+b*np.log10(x)

x=np.array([1,2,3,4,5,10])
y=np.array([2,5,3,6.5,9,11])

plt.scatter(x,y,color='red',s=50)
n=len(x)

X=np.log10(x)/x
Y=y/x

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
    yp=f(sol[1],sol[0],i)
    yplt=np.append(yplt,yp)

print(sol)
plt.plot(xplt,yplt,color='black',linewidth=2)
plt.show()