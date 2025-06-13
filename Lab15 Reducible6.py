import numpy as np
import matplotlib.pyplot as plt


f=lambda a,b,x:a*np.exp(b*x)

x=np.array([0,2,4,6,8])
y=np.array([150,63,28,12,5.6])

plt.scatter(x,y,color='red',s=50)
n=len(x)

X=x
Y=np.log(y)

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
    yp=f(np.exp(sol[1]),sol[0],i)
    yplt=np.append(yplt,yp)

print(sol[0],np.exp(sol[1]))
plt.plot(xplt,yplt,color='black',linewidth=2)
plt.show()