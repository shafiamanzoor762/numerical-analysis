import numpy as np
import matplotlib.pyplot as plt

x=np.array([3,5,6,7,-1])
y=np.array([-6,8,5,2,-10])
poi=5
plt.scatter(x,y,color='red')
xplt=np.linspace(x[0],x[-1],100)
yplt=np.array([],float)

for xp in xplt:
    yp=0
    for xi,yi in zip(x,y):
        yp+=yi*np.prod((xp-x[x!=xi])/(xi-x[x!=xi]))
    yplt=np.append(yplt,yp)
plt.plot(xplt,yplt,color='black')

ypoi=0
for xi,yi in zip(x,y):
    ypoi+=yi*np.prod((poi-x[x!=xi])/(xi-x[x!=xi]))
print(ypoi)
plt.title('the value of f(4)='+str(ypoi))

plt.grid()
plt.show()