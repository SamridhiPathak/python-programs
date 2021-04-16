T=int(input())
for j in range(T):
    A=[int(x) for x in input.split()]
    K=int(input())
    for i in range(9,-1,-1):
        if(K!=0):
            if(K>=A[i]):
                K=K-A[i]
                A[i]=0
            else:
                A[i]=A[i]-K
                
        else:
            break
    for i in range(9,-1,-1):
        if(A[i]!=0):
            print(i+1)
            break
