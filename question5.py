# Do lists lekar ek dictionary banaiye jisme pehli list ke elements keys ho aur dusri 
# list ke elements unn keys ki values ho. Example :- Input :-


list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
my_dic={}
for i in list1:
    for value in list2:
        my_dic[i]=value
        #list2.remove(value)
        break
print(my_dic)