# Ek program likhiye jisse ki niche di hui dictionaries ek hi dictionary me aa jaaye jaise ki 
# niche Expected result me diya gaya hain or jisski bhi keys same hai unki values add ho jai. 
# Example :- Input :- Output :- 






dic1={1:10,2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
# dic2={}
for i in dic1:
    if i in dic2:
        dic3[i]=dic2[i]+dic1[i]
        dic2.update(dic3)
        # print(dic3)
    else:
        dic2[i]=dic1[i]
print(dic2)