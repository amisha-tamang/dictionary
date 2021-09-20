# Ek code likhiye jo dictionary ki 3 highest value print karaye. Example :-


my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
# a=[]
# for i in my_dict.keys():
#     a.append(i)
# b=[]
# for i in range(3):
#   b.append(max(a))
#   a.remove(max(a))
# print(b)

a=[]
b=[]
for i in range(3):
    max=0
    for x in my_dict:
        if max<my_dict[x]:
            max=my_dict[x]
            key=x
    a.append(max)
    b.append(key)
    my_dict.pop(key)
# print(a)
print(b)



