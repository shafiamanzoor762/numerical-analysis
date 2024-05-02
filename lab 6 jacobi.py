# Jacobi
import numpy as np

data_str = "[4,-1,-1],[1,-7,2],[3,-4,-10]"
# Split the string into individual row strings
row_strings = data_str.split('],[')
# Remove '[' and ']' characters from the first and last row strings
row_strings[0] = row_strings[0].replace('[', '')
row_strings[-1] = row_strings[-1].replace(']', '')
# Convert string elements to integers and split each row string into individual elements
data_list = [list(map(int, row.split(','))) for row in row_strings]
# Convert list to NumPy array
A = np.array(data_list)
print(A)

# Question 1
# A = np.array([[10,2,3,1],[2,20,3,7],[3,5,30,7],[-5,-6,-2,-30]])
# b = np.array([[12],[13],[14],[17]])
# x0=np.array([[0],[0],[0],[0]])

# Question 2

# A = np.array([[4,-1,-1],[1,-7,2],[3,-4,-10]])
b = np.array([[10],[20],[30]])
x0=np.array([[0],[0],[0]])

# L = np.tril(A,-1)
# U = np.triu(A,1)
# D = A - L - U
# R = L + U

# alternative method to find D^-1
# diag => to find diagnonal ele and then diagflat => to spread out in flat
D=np.diagflat(np.diag(A,0))
D_inv=np.linalg.inv(D)
R=A-D


for i in range(50):
    print(i,np.transpose(x0),end='\n\n')
    x1=np.dot(D_inv,(b-np.dot(R ,x0)))
    # x1=D_inv@(b-(R @ x0))
    x0=x1
