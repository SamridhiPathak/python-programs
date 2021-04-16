def odd_even(l):
    odd_nums=[]
    even_nums=[]
    for i in l:
        if(i%2==0):
            odd_nums.append(i)
        else:
            even_nums.append(i)
        odd_nums.sort()
        even_nums.sort()
        output=(odd_nums,even_nums)
    return output
lst=[5,7,3,4,6,0]
print(odd_even(lst))
            
