v='AEIOUaeiou'
s=input().split()
c=0
b=[]
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    b.append(c)
print(max(b))