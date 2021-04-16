
def same_ch(l1,l2):
    com_list=[]
    
    for i in l1:
        for j in l2:
            if(i==j):
                com_list.append(i)
    print(com_list)
    
list1=[1,2,3,4,5]
list2=[1,4,6,7,8]
same_ch(list1,list2)
        
'''
def m(l1):
    for i in l1:
        print(i);

list3=[9,7,3];
m(list3)
'''
