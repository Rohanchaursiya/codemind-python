n=int(input())
a=1
b=0
c=0
for i in range(n*n):
    if(c<n):
        min=c
    if(c>n):
        max=c
        break
    c=a+b
    a=b
    b=c
x=n-min
y=max-n
if(x==y):
    print(min,max)
elif(x<y):
    print(min)
else:
    print(max)
        
    