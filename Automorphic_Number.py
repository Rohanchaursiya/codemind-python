n=int(input())
m=n*n
flag=0
while(n>0):
    if(n%10!=m%10):
        print("Not an Automorphic Number")
        flag=1
        break
    n=n//10
    m=m//10
if(flag==0):
    print("Automorphic Number")