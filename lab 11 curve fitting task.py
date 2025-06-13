import numpy as np
import matplotlib.pyplot as plt

x=np.array([3,4,5,6,7])
y=np.array([10,15,23,38,48])
n=len(x)

plt.scatter(x,y,color='red')

sx=sx2=sxy=sy=sx2y=sx3=sx4=0

for i in range(n):
    sx+=x[i]
    sx2+=x[i]**2
    sxy+=x[i]*y[i]
    sy+=y[i]
    sx2y+=x[i]**2*y[i]
    sx3+=x[i]**3
    sx4+=x[i]**4

A=np.matrix(str(sx4)+' '+str(sx3)+' '+str(sx2)+';'+str(sx3)+' '+str(sx2)+' '+str(sx)+';'+str(sx2)+' '+str(sx)+' '+str(n))
b= np.matrix(str(sx2y)+';'+str(sxy)+';'+str(sy))
sol=np.linalg.solve(A,b)
print(sol)

xplt=np.linspace(x[0],x[-1],100)
yplt=np.array([],float)

for i in range(len(xplt)):
    yp=float(sol[0]*xplt[i]**2+sol[1]*xplt[i]+sol[2])
    yplt=np.append(yplt,yp)
    # Ax^2+Bx+C
plt.plot(xplt,yplt,color='black')
plt.show()