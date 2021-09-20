# Ek dictionary ki value ke sabhi items ko count kijiye jo ki ek list me hai. Input :- Output :-


dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']
}
count=0
for i  in dict1:
    a=(len(dict1[i]))
    count+=a
print(count)









