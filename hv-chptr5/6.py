def typeofnestedlist(l):
    count=0
    for i in range(0,len(l)):
        if(type(l[i])==list):
            count+=1
    return count
list1=[1,[3,4],[5,6],7,9,0]
print(typeofnestedlist(list1))
