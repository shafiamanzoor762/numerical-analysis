# Seidal Method
import numpy as np

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

for i in range(14):
    print(i,np.transpose(x0),end='\n\n')
    x1=np.dot(LD_inv,(b-np.dot(U ,x0)))
    # x1=LD_inv@(b-(U @ x0))
    x0=x1