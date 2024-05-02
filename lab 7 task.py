# Jacobi
# Seidal Method
import numpy as np

import matplotlib.pyplot as plt

A = np.array([[10,1,-1,-1,1],[3,17,-1,-1,-1],[1,-1,20,-4,1],[3,-1,3,25,-1],[4,-1,1,-4,18]])
b = np.array([[10],[20],[18],[22],[19]])
x0=np.array([[1],[1],[1],[0],[0]])
L = np.tril(A,-1)
U = np.triu(A,1)
# D = A - L - U

# alternative method to find D^-1
# diag => to find diagnonal ele and then diagflat => to spread out in flat
D=np.diagflat(np.diag(A,0))
LD_inv=np.linalg.inv(L+D)
D_inv=np.linalg.inv(D)
R=A-D

i=0
print(i,np.transpose(x0),end='\n\n')

prev=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]

z1=[]
z2=[]
z3=[]
z4=[]
z5=[]
while(i!=15):
    i=i+1
    x1=D_inv@(b-(R @ x0))
    prev=x1
    x1=LD_inv@(b-(U @ x0))       
    if(i==15):
        break    
    x0=x1
    y1.append(prev[0,0])
    z1.append(x1[0,0])
    y2.append(prev[1,0])
    z2.append(x0[1,0])
    y3.append(prev[2,0])
    z3.append(x0[2,0])
    y4.append(prev[3,0])
    z4.append(x0[3,0])
    y5.append(prev[4,0])
    z5.append(x0[4,0])
    print(i,np.transpose(x0),end='\n\n')
    

plt.grid()
plt.plot(range(len(y1)), y1,label='x1')
plt.plot(range(len(y2)), y2, color='red', linewidth=1, linestyle='dashdot',label='x2')
plt.plot(range(len(y3)), y3, color='blue', linewidth=2, linestyle='--',label='x3')
plt.plot(range(len(y4)), y4,color='black', linewidth=2, linestyle='dotted',label='x4')
plt.plot(range(len(y5)), y5,label='x5')

plt.plot(range(len(z1)), z1,label='x1')
plt.plot(range(len(z2)), z2, color='red', linewidth=1, linestyle='dashdot',label='x2')
plt.plot(range(len(z3)), z3, color='blue', linewidth=2, linestyle='--',label='x3')
plt.plot(range(len(z4)), z4,color='black', linewidth=2, linestyle='dotted',label='x4')
plt.plot(range(len(z5)), z5,label='x5')
plt.legend()
plt.show()