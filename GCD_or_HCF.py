m,n=map(int,input().split())
if m>n:
    c=m
else:
    c=n
for i in range(1,c+1):
    if(m%i==0)and(n%i==0):
        h=i
print(h)