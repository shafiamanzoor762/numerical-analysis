import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([5,7,9,13,19])
n=len(x)

plt.scatter(x,y,color='red')

sx=sx2=sxy=sy=0

for i in range(n):
    sx+=x[i]
    sx2+=x[i]**2
    sxy+=x[i]*y[i]
    sy+=y[i]

A=np.matrix(str(sx2)+' '+str(sx)+';'+str(sx)+' '+str(n))
b= np.matrix(str(sxy)+';'+str(sy))
sol=np.linalg.solve(A,b)
p1_y=sol[0]*x[0]+sol[1]
p2_y=sol[0]*x[-1]+sol[1]

print(sol)
plt.plot([x[0],x[-1]],[float(p1_y),float(p2_y)],color='black')
plt.show()