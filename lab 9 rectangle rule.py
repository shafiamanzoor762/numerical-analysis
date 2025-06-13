import numpy as np
import matplotlib.pyplot as plt

f=lambda x:x**2*np.exp(2*x)*np.tanh(x)

a=np.pi
b=2*np.pi
n=9

x=np.linspace(a,b,200)
y=f(x)
plt.plot(x,y,color='black')
for i in range(199):
    xp=[x[i],x[i],x[i+1],x[i+1]] #x rectangle plot
    yp=[0,y[i],y[i],0]
    plt.fill(xp,yp,edgecolor='gray',color='gray',alpha=0.2)

xr=np.linspace(a,b,n+1)
yr=f(xr)

for i in range(n):
    xrp=[xr[i],xr[i],xr[i+1],xr[i+1]] #xr rectangle plot
    yrp=[0,yr[i],yr[i],0]
    plt.fill(xrp,yrp,edgecolor='green',color='green',alpha=0.2)

dis_fun='$x^2exp^{2x}tanh(x)$'
plt.title('Integral of '+dis_fun+ ' for n={}'.format(n))
plt.show()


h=(b-a)/n
i=a
res=0
print('f','f(x)',sep='\t')
while i<b-h:
    print(i,f(i),sep='\t')
    res=res+f(i)
    i=i+h
print('Rectangle Rule:',h*res)