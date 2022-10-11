a=input()
t=1
m=0
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        t+=1
        m=max(t,m)
    else:
        t=0
print(m+1)