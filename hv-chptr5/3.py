def rerv_list(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements
lst=['abc','def','ghi']
print(rerv_list(lst))
