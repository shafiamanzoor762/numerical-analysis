# SECANT METHOD
def Secant():
    A=1
    B=2
    c=0
    i=0
    print('n','Xn-1','Xn','Xn+1')
    
    while(A!=B):
            i=i+1
            f1=5*B**2-10
            f2=5*A**2-10
            X=(A*(f1)-B*(f2))/(f1-f2)
            print(i,A,B,X)
            if(c==0):
                  A=X
                  c=1
            else:
                  B=X
                  c=0
        
Secant()