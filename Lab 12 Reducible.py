import numpy as np
import matplotlib.pyplot as plt

f=lambda a,b,x:(a/x)+b

x=np.array([-5,-4,-3,0.02,1,2])
y=np.array([5,5,4.2,140,10,5])
n=len(x)

x=np.linspace(-3,3,100)
y=f(3.2,5.6,x)

plt.plot(x,y,color='black',linewidth=2)

sx=sxy=sx2=sy=0
X=1/x
for i in range(n):
    sx+=X[i]
    sx2+=X[i]**2
    sxy+=X[i]*y[i]
    sy+=y[i]

A=np.matrix(str(sx)+' '+str(n)+';'+str(sx2)+' '+str(sx))
b= np.matrix(str(sy)+';'+str(sxy))
sol=np.linalg.solve(A,b)

print(sx,sx2,sxy)
xplt=np.linspace(x[0],x[-1],100)
yplt=np.array([],float)

for i in range(len(xplt)):
    yp=f(sol[1],sol[0],xplt[i])
    yplt=np.append(yplt,yp)

print(sol)
plt.plot(xplt,yplt,color='red',linewidth=2)
plt.show()