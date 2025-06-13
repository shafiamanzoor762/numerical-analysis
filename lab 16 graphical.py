from pulp import*
import numpy as np
import matplotlib.pyplot as plt

prob=LpProblem('LPP_lab',LpMaximize)
x=LpVariable('x',0)
y=LpVariable('y',0)
prob+=140*x+235*y
prob+=x+y<=150,'Land_Constraint'
prob+=x+2*y<=240,'Triming_Constraint'
prob+=0.3*x+0.1*y<=30,'Picking_Constraint'
print(prob)
prob.solve()
print('Status of problem',LpStatus[prob.status]) #to check whether the problem is optimal or not

for v in prob.variables():
    print(v.name,'=',v.varValue)
print('Optimal Value of objective function=',value(prob.objective))

x=np.arange(0,240)
plt.plot(x,150-x,label='X+y<=150----(l1)')
plt.plot(x,(240-x)/2,label='x+2y<=240----(l2)')
plt.plot(x,(30-0.3*x)/0.1,label='0.3x+0.1y<=30----(l3)')
plt.fill([0,100,75,60,0],[0,0,75,90,120],color='grey')
plt.legend()
plt.grid()
plt.show()