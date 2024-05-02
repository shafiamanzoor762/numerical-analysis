# Seidal Method
import numpy as np

import matplotlib.pyplot as plt

A = np.array([[10,2,3,1],[2,20,3,7],[3,5,30,7],[-5,-6,-2,-30]])
b = np.array([[12],[13],[14],[17]])
x0=np.array([[0],[0],[0],[0]])

L = np.tril(A,-1)
U = np.triu(A,1)
# D = A - L - U

# alternative method to find D^-1
# diag => to find diagnonal ele and then diagflat => to spread out in flat
D=np.diagflat(np.diag(A,0))
LD_inv=np.linalg.inv(L+D)

y1=[]
y2=[]
y3=[]
y4=[]
for i in range(14):
    y1.append(x0[0,0])
    y2.append(x0[1,0])
    y3.append(x0[2,0])
    y4.append(x0[3,0])
    print(i,np.transpose(x0),end='\n\n')
    # x1=np.dot(LD_inv,(b-np.dot(U ,x0)))
    x1=LD_inv@(b-(U @ x0))
    x0=x1

plt.grid()
plt.plot(range(len(y1)), y1,label='x1')
plt.plot(range(len(y2)), y2, color='red', linewidth=1, linestyle='dashdot',label='x2')
plt.plot(range(len(y3)), y3, color='blue', linewidth=2, linestyle='--',label='x3')
plt.plot(range(len(y4)), y4,color='black', linewidth=2, linestyle='dotted',label='x4')
plt.legend()
plt.show()
