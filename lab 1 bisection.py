# BISECTION
import matplotlib.pyplot as plt
'''numpy matplotlib pulp'''
#function
def f(x):
    return 5*x**2-10
# f=lambda x:5*x**2-10

def mean(x0,x1):
    return (x0+x1)/2

#Root interval
y=[]

def main():
    x0,x1=1,2
    diff=0
    
    print("i \t x(n-1) \t  x(n) \t  mean  \t  funct \t diff")
    for i in range (20):
        mea=mean(x0,x1)
        fnt=f(mea)
        print(i+1,'\t',x0,'\t',x1,'\t',mea,'\t',fnt,'\t',diff)
        if(f(mea)*f(x0)>0):
            x0=mea
        elif(f(mea)*f(x1)>0):
            x1=mea
        diff = abs(mea-mean(x0,x1))
        y.append(diff)
    graphPlot()
    
def graphPlot():
        plt.grid()
        plt.plot(range(len(y)), y)
        plt.show()

main()