import matplotlib.pyplot as plt

#function
def f(x):
    return 5*x**2-10
# f=lambda x:5*x**2-10

def mean(x0,x1):
    return (x0+x1)/2

#Root interval
y=[]
y1=[]
y2=[]
y3=[]

def mainn():
    x0=1
    x1=2
    diff=0
    
    print("i \t x(n-1) \t  x(n) \t  mean  \t  funct \t diff")
    for i in range (10):
        mea=mean(x0,x1)
        fnt=f(mea)
        print(i+1,'\t',x0,'\t',x1,'\t',mea,'\t',fnt,'\t',diff)
        if(f(mea)*f(x0)>0):
            x0=mea
        elif(f(mea)*f(x1)>0):
            x1=mea
        diff = abs(mea-mean(x0,x1))
        y.append(diff)

mainn()

def fnt():
     x1=1
     x2=2
     x=(x1+x2)/2
     dif=0
     prev=0
     print('n |      Xn | dif')
     for i in range(10):
              print(i,'|',x,'|',dif)
              fx=5*x**2-10
              der=10*x
              prev=x
              x=x-(fx/der)    
              dif= abs(prev-x)
              y1.append(dif)
              
fnt()
# 

def Secant():
    A=1
    B=2
    c=0
    i=0
    p=0
    di=0
    X=0
    print('n','Xn-1','Xn','Xn+1','diff')
    
    while(A!=B):
            i=i+1
            f1=5*B**2-10
            f2=5*A**2-10
            p=X
            X=(A*(f1)-B*(f2))/(f1-f2)
            di=abs(p-X)
            y2.append(di)
            print(i,A,B,X,di)
            if(c==0):
                  A=X
                  c=1
            else:
                  B=X
                  c=0
        
Secant()


#function
def f(x):
    return 5*x**2-10
# f=lambda x:5*x**2-10

def main():
    A=1
    B=2
    X=0
    pr=0
    fnt=0
    
    print("i \t x(n-1) \t  x(n) \t  x(n+1)  \t  funct")
    for i in range (10):
        fa=5*B**2-10
        fb=5*A**2-10  
        pr=X      
        X=(A*(fa)-B*(fb))/(fa-fb)               
        fnt=f(X)
        y3.append(abs(pr-X))
        print(i+1,'\t',A,'\t',B,'\t',X,'\t',fnt,'\t')
        if fnt*fa<0:
            A=X
            fa=fb
        elif fnt*fb>0:
            B=X
            fa=fb
        else:
            break

main()   

def graphPlot():
        plt.grid()
        plt.title('Find Root')
        # bisection
        plt.plot(range(len(y)), y, color='blue', linewidth=2, linestyle='--',label='Bisection')
        # Newton
        plt.plot(range(len(y1)), y1, color='red', linewidth=1, linestyle='dashdot',label='Newton')
        # Secant
        plt.plot(range(len(y2)), y2,color='black', linewidth=2, linestyle='dotted',label='Secant')
        # Regula Falsi
        plt.plot(range(len(y3)), y3,label='Regula Falsi')
        plt.legend()        

        plt.show()

graphPlot()
