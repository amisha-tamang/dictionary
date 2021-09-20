# Ek code likhiye jo dictionary ki 3 highest value print karaye. Input :- Output :-


my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
print(len(my_dict)) 
a=[]
for i in my_dict.values():
    a.append(i)
b=[]
for i in range(3):
    b.append(max(a))
    a.remove(max(a))
print(b)

