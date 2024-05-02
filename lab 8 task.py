# BISECTION
import matplotlib.pyplot as plt
'''numpy matplotlib pulp'''

f=lambda x:(x+2)*(x+1)**2*x*(x-1)**3*(x-2)

def mean(x0,x1):
    return (x0+x1)/2

#Root interval
y=[]

def main():
    x0=-1.5
    x1=2.5
    diff=0
    
    print("i \t x(n-1) \t  x(n) \t  mean  \t  funct \t diff")
    for i in range (50):
        mea=mean(x0,x1)
        fnt=f(mea)
        print(i+1,'\t',x0,'\t',x1,'\t',mea,'\t',fnt,'\t',diff)
        if(f(mea)*f(x0)>0):
            x0=mea
        elif(f(mea)*f(x1)>0):
            x1=mea
        elif f(mea)==0:
             print('Root Found')
             break
        diff = abs(mea-mean(x0,x1))
        y.append(diff)
    graphPlot()
    
def graphPlot():
        it = range(len(y))
        plt.grid()
        plt.plot(it, y)
        plt.show()

main()