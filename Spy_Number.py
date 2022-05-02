n=int(input())
n1=n
s=0
f=1
while(n>0):
    r=n%10;
    s=s+r;
    f=f*r;
    n=n//10;
if(s==f):
    print("Spy Number")
else:
    print("Not Spy Number")