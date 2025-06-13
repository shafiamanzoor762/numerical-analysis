import numpy as np
import matplotlib.pyplot as plt

f=lambda a,b,x:a*x+b*(10**x)

x=np.array([0.1,0.4,1,1.2,2.0,3.3])
y=np.array([280,115,240,240,1050,12000])

# x=np.array([1,1.5,2.2,2.8,3,3.2,3.5])
# y=np.array([65,150,790,3100,4990,8000,15900])

plt.scatter(x,y,color='red',s=50)
n=len(x)

X=10**x/x
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

for i in range(len(xplt)):
    yp=f(sol[1],sol[0],xplt[i])
    yplt=np.append(yplt,yp)

print(sol)
plt.plot(xplt,yplt,color='black',linewidth=2)
plt.show()