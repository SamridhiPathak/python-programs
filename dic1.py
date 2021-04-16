dic1={1:10,2:20}
dic2={3:30,4:40}
dictt={}
for i in (dic1,dic2):
    dictt.update(i)
print(dictt)

