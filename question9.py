# "MISSISSIPPI" iss word me har letter ki occurrency count karke ek dictionary me 
# store karaye. Jisme letter dictionary ki keys aur occurrency Uss dictionary ki values 
# hongi. Example:- Output :-




a="MISSISSIPPI"
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)