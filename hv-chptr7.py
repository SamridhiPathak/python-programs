def cube(n):
    dictt={}
    for i in range(1,n+1):
        dictt[i]=i**2
    print(dictt)
x=int(input('enter a number'))
cube(x)
