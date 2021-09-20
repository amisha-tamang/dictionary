# Ek program likho jo ki dictionaries ki values ko sort(ascending or descending) kar de. Input :- 



dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a={}
length=len(dic)
for i in range(length):
    max_1=0
    for value in dic:
        if max_1<dic[value]:
            max_1=dic[value]
            key=value
    a.update({key:max_1})
    dic.pop(key)
print(a)








