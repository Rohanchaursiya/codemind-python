n=int(input())
pd=0
sd=0
t=[]
for i in range(0,n):
    a=list(map(int,input().split()))
    t.append(a)
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            pd+=t[i][j]
        if i==n-j-1:
            sd+=t[i][j]
print('Principal Diagonal:',end='')
print(pd)
print('Secondary Diagonal:',end='')
print(sd)