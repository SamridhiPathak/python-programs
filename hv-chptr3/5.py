name=input('enter a name')
i=0
while (i<len(name)):
    ch=name[i]
    print(f"{name[i]}:{name.count(ch)}")
    i=i+1


