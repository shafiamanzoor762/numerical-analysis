# from sympy import *
# NEWTON METHOD
x1=1
x2=2
x=(x1+x2)/2
print('n |      Xn')
for i in range(10):
    print(i,'|',x)
    fx=5*x**2-10
    der=10*x
    x=x-(fx/der)
    