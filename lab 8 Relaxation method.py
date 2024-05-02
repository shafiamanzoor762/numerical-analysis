# import numpy as np

# A = np.array([[7,1,-1],[1,-3,-1],[3,-7,-15]])
# b = np.array([[10],[7],[30]])
# x0= np.array([[0],[1],[0]])
# L = np.tril(A,-1)
# U = np.triu(A,1)
# D=np.diagflat(np.diag(A,0))
# w=0.2
# DwL_inv=np.linalg.inv((D/w)+L)
# print(DwL_inv)
# for i in range(100):
#     print(i,np.transpose(x0),end='\n\n')
#     x1=np.dot(DwL_inv,(b+np.dot((D/w-U-D),x0)))
#     x0=x1

# Relaxation Method
import numpy as np

A = np.array([[7,1,-1],[1,-3,-1],[3,-7,-15]])
b = np.array([[10],[7],[30]])
x0= np.array([[0],[1],[0]])
L = np.tril(A,-1)
U = np.triu(A,1)
# D = A - L - U

# alternative method to find D^-1
# diag => to find diagnonal ele and then diagflat => to spread out in flat
D=np.diagflat(np.diag(A,0))
w=0.2
LD_inv=np.linalg.inv(L+D)
print(LD_inv)

for i in range(100):
    print(i,np.transpose(x0),end='\n\n')
    # x1 = np.dot(LwD_inv,b+np.dot(D/w-U-D,x0))
    x1=(1-w)*x0+w*np.dot(LD_inv,(b-np.dot(U ,x0)))
    x0=x1