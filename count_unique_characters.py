s=list(input().lower())
count=0
for i in s:
    if s.count(i)==1 and i!=" ":
        count+=1
print(count)