n=int(input())
l=list(map(int,input().split()))
g=[]
for i in range(0,n,2):
    for j in range(0,l[i+1]):
        g.append(l[i])
print(*g)