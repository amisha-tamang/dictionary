# User se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye. Output :- 32


# dict={
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 

dict={}
for i in range(1,11):  
    a=input("enter student name:-")
    b=int(input("enter your marks:-"))
    print(i)
    dict[a]=b
print(dict)
    
