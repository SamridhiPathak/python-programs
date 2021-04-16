'''
n=int(input("enter a number"))
cubic_no={1:1}
for i in range(2,n+1):
    cubic_no[i]=i**2cube={}print(cubic_no,end=" ")
'''
def cubic_no(n):
    cube={}
    for i in range(1,n+1):
        
        cube[i]=i**2
    return cube
print(cubic_no(5))
