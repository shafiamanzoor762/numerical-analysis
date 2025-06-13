import numpy as np
import matplotlib.pyplot as plt

f=lambda a,b,x:a/(1-b*x)

x=np.array([2,5,10,12,17,20])
y=np.array([-4,-1.3,-0.6,-0.3,-0.25,-0.3])

plt.scatter(x,y,color='red',s=50)
n=len(x)

X=x*y

sX = np.sum(X)

sy = np.sum(y)
sX2 = np.sum(X**2)
sXy=np.dot(X,y)

A=np.matrix(str(sX)+' '+str(n)+';'+str(sX2)+' '+str(sX))
b= np.matrix(str(sy)+';'+str(sXy))
sol=np.linalg.solve(A,b)

xplt=np.linspace(x[0],x[-1],200)
yplt=np.array([],float)

for i in range(len(xplt)):
    yp=f(sol[1],sol[0],xplt[i])
    yplt=np.append(yplt,yp)

print(sol)
plt.plot(xplt,yplt,color='black',linewidth=2)
plt.show()