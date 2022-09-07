a=list(map(int,input().split(",")))
n=len(a)
l=[]
for i in range(n):
    sum=0
    for j in range(1,(a[i]+1)):
        if a[i]%j==0:
            sum+=j
    if sum in a:
        l.append(a[i])
b=sorted(l)
for i in b:
    print(i,end=" ")
if len(l)==0:
    print("-1")