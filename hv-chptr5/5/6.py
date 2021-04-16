def similar_list(l1,l2):
    lst=[]
    for i in l1:
        if i in l2:
            lst.append(i)
    return lst
lst1=[1,2,3,4,5]
lst2=[1,2,4,6]
print(similar_list(lst1,lst2))
            
